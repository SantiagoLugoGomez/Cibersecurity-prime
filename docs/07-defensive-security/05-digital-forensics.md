# Digital forensics

> [!TIP]
> **In short:** forensics is the discipline of answering "what actually happened?" from evidence that can **survive being challenged**. During an incident this means two things at once: follow the **order of volatility** so you capture what disappears first (memory, network state) before what persists (disk, logs), and keep a **chain of custody** so that what you captured can be trusted later, by your own team, by auditors, or in court. The tools matter less than the discipline: a perfect memory capture handled carelessly is weaker evidence than an ordinary disk image handled correctly.

## Why forensics is its own discipline inside incident response

[Incident response](04-incident-response.md) describes containment and recovery; forensics is what makes the *conclusions* behind those decisions defensible. "The attacker did not reach the database" is either a forensic finding, backed by evidence you can show your work on, or it is a guess. The difference matters most exactly when the stakes are highest: a legal proceeding, a regulatory inquiry, or simply a postmortem someone outside the response team needs to trust.

## Order of volatility

Evidence decays at different rates. Capture in this order, adapting to what the incident actually needs:

| Order | Evidence | Why it goes early |
|---|---|---|
| 1 | **CPU registers, cache** | Gone the instant power changes or the process ends; rarely practical to capture outside specialized tooling |
| 2 | **RAM (memory)** | Running processes, network connections, injected code, encryption keys, and malware that never touches disk all live here; lost completely on power-off or reboot |
| 3 | **Network state** | Active connections, ARP tables, routing tables; changes constantly |
| 4 | **Running system state** | Logged-on users, open files, loaded drivers |
| 5 | **Disk** | Persists through a reboot, but files get overwritten, logs rotate, and attackers may actively delete data |
| 6 | **Remote logging and backups** | Already captured elsewhere, so least urgent to re-collect, but confirm it actually has what you need before assuming so |
| 7 | **Physical configuration and topology** | Rarely time-critical |

