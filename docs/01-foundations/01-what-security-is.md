# What security is

> [!TIP]
> **In short:** security is the discipline of reasoning about how a system can fail when someone is trying to make it fail. You name what you protect (assets), who or what can hurt it (threats), the weaknesses that allow it (vulnerabilities), and the controls that reduce the damage. Every other topic in this handbook is a detail of that loop. Learn the vocabulary precisely, because most arguments in security are arguments about word choice.

## Why start here

Tools change every year. The questions do not. Whether you are reading a firewall rule, a TLS handshake or a ransomware report, you are always answering the same four things: what is being protected, from whom, how it can break, and what we do about it. If you can answer them for a system you have never seen, you can learn any tool on top.

## The vocabulary that must be exact

These terms get mixed up constantly, including in professional reports. Mixing them up changes the meaning of a finding.

| Term | Meaning | Example |
|---|---|---|
| **Asset** | Anything of value to the organization or the user | Customer database, signing key, uptime of a payment API |
| **Threat** | A potential cause of harm | Ransomware crew, malicious insider, flood that takes down a data center |
| **Threat actor** | The party that carries out a threat | Criminal group, state-backed team, disgruntled employee |
| **Vulnerability** | A weakness that a threat can use | Unpatched library, missing authorization check, default password |
| **Exploit** | A method or code that uses a vulnerability | A script that sends a crafted request to the unpatched library |
| **Attack** | An attempt to cause harm, using an exploit or another technique | The crew sends that request to your server |
| **Control** | Anything that reduces likelihood or impact | MFA, patching, backups, network segmentation, a policy |
| **Risk** | The possibility of loss, combining how likely it is and how bad it would be | "Probable loss of the customer database through the unpatched library" |
| **Incident** | A confirmed event that harms or threatens security | The database was copied |
| **Breach** | An incident in which protected data was accessed or disclosed without authorization | Records appear for sale |

Three consequences follow from the table.

1. A vulnerability alone is not a risk. A critical flaw on a machine nobody can reach carries little risk; a modest flaw on an internet-facing login page may carry a lot.
2. An exploit is not a vulnerability. The weakness exists before anyone writes code for it, and it keeps existing after the exploit is gone.
3. Risk is always about a specific asset, threat and impact. "The network is high risk" is not a finding.

**Practical implication:** when you write or read a finding, check that it names an asset, a weakness and an impact. If one is missing, the finding is incomplete.

## The security properties

The classic triad has three properties. Real work usually needs a few more.

| Property | Question it answers | Typical attack | Typical control |
|---|---|---|---|
| **Confidentiality** | Can only the right parties read it? | Data theft, eavesdropping, misconfigured storage | Encryption, access control, data classification |
| **Integrity** | Can it be changed only by the right parties, and would we notice otherwise? | Tampering, supply chain compromise, SQL injection that rewrites data | Hashes and signatures, input validation, write access limits |
| **Availability** | Is it there when it is needed? | Ransomware, denial of service, deleting backups | Redundancy, backups, capacity, rate limiting |
| **Authenticity** | Is it really from who it claims? | Phishing, spoofed email, forged tokens | Digital signatures, MFA, certificate validation |
| **Accountability** | Can we tell who did what? | Shared accounts, log deletion | Individual accounts, tamper-resistant logs |
| **Non-repudiation** | Can the actor deny it later? | Disputed transactions | Signatures, audit trails with trusted timestamps |
| **Privacy** | Is personal data used only for the stated purpose? | Over-collection, secondary use, re-identification | Data minimization, consent, retention limits |

The triad is a checklist, not a theory. When you analyze an incident, ask which property was violated first; the answer often points to the control that was missing. A ransomware attack is primarily an availability attack, but modern groups also steal data first, so confidentiality is hit as well. That "double extortion" pattern is why backups alone no longer end the story.

Some controls trade properties against each other. Strong encryption protects confidentiality and, if the key is lost, destroys availability. Aggressive logging helps accountability and can harm privacy. Good security design makes these trade-offs explicit instead of discovering them in production.

## Controls: how to classify them

Controls are grouped in two ways at once: by what they do, and by what kind of thing they are.

| By function | What it does | Example |
|---|---|---|
| Preventive | Stops the event | MFA, firewall rule, input validation |
| Detective | Notices the event | Log alert, file integrity monitoring, IDS |
| Corrective | Limits damage and restores | Restoring from backup, isolating a host |
| Deterrent | Discourages the actor | Banners, visible cameras, legal notices |
| Compensating | Substitutes when the ideal control is not possible | Network isolation for a system that cannot be patched |

