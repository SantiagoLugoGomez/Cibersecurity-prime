# Start here

> [!TIP]
> **In short:** `docs/` is a reference knowledge base: concepts, evidence and depth, organized by topic rather than by week. [`roadmap/`](../roadmap/README.md) is the schedule: what to read and practice, in what order, on what week. Use the roadmap to decide what to study next; come to `docs/` for the full, verified treatment of that topic, then go back to the roadmap for the hands-on exercise. This page is the map between the two, plus the one-hour setup that makes everything else in this repository usable.

## How this repository fits together

| Folder | Answers | Use it when |
|---|---|---|
| [`docs/`](../docs) (this folder) | "What is this, exactly, and why does it work this way?" | You want the concept explained properly, with evidence, before or after practicing it |
| [`roadmap/`](../roadmap/README.md) | "What do I study this week?" | You want the next concrete assignment: readings, exercises, a deliverable |
| [`homelab/`](../homelab/README.md) | "What do I actually build to practice on?" | You are setting up or extending your lab environment |
| [`writeups/`](../writeups/README.md) | "How do I document what I did?" | You finished a machine, challenge or exercise and need to write it up |
| [`templates/`](../templates/README.md) | "What structure do I fill in?" | You need a reusable template rather than writing a structure from scratch |
| [`tools/`](../tools/README.md) | "I need a quick calculation or lookup, offline." | Subnetting, entropy, a JWT, a hash, a port number |
| [`english/`](../english/README.md) | "How do I build the English this field runs on?" | Vocabulary, reading, writing reports, speaking practice |

`docs/` and `roadmap/` are written to point at each other: most pages here end with "These support Module X.Y of the roadmap," and the roadmap's weekly sessions assume you will come here for the full explanation behind a topic it assigns briefly.

## I want to learn about...

| Topic | Start at |
|---|---|
| What security actually is, and why it is hard | [01-foundations/01-what-security-is.md](01-foundations/01-what-security-is.md) |
| Threat modeling, STRIDE, attack trees | [01-foundations/03-threat-modeling.md](01-foundations/03-threat-modeling.md) |
| Colombian cybercrime law and ethics | [01-foundations/05-legal-and-ethics.md](01-foundations/05-legal-and-ethics.md) |
| Linux, Windows and Active Directory internals | [02-systems/](02-systems/01-linux-for-security.md) |
| Networking, packet analysis, Nmap | [03-networking/](03-networking/01-models-and-addressing.md) |
| Cryptography, PKI, TLS, passwords, OAuth, Kerberos | [04-cryptography-and-identity/](04-cryptography-and-identity/01-cryptography-foundations.md) |
| Web and API security, the OWASP Top 10, LLM security | [05-application-security/](05-application-security/01-browser-security-model-and-headers.md) |
| Penetration testing, privilege escalation, red teaming | [06-offensive-security/](06-offensive-security/01-penetration-testing-methodology.md) |
| SOC, detection engineering, incident response, forensics | [07-defensive-security/](07-defensive-security/01-logging-and-telemetry.md) |
| Cloud security, IAM attack paths, Kubernetes | [08-cloud-and-infrastructure/](08-cloud-and-infrastructure/01-cloud-security-fundamentals.md) |
| Malware analysis and reverse engineering | [09-malware-and-reverse-engineering/](09-malware-and-reverse-engineering/01-malware-landscape.md) |
| Risk, frameworks, compliance, privacy | [10-governance-risk-and-compliance/](10-governance-risk-and-compliance/01-risk-management.md) |
| How to actually study this and build a career | [11-learning-and-career/](11-learning-and-career/01-learning-science.md) |
| Whether you are actually making progress | [12-measuring-progress/](12-measuring-progress/01-how-to-measure-progress.md) |
| A myth you want checked, a term you forgot, a source | [13-myths.md](13-myths.md) · [14-glossary.md](14-glossary.md) · [15-references.md](15-references.md) |