**Practical implication:** the instinct to "pull the plug" on a compromised machine is usually wrong. Powering off destroys memory evidence and network state permanently, for a benefit (stopping active damage) that isolation at the network layer often achieves without the cost. Reserve power-off for genuinely destructive, fast-moving threats (a wiper actively running), as covered in the containment table in [Incident response](04-incident-response.md#containment-strategies-compared).

## Chain of custody

A chain of custody is a continuous, documented record of who had possession of a piece of evidence, from collection to its final use, with no gap unaccounted for. Without it, the honest answer to "how do you know this wasn't altered?" is "we don't," which can make strong technical evidence worthless in any proceeding that challenges it.

| Element | What to record |
|---|---|
| **Identification** | What the evidence is, where it came from, a unique identifier |
| **Collection details** | Who collected it, when, how, with what tool and version |
| **Integrity verification** | A cryptographic hash (SHA-256) taken at collection, and verified again at every subsequent access |
| **Every transfer** | Who had it, from whom, to whom, when, why |
| **Storage** | Where it is kept, who can access it, how access is logged |

```
Evidence: disk image, host WKS-042
Collected by: A. Ramirez, 2026-11-03 14:30 UTC
Method: dd via write-blocked external enclosure
SHA-256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
Stored: encrypted evidence volume, access logged
Transfers: none since collection
```

Verify the hash again every time the evidence is accessed, and log the verification. A hash mismatch is itself a finding: either corruption or tampering, and either way the evidence's reliability from that point needs to be addressed explicitly, not quietly worked around.

## Collecting memory

Memory capture needs to happen while the system is running, with a tool that minimizes its own footprint, because the act of capturing memory necessarily changes memory slightly. Tools exist for live acquisition on each major platform (for example, built-in utilities and vendor tools for Windows; `/proc`-based or kernel-module tools on Linux; dedicated agents for cloud instances where you cannot physically touch the hardware).

Once captured, an image can be analyzed with an open-source framework such as **Volatility**, which can enumerate running and hidden processes, network connections at the time of capture, loaded drivers and kernel modules, and in many cases recover injected code or extract strings and credentials still resident in memory. Memory analysis is how you find malware that never wrote a file to disk at all, which disk forensics alone cannot see.

## Disk and file system artifacts

| Artifact (Windows) | What it shows |
|---|---|
| **`$MFT` (NTFS Master File Table)** | Every file's metadata, including some that were deleted; timestamps |
| **Prefetch files** | Which executables ran and roughly when, even after the executable itself is gone |
| **Shimcache / Amcache** | Evidence of program execution, including from removable media |
| **Registry hives** (`NTUSER.DAT`, `SYSTEM`, `SOFTWARE`) | User activity, installed software, USB device history, run keys, network history |
| **Event logs** | See [Logging and telemetry](01-logging-and-telemetry.md) and the Windows-specific events in [Windows internals](../02-systems/02-windows-internals-for-security.md) |
| **Volume Shadow Copies** | Point-in-time snapshots that can reveal prior versions of files, including ones an attacker deleted |
| **Browser artifacts** | History, downloads, cached credentials |

| Artifact (Linux) | What it shows |
|---|---|
| **Shell history** | Commands run, though trivially alterable, so corroborate with other sources |
| **`auditd` logs** | See the rules introduced in [Privilege escalation](../06-offensive-security/04-privilege-escalation.md) |
| **`/var/log/`** | Authentication, system and service logs |
| **File timestamps (MACB)** | Modified, accessed, changed, born; interpret carefully, since many legitimate actions also change them |
| **Cron and systemd timers** | Persistence mechanisms |

**Timestamps deserve care.** "Modified, accessed, changed, born" (MACB) timestamps are easy to misread and, on some file systems, easy for an attacker to manipulate deliberately (timestomping). Treat a single timestamp as a lead, not a conclusion, and corroborate it against independent sources: a log entry, a network record, another artifact that could not have been altered the same way.

## Triage and collection at scale

A full disk image of every potentially involved host does not scale to a real incident touching dozens or hundreds of machines, and it is usually unnecessary. **Triage collection** gathers a defined, prioritized set of artifacts (the tables above) quickly from many hosts, so you can scope an incident before deciding which few hosts need a full forensic image.

| Tool | Role |
|---|---|
| **KAPE** | Collects and processes a configurable set of forensic artifacts from Windows hosts quickly, for triage at scale |
| **Velociraptor** | An open-source endpoint monitoring and response platform that can hunt for artifacts across a fleet of hosts remotely, built for exactly this kind of large-scale triage |
| Built-in and lightweight live-response scripts | Useful for a single host when no other tooling is deployed |

**A dual-use note:** tools built for legitimate large-scale remote triage, Velociraptor among them, are powerful enough that attackers have also installed them on compromised networks to use the same capability for their own reconnaissance and persistence. Treat any instance of such tooling you did not deploy yourself as a finding, and restrict who can deploy and control your own instance, the same discipline covered for other dual-use software in [Reconnaissance and enumeration](../06-offensive-security/02-reconnaissance-and-enumeration.md).

## Cloud and ephemeral environments

Forensics assumptions built around a physical disk you can seize do not transfer directly to the cloud:

| Challenge | Approach |
|---|---|
| **Ephemeral instances** (containers, auto-scaled virtual machines) | The evidence may vanish when the resource is terminated; snapshot or preserve before any termination, and build this into automated scaling policies in advance |
| **No physical access** | Rely on the provider's own snapshot, logging and forensic-image capabilities |
| **Shared responsibility** | Know what logs and images the provider gives you versus what you must have instrumented yourself; see [Cloud security fundamentals](../08-cloud-and-infrastructure/01-cloud-security-fundamentals.md) |
| **Control-plane evidence** | Who changed what, via the provider's API, is often the most important evidence and lives in the cloud audit log, not on any instance |

## Writing it up

A forensic finding is only as useful as its explanation. Structure findings the way a reader who was not in the room needs them:

| Section | Content |
|---|---| 
| **Question asked** | What you were trying to determine |
| **Evidence examined** | What sources, with chain-of-custody references |
| **Methodology** | What you did, specifically enough to be reproduced |
| **Findings** | What the evidence shows, distinguished clearly from interpretation |
| **Limitations** | What the evidence cannot tell you, stated honestly |
| **Conclusion** | Your answer to the original question, with its confidence level |

Being explicit about limitations is not a weakness in the write-up; a reviewer who finds an unstated limitation on their own will distrust everything else in the report.

## Practice

1. In your lab, capture a memory image of a running VM, then use Volatility to list its running processes and network connections, and compare that list against what you know you started.
2. Create a file, note its SHA-256 hash, copy it, and verify the hash matches. Then modify one byte and show the hash changes, as a concrete demonstration of why integrity verification matters.
3. Run a KAPE or equivalent triage collection against a lab Windows VM and identify, from the collected artifacts alone, which programs ran in the last hour.
4. Write a one-page chain-of-custody log for a piece of "evidence" (any file) as you move it between two machines in your lab.
5. Take one finding from an earlier lab exercise and rewrite it using the report structure above, being explicit about its limitations.

These support [Module 2.4](../../roadmap/phase-2-guided-practice/04-blue-team-labs.md) and the [defensive track](../../roadmap/phase-3-specialization/track-defensive.md) of the roadmap.

## What to do with this

- [ ] Explain the order of volatility from memory and say why "pull the plug" is usually the wrong first move.
- [ ] Explain chain of custody well enough to describe what breaks when a transfer goes unrecorded.
- [ ] Capture and analyze one memory image in your lab.
- [ ] List five Windows and five Linux artifacts from the tables above and what each one shows.
- [ ] Write one forensic finding using the structure above, including an honest limitations section.

## Key references

Carrier (2005) · NIST SP 800-61 Revision 3 · SANS digital forensics posters and course material · Volatility Foundation documentation. Full list in [References](../15-references.md).
