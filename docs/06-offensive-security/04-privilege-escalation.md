# Privilege escalation

> [!TIP]
> **In short:** a foothold is usually a low-privilege account: a web server user, a service account, a standard employee. **Privilege escalation** turns it into administrator or root. In practice it is rarely a clever exploit; it is almost always a **misconfiguration**: an over-generous `sudo` rule, a SUID binary, a scheduled job running a script anyone can edit, a service with weak permissions, credentials left in a file, a token privilege nobody needed to grant. The method is systematic enumeration first and tools second. The defense is the same list read backwards: remove each misconfiguration, patch, and monitor for the changes that precede escalation.

> [!CAUTION]
> Use these checks on systems you own or are authorized to test. On your own machines, they are the fastest way to audit your hardening.

## Concepts

| Term | Meaning |
|---|---|
| **Vertical escalation** | Gaining higher privileges (user to root or SYSTEM, user to domain admin) |
| **Horizontal escalation** | Gaining access to another account at the same level (one user to another) |
| **Local privilege escalation** (LPE) | Starting with code execution on a host and gaining higher privileges on that host |
| **Misconfiguration** | A permission or setting that grants more than intended; the dominant source |
| **Exploit** | A vulnerability in the OS, a driver or a privileged program; less common, riskier to use |

A good order of attack is **cheapest and quietest first**: credentials and trust relationships, then misconfigurations, then known-vulnerable software, and kernel exploits last because they can crash the system. ATT&CK groups these under *Privilege Escalation* (TA0004), with techniques such as T1548 (abuse elevation control), T1068 (exploitation), T1134 (access token manipulation), T1574 (hijack execution flow) and T1053 (scheduled tasks). **●●●**

## Method

1. **Who and what am I?** User, groups, privileges, OS version and patch level, hostname, network position.
2. **What can I run as someone else?** `sudo` rules, SUID programs, capabilities, token privileges.
3. **What runs with high privilege that I can influence?** Services, cron jobs, scheduled tasks, startup items, drivers; files, libraries and paths they use.
4. **What secrets are lying around?** History files, configuration files, backups, scripts, browser data, keys, cached credentials.
5. **What is vulnerable?** Software and OS versions compared with advisories (KEV first).
6. **Try the lowest-risk path, verify, document.**

Do the steps by hand until you understand them. Enumeration scripts (LinPEAS and WinPEAS from PEASS-ng, PowerUp, Seatbelt) are excellent at collecting the same facts quickly, but they hand you a long list: you need to know which lines matter and why. **●●●**

## Linux