## Starting points by background

| You are... | Do this |
|---|---|
| **A complete beginner** | Read [01-foundations](01-foundations/01-what-security-is.md) in full first, in order; everything else assumes its vocabulary. Then follow [Phase 0 of the roadmap](../roadmap/phase-0-foundations/README.md) week by week, reading the matching `docs/` page each time it is linked. |
| **Partway through the roadmap already** | Keep following the roadmap; use the lookup table above whenever a week references a `docs/` page you have not read yet. |
| **Preparing for a specific role or certification** | Read [Certification strategy](11-learning-and-career/05-certification-strategy.md) first, then the relevant numbered section in full (offensive: 06; defensive: 07; cloud: 08; malware: 09; GRC: 10). |
| **Here for reference, not a full course** | Use [cheatsheet.md](cheatsheet.md) for quick lookups and [14-glossary.md](14-glossary.md) for terms; follow a "Key references" line to the primary source when you need to verify a claim yourself. |
| **Reviewing this as a portfolio piece** | Start with the main [README](../README.md), then read one complete section (04 or 06 are good examples of the depth) and one [writeup](../writeups/2026-example-juice-shop-login-sqli.md). |

## The first hour

Do this once, before your first real study session:

1. **Set up version control for your own notes.** Fork or clone this repository for your public portfolio work; create a second, private repository for raw notes, following [the study system](11-learning-and-career/02-the-study-system.md#notes-the-two-repository-system).
2. **Install a spaced-repetition tool.** [Anki](https://apps.ankiweb.net/) is free; you will use it from week one.
3. **Open [tools/toolkit.html](../tools/toolkit.html) once** in your browser and bookmark it locally; it needs no installation and no internet connection.
4. **Copy [templates/README.md](../templates/README.md)'s templates** into wherever you keep notes, so you are not building structure from memory under pressure later.
5. **Read [Learning science](11-learning-and-career/01-learning-science.md) and [The study system](11-learning-and-career/02-the-study-system.md)** in full before your first content week; they explain why the roadmap is shaped the way it is, and skipping them tends to produce exactly the low-value study habits they warn against.
6. **Decide your current [study load mode](11-learning-and-career/03-study-load-modes.md)** honestly, for this week, right now.

## What to expect

- **This is dense, verified, and not padded.** Every factual claim carries a confidence marker (explained in the main [README](../README.md#how-to-read-the-evidence-markers)) and traces to a source in [References](15-references.md). Where something is genuinely unsettled or moving (a bill in Congress, a vendor rollout timeline), the text says so explicitly rather than guessing.
- **Nothing here is a substitute for hands-on practice.** Every page ends with a "Practice" section and a "What to do with this" checklist; reading without doing them produces exactly the shallow, overconfident learning that [How to measure progress](12-measuring-progress/01-how-to-measure-progress.md) warns about.
- **This is in English on purpose.** The original request behind this repository, and the English track that runs alongside it, treats professional technical English as a deliberate goal, not an afterthought. If you want a Spanish version of a specific page, that is a reasonable, separate request to make of whoever maintains this repository.
- **Some content is adjacent to offensive techniques.** Every page that touches them carries an explicit authorization boundary and points to [Legal limits and ethics](01-foundations/05-legal-and-ethics.md). Nothing here is written to enable unauthorized access to a real system, and content that could be mistaken for that is deliberately kept conceptual, with hands-on practice directed at your own lab or named, authorized platforms.

## What to do with this

- [ ] Complete the first-hour checklist above before your next study session.
- [ ] Bookmark this page and the [cheatsheet](cheatsheet.md) for quick return visits.
- [ ] Know, right now, which numbered section you would open first for your current goal.
- [ ] Set your study load mode for this week honestly.

## Key references

Every linked section's own Key references line. Full list in [References](15-references.md).

<!-- navigation -->
[Index](../README.md) · [What security is →](01-foundations/01-what-security-is.md)
