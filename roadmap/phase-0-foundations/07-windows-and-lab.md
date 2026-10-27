# Module 0.7: Windows, PowerShell and finishing the lab (weeks 16-18)

Most enterprise environments are Windows and Active Directory, and most SOC alerts come from Windows. This module gives you a working command of Windows internals and PowerShell, and finishes building the home lab you will use for the rest of the roadmap.

**Main resources:** [Microsoft Learn PowerShell docs](https://learn.microsoft.com/en-us/powershell/), [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/), the Windows 11 and Windows Server 2025 evaluation VMs.

## Week 16: Windows internals and the command line

**Goal:** navigate and inspect a Windows system from both `cmd` and PowerShell, and understand its security model.

**R. Read and study (75 min)**
- Microsoft Learn: "What is PowerShell?" and "Discover PowerShell" (cmdlets, objects, the pipeline).
- Read about the Windows security model: users, groups, SIDs, access tokens, UAC, and NTFS permissions (ACLs). Microsoft Learn's "Access Control" overview.
- Notes: how PowerShell passes objects (not text) through the pipeline; what a SID and an access token are; NTFS ACLs vs Linux permissions; the registry's role.
- Flashcards: `Get-Process`, `Get-Service`, `Get-ChildItem`, SID, access token, UAC, HKLM vs HKCU.

**P. Guided practice (90 min)**
- On the Windows 11 VM, explore with PowerShell: list processes, services, local users and group memberships, scheduled tasks and autostart entries. Compare each command with its Linux equivalent from Module 0.2.
- Use `icacls` on a folder and compare its output with Linux `ls -l`.

**D. Deep practice (3 h)**
- Write a PowerShell script `Get-WinHostReport.ps1`, the Windows counterpart of your Bash `host-report.sh`: OS version, local admins, listening ports with owning process, scheduled tasks, autoruns, and the last logons from the Security event log.
- Run it and compare the report structure with your Linux one. Note what is easy to see on each OS and what is hidden.

**E. English (60 min)**
- Read a Microsoft Learn cmdlet reference page (e.g. `Get-WinEvent`). Note the structure (Syntax, Description, Examples, Parameters) and write a 4-sentence summary of what the cmdlet does.

**Check yourself**
1. How does the PowerShell pipeline differ from the Bash pipeline?
2. What is an access token, and what does it carry?
3. What does UAC actually do when it prompts?
4. How do NTFS ACLs differ from Linux `rwx` permissions?
5. Where do autostart programs hide on Windows, and why does that matter for persistence?

**Deliverable:** `Get-WinHostReport.ps1` with sample output, and a Linux-vs-Windows comparison note.

## Week 17: Windows logging, Sysmon and the attacker's view

**Goal:** know where Windows records activity, because this is what you will hunt through in Phase 2 and the defensive track.

**R. Read and study (75 min)**
- Microsoft Learn: Windows Event Logs overview; the Security log and important event IDs (4624/4625 logon, 4688 process creation, 4672 special privileges).
- Read about [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and why it adds detail the default logs lack.
- Notes: the main event channels; the event IDs above; what Sysmon logs (process creation with hashes, network connections, image loads); why attackers clear or avoid logs.
- Flashcards: event ID 4624 vs 4625, 4688, what Sysmon event ID 1 and 3 are, where event logs live on disk.

**P. Guided practice (90 min)**
- Install Sysmon on the Windows 11 VM with a known-good config ([SwiftOnSecurity's sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) is a well-documented starting point; [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular) is the modular, ATT&CK-mapped option).
- Perform benign "suspicious" actions (run `whoami`, download a file, open a network connection) and find each in the Sysmon and Security logs with `Get-WinEvent`.

**D. Deep practice (3 h)**
- Run a simple, well-documented technique against your own Windows VM from Kali (for example a basic authenticated remote command, nothing destructive), then switch to the defender's seat: find every trace in the Windows logs and Sysmon, and write a short timeline of what the logs show.
- Map each log entry to the [MITRE ATT&CK](https://attack.mitre.org/) technique it represents. This is exactly what a SOC analyst does.

**E. English (60 min)**
- Write a short "detection note" in English: the technique, the event IDs that reveal it, and what a defender should alert on. Use the report style from [writing-reports.md](../../english/writing-reports.md).

**Check yourself**
1. What is the difference between event ID 4624 and 4625?
2. What does Sysmon add that the default Windows logs do not?
3. Which event records process creation, and why is that central to detection?
4. Why do attackers try to clear or bypass the event log?
5. Where are the `.evtx` files stored, and why would a responder collect them?

**Deliverable:** your Sysmon install notes, the attack-and-detect timeline, and one detection note mapped to ATT&CK.

## Week 18: Finish and validate the home lab

**Goal:** a complete, isolated, snapshot-ready lab you will use for the next three phases.

**R. Read and study (75 min)**
- Re-read the [homelab guide](../../homelab/README.md) in full now that you understand networking, Linux and Windows.
- Notes: your final network diagram, every VM with its role and IP, and your snapshot and reset procedure.
- Flashcards: your lab subnets, which segment is isolated and why, the order to start VMs in.

**P. Guided practice (90 min)**
- Verify isolation: run [`check-isolation.sh`](../../homelab/scripts/check-isolation.sh) in each target VM; confirm the vulnerable and malware VMs cannot reach the internet or your home network.
- Take a baseline snapshot of every VM with [`snapshot-all.sh`](../../homelab/scripts/snapshot-all.sh) (VirtualBox) or the equivalent.

**D. Deep practice (3 h)**
- Bring the whole lab up together: OPNsense routing, Kali, the Docker target host with Juice Shop and DVWA, the Windows domain controller and workstation, and Wazuh. Enroll Wazuh agents on the Windows and Linux hosts and confirm events arrive.
- Run one end-to-end check: from Kali, scan the Docker host, and confirm the activity appears in Wazuh. You now have a working attack-and-detect environment.

**E. English (60 min)**
- Write the README for your lab in your notes repo in English: topology, purpose of each VM, how to reset, and the safety rules. Portfolio-quality.

**Check yourself**
1. Which VMs must never reach the internet, and how do you enforce that?
2. What is your procedure to reset a VM to a clean state?
3. In what order do you start the lab, and why does OPNsense come first?
4. How do you confirm a Wazuh agent is reporting?
5. What would you change in the lab to practice your chosen Phase 3 track?

**Deliverable:** a fully working lab, all VMs snapshotted, isolation verified, and a lab README in your notes repo. Tick the final Phase 0 boxes in [progress.md](../../progress.md).

## End of Phase 0

Before moving to Phase 1, you should be able to answer every check-yourself question in this phase without notes. If more than a few are shaky, repeat those weeks' R sessions. The [Phase 0 overview](README.md) lists the full mastery checklist.

Next: [Phase 1, security fundamentals](../phase-1-security-fundamentals/README.md).
