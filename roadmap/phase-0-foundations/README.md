# Phase 0: Foundations

**Duration:** 14 weeks at about 7 hours per week (roughly 100 hours).
**When:** Semester 2 and the following break. Networking gets a second pass when the degree's networking course starts.
**Prerequisites:** None.

Every later phase assumes you can work in a terminal, read a packet capture, write a small script and explain what the operating system is doing. Weak foundations show up later as slow, frustrating progress on labs, so this phase is worth doing properly.

## Objectives

By the end of this phase you can:

1. Work in a Linux shell without a GUI: navigate, edit and search files, manage permissions, processes, services, packages and SSH keys.
2. Explain the path of a web request (DNS resolution, TCP handshake, TLS handshake, HTTP exchange) and point to each step in a Wireshark capture.
3. Write Python scripts of 50 to 150 lines that use sockets, HTTP, files, regular expressions and `argparse`.
4. Use Git every day: commits, branches, merges, pull requests and conflict resolution.
5. Describe processes, threads, virtual memory, system calls, file systems and permissions on both Linux and Windows.

## Plan

| Weeks | Block | Main output |
|---|---|---|
| 1 | Git basics | This repo cloned locally, first commits on a branch, one merged pull request |
| 2-4 | Linux and the terminal | Linux Luminarium finished, Bandit levels 0-15 |
| 5-8 | Networking | Four annotated packet captures, subnetting drills |
| 9-11 | Python for security | The three scripts in [`exercises/`](exercises/) extended and committed |
| 12-14 | How operating systems work | OS notes, `strace` and Sysinternals exercises, Bandit up to level 25 |

## Resources

Ordered by priority. Free resources come first; paid options are listed separately and are never required.