| Vector | How to check | Why it works | Fix |
|---|---|---|---|
| **`sudo` rules** | `sudo -l` | A permitted command can start a shell, read or write arbitrary files, or load code (editors, interpreters, `find`, `tar`, `less`; see GTFOBins). `NOPASSWD`, wildcards and `env_keep` (for example `LD_PRELOAD`) widen it | Grant exact commands and arguments; avoid shell-capable programs; use `sudoedit`; no wildcards |
| **SUID / SGID programs** | `find / -perm -4000 -type f 2>/dev/null` | A program owned by root with the SUID bit runs as root; if it can read files or run commands, so can you | Remove the bit from anything not needed; mount user-writable filesystems `nosuid` |
| **Capabilities** | `getcap -r / 2>/dev/null` | A binary with a capability such as `cap_setuid` or `cap_dac_read_search` is root-equivalent for that action | Remove or restrict |
| **Cron jobs and timers** | `cat /etc/crontab /etc/cron.*/*`, `systemctl list-timers` | Root runs a script or binary that a normal user can modify, or uses a relative path or an unquoted wildcard | Root-owned, non-writable scripts; absolute paths; quote wildcards |
| **Writable files in privileged places** | `find / -xdev -writable -type f 2>/dev/null`; inspect `$PATH` | Writable systemd units, scripts called by root, files in `/etc/sudoers.d/`, a writable directory early in a privileged `PATH` | Fix ownership and permissions; no current directory in root's `PATH` |
| **Services running as root** | `ps aux`, `ss -tulpn` | A local-only database or console with weak authentication or a known bug gives root | Drop privileges; authenticate local services; patch |
| **Credentials left behind** | Shell history, `.env`, application config files, backups, SSH keys, `grep -ri password /etc 2>/dev/null` | Passwords are reused for `su`, `sudo` and SSH to other hosts | Secrets manager; permissions `600`; never reuse |
| **NFS exports** | `cat /etc/exports` | `no_root_squash` makes root on a client root on the share | Use `root_squash`; restrict clients |
| **Group memberships** | `id` | The `docker` group is root-equivalent (a container can mount the host's file system); `disk`, `lxd` and others are similar | Avoid; use rootless containers |
| **Kernel and system bugs** | `uname -r`, `cat /etc/os-release` | Known local exploits, for example Dirty COW (CVE-2016-5195), PwnKit in polkit's `pkexec` (CVE-2021-4034) and Dirty Pipe (CVE-2022-0847) | Patch; live patching; reboot after kernel updates |
| **Library and loader hijack** | `ldd BINARY`, `sudo -l` showing `env_keep` | A privileged program loads code from a path you can write | Secure `rpath`; no `env_keep+=LD_PRELOAD` |
| **Containers** | `mount`, check for `/var/run/docker.sock`, privileged mode | A mounted Docker socket or a privileged container is the host | Do not mount the socket; avoid privileged mode; drop capabilities |

**GTFOBins** lists, per Unix binary, which abuses are possible under `sudo`, SUID or capabilities. Look a binary up in it whenever you see one in a rule. **●●●**

A minimal audit script for a host you administer:

```bash
#!/usr/bin/env bash
echo "== identity ==";           id
echo "== sudo rights ==";        sudo -l 2>/dev/null
echo "== SUID files ==";         find / -xdev -perm -4000 -type f 2>/dev/null
echo "== capabilities ==";       getcap -r / 2>/dev/null
echo "== writable files (first 50) =="; find / -xdev -type f -perm -0002 -not -path "/proc/*" 2>/dev/null | head -50
echo "== cron ==";               cat /etc/crontab 2>/dev/null; ls -la /etc/cron.* 2>/dev/null
echo "== timers ==";             systemctl list-timers --all 2>/dev/null
echo "== listening services =="; ss -tulpn 2>/dev/null
```

## Windows

| Vector | How to check | Why it works | Fix |
|---|---|---|---|
| **Token privileges** | `whoami /priv` | `SeImpersonatePrivilege` and `SeAssignPrimaryTokenPrivilege` (held by many service accounts such as IIS and SQL Server) can be turned into SYSTEM with the "Potato" family of techniques; `SeBackupPrivilege` can read any file including the SAM and `ntds.dit`; `SeDebugPrivilege` and `SeLoadDriverPrivilege` are equally dangerous | Run services with virtual or managed accounts and minimal privileges; remove privileges not needed |
| **Unquoted service paths** | `wmic service get name,pathname,startmode` (or PowerShell `Get-CimInstance Win32_Service`) | A path with spaces and no quotes makes Windows try shorter names (`C:\Program Files\App\svc.exe` tries `C:\Program.exe`); a writable folder on that path lets a user plant a binary | Quote paths; correct folder permissions |
| **Weak service permissions** | `accesschk.exe`, `sc sdshow SERVICE` | A user can reconfigure a service or replace its binary and restart it | Fix service ACLs and file ACLs |
| **Scheduled tasks** | `schtasks /query /fo LIST /v` | A task runs as SYSTEM and calls a writable script or binary | Tighten ACLs; sign and allowlist |
| **Autoruns and registry** | Sysinternals Autoruns, `reg query` | Writable Run keys, services keys or startup folders | Fix ACLs |
| **`AlwaysInstallElevated`** | Both registry values `AlwaysInstallElevated` set to 1 (HKLM and HKCU) | Any user can install an MSI package as SYSTEM | Disable |
| **DLL search-order hijacking** | Process Monitor: privileged process with `NAME NOT FOUND` for a DLL in a writable path | A privileged program loads a library from a location a user controls | Full paths; safe search mode; ACLs; application control |
| **Stored credentials** | `cmdkey /list`, unattended-install files, autologon registry values, PowerShell history, application config, Group Policy Preferences `cpassword` (MS14-025) | Credentials that are reused or privileged | Remove; deploy Windows LAPS; use vaults |
| **Weak folder permissions** | `icacls` on application and service directories | Replace an executable run by a privileged user | Restore standard ACLs |
| **UAC** | n/a | User Account Control is **not a security boundary** in Microsoft's servicing criteria, so bypasses exist and are not always fixed | Do not give daily accounts administrator rights; treat UAC as one layer |
| **Unpatched OS and drivers** | `systeminfo`, installed updates | Kernel and driver flaws; **bring your own vulnerable driver** (BYOVD) uses a signed but vulnerable driver to reach the kernel | Patch; enable the vulnerable-driver blocklist and memory integrity |
| **Credentials in memory** | n/a | An administrator can read secrets from LSASS | Credential Guard, LSA protection (see [Windows internals](../02-systems/02-windows-internals-for-security.md)) |

The **LOLBAS** project catalogs signed Microsoft binaries and scripts that can be abused for execution, download, and bypasses ("living off the land"). **●●●**

## Beyond the single host

| Environment | Escalation idea | Where to learn it |
|---|---|---|
| **Active Directory** | From a local administrator or a stolen ticket to domain administrator | [Active Directory attacks](05-active-directory-attacks.md) |
| **Containers and Kubernetes** | From inside a container to the node (privileged mode, host mounts, mounted runtime socket, excessive RBAC) | [Containers, Kubernetes and IaC](../08-cloud-and-infrastructure/03-containers-kubernetes-and-iac.md) |
| **Cloud** | From a limited identity to administrator through permission paths (for example the ability to pass a powerful role to a service, or to create a new policy version) | [Cloud IAM and attack paths](../08-cloud-and-infrastructure/02-cloud-iam-and-attack-paths.md) |

## The defender's view

| Control | What it stops |
|---|---|
| **Least privilege**: few administrators, narrow `sudo`, minimal service privileges | Most of both tables |
| **Hardening baselines** (CIS Benchmarks) and drift checks | Reintroduced misconfigurations |
| **Patching** the OS, drivers and privileged software | Exploit-based escalation |
| **Application control** (AppLocker or WDAC on Windows; AppArmor or SELinux on Linux) | Planted binaries and living-off-the-land abuse |
| **Credential hygiene**: unique local administrator passwords (LAPS), no secrets in files | Reuse and credential harvesting |
| **File integrity monitoring** on binaries, service definitions and `sudoers` | Silent changes |

### Detection

| Platform | Signal |
|---|---|
| **Linux** | Audit rules on `sudoers`, `passwd` and `shadow`; creation of files with the SUID bit; new cron entries and systemd units; unexpected `su` or `sudo` use; processes spawned by services (a web server starting a shell) |
| **Windows** | Event 4672 (special privileges assigned) for unexpected accounts; 4688 process creation with command line; 7045 and 4697 service installed; 4698 scheduled task created; Sysmon events for process creation, file creation, driver and image loads; new local administrators (4732) |
| **Both** | EDR detections for token manipulation and credential access; a standard user suddenly running as root or SYSTEM; privileged child processes of unprivileged parents |

Examples of auditd rules for the Linux checks above:

```
-w /etc/sudoers -p wa -k sudoers
-w /etc/sudoers.d/ -p wa -k sudoers
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
```

Detection rules for the rest are built in [Detection engineering](../07-defensive-security/02-detection-engineering.md).

## Practice

1. Build a deliberately misconfigured Linux VM in your lab with five problems: a `NOPASSWD` `sudo` rule for an editor, a SUID copy of `find`, a root cron job running a writable script, membership in the `docker` group and a password in a history file. Enumerate **by hand** first, then with LinPEAS, escalate using GTFOBins, then fix every issue and re-run the audit.
2. Do the same on a Windows evaluation VM with an unquoted service path in a writable folder, a weak service ACL and `SeImpersonatePrivilege` on a service account. Enumerate with the commands above, then with WinPEAS or PowerUp, and fix each issue.
3. Complete the Hack The Box Academy module *Linux Privilege Escalation*, and the TryHackMe rooms on Linux and Windows privilege escalation.
4. Write the auditd or Sysmon rule that would have alerted on each of your lab misconfigurations being used.
5. Document one escalation as a [writeup](../../writeups/TEMPLATE.md) with the root cause, the evidence and the fix.

These support [Module 2.3](../../roadmap/phase-2-guided-practice/03-machines-and-ad.md) of the roadmap.

## What to do with this

- [ ] Memorize the first ten minutes of Linux and Windows enumeration and run them on your own systems.
- [ ] For each vector in the tables, say what you would change in a hardening baseline.
- [ ] Look up five binaries in GTFOBins and five in LOLBAS and explain the abuse in your own words.
- [ ] Audit your daily machines for the issues above and fix what you find.
- [ ] Record in your notes which misconfiguration you found most often in labs.

## Key references

GTFOBins · HackTricks · LOLBAS · Microsoft security servicing criteria · MITRE ATT&CK · PEASS-ng. Full list in [References](../15-references.md).
