# Windows internals for security

> [!TIP]
> **In short:** Windows security rests on four things. **Identities** (accounts, SIDs and the access token a process carries), **access control** (ACLs, privileges, integrity levels), **secrets** (the SAM, LSASS memory, the registry) and **telemetry** (Event Log, ETW, Sysmon, PowerShell logging). Most enterprise intrusions end on Windows and Active Directory, so you need to know where things live, which ones attackers go after and what each action leaves behind.

## Architecture in one page

Windows runs code in **user mode** (applications, most services) and **kernel mode** (the kernel, drivers). A bug in kernel code, including third-party drivers, can compromise the whole system, which is why driver signing and driver blocklists matter.

A handful of system processes have fixed parents and counts. Deviations from the table are a classic detection signal, because malware often imitates their names.

| Process | Expected parent | Notes |
|---|---|---|
| `System` (PID 4) | none | Kernel threads |
| `smss.exe` | `System` | Session manager; starts the others and exits |
| `wininit.exe` | `smss.exe` (exits) | One instance; starts services and LSASS |
| `services.exe` | `wininit.exe` | One instance; the Service Control Manager |
| `lsass.exe` | `wininit.exe` | **One** instance; authentication and credentials |
| `svchost.exe` | `services.exe` | Many instances; hosts services. A `svchost.exe` with another parent or started from a user folder is suspect |
| `winlogon.exe` | `smss.exe` (exits) | One per interactive session |
| `explorer.exe` | `userinit.exe` (exits) | Appears as an orphan; the user's desktop |

If you see a second `lsass.exe`, a `svchost.exe` whose command line lacks `-k`, or `services.exe` running from a path other than `C:\Windows\System32`, investigate. **●●●**

## Identity

### Accounts and SIDs

Every account and group has a **security identifier (SID)**, for example `S-1-5-21-<domain>-<RID>`. The RID is the final number, and some are fixed:

