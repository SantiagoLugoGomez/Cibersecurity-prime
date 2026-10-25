# Glossary of core security terminology

Definitions a practitioner should know precisely, with an example sentence in the register you will actually use. The example sentences are the point: they show the collocations (which words go together) that make English sound native. Read the example aloud, then write your own sentence for each term that matters to you.

Terms Spanish speakers often confuse are marked **[confused]** with a note.

## Core concepts

| Term | Definition | Example sentence |
|---|---|---|
| Vulnerability | A weakness in a system that could be exploited | "The scan found a critical vulnerability in the login endpoint." |
| Threat | A potential cause of harm (an actor or event) | "Ransomware is the top threat to the healthcare sector this year." |
| Exploit | Code or a technique that takes advantage of a vulnerability | "A working exploit for the flaw was published within days." |
| Risk | The likelihood and impact of a threat exploiting a vulnerability | "We accepted the risk because the asset is isolated and low value." |
| Threat actor / adversary | The entity behind an attack | "The threat actor used stolen credentials to move laterally." |
| Attack surface | The sum of points where an attacker could try to enter | "Closing the unused ports reduced the attack surface." |
| Attack vector | The path or means an attacker uses | "Phishing remains the most common initial attack vector." |
| Payload | The part of an exploit that performs the malicious action | "The macro downloaded a second-stage payload." |
| Indicator of compromise (IoC) | An artifact that suggests an intrusion | "The report lists file hashes and domains as indicators of compromise." |
| Zero-day | A vulnerability with no patch available, often unknown to the vendor | "The group chained two zero-days to bypass the sandbox." |

**[confused] Vulnerability vs exploit vs threat.** A vulnerability is the weakness, an exploit is how you abuse it, a threat is what might come through. Spanish uses "amenaza" and "vulnerabilidad" similarly, but in English do not call an exploit a "vulnerability" or a vulnerability a "threat."

**[confused] Mitigate vs remediate.** To *mitigate* is to reduce impact or likelihood without fully fixing ("we mitigated it with a firewall rule"); to *remediate* is to fix the root cause ("the patch remediates the flaw"). *Resolve* and *fix* are the plain-English versions.

## The CIA triad and principles

| Term | Definition | Example sentence |
|---|---|---|
| Confidentiality | Keeping data from unauthorized disclosure | "Encryption at rest protects the confidentiality of the backups." |
| Integrity | Preventing unauthorized modification of data | "The signature verifies the integrity of the update." |
| Availability | Keeping systems and data accessible when needed | "The DDoS attack targeted availability, not data." |
| Non-repudiation | Being unable to deny an action one took | "Digital signatures provide non-repudiation." |
| Least privilege | Granting only the access strictly needed | "The service account violated least privilege by having admin rights." |
| Defense in depth | Layering controls so one failure is not fatal | "Defense in depth meant the breach stopped at the segmented network." |
| Hardening | Reducing a system's weaknesses by configuration | "We hardened the server by disabling unused services." |

## Cryptography

| Term | Definition | Example sentence |
|---|---|---|
| Encryption | Reversibly transforming data so only authorized parties can read it | "Traffic is encrypted end to end." |
| Hashing | A one-way function producing a fixed-length digest | "Passwords are stored as salted hashes, never in plaintext." |
| Salt | Random data added before hashing to defeat precomputation | "A unique salt per user defeats rainbow tables." |
| Key exchange | A protocol for two parties to agree on a shared secret | "The handshake uses an elliptic-curve key exchange." |
| Cipher | An algorithm for encryption and decryption | "AES is a block cipher; ChaCha20 is a stream cipher." |
| Plaintext / ciphertext | The readable input / the encrypted output | "The ciphertext leaked patterns because ECB mode was used." |
| Nonce | A number used once, to keep encryption outputs unique | "Reusing a nonce broke the confidentiality of the stream." |

**[confused] Encryption vs encoding vs hashing.** Encoding (like Base64) is reversible and provides no security; encryption is reversible only with a key; hashing is not reversible at all. English keeps these strictly separate, and saying "the password is encrypted" when you mean hashed is a real error in a report.

**[confused] Cipher vs cypher, and "encrypt" vs "encript".** Use *cipher* and *encrypt*. "Encript" and "encripted" are not English words; the Spanish "encriptar" leads many writers to them.

## Web security

