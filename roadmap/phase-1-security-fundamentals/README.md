# Phase 1: Security fundamentals

**Duration:** 16 weeks at about 7.5 hours per week (around 120 hours).
**When:** Alongside the Fundamentals of Cybersecurity course and into the next semester. Phase 0 labs can continue in parallel.
**Prerequisites:** Phase 0 networking, Linux and Python modules.

This phase turns vocabulary into understanding. The goal is not to memorize definitions but to reason about a system: what it protects, how it fails, and which control would have stopped the failure. Each module is a separate file with the full week-by-week plan.

## Modules

| Module | Weeks | Topic |
|---|---|---|
| [1.1 Principles and threat modeling](01-principles-threat-modeling.md) | 1-2 | CIA, security principles, STRIDE threat modeling |
| [1.2 Applied cryptography](02-applied-cryptography.md) | 3-5 | Hashing, symmetric and asymmetric crypto, TLS, post-quantum |
| [1.3 Identity and access](03-identity-and-access.md) | 6-7 | Authentication, MFA, authorization, sessions, OAuth, enterprise identity |
| [1.4 Web security and OWASP Top 10](04-web-security-owasp.md) | 8-11 | The full OWASP Top 10:2025 with labs, plus APIs and a report |
| [1.5 Network security and monitoring](05-network-defense-monitoring.md) | 12-13 | Traffic analysis, IDS, SIEM, detections, ATT&CK |
| [1.6 Frameworks and governance](06-frameworks-and-governance.md) | 14-16 | NIST CSF 2.0, CIS, vulnerability prioritization, risk, Colombian context |

## What is current in this phase

- **OWASP Top 10:2025** (November 2025): A03 Software Supply Chain Failures and A10 Mishandling of Exceptional Conditions are new; SSRF folded into A01. Use the 2025 list, not 2021.
- **NIST SP 800-63B-4** (final): 15-character minimum for single-factor passwords, no forced rotation, no composition rules.
- **MITRE ATT&CK v19+** (2026): Defense Evasion split into Stealth (TA0005) and Defense Impairment (TA0112).
- **NIST CSF 2.0** (2024): six functions including the new Govern.
- **NIST post-quantum standards** FIPS 203/204/205 (August 2024).
- **CVSS v4.0** and **EPSS** for prioritization, alongside the **CISA KEV** catalog.

## Objectives

By the end of this phase you can:

1. Analyze a system with the CIA triad and core principles and produce a STRIDE threat model.
2. Choose and correctly use cryptographic primitives, and explain the classic misuses.
3. Explain modern authentication and authorization and exploit their common failures.
4. Describe and exploit every OWASP Top 10:2025 category, and write a professional web assessment report.
5. Read traffic and logs for signs of attack, write detections and map activity to ATT&CK.
6. Describe a security program with NIST CSF 2.0, prioritize vulnerabilities sensibly, and write risk and policy documents with Colombian legal context.

## You've mastered this phase when...

- [ ] For any real incident, you can state which CIA property was violated and which principle failed.
- [ ] You can produce a STRIDE threat model with a data-flow diagram.
- [ ] You can explain how a password should be stored in 2026 and justify it, and why encryption without integrity is dangerous.
- [ ] You can name all ten OWASP 2025 categories, give an example and fix for each, and you have exploited a lab in every one.
- [ ] You have written at least one professional web assessment report.
- [ ] You can read an intrusion report, map it to ATT&CK (post-v19 names), and propose detections.
- [ ] You can write a CSF 2.0 profile, a risk register and a security policy, and prioritize vulnerabilities with CVSS, EPSS and KEV together.

Track these in [progress.md](../../progress.md).

Next: [Phase 2, guided practice](../phase-2-guided-practice/README.md).
