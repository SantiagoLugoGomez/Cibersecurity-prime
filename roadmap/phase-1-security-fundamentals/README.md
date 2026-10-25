# Phase 1: Security fundamentals

**Duration:** 12 weeks at about 7 hours per week (roughly 85 hours).
**When:** Starts alongside the Fundamentals of Cybersecurity course and finishes in semester 3. Phase 0 labs can continue in parallel.
**Prerequisites:** Phase 0 networking and Linux blocks.

This phase turns vocabulary into understanding. The goal is not to memorize definitions for an exam but to be able to reason about a system: what it protects, how it fails, and which control would have stopped the failure.

## Objectives

By the end of this phase you can:

1. Analyze a system with the CIA triad and the core principles (least privilege, defense in depth, separation of duties, secure defaults) and produce a simple STRIDE threat model.
2. Choose the right cryptographic primitive for a task, use it correctly in Python, and explain why common misuses (ECB mode, unsalted hashes, nonce reuse, home-made crypto) fail.
3. Explain how modern authentication works: password storage, MFA and phishing-resistant MFA, sessions and cookies, OAuth 2.0 and OpenID Connect, and the basics of Kerberos.
4. Describe each OWASP Top 10:2025 category with a concrete example and its fix, and exploit at least one lab per category.
5. Use MITRE ATT&CK to describe an intrusion, and use NIST CSF 2.0 to describe an organization's security program.

## Plan

| Weeks | Block | Main output |
|---|---|---|
| 1-2 | Principles and threat modeling | STRIDE model of a small web app (your own or Juice Shop) |
| 3-6 | Applied cryptography | CryptoHack Introduction and Symmetric starter challenges; crypto notes with code |
| 7-8 | Authentication and identity | Password storage demo, TOTP setup, PortSwigger authentication labs |
| 9-10 | OWASP Top 10:2025 | One lab per category, mapped in a table in your notes |
| 11 | MITRE ATT&CK | ATT&CK Navigator layer for a real public intrusion report |
| 12 | NIST CSF 2.0 | Current and target profile for a fictional small Colombian business |

## Key content and recent changes