| Term | Definition | Example sentence |
|---|---|---|
| Injection | Sending data that is interpreted as a command | "The form was vulnerable to SQL injection." |
| Cross-site scripting (XSS) | Injecting script that runs in another user's browser | "A stored XSS in the comments ran on every visitor's session." |
| Cross-site request forgery (CSRF) | Forcing a user's browser to make an unwanted request | "The token stops CSRF by binding the request to the session." |
| Broken access control | Failing to enforce what a user is allowed to do | "Broken access control let any user read other users' invoices." |
| Server-side request forgery (SSRF) | Making the server send attacker-controlled requests | "SSRF reached the cloud metadata endpoint and leaked credentials." |
| Sanitize / validate | Clean input / check input against rules | "Validate the input and encode the output; do not rely on sanitizing alone." |

## Offensive operations

| Term | Definition | Example sentence |
|---|---|---|
| Reconnaissance | Gathering information about a target | "Passive reconnaissance avoids touching the target directly." |
| Enumeration | Actively listing a target's services, users and resources | "Enumeration of the SMB shares revealed a config file with a password." |
| Privilege escalation | Gaining higher rights than initially granted | "A misconfigured SUID binary allowed privilege escalation to root." |
| Lateral movement | Moving from one compromised host to others | "They used pass-the-hash for lateral movement across the domain." |
| Persistence | Maintaining access across reboots or credential changes | "The implant established persistence with a scheduled task." |
| Pivot | Using a compromised host to reach a new network | "We pivoted through the web server to reach the internal subnet." |
| Scope | What you are authorized to test | "The API was out of scope, so we did not touch it." |
| Rules of engagement | The agreed constraints of an engagement | "The rules of engagement forbid any denial-of-service testing." |

## Defensive operations

| Term | Definition | Example sentence |
|---|---|---|
| Detection | Identifying malicious or anomalous activity | "The detection fired on an unusual volume of failed logins." |
| False positive / false negative | A benign event flagged as malicious / a malicious event missed | "Tuning the rule cut the false positives without adding false negatives." |
| Triage | Quickly assessing and prioritizing alerts | "Level 1 analysts triage the queue and escalate real incidents." |
| Containment | Stopping an incident from spreading | "Containment meant isolating the host from the network." |
| Eradication | Removing the threat from the environment | "Eradication involved rebuilding the infected servers." |
| Threat hunting | Proactively searching for threats that evaded detection | "The hunt uncovered a dormant web shell." |
| Baseline | The normal behavior against which anomalies are measured | "Traffic to that country was well outside the baseline." |
| Dwell time | How long an attacker stays undetected | "Reducing dwell time is the main goal of the detection program." |

## Governance, risk and compliance

| Term | Definition | Example sentence |
|---|---|---|
| Control | A safeguard that reduces risk | "Multi-factor authentication is a preventive control." |
| Compliance | Meeting a law, standard or policy | "Compliance with the data protection law is mandatory, not optional." |
| Audit | A formal review of controls against a standard | "The audit found three controls operating but not documented." |
| Policy / standard / procedure | What is required / the specific rule / the step-by-step | "The policy requires encryption; the standard names the algorithm; the procedure says how to enable it." |
| Risk appetite | The amount of risk an organization accepts | "This exceeds our risk appetite, so it must be remediated." |
| Framework | A structured set of outcomes or controls | "We mapped our controls to the NIST Cybersecurity Framework." |

## Incident and disclosure

| Term | Definition | Example sentence |
|---|---|---|
| Incident | A confirmed adverse security event | "The incident was declared when data exfiltration was confirmed." |
| Breach | An incident with confirmed unauthorized data access | "The breach exposed records of two million customers." |
| Responsible / coordinated disclosure | Reporting a flaw privately and allowing time to fix | "We followed coordinated disclosure and waited for the patch." |
| Safe harbor | A program's promise not to pursue researchers who follow the rules | "The policy's safe harbor covers testing within scope." |
| Proof of concept (PoC) | A minimal demonstration that a flaw is real | "The report included a proof of concept but no weaponized exploit." |
| Patch | A fix released by a vendor | "Apply the patch; the vulnerability is being exploited in the wild." |

## Building your own glossary

This list is a start, not a limit. The fastest way to C2 vocabulary is to collect terms from the real texts you read:

1. When you meet a term you understand but could not have produced yourself, add a row to your personal glossary.
2. Copy the sentence you found it in; the collocation matters more than the definition.
3. Note any word that a Spanish cognate would have led you to get wrong.
4. Review the list before writing a report or an interview.

The method for mining texts is in [reading-professional-material.md](reading-professional-material.md).