| By nature | Example |
|---|---|
| Technical | Encryption, endpoint protection, access control lists |
| Administrative | Policies, training, background checks, approval workflows |
| Physical | Locks, badge readers, cable protection |

A mature program has all three functions for its most important assets. Teams that only invest in prevention discover that prevention eventually fails and that they have no way to notice. Teams that only invest in detection get a very detailed record of their own compromise.

## Why security is hard

Several structural facts explain why good intentions are not enough.

- **Asymmetry.** The defender has to cover every path; the attacker needs one. The defender usually also has to keep the business running while doing it. **●●●**
- **Complexity.** Systems are built from layers written by different parties. Each interface is a place where assumptions differ, and security bugs live in the gaps between components more often than inside them.
- **Humans.** People reuse passwords, click links and bypass controls that slow them down. A control that users work around has failed, even if it works on paper (see *psychological acceptability* in [Security principles](02-security-principles.md)).
- **Economics.** The party who could fix a problem is often not the party who pays for it. Anderson and Moore describe how misaligned incentives, such as vendors shipping insecure defaults while customers absorb the damage, explain many persistent failures (Anderson and Moore, 2006). **●●○**
- **Invisible failure.** A system can be insecure for years with no visible symptom. Unlike a crashed server, a compromise does not announce itself.

**Practical implication:** do not ask "is it secure?". Ask "against which attackers, for which assets, at what cost to them and to us?". The first question has no answer; the second does.

## Reading incidents: five short case studies

Real incidents are the best training data. The pattern to look for is a chain: a small weakness, a missed control, then a large impact. The summaries below follow public reporting; treat them as simplified.

| Incident | Property hit | Reported root cause | Control that would have changed the outcome |
|---|---|---|---|
| **Equifax, 2017** | Confidentiality | A known flaw in Apache Struts (CVE-2017-5638) left unpatched on an internet-facing system; roughly 147 million people affected | Asset inventory and timely patching; segmentation; detection of unusual data egress |
| **Capital One, 2019** | Confidentiality | A server-side request forgery in a misconfigured web application firewall let the attacker obtain cloud credentials from the instance metadata service and read storage buckets | Least-privilege role, IMDSv2, egress filtering, alerting on unusual API use (see [Cloud IAM and attack paths](../08-cloud-and-infrastructure/02-cloud-iam-and-attack-paths.md)) |
| **SolarWinds, 2020** | Integrity | Attackers compromised the build system and inserted a backdoor into signed software updates delivered to thousands of customers | Build pipeline hardening, reproducible builds, behavior-based detection after install |
| **Colonial Pipeline, 2021** | Availability | Ransomware operators entered through a VPN account that reportedly lacked MFA; the company shut down operations to contain the spread | MFA on remote access, segmentation between IT and operational systems, tested recovery |
| **Uber, 2022** | Confidentiality, integrity | An attacker bought or obtained a contractor's credentials, repeatedly pushed MFA approval requests until the victim accepted, then found privileged credentials in an internal script | Phishing-resistant MFA, number matching, secrets management instead of credentials in scripts |

Notice what these have in common: none required an unknown, exotic exploit. Each combined an ordinary weakness (patching, a default, missing MFA, a stored secret) with a missing detective or containing control. That pattern is why the fundamentals in this handbook matter more than any single technique. **●●○**

## The security mindset

A few habits distinguish people who are good at this from people who know a lot of facts.

1. **Question assumptions.** Every system rests on assumptions ("only employees can reach this", "this ID is random"). Security work is mostly finding the one that is false.
2. **Think in paths.** Draw how an attacker gets from where they are to what they want. Controls are valuable where they cut many paths.
3. **Assume breach.** Design as if one component is already compromised, and ask what limits the damage. This is the core idea behind segmentation, least privilege and zero trust.
4. **Prefer simple, verifiable controls.** A control you can test and explain beats a clever one you cannot.
5. **Hold both views.** An attacker who does not understand the defense wastes time; a defender who does not understand the attack builds the wrong controls. This handbook teaches each topic from both sides.

## What to do with this

- [ ] Memorize the table of terms and use them precisely in everything you write.
- [ ] For a recent breach in the news, name the asset, the weakness, the property violated and the control that was missing.
- [ ] Take a system you use daily (your phone, your university portal) and list its three most valuable assets and one threat to each.
- [ ] Do [Module 1.1 of the roadmap](../../roadmap/phase-1-security-fundamentals/01-principles-threat-modeling.md), which turns this page into exercises.

## Key references

Anderson (2020) · Anderson and Moore (2006) · NIST CSF 2.0 · NIST SP 800-30 Rev. 1 · RFC 4949 · Saltzer and Schroeder (1975). Full list in [References](../15-references.md).
