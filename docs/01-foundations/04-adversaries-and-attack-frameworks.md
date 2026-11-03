# Adversaries and attack frameworks

> [!TIP]
> **In short:** defenses make sense only against a specific kind of attacker. Most organizations face **financially motivated criminals** far more often than state-backed teams. To talk about what attackers do, the field uses shared frameworks: the **Cyber Kill Chain** for the shape of an intrusion, **MITRE ATT&CK** for the concrete behaviors, the **Diamond Model** for analysis and the **Pyramid of Pain** for choosing what to detect. Learn ATT&CK well; it is the common language of reports, detections and tests.

## Who attacks

| Actor | Main motive | Typical behavior | Implication for defense |
|---|---|---|---|
| **Cybercriminals** (ransomware affiliates, fraud rings, access brokers) | Money | Opportunistic scanning, phishing, stolen credentials, exploiting known flaws quickly; double extortion | Patching speed, MFA, backups, detection of mass encryption and data staging |
| **State-backed groups (APT)** | Espionage, sabotage, influence | Patient, well resourced, custom tooling, supply chain and zero-day use against selected targets | Strong monitoring, segmentation, assume long dwell time |
| **Hacktivists** | Ideology, publicity | Defacement, DDoS, data leaks, often against visible targets | DDoS protection, web hardening, incident communications |
| **Insiders** (malicious or negligent) | Grievance, money, or none (mistakes) | Misuse of legitimate access, mis-sent data, shadow IT | Least privilege, logging, data loss controls, offboarding |
| **Opportunists** ("script kiddies") | Curiosity, status | Run public tools against whatever answers | Basic hygiene stops most of them |

Two points correct common intuitions.

- **The most likely attacker is the least glamorous.** Large breach studies such as the Verizon *Data Breach Investigations Report* have for years found that most breaches are financially motivated, and that the most common entry routes are stolen credentials, phishing and exploitation of known vulnerabilities (Verizon DBIR). The 2026 edition reports vulnerability exploitation as the most common initial access vector, ahead of credential abuse. **●●○**
- **The criminal economy is specialized.** Groups buy and sell access (*initial access brokers*), rent ransomware (*ransomware as a service*), and use commodity loaders and infostealers. An attacker with little skill can still do serious damage by purchasing the early stages of an intrusion. **●●○**

**Practical implication:** build for the attacker you will actually meet. For most organizations that means credential theft, phishing and unpatched internet-facing systems, followed by ransomware.

### Reading actor names