### Linux and the terminal

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [pwn.college Linux Luminarium](https://pwn.college/linux-luminarium) | Free | Runs in the browser, no setup, assumes no prior Linux knowledge |
| 2 | [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) | Free | 34 levels over SSH; teaches the commands you will use in every lab |
| 3 | [The Linux Command Line](https://linuxcommand.org/tlcl.php), William Shotts | Free PDF (Creative Commons) | Reference book; read chapters as Bandit demands them |
| 4 | [Linux Journey](https://labex.io/linuxjourney) | Free | Short lessons; the original linuxjourney.com now redirects to this LabEx-hosted version |

### Networking

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [Professor Messer N10-009 Network+ videos](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) | Free videos | Full coverage of OSI, TCP/IP, addressing and common protocols |
| 2 | [Computer Networking: Principles, Protocols and Practice](https://github.com/CNP3/ebook), Olivier Bonaventure | Free (Creative Commons) | Open textbook; good for the "why" behind each protocol |
| 3 | [High Performance Browser Networking](https://hpbn.co/) | Free online | The TCP, TLS and HTTP chapters are the clearest explanations available |
| 4 | [The Illustrated TLS 1.3 Connection](https://tls13.xargs.org/) | Free | Every byte of a real handshake, explained |
| 5 | [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/) | Free | Display filters, following streams, statistics |
| 6 | Primary sources: [RFC 9293 (TCP)](https://www.rfc-editor.org/rfc/rfc9293), [RFC 1035 (DNS)](https://www.rfc-editor.org/rfc/rfc1035), [RFC 9110 (HTTP semantics)](https://www.rfc-editor.org/rfc/rfc9110), [RFC 8446 (TLS 1.3)](https://www.rfc-editor.org/rfc/rfc8446) | Free | Read the overview sections only; see [english/reading-professional-material.md](../../english/reading-professional-material.md) |

### Python for security

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | Your Data Structures and Algorithms course | Already covered | Use course assignments to practice clean Python |
| 2 | [Automate the Boring Stuff with Python, 3rd edition](https://automatetheboringstuff.com/) | Free online (CC BY-NC-SA) | Files, regex, web requests, automation |
| 3 | [Official Python tutorial](https://docs.python.org/3/tutorial/) and the docs for [`socket`](https://docs.python.org/3/library/socket.html), [`ssl`](https://docs.python.org/3/library/ssl.html), [`hashlib`](https://docs.python.org/3/library/hashlib.html), [`re`](https://docs.python.org/3/library/re.html) | Free | The modules security scripts use most |
| 4 | [Scapy documentation](https://scapy.readthedocs.io/en/latest/) | Free | Build and parse packets; use only inside your home lab |

### Git

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [Learn Git Branching](https://learngitbranching.js.org/) | Free | Visual, interactive; branching and rebasing make sense after an hour |
| 2 | [Pro Git](https://git-scm.com/book/en/v2) | Free | The reference book, kept up to date online |
| 3 | [GitHub Docs](https://docs.github.com/en) | Free | Pull requests, Actions, SSH keys |

### How operating systems work

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | Free | Virtualization, concurrency and persistence, with homework simulators |
| 2 | [Linux man-pages project](https://man7.org/linux/man-pages/) | Free | Read `proc(5)`, `signal(7)`, `capabilities(7)` and `credentials(7)` |
| 3 | [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) | Free tools | Process Explorer, Process Monitor and Autoruns show Windows internals directly |

### Paid options (optional)

| Resource | Cost (October 2026) | When it is worth it |
|---|---|---|
| [TryHackMe Premium](https://tryhackme.com/pricing) | About $14/month, or about $10/month on the annual plan | Only if you want guided paths such as Pre Security in one place. Free accounts get 650+ free rooms and one hour of AttackBox per day. |

## Required hands-on practice

- **Bandit:** levels 0-20 at minimum, 25 if time allows. Keep notes on *how* you solved each level in `private/` (ignored by Git). Never store level passwords in the public repo.
- **Linux Luminarium:** every module.
- **Packet captures:** record and annotate four captures in your home lab or on your own machine:
  1. A DNS lookup with `dig`, showing query, response and TTL.
  2. A TCP connection: three-way handshake, data, FIN or RST teardown.
  3. An HTTP/1.1 request to a local server (`python3 -m http.server`), followed with *Follow TCP Stream*.
  4. A TLS 1.3 handshake to a public site: find the ClientHello, the SNI, the offered cipher suites and key shares. Note that the server certificate is encrypted in TLS 1.3, unlike TLS 1.2.
- **Subnetting:** 20 problems by hand. Split a /24 into /26, /27 and /28 networks and give network, broadcast and usable range for each.
- **Scripts:** extend the three starter scripts in [`exercises/`](exercises/) as described there.
- **Git:** do all work in this repo on branches and merge through pull requests. Create and resolve one merge conflict on purpose.
- **Operating systems:**
  - Run `strace -f` on `ls` and on `curl`, and identify `execve`, `openat`, `connect` and `write`.
  - Inspect `/proc/<pid>/status` and `/proc/<pid>/maps` for a running process.
  - On a Windows VM, compare `icacls` output with Linux `ls -l`, and list autostart entries with Autoruns.
  - Find every listening service on a Linux VM with `ss -tlnp`, then identify the owning user with `ps`.

## You've mastered this phase when...

- [ ] You can redo Bandit levels 0-20 from scratch in under two hours without notes.
- [ ] You can explain, without notes, everything between typing `https://example.com` and seeing the page, naming the protocol, port and layer at each step.
- [ ] Given an unknown capture, you can isolate one TCP stream and identify the handshake, retransmissions and resets.
- [ ] You can subnet a /24 into /27 networks and state network, broadcast and usable range for each in under two minutes.
- [ ] You can read `rwx`, setuid, setgid and sticky bits and fix a misconfigured permission.
- [ ] You can explain the difference between a process and a thread, what a system call is, and show one with `strace`.
- [ ] Your three scripts run with `--help`, handle bad input without a stack trace, and are committed.
- [ ] You can create a branch, open a pull request and resolve a merge conflict without looking anything up.

Track these in [progress.md](../../progress.md). Course overlaps are covered in [degree-connections.md](../../degree-connections.md).

Next: [Phase 1, security fundamentals](../phase-1-security-fundamentals/README.md).