| RID | Meaning |
|---|---|
| 500 | Built-in Administrator |
| 501 | Guest |
| 502 | `krbtgt` (the domain's Kerberos ticket-granting account) |
| 512 | Domain Admins |
| 513 | Domain Users |
| 519 | Enterprise Admins |

Well-known SIDs include `S-1-5-18` (SYSTEM), `S-1-5-19` (Local Service), `S-1-5-20` (Network Service) and `S-1-5-32-544` (the local Administrators group). Names change; SIDs do not. Detections and ACLs should use SIDs where possible.

Services run as `LocalSystem` (very powerful), `NT AUTHORITY\NetworkService`, a virtual account, a domain user or a **group managed service account (gMSA)**. gMSAs have long, automatically rotated passwords and are the preferred choice for domain services.

### Access tokens

When you log on, Windows builds an **access token** that every process you start inherits. It contains the user SID, group SIDs, **privileges** and an integrity level. Inspect your own:

```powershell
whoami /all
```

**Privileges** are separate from group membership. A few are dangerous enough that holding them should be treated as near-administrator:

| Privilege | Why it matters |
|---|---|
| `SeDebugPrivilege` | Open and read any process, including LSASS |
| `SeImpersonatePrivilege` | Impersonate other users' tokens; the basis of the "potato" family of local escalations on service accounts |
| `SeBackupPrivilege` / `SeRestorePrivilege` | Read or write any file regardless of ACLs |
| `SeTakeOwnershipPrivilege` | Take ownership of any object |
| `SeLoadDriverPrivilege` | Load kernel drivers |

Web servers and database services often run as accounts holding `SeImpersonatePrivilege`, so an application bug on such a host can become SYSTEM. **●●●**

### Integrity levels and UAC

Processes also run at an **integrity level**: Low (sandboxes, browser content), Medium (standard users), High (elevated administrators) and System. A lower-integrity process cannot write to higher-integrity objects.

**User Account Control (UAC)** gives an administrator two tokens: a filtered Medium token for everyday work and a full High token after a consent prompt. Microsoft's position is that UAC is a convenience for limiting accidental elevation, not a security boundary, so a bypass is not serviced as a vulnerability. Do not rely on it to stop an attacker who already runs as an administrator. **●●●**

## Access control

Securable objects (files, registry keys, services, processes) have a **security descriptor** with:

- an **owner**,
- a **DACL** (discretionary ACL), a list of ACEs that allow or deny access to SIDs,
- a **SACL** (system ACL) that controls auditing.

```powershell
icacls C:\App\config.ini
Get-Acl C:\App\config.ini | Format-List
```

Common NTFS rights in `icacls` output: `F` full, `M` modify, `RX` read and execute, `R` read, `W` write. Permissions are inherited from parent folders unless broken. Two traps:

- **Share permissions and NTFS permissions both apply**; the more restrictive wins on a network share.
- **Alternate data streams (ADS)** attach hidden data to a file (`file.txt:hidden`), which attackers have used to stash payloads. `dir /r` lists them.

Overly permissive ACLs on services, scheduled-task binaries and installation folders are a major source of local privilege escalation (see [Privilege escalation](../06-offensive-security/04-privilege-escalation.md)).

## The registry

The registry is the central configuration database. Key locations:

| Hive or key | Holds |
|---|---|
| `HKLM\SYSTEM` | Boot and service configuration, `ControlSet001\Services` (every service) |
| `HKLM\SOFTWARE` | Installed software and system settings |
| `HKLM\SAM` | Local account password hashes (protected; readable only by SYSTEM) |
| `HKLM\SECURITY` | LSA secrets and cached domain logon verifiers |
| `HKU\<SID>` (`NTUSER.DAT`) | A user's settings, history and run keys |

Common autostart keys (check both `HKLM` and `HKCU`):

```
Software\Microsoft\Windows\CurrentVersion\Run
Software\Microsoft\Windows\CurrentVersion\RunOnce
Software\Microsoft\Windows NT\CurrentVersion\Winlogon   (Userinit, Shell)
```

## Persistence and autostart locations

Besides the run keys, a thorough review includes:

| Mechanism | Where to look |
|---|---|
| Services | `HKLM\SYSTEM\CurrentControlSet\Services`; `Get-Service`; event 7045 |
| Scheduled tasks | `schtasks /query /fo LIST /v`; `Get-ScheduledTask`; event 4698 |
| Startup folders | `shell:startup`, `shell:common startup` |
| WMI event subscriptions | `Get-CimInstance -Namespace root\subscription -ClassName __EventConsumer` |
| DLL hijacking | A writable directory earlier in a program's DLL search order |
| Image File Execution Options, AppInit DLLs | Debugger and injection hooks in the registry |
| Browser extensions, Office add-ins | Per-user persistence |

The Sysinternals **Autoruns** tool enumerates nearly all of these and can compare against a baseline. It is the first tool to run when you suspect persistence.

## Credentials: where secrets live

Knowing where credentials are stored explains both the attacks and the defenses.

| Store | What it contains | Notes |
|---|---|---|
| **SAM** | Local account NT hashes | The NT hash is an unsalted MD4 of the UTF-16 password, so it is fast to crack and usable directly in "pass-the-hash" |
| **LSASS memory** | Credentials for logged-on sessions: NT hashes, Kerberos tickets and keys | Why `lsass.exe` is the most targeted process |
| **LSA secrets** | Service account passwords, auto-logon passwords | In `HKLM\SECURITY` |
| **Cached domain logons** | Verifiers (MS-Cache v2) so users can log on offline | Slow to crack, but crackable |
| **DPAPI** | Keys protecting browser passwords, Wi-Fi keys and other user secrets | Tied to the user's logon |
| **NTDS.dit** (domain controllers) | The domain's password hashes | Total compromise if copied |

Protections to know:

- **Credential Guard** isolates secrets in a virtualization-based container so that even code running as SYSTEM cannot read them from LSASS. Recent Windows releases enable it by default on eligible hardware and editions; verify for your build. **●●○**
- **LSA protection** (`RunAsPPL`) runs LSASS as a protected process so that non-protected code cannot open it.
- **WDigest** cleartext password caching is off by default on supported systems; make sure nobody turned it back on.
- **Protected Users** group members cannot use NTLM or weak Kerberos encryption and have short ticket lifetimes.
- **Windows LAPS** gives each computer a unique, rotating local administrator password, ending the shared-password lateral movement path.

## Defensive features of the platform

| Feature | Purpose |
|---|---|
| **Microsoft Defender** (antivirus, cloud protection) | Signature and behavior detection built in |
| **Attack Surface Reduction (ASR) rules** | Block risky behaviors such as Office spawning child processes |
| **AppLocker / App Control for Business (WDAC)** | Allow only approved executables, scripts and drivers |
| **AMSI** | Lets antivirus inspect script content (PowerShell, VBScript, JavaScript) at runtime |
| **Windows Firewall** | Host firewall; keep it on and managed centrally |
| **BitLocker, Secure Boot, TPM** | Protect data at rest and the boot chain |
| **Event Tracing for Windows (ETW)** | The telemetry backbone used by EDR products and Sysmon |

## PowerShell, LOLBins and why attackers like built-ins

PowerShell is installed everywhere, powerful and trusted, so attackers use it in preference to bringing their own tools. The same holds for other signed binaries (certutil, bitsadmin, mshta, rundll32, regsvr32), a category called **living off the land**. The LOLBAS project catalogs them with the abuse each allows. Defensive consequences:

- The *execution policy* is not a security control; it is a guard against accidents.
- Turn on **PowerShell logging**: module logging (event 4103), **script block logging** (event 4104) and transcription. Script block logging records the code that actually ran, including after deobfuscation.
- Use **Constrained Language Mode** with application control for high-value systems.
- Disable PowerShell v2 where present, because it bypasses newer protections.
- Detect on behavior (a document spawning PowerShell; encoded commands; download cradles), not on the mere presence of PowerShell.

## What Windows records

Windows logs a great deal, but several important sources are off or incomplete by default. Enable **Advanced Audit Policy** categories deliberately, and turn on command-line capture for process creation.

### Security log (key events)

| Event ID | Meaning |
|---|---|
| **4624 / 4625** | Successful / failed logon (check the logon type) |
| 4634, 4647 | Logoff |
| 4648 | Logon attempted with explicit credentials |
| **4672** | Special privileges assigned to a new logon (admin-like logon) |
| **4688** | Process created (command line appears only if the policy is enabled) |
| 4697 | A service was installed |
| 4698 / 4699 | Scheduled task created / deleted |
| 4720, 4722, 4724, 4738 | Account created, enabled, password reset, changed |
| 4728, 4732, 4756 | Member added to a global, local or universal group |
| 4768, 4769, 4771 | Kerberos TGT request, service ticket request, pre-authentication failure |
| 4776 | NTLM credential validation |
| **1102** | The audit log was cleared |

### Logon types (field in 4624/4625)

| Type | Meaning |
|---|---|
| 2 | Interactive (console) |
| 3 | Network (SMB, remote admin, most lateral movement) |
| 4 / 5 | Batch (scheduled task) / Service |
| 7 | Unlock |
| 9 | NewCredentials (`runas /netonly`, also used in pass-the-hash tooling) |
| 10 | RemoteInteractive (RDP) |
| 11 | CachedInteractive (offline domain logon) |

### Other logs worth enabling and collecting

| Log | Event IDs | Meaning |
|---|---|---|
| System | **7045**, 104 | New service installed; System log cleared |
| Microsoft-Windows-PowerShell/Operational | 4103, **4104** | Module and script block logging |
| Microsoft-Windows-TaskScheduler/Operational | 106, 200, 201 | Task registered, action started, action completed |
| Microsoft-Windows-WMI-Activity/Operational | 5861 | Permanent WMI event subscription |
| Microsoft-Windows-Windows Defender/Operational | 1116, 1117, 5001 | Threat detected, action taken, real-time protection disabled |
| TerminalServices-RemoteConnectionManager/Operational | 1149 | RDP authentication succeeded |
| TerminalServices-LocalSessionManager/Operational | 21 to 25 | RDP session logon, shell start, logoff, disconnect, reconnect |

### Sysmon

**Sysmon** (from Sysinternals) adds the detail that default logging lacks: process creation with hashes and parent, network connections, image loads, process access and more. Microsoft has also begun shipping it as an optional Windows feature on Windows 11 (check the Microsoft Learn documentation for the current status on your edition); the standalone Sysinternals download remains available. **●●○** Useful event IDs:

| ID | Event |
|---|---|
| 1 | Process creation (command line, hashes, parent) |
| 3 | Network connection |
| 7 | Image (DLL) loaded |
| 8 | CreateRemoteThread (injection) |
| 10 | Process access (for example, reading LSASS memory) |
| 11 | File created |
| 12, 13, 14 | Registry object created or deleted, value set, renamed |
| 22 | DNS query |

A configuration decides what is logged. Do not run Sysmon with defaults; start from a maintained community configuration such as SwiftOnSecurity's `sysmon-config` or the modular configs by Olaf Hartong, then tune them for your environment. See [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md).

## Hardening checklist

| Area | Action |
|---|---|
| Patching | Automatic updates; track out-of-band emergency patches |
| Local admin | Remove standing local administrator rights; deploy Windows LAPS |
| Credentials | Credential Guard and LSA protection on; Protected Users for privileged accounts |
| Protocols | Disable SMBv1; require SMB signing; disable LLMNR, NetBIOS name resolution and mDNS where not needed |
| Execution | App Control or AppLocker; ASR rules; PowerShell Constrained Language Mode on high-value systems |
| Logging | Advanced audit policy, command-line process auditing, PowerShell logging, Sysmon; forward to a SIEM |
| Network | Host firewall on; block inbound SMB and RDP from workstation to workstation |
| Baselines | Apply Microsoft Security Baselines or CIS Benchmarks; check with the Security Compliance Toolkit |
| Endpoint | Defender or an EDR with tamper protection |

## The first ten minutes on a Windows host

For lab machines and authorized investigations. Run in an elevated PowerShell and save the output.

```powershell
# Context
whoami /all; hostname; Get-ComputerInfo | Select OsName, OsVersion, CsDomain
Get-Date; (Get-CimInstance Win32_OperatingSystem).LastBootUpTime

# Accounts
Get-LocalUser | Select Name, Enabled, LastLogon
Get-LocalGroupMember Administrators

# What is running and listening
Get-Process | Sort-Object CPU -Descending | Select -First 25 Name, Id, Path
Get-NetTCPConnection -State Listen | Sort LocalPort |
  Select LocalAddress, LocalPort, @{n='Process';e={(Get-Process -Id $_.OwningProcess).Name}}
Get-Service | Where Status -eq Running

# Persistence candidates
Get-ScheduledTask | Where State -ne Disabled | Select TaskName, TaskPath
Get-CimInstance Win32_StartupCommand | Select Name, Command, Location
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run

# Recent activity
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} -MaxEvents 30 |
  Select TimeCreated, Id, Message
Get-MpThreatDetection | Select InitialDetectionTime, ThreatID, ProcessName
```

Then run **Autoruns** and **Process Explorer** (Sysinternals) for a visual view of persistence and the process tree. For a deeper treatment of how to preserve and analyze evidence, see [Digital forensics](../07-defensive-security/05-digital-forensics.md).

## What to do with this

- [ ] Run `whoami /all` as a standard user and as an administrator and explain the differences.
- [ ] Find three autostart locations on your lab VM and add a harmless entry to each, then find it again with Autoruns.
- [ ] Enable command-line auditing and script block logging, run a command, and find it in the logs.
- [ ] Install Sysmon with a community configuration and write down five events it adds over the default logs.
- [ ] Do [Module 0.7](../../roadmap/phase-0-foundations/07-windows-and-lab.md) of the roadmap.

## Key references

CIS Benchmarks · LOLBAS Project · Microsoft Learn: Sysmon · Microsoft Learn: Windows security · Microsoft Security Baselines · MITRE ATT&CK · SwiftOnSecurity sysmon-config. Full list in [References](../15-references.md).
