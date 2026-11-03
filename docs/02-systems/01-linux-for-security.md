# Linux for security

> [!TIP]
> **In short:** Linux security comes down to five things you can inspect from a shell: **who** exists (users, groups, `sudo`), **what they may touch** (permissions, setuid, capabilities), **what is running** (processes, services, scheduled jobs), **who can reach it** (network and SSH) and **what was recorded** (logs). Learn to read those five quickly and you can triage an unfamiliar server in ten minutes, harden your own, and recognize almost every classic privilege escalation.

## The filesystem, through a security lens

The Filesystem Hierarchy Standard puts things in predictable places. Knowing the places is half of any investigation.

| Path | Holds | Why it matters |
|---|---|---|
| `/etc` | System configuration | `passwd`, `shadow`, `sudoers`, `ssh/`, cron files, service configs. A write here is usually a full compromise |
| `/var/log` | Logs | Authentication, system and service logs; the first place an investigator looks |
| `/home`, `/root` | User data | SSH keys, shell history, tokens in dotfiles |
| `/tmp`, `/var/tmp`, `/dev/shm` | Scratch space, world-writable | Where attackers drop tools; mount with `noexec,nosuid` where possible |
| `/proc`, `/sys` | Kernel and process information (virtual) | Live view of processes, memory maps and network state; not on disk |
| `/usr/bin`, `/usr/sbin`, `/bin`, `/opt` | Programs | Setuid binaries and unexpected additions hide here |
| `/boot` | Kernel and bootloader | Tampering gives persistence below the operating system |
| `/var/spool/cron` | Per-user cron jobs | A classic persistence location |

## Users, groups and passwords

Every account has a numeric ID. **UID 0 is root**, whatever the name; any account with UID 0 has full control.

```
user:x:1001:1001:Full Name:/home/user:/bin/bash
 |   |   |    |      |         |          |
 |   |   |    |      |         |          login shell
 |   |   |    |      |         home directory
 |   |   |    |      comment
 |   |   |    primary group ID
 |   |   user ID
 |   "x" = password hash is in /etc/shadow
 login name
```

`/etc/passwd` is world-readable because programs need to map IDs to names. The password hashes live in `/etc/shadow`, readable only by root and a privileged group. The hash prefix tells you the algorithm: `$y$` is yescrypt (the default on current Debian and Ubuntu), `$6$` is SHA-512 crypt, `$2b$` is bcrypt. A `!` or `*` in the hash field means password login is disabled for that account.

Groups can be as powerful as users. Know the ones that matter:

| Group | Power |
|---|---|
| `sudo` / `wheel` | May run commands as root through `sudo` |
| `docker` | **Root-equivalent.** Anyone who can talk to the Docker daemon can mount the host filesystem into a container |
| `adm` | Can read most logs, which may contain secrets |
| `shadow` | Can read `/etc/shadow` |
| `disk` | Raw access to block devices, which bypasses file permissions |

**Practical implication:** adding a user to `docker` is granting root. Audit group membership as carefully as `sudo` rules.

## Permissions

Each file has an owner, a group and three sets of bits (owner, group, others), each with read (4), write (2) and execute (1).

```
-rwxr-x---   1 root  devs  4096  app.sh
 |||||||||
 ||| ||| others: no access
 ||| group (devs): read and execute
 owner (root): read, write, execute
```

| Mode | Meaning | Note |
|---|---|---|
| `644` | Owner read/write; others read | Typical data file |
| `755` | Owner full; others read/execute | Typical program or directory |
| `600` | Owner read/write only | Private keys, tokens |
| `700` | Owner only | `~/.ssh` |

On a **directory**, read lets you list names, write lets you create or delete entries, and execute (search) lets you enter it. Deleting a file needs write permission on its *directory*, not on the file.

### The three special bits

| Bit | Octal | On a file | On a directory |
|---|---|---|---|
| **setuid** (`s` in owner position) | 4000 | Runs with the file *owner's* privileges | Ignored |
| **setgid** (`s` in group position) | 2000 | Runs with the file *group's* privileges | New files inherit the directory's group |
| **sticky** (`t`) | 1000 | Ignored | Only the owner of a file may delete or rename it (as in `/tmp`) |

`-rwsr-xr-x root root` means "any user who runs this executes it as root". This is how `passwd` can edit `/etc/shadow`, and it is why every extra setuid binary is attack surface. Find them and justify each:

```bash
find / -perm -4000 -type f 2>/dev/null   # setuid
find / -perm -2000 -type f 2>/dev/null   # setgid
```

Also know **ACLs** (`getfacl`, `setfacl`), which add per-user entries beyond the three sets, and the **immutable attribute** (`chattr +i`), which prevents even root from modifying a file until it is removed. The default `umask` (usually `022` or `027`) controls what permissions new files receive.

## sudo

`sudo` lets permitted users run commands as another user, normally root, and logs each use. Configuration is in `/etc/sudoers` and `/etc/sudoers.d/`, edited with `visudo` so a syntax error cannot lock you out.

