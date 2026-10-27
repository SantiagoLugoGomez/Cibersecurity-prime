# Phase 0: Foundations

**Duration:** 18 weeks at about 7.5 hours per week (around 135 hours).
**When:** This semester and the following break.
**Prerequisites:** None.

Every later phase assumes you can work in a terminal, read a packet capture, write a script and explain what the operating system is doing. This is the longest foundational phase on purpose: weak foundations show up later as slow, frustrating progress on everything else.

Each module below is a separate file with the full week-by-week plan (R/P/D/E sessions, check-yourself questions and a deliverable per week). Read [the roadmap overview](../README.md) first for how the sessions work.

## Modules

| Module | Weeks | Topic |
|---|---|---|
| [0.1 Study setup and Git](01-study-setup-and-git.md) | 1 | Workstation, notes repo, Git branches and pull requests |
| [0.2 Linux and the command line](02-linux-command-line.md) | 2-4 | Shell, files, permissions, processes, services, SSH, text processing |
| [0.3 Bash scripting](03-bash-scripting.md) | 5 | Automating tasks with readable, safe scripts |
| [0.4 Networking](04-networking.md) | 6-9 | OSI/TCP-IP, subnetting, TCP/UDP, DNS/HTTP/TLS, scanning, firewalls |
| [0.5 Python for security](05-python-for-security.md) | 10-12 | Files, regex, sockets, HTTP, crypto, packaging a tool |
| [0.6 How operating systems work](06-operating-systems.md) | 13-15 | Processes, syscalls, memory, concurrency, filesystems, OS security |
| [0.7 Windows, PowerShell and the lab](07-windows-and-lab.md) | 16-18 | Windows internals, PowerShell, event logs, Sysmon, finishing the home lab |

## Objectives

By the end of this phase you can:

1. Work in a Linux shell without a GUI: navigate, edit and search files, manage permissions, processes, services, packages and SSH keys, and automate with Bash.
2. Explain the full path of a web request (DNS, TCP, TLS, HTTP) and point to each step in a packet capture, and subnet IPv4 by hand.
3. Write Python tools of 50 to 200 lines using sockets, HTTP, regex, hashing and `argparse`, packaged so others can run them.
4. Explain processes, system calls, virtual memory, concurrency, filesystems and the Unix/Windows permission models, and observe them live with `strace`, `/proc` and Sysinternals.
5. Operate a Windows system from PowerShell, read its event logs, and run and detect a basic technique.
6. Use Git daily, and run a complete, isolated home lab.

## Runnable exercises

The [`exercises/`](exercises/) folder holds three starter Python scripts (`port_check.py`, `http_headers.py`, `failed_logins.py`) with a safe sample log. Modules 0.5 and 0.7 extend them. They run with no third-party dependencies.

## You've mastered this phase when...

- [ ] You can redo Bandit levels 0-20 from scratch in under two hours without notes.
- [ ] You can explain, without notes, everything between typing `https://example.com` and seeing the page, naming the protocol, port and layer at each step.
- [ ] Given an unknown capture, you can isolate one TCP stream and identify the handshake, retransmissions and resets.
- [ ] You can subnet a /24 into /27 networks and state network, broadcast and usable range for each in under two minutes.
- [ ] You can read `rwx`, setuid, setgid and sticky bits, find dangerous ones, and explain the risk.
- [ ] You can explain `fork`/`execve`, a system call, a race condition and virtual memory, and show a syscall with `strace`.
- [ ] You have a packaged, documented Python tool installed from a clean virtual environment.
- [ ] You can inspect a Windows host from PowerShell, read its Security and Sysmon logs, and map an event to an ATT&CK technique.
- [ ] Your home lab runs end to end: an attack from Kali shows up in Wazuh.

Track these in [progress.md](../../progress.md). Course overlaps are in [degree-connections.md](../../degree-connections.md).

Next: [Phase 1, security fundamentals](../phase-1-security-fundamentals/README.md).