Reports use many names for the same group. MITRE ATT&CK assigns group IDs (G####), and vendors use their own naming. Microsoft's taxonomy encodes origin in the name: *Blizzard* for Russia, *Typhoon* for China, *Sandstorm* for Iran, *Sleet* for North Korea and *Tempest* for financially motivated actors. When you read a report, look for the technique list rather than the name; the behaviors are what you can detect.

## The Cyber Kill Chain

Lockheed Martin analysts described an intrusion as seven sequential phases (Hutchins et al., 2011). **●●●**

| # | Phase | What the attacker does | Defender's chance |
|---|---|---|---|
| 1 | Reconnaissance | Researches the target, finds people and exposed systems | Limit public information; monitor for scanning |
| 2 | Weaponization | Prepares an exploit and payload | Usually invisible to the defender |
| 3 | Delivery | Sends it (phishing, drive-by, USB) | Email and web filtering, user training |
| 4 | Exploitation | Triggers a vulnerability or user action | Patching, application hardening |
| 5 | Installation | Establishes persistence | Endpoint detection, application control |
| 6 | Command and control | Opens a channel back to the attacker | Egress filtering, DNS and proxy monitoring |
| 7 | Actions on objectives | Steals, destroys or encrypts | Data loss controls, segmentation, backups |

The idea is that stopping the attacker at *any* phase breaks the chain, and the earlier the better. The model's limits are real: it is linear, built around a perimeter, and says little about what happens after the first foothold (lateral movement, privilege escalation), insiders, or cloud environments. Use it as a mental picture, and use ATT&CK for detail.

## MITRE ATT&CK

ATT&CK is a publicly available knowledge base of adversary behavior, built from observed real-world intrusions and maintained by MITRE. **●●●** Its structure has four levels.

| Level | Meaning | Example |
|---|---|---|
| **Tactic** | The attacker's short-term goal (the "why") | Credential Access |
| **Technique** | How the goal is achieved (the "how") | OS Credential Dumping (T1003) |
| **Sub-technique** | A specific variant | LSASS Memory (T1003.001); Kerberoasting (T1558.003) |
| **Procedure** | The exact way a group or tool did it | A named tool reading LSASS memory with a specific API call |

Identifiers follow patterns: tactics `TA####`, techniques `T####`, sub-techniques `T####.###`, groups `G####`, software `S####`, campaigns `C####` and mitigations `M####`.

### The Enterprise tactics (ATT&CK v19 and later)

ATT&CK v19, released on 28 April 2026, split the long-standing *Defense Evasion* tactic into two, which brought the Enterprise matrix to 15 tactics. The same release reports 222 techniques and 475 sub-techniques. **●●○** Older material still refers to Defense Evasion; read it as the union of the two new tactics.

| ID | Tactic | Goal in one line |
|---|---|---|
| TA0043 | Reconnaissance | Gather information to plan the attack |
| TA0042 | Resource Development | Build or buy infrastructure, accounts and tools |
| TA0001 | Initial Access | Get a first foothold |
| TA0002 | Execution | Run attacker-controlled code |
| TA0003 | Persistence | Keep access across restarts and credential changes |
| TA0004 | Privilege Escalation | Obtain higher rights |
| TA0005 | **Stealth** (formerly Defense Evasion) | Hide activity so it looks normal |
| TA0112 | **Defense Impairment** | Disable or degrade security tooling and logging |
| TA0006 | Credential Access | Steal account names and secrets |
| TA0007 | Discovery | Learn the environment |
| TA0008 | Lateral Movement | Move to other systems |
| TA0009 | Collection | Gather data of interest |
| TA0011 | Command and Control | Communicate with compromised systems |
| TA0010 | Exfiltration | Take data out |
| TA0040 | Impact | Disrupt, destroy or encrypt |

The split tracks defender thinking. Hiding in plain sight (blending in with normal tools and traffic) and breaking the defender's tools (stopping an agent, clearing logs) call for different detections, so they are now different tactics. Some techniques are mapped to both, because intent is not always clear. **●●○**

### What ATT&CK is good for

- **A shared vocabulary.** "T1558.003" means the same thing to every team and vendor.
- **Mapping intelligence.** Tag a report's techniques and see which you cannot detect.
- **Planning detection coverage.** The ATT&CK Navigator colors a matrix by what you can see (see [Detection engineering](../07-defensive-security/02-detection-engineering.md)).
- **Adversary emulation.** Run tests per technique to check detections (for example with Atomic Red Team).
- **Reporting.** Tie findings to behaviors executives and other teams can look up.

### What it is not

- **Not a checklist to complete.** Having a detection tagged to a technique does not mean you detect it. A technique has many procedures, and one rule rarely covers all of them.
- **Not equally weighted.** Some techniques appear in nearly every intrusion (valid accounts, PowerShell, scheduled tasks); others are rare. Prioritize by relevance to the actors in your threat model.
- **Not stable.** Techniques are added, merged and renamed with each release. Always record the version when you cite an ID.

### Companion resources

| Resource | Purpose |
|---|---|
| **CVE** | Identifier for a specific vulnerability |
| **CWE** | Classification of weakness types (for example CWE-79, cross-site scripting) |
| **CAPEC** | Catalog of attack patterns against applications and systems |
| **D3FEND** | Knowledge graph of defensive techniques, mapped to ATT&CK |
| **ATLAS** | An ATT&CK-style matrix for attacks on machine learning systems |

## The Diamond Model

The Diamond Model describes every intrusion event with four core features: **adversary**, **capability**, **infrastructure** and **victim**, connected as a diamond (Caltagirone et al., 2013). **●●○** Its practical value is *pivoting*: when you know one vertex (a malware sample), you ask what it tells you about the others (the infrastructure it talks to, the victims who share it, the actor who owns the capability). Analysts use it to cluster events into activity groups and campaigns.

## The Pyramid of Pain

David Bianco's pyramid ranks the indicators you can detect by how much it hurts the attacker when you deny them (Bianco, 2013). **●●○**

| Level | Indicator | Cost to attacker when blocked | Cost to defender to detect |
|---|---|---|---|
| 6 (top) | **TTPs** (behavior) | Tough: they must change how they operate | High: needs understanding and good telemetry |
| 5 | Tools | Challenging: they must find or build new tools | Medium |
| 4 | Network and host artifacts | Annoying: they must change their implants | Medium |
| 3 | Domain names | Simple: register another | Low |
| 2 | IP addresses | Easy: change address | Low |
| 1 (bottom) | File hashes | Trivial: recompile | Very low |

**Practical implication:** hashes and IP addresses are cheap to block and cheap to evade; they are useful for fast triage and known-bad matching. Durable detection comes from behaviors. When you write a detection, ask which level of the pyramid it targets.

## The Unified Kill Chain

The Unified Kill Chain extends the original model to eighteen phases grouped into three cycles: getting *in*, moving *through* the network, and getting *out* with the objective (Pols, 2017). **●●○** It exists to cover what the 2011 model leaves out, namely lateral movement and escalation inside the environment. If you want a single model for a full intrusion narrative, it is a better fit than the seven-phase chain.

## Worked example: mapping an intrusion

An incident summary: a user opens an email attachment, a macro starts PowerShell, a beacon connects to an external server, the attacker requests service tickets for service accounts, cracks one offline, uses it to log on to a file server over SMB, copies documents to a staging folder, uploads them to cloud storage and then runs ransomware.

| Step | Kill chain phase | ATT&CK tactic | Example technique | Where to detect |
|---|---|---|---|---|
| Phishing with attachment | Delivery | Initial Access | Phishing: spearphishing attachment (T1566.001) | Mail gateway, user reports |
| Macro starts PowerShell | Exploitation, installation | Execution | Command and scripting interpreter: PowerShell (T1059.001) | Process creation (Event 4688 or Sysmon 1), script block logging (4104) |
| Beacon to external server | Command and control | Command and Control | Application layer protocol: web (T1071.001) | Proxy and DNS logs, beaconing analysis |
| Service ticket requests | Actions on objectives (early) | Credential Access | Steal or forge Kerberos tickets: Kerberoasting (T1558.003) | Event 4769 with weak encryption type for service accounts |
| Logon to file server | Actions on objectives | Lateral Movement | Remote services: SMB/Windows admin shares (T1021.002) | Event 4624 logon type 3, unusual account-host pairs |
| Staging and upload | Actions on objectives | Collection, Exfiltration | Archive collected data (T1560); exfiltration to cloud storage (T1567.002) | Large outbound transfers, new cloud destinations |
| Ransomware execution | Actions on objectives | Impact | Data encrypted for impact (T1486) | Mass file modification, shadow copy deletion |

Reading the table top to bottom shows how many chances the defender had. The earlier steps are the cheapest to catch and the least costly to remediate. This mapping is the core skill of [Module 1.5](../../roadmap/phase-1-security-fundamentals/05-network-defense-monitoring.md).

## Which framework for which job

| Job | Use |
|---|---|
| Explain an intrusion to a non-specialist | Cyber Kill Chain or Unified Kill Chain |
| Describe behavior precisely; plan detections; map intelligence | MITRE ATT&CK |
| Cluster events into campaigns and attribute | Diamond Model |
| Decide which indicators are worth detecting | Pyramid of Pain |
| Classify a vulnerability or weakness | CVE, CWE |
| Pick defensive countermeasures | D3FEND, CIS Controls, NIST CSF |

## What to do with this

- [ ] Memorize the 15 Enterprise tactics in order, with a one-line goal for each.
- [ ] Take a public incident report (for example from The DFIR Report) and map each step to a tactic and technique, noting the ATT&CK version.
- [ ] Place five detections you know on the Pyramid of Pain and decide which are weakest.
- [ ] Build an ATT&CK Navigator layer for an attack you ran in your lab, as in [Module 1.5](../../roadmap/phase-1-security-fundamentals/05-network-defense-monitoring.md).

## Key references

Bianco (2013) · Caltagirone et al. (2013) · Hutchins et al. (2011) · MITRE ATT&CK · MITRE ATT&CK v19 release notes · Pols (2017) · Verizon DBIR. Full list in [References](../15-references.md).