```bash
sudo -l       # what may I run?
```

Frequent mistakes, and why they are dangerous:

| Rule | Problem |
|---|---|
| `user ALL=(ALL) NOPASSWD: ALL` | Any compromise of the account is a root compromise with no further barrier |
| Allowing an editor, pager or interpreter (`vim`, `less`, `find`, `python`) | These programs can spawn a shell; the allowed command becomes a full root shell |
| Wildcards in paths or arguments | The wildcard can match attacker-chosen input |
| A writable script or directory in a root-run command | Whoever can write it controls root |

The GTFOBins project catalogs which common binaries can be abused for this when granted through `sudo`, setuid or capabilities. It is a reference for finding weaknesses and for knowing what *not* to allow.

## Capabilities

Traditional Unix has one all-powerful user. **Capabilities** split root's authority into about forty separate privileges so a program can have only what it needs. **●●●**

| Capability | Allows |
|---|---|
| `CAP_NET_BIND_SERVICE` | Bind to ports below 1024 |
| `CAP_NET_RAW` | Open raw sockets (ping, packet capture) |
| `CAP_DAC_READ_SEARCH` | Bypass read and traversal permission checks |
| `CAP_SYS_PTRACE` | Inspect and modify other processes |
| `CAP_SYS_ADMIN` | A very large set of administrative operations; nearly equivalent to root |

A binary given powerful capabilities is a privilege escalation path just like a setuid binary. List them with `getcap -r / 2>/dev/null`. Containers are built on capabilities: dropping them is a major part of container hardening (see [Containers, Kubernetes and IaC](../08-cloud-and-infrastructure/03-containers-kubernetes-and-iac.md)).

## Processes and services

```bash
ps auxf                          # all processes, tree view
ls -l /proc/<pid>/exe            # the actual binary behind a process
cat /proc/<pid>/cmdline | tr '\0' ' '
ls -l /proc/<pid>/fd             # open files and sockets
```

`/proc/<pid>` is the best view of a running process. Attackers sometimes rename a process or delete its binary after launch; `/proc/<pid>/exe` then shows `(deleted)`, which is a reliable red flag.

Services are managed by **systemd**:

```bash
systemctl list-units --type=service --state=running
systemctl status ssh
journalctl -u ssh --since "1 hour ago"
```

Unit files live in `/etc/systemd/system/` (local) and `/usr/lib/systemd/system/` or `/lib/systemd/system/` (packages). Check them for unexpected `ExecStart` lines and writable paths.

### Where persistence hides

Anything that runs automatically can be abused to keep access. When investigating, check all of these.

| Location | Mechanism | Check |
|---|---|---|
| `/etc/crontab`, `/etc/cron.d/`, `/etc/cron.*`, `/var/spool/cron/` | Scheduled jobs | `crontab -l` for each user; read every file |
| systemd units and timers | Services started at boot or on a schedule | `systemctl list-unit-files`, `systemctl list-timers` |
| `~/.ssh/authorized_keys`, `/root/.ssh/` | Added public keys | Look for keys you do not recognize |
| `~/.bashrc`, `~/.profile`, `/etc/profile.d/` | Shell startup | Look for commands you did not write |
| `/etc/ld.so.preload`, `LD_PRELOAD` | Libraries loaded into every process | The file should usually not exist |
| Setuid or capability-bearing binaries | Backdoor shells | Compare with a known baseline |
| PAM modules, `/etc/pam.d/` | Authentication hooks | Unexpected modules that log or accept passwords |
| Kernel modules (`lsmod`) | Rootkits | Unknown modules |
| `/etc/rc.local`, init scripts | Legacy startup | Often forgotten |

## SSH

SSH is the main remote entry point and a frequent target. A sound baseline in `/etc/ssh/sshd_config`:

```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers alice bob
MaxAuthTries 3
LogLevel VERBOSE
```

Use Ed25519 keys (`ssh-keygen -t ed25519`), protect them with a passphrase, and keep private keys off shared machines. Be careful with **agent forwarding** (`-A`): anyone with root on the intermediate host can use your forwarded agent while you are connected. Prefer `ProxyJump` (`-J`). Tools such as `ssh-audit` check a server's algorithms and configuration. Expect to see brute-force attempts within minutes on any internet-exposed SSH port; key-only login makes them harmless, and rate limiting or a tool like fail2ban reduces the noise.

## Network view

```bash
ip -br a                # interfaces and addresses
ss -tulpn               # listening sockets with owning process
ip route                # routing table
sudo nft list ruleset   # firewall (or iptables -S, ufw status)
```

`ss -tulpn` answers "what is this machine exposing?", and every listening port you cannot explain deserves attention. Bind internal services to `127.0.0.1` or to a private interface, not `0.0.0.0`.

## What Linux records