- **CIA triad and beyond:** confidentiality, integrity, availability, plus authenticity, non-repudiation and accountability. Learn to classify any incident by which property it violated.
- **Applied cryptography:** encoding vs encryption vs hashing; AES with authenticated modes (GCM) and ChaCha20-Poly1305; SHA-2/SHA-3 and HMAC; password hashing with Argon2id, scrypt or bcrypt; RSA, elliptic-curve key exchange and Ed25519 signatures; X.509 certificates and chains of trust; secure randomness with Python's `secrets`. NIST published the first post-quantum standards in August 2024: [FIPS 203 (ML-KEM)](https://csrc.nist.gov/pubs/fips/203/final), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA). Know what they replace and why.
- **Authentication:** the final [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) requires a minimum of 15 characters for passwords used as a single factor (8 when part of MFA), recommends allowing at least 64, and drops composition rules and forced periodic changes. Use it as the reference when you evaluate a password policy.
- **OWASP Top 10:2025** ([official list](https://owasp.org/Top10/2025/0x00_2025-Introduction/), released November 2025): A01 Broken Access Control (now including SSRF), A02 Security Misconfiguration, A03 Software Supply Chain Failures (new), A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions (new). Many courses and books still teach the 2021 list; use the 2025 one.
- **MITRE ATT&CK:** tactics (the adversary's goal), techniques and sub-techniques (how), procedures (specific implementations). ATT&CK v19 (April 2026) split the old Defense Evasion tactic into **Stealth** (TA0005) and **Defense Impairment** (TA0112). Older material that mentions "Defense Evasion" is describing the pre-v19 matrix. Check the [updates page](https://attack.mitre.org/resources/updates/) for the current version.
- **NIST CSF 2.0** (February 2024): six functions, Govern, Identify, Protect, Detect, Respond and Recover. Govern is new in 2.0 and sits at the center because it shapes the other five.

## Resources

### Principles and threat modeling

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | Your Fundamentals of Cybersecurity course | Already covered | Use this phase to go deeper on each course unit |
| 2 | [Professor Messer Security+ SY0-701 videos](https://www.professormesser.com/sy0-701-certification-course/) | Free videos | Broad, exam-aligned coverage of fundamentals |
| 3 | [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling) and [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | Free | STRIDE and data-flow diagrams in practice |
| 4 | [Cisco Skills for All: Introduction to Cybersecurity](https://www.skillsforall.com/) | Free, self-paced | Short course with a digital badge; useful as a structured first pass |

### Applied cryptography

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [CryptoHack](https://cryptohack.org/) | Free | Learn by breaking flawed implementations of AES, RSA and elliptic curves in Python |
| 2 | [Dan Boneh, Online Cryptography Course](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) | Free lectures | Rigorous foundations from Stanford; graded work is on [Coursera](https://www.coursera.org/learn/crypto) |
| 3 | [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) and [Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | Free | What to use in real code and why |
| 4 | [The Illustrated TLS 1.3 Connection](https://tls13.xargs.org/) | Free | Revisit it now that you know the primitives |

### Authentication and identity

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [PortSwigger Web Security Academy: Authentication](https://portswigger.net/web-security/authentication) and [OAuth](https://portswigger.net/web-security/oauth) | Free | Explanations plus hands-on labs |
| 2 | [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) | Free | The current reference for passwords, MFA and authenticators |
| 3 | [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) and [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Free | Implementation guidance |

### OWASP Top 10, ATT&CK and CSF

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/) | Free | Read every category page, including the CWE mappings |
| 2 | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Free | The labs for this phase; see the mapping below |
| 3 | [MITRE ATT&CK](https://attack.mitre.org/) and [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | Free | The matrix and the tool to build layers |
| 4 | [The DFIR Report](https://thedfirreport.com/) | Free | Detailed real intrusions to map to ATT&CK |
| 5 | [NIST CSF 2.0 (CSWP 29)](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) and the [CSF home page](https://www.nist.gov/cyberframework) | Free | The framework itself, plus quick-start guides |
| 6 | [CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls/v8-1) | Free download | Concrete controls that implement CSF outcomes |

### Paid options (optional)

| Resource | Cost (October 2026) | When it is worth it |
|---|---|---|
| [Google Cybersecurity Professional Certificate](https://www.coursera.org/professional-certificates/google-cybersecurity) | $49/month on Coursera after a 7-day trial; financial aid available through the course page | Structured beginner program; apply for financial aid before paying |

## OWASP Top 10:2025 lab mapping

| Category | Practice |
|---|---|
| A01 Broken Access Control | WSA [Access control](https://portswigger.net/web-security/access-control) and [SSRF](https://portswigger.net/web-security/ssrf) apprentice labs |
| A02 Security Misconfiguration | WSA [Information disclosure](https://portswigger.net/web-security/information-disclosure) and [CORS](https://portswigger.net/web-security/cors) labs |
| A03 Software Supply Chain Failures | Run [`pip-audit`](https://pypi.org/project/pip-audit/) on one of your Python projects and explain each finding |
| A04 Cryptographic Failures | CryptoHack symmetric starter challenges; review how Juice Shop stores passwords |
| A05 Injection | WSA [SQL injection](https://portswigger.net/web-security/sql-injection), [XSS](https://portswigger.net/web-security/cross-site-scripting) and [OS command injection](https://portswigger.net/web-security/os-command-injection) apprentice labs |
| A06 Insecure Design | WSA [Business logic vulnerabilities](https://portswigger.net/web-security/logic-flaws) |
| A07 Authentication Failures | WSA [Authentication](https://portswigger.net/web-security/authentication) apprentice labs |
| A08 Software or Data Integrity Failures | WSA [Insecure deserialization](https://portswigger.net/web-security/deserialization) introduction |
| A09 Security Logging and Alerting Failures | Write one detection for failed logins in your lab with the Phase 0 log script or Wazuh |
| A10 Mishandling of Exceptional Conditions | Find a verbose error or fail-open path in Juice Shop and write up the root cause |

## Required hands-on practice

- **Threat model:** a STRIDE table and a data-flow diagram (Mermaid is fine) for one small application.
- **CryptoHack:** the Introduction course and the General category, plus the first Symmetric Ciphers challenges.
- **Crypto in code:** a short Python notebook or script that (1) shows why ECB leaks patterns, (2) encrypts and decrypts with AES-GCM using the `cryptography` package, (3) hashes passwords with Argon2id, and (4) signs and verifies a message with Ed25519.
- **Authentication:** enable TOTP and a passkey on your own accounts and describe what each protects against. Complete the WSA authentication apprentice labs.
- **OWASP:** one lab or exercise per category from the table above, each summarized in two or three sentences in your notes.
- **ATT&CK:** pick one report from The DFIR Report, build a Navigator layer of the techniques used, and export it into your notes with a paragraph on which detections would have caught it earliest.
- **CSF 2.0:** write a one-page current and target profile for a fictional 20-person accounting firm in Bogotá, covering all six functions.

## You've mastered this phase when...

- [ ] For any real incident in the news, you can say which CIA property was violated and which principle failed.
- [ ] You can explain to a classmate why encryption without integrity is dangerous, and which AEAD mode you would use instead.
- [ ] You can describe how a password should be stored in 2026 and justify the algorithm and parameters.
- [ ] You can explain the difference between authentication and authorization, and between OAuth 2.0 and OpenID Connect, without notes.
- [ ] You can name all ten OWASP Top 10:2025 categories, give an example of each, and state the primary fix.
- [ ] You have exploited at least one lab in every OWASP category and written down the root cause.
- [ ] You can read an incident report and map it to ATT&CK tactics and techniques, using the post-v19 tactic names.
- [ ] You can explain the six CSF 2.0 functions and what a profile is.

Next: [Phase 2, guided practice](../phase-2-guided-practice/README.md).