| Source | Location | Typical content |
|---|---|---|
| Authentication log | `/var/log/auth.log` (Debian, Ubuntu); `/var/log/secure` (RHEL family) | SSH logins and failures, `sudo` use, `su`, PAM events |
| System log | `/var/log/syslog` or `/var/log/messages` | Service messages, kernel events |
| Journal | `journalctl` | Structured logs from systemd units |
| Login records | `/var/log/wtmp`, `/var/log/btmp`; commands `last`, `lastb` | Successful and failed logins |
| Audit framework | `auditd`; `ausearch`, `aureport` | Rule-based records of file access, syscalls and commands |
| Web and service logs | `/var/log/nginx/`, `/var/log/apache2/` | Requests, errors |

The default logs say little about *what a user ran*. For that, enable `auditd` with rules for sensitive files and commands, for example:

```
-w /etc/passwd -p wa -k identity
-w /etc/sudoers -p wa -k identity
-a always,exit -F arch=b64 -S execve -k exec
```

Ship logs off the host, because an intruder with root can edit local files (see [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md)).

## Hardening checklist

| Area | Action |
|---|---|
| Updates | Enable automatic security updates; reboot for kernel fixes |
| Services | Remove or disable what you do not need; bind the rest narrowly |
| Accounts | No shared accounts; lock unused ones; strong or no passwords; keys for SSH |
| Privileges | Minimal `sudo` rules; audit setuid, capabilities and group membership |
| Filesystem | Mount `/tmp`, `/var/tmp` and `/dev/shm` with `noexec,nosuid,nodev` where compatible |
| Mandatory access control | Keep SELinux (RHEL family) or AppArmor (Ubuntu, SUSE) enabled and enforcing |
| Kernel | Keep `kernel.randomize_va_space=2`; restrict `dmesg` and kernel pointers where appropriate |
| Firewall | Default deny inbound; allow only required ports |
| Logging | Enable `auditd`; forward logs to a central system |
| Verification | Run a benchmark such as the CIS Benchmark for your distribution or an audit tool such as Lynis |

## The first ten minutes on an unfamiliar host

Use this on lab machines and in authorized investigations. The point is a quick, structured picture before you change anything.

```bash
# Identity and context
whoami; id; hostname; date; uptime
uname -a; cat /etc/os-release

# Who is here, who was here
w; last -n 20; lastb -n 20 2>/dev/null

# What is running and listening
ps auxf
ss -tulpn
systemctl list-units --type=service --state=running

# Accounts and privileges
awk -F: '$3==0 {print $1}' /etc/passwd     # extra UID 0 accounts
getent group sudo docker adm
sudo -l

# Persistence candidates
crontab -l; ls -la /etc/cron.* /var/spool/cron 2>/dev/null
ls -la ~/.ssh /root/.ssh 2>/dev/null
systemctl list-timers

# Privilege escalation surface
find / -perm -4000 -type f 2>/dev/null
getcap -r / 2>/dev/null

# Recent change
find / -xdev -type f -mtime -2 2>/dev/null | head -50
```

Read the output as a story: unexpected accounts, listeners with no explanation, recent files in odd places, scheduled jobs you did not create. On an investigation, collect and hash evidence before altering the system (see [Digital forensics](../07-defensive-security/05-digital-forensics.md)).

## Common weaknesses and their fixes

| Weakness | How it is abused | Fix |
|---|---|---|
| Root cron job runs a world-writable script | Edit the script, wait for root to run it | Make the script and its directory root-owned and not writable by others |
| `NOPASSWD` `sudo` on `vim`, `find`, `less` | Spawn a shell from the allowed program | Allow only specific, non-interactive commands; avoid wildcards |
| Setuid on a shell, interpreter or copy tool | Run a root shell | Remove the bit; justify every setuid binary |
| User in `docker` group | Mount the host and read or write anything | Treat as root; use rootless containers where possible |
| Writable `/etc/passwd` or `/etc/sudoers` | Add a root user | Correct ownership and permissions; monitor with auditd |
| SSH with passwords enabled and weak accounts | Brute force | Key-only login, `AllowUsers`, rate limiting |
| Secrets in shell history, environment or world-readable files | Credential reuse | Use a secrets manager; `chmod 600`; clear sensitive history |
| Old kernel or privileged service | Public exploits | Patch quickly; track advisories for installed packages |

## What to do with this

- [ ] Run the first-ten-minutes commands on your own VM and explain every line of output.
- [ ] Find the setuid binaries on your system and justify each one.
- [ ] Harden SSH on a lab VM, then try to break in with passwords from another VM and confirm it fails.
- [ ] Write three auditd rules and trigger them.
- [ ] Do [Module 0.2](../../roadmap/phase-0-foundations/02-linux-command-line.md) and [Module 0.3](../../roadmap/phase-0-foundations/03-bash-scripting.md) of the roadmap.

## Key references

CIS Benchmarks · GTFOBins · man7.org Linux manual pages · OpenSSH sshd_config(5) · OWASP Docker Security Cheat Sheet. Full list in [References](../15-references.md).

<!-- navigation -->
[← Legal limits and ethics](../01-foundations/05-legal-and-ethics.md) · [Index](../00-start-here.md) · [Windows internals for security →](02-windows-internals-for-security.md)
