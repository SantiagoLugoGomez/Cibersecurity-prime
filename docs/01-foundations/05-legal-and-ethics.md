# Legal limits and ethics

> [!TIP]
> **In short:** test only what you **own** or what someone with the authority to grant it has authorized **in writing**, and stay inside the **scope** of that permission. In Colombia, Ley 1273 de 2009 punishes access "without authorization or outside what was agreed", with prison terms of 48 to 96 months for the basic offense, and being a student or having good intentions is not a defense. Practice in your own lab and on platforms built for it; report anything you find through the proper channel.

> [!WARNING]
> This page is a practical summary for a student practitioner. It is not legal advice and it can be out of date. When a situation is unclear, stop and ask a qualified lawyer before acting.

## The one rule that keeps you safe

**Only test systems you own, or have explicit written authorization to test, and only within the agreed scope.**

Everything else follows from it. Your home lab, vulnerable applications you host yourself, and platforms that invite testing (TryHackMe, Hack The Box, picoCTF, OverTheWire, and bug bounty targets inside their stated scope) are fine. A website, app, network or device that does not fall into one of those groups is off limits, however easy the flaw looks and however good your intentions are.

"I was just looking" and "I didn't change anything" do not work as defenses. The unauthorized access is itself the offense.

## Colombian law

### Ley 1273 de 2009: computer crimes

Ley 1273 de 2009 added a title called *De la protección de la información y de los datos* to the Penal Code (Ley 599 de 2000). It defines separate offenses, with prison terms in months and fines in monthly minimum wages (SMMLV). Official texts: [Secretaría del Senado](http://www.secretariasenado.gov.co/senado/basedoc/ley_1273_2009.html) and [Función Pública](https://www.funcionpublica.gov.co/eva/gestornormativo/norma_pdf.php?i=34492). **●●●**

| Article | Offense | Penalty |
|---|---|---|
| **269A** | Abusive access to a computer system | 48 to 96 months of prison, fine of 100 to 1,000 SMMLV |
| 269B | Illegitimate obstruction of a system or network | 48 to 96 months, 100 to 1,000 SMMLV |
| 269C | Interception of computer data without a court order | 36 to 72 months |
| 269D | Computer damage (destroying, damaging, deleting or altering data) | 48 to 96 months, 100 to 1,000 SMMLV |
| 269E | Use of malicious software (producing, trafficking, acquiring, distributing, selling, sending or introducing it) | 48 to 96 months, 100 to 1,000 SMMLV |
| 269F | Violation of personal data (obtaining, compiling, selling or disclosing it without authorization, for gain) | 48 to 96 months, 100 to 1,000 SMMLV |
| 269G | Impersonation of websites to capture personal data (phishing pages, malicious links, pop-ups) | 48 to 96 months, 100 to 1,000 SMMLV |
| 269H | Aggravating circumstances | Penalties increase by one half to three quarters |
| 269I | Theft by computer means | Penalties of theft (art. 240 of the Penal Code) |
| 269J | Non-consensual transfer of assets | 48 to 120 months, 200 to 1,500 SMMLV |

Aggravating circumstances (269H) apply, among other cases, when the conduct targets official or state systems or the financial sector, or is committed by someone abusing a position of trust.

### Reading article 269A closely

Article 269A is the one that matters most for anyone who tests systems. In substance, it punishes whoever, **"sin autorización o por fuera de lo acordado"** (without authorization or outside what was agreed), accesses all or part of a computer system, *protected by a security measure or not*, or **stays inside it against the will of whoever has the legitimate right to exclude them**. The quoted phrase is the statute's own wording; read the full article in the linked official sources.

Four consequences are worth stating plainly.

1. **Authorization is the dividing line.** The same scan, login attempt or exploit is lawful with permission and a crime without it.
2. **"Outside what was agreed" covers scope creep.** A tester who has permission for one web application and also probes the server next to it can fall outside the agreement. Scope is not paperwork; it is the legal boundary of your work.
3. **No security measure needs to be bypassed.** An open door is still not an invitation. Reaching something because it was left unprotected does not make the access authorized.
4. **Staying counts.** If you were allowed in but were told to leave, or your permission ended, remaining is covered.

The offense is committed with intent (*dolo*), but do not treat that as a defense. Running a tool against a target on purpose is intentional access. Ignorance of the scope or a wish to "help" does not change that.

**Practical implication:** if you cannot point to a written permission that covers this system, this action and this time window, do not do it.

### Other offenses that touch your practice

| Activity | Risk |
|---|---|
| Scanning or brute-forcing a system you do not control | 269A; if it disrupts service, 269B |
| Capturing traffic on a network you do not own or administer | 269C |
| Running or sharing malware outside an isolated lab, or distributing samples | 269E (the verbs include *traffic*, *distribute* and *send*) |
| Building a phishing page, even "for a demo", against a real brand | 269G |
| Keeping or sharing personal data obtained in a test | 269F, plus data protection law |
| Impersonating someone with a synthetic voice or video | Ley 2502 de 2025 adds an aggravating circumstance when artificial intelligence is used in identity impersonation **●●○** |

### Related laws

- **Ley 1928 de 2018** approved the Budapest Convention on Cybercrime, and the Constitutional Court upheld it in judgment C-224 of 2019. International cooperation means that practising "abroad" on systems in other countries does not avoid liability; their laws apply too.
- **Ley 1581 de 2012** (personal data protection) and **Ley 1266 de 2008** (financial and credit data) govern what you may do with personal data you handle. See [Privacy and data protection](../10-governance-risk-and-compliance/04-privacy-and-data-protection.md) and [Colombian regulatory landscape](../10-governance-risk-and-compliance/05-colombian-regulatory-landscape.md).

### Other countries

When you touch a system abroad, the law of that country can apply. The United States has the Computer Fraud and Abuse Act, the United Kingdom the Computer Misuse Act 1990, and the European Union a directive on attacks against information systems (Directive 2013/40/EU). In May 2022 the US Department of Justice announced that it would generally not prosecute good-faith security research under the CFAA (US DOJ CFAA policy, 2022). **●●○** That is a prosecutorial policy for one country. It is not a license, it does not bind other states or private plaintiffs, and it does not apply to Colombian law. Do not read it as a safe harbor for you.

## Authorization in practice

For paid work, authorization is a document, usually part of the contract and the rules of engagement. A useful one answers the following.

| Item | What it should say |
|---|---|
| **Who authorizes** | Name and role of someone with the authority to grant access to these systems |
| **Scope** | Exact targets: IP ranges, domains, applications, cloud accounts, physical locations |
| **Out of scope** | Systems and actions explicitly excluded (production databases, third-party services, other tenants) |
| **Techniques** | Allowed and forbidden methods (denial of service, social engineering, phishing, physical entry) |
| **Window** | Dates and times, and contact points during the test |
| **Data handling** | What you may access, how evidence is stored and encrypted, when it is destroyed |
| **Safety** | An emergency contact and a way to stop the test immediately |
| **Third parties** | Cloud and hosting providers may have their own testing policies; check them |
| **Liability** | Responsibilities if something breaks |

Treat the scope as a hard limit. If you discover a path to something outside it, stop, record what you saw, and ask the client; do not "just check".

## Gray areas, answered cautiously

These come up constantly. The answers are conservative on purpose (◇).

| Situation | Conservative answer |
|---|---|
| Scan my university's network or Wi-Fi to learn | No. Ask the IT department in writing; many will say no, some will help set up a lab |
| Port-scan a public website "just to see" | Treat as unauthorized. Scanning is also against many ISPs' terms |
| Use Shodan, Censys or certificate search | Searching an index built by someone else is passive and fine; connecting to what you find is not |
| Test my own account on a service for weak spots | Normal use is fine; automated attacks, fuzzing or probing others' data is not, and may violate the terms of service |
| Download malware samples to analyze | Possession for analysis is common practice; do it only in an isolated lab and never distribute (269E) |
| I found a vulnerability while using a site normally | Stop, do not go further, and report it (see below) |
| A friend asks me to "check" their company's site | Not without written permission from someone who can authorize it |
| Join a bug bounty program | Yes, and stay strictly inside its published scope and rules |

## Platforms and competitions

Platforms are authorized environments, but they have rules too.

- Attack only the machines and challenges assigned to you; never the platform infrastructure or other players.
- Do not share flags or solutions for live competitions or active content. Hack The Box permits public writeups only for retired content, so keep notes on active machines private.
- Do not scan shared lab networks beyond your assigned range.
- Respect rate limits and fair use on free tiers.

## Responsible disclosure

When you find a vulnerability, how you report it matters as much as the finding.

| Model | Idea |
|---|---|
| **Coordinated (responsible) disclosure** | Report privately; the vendor fixes; details are published after a fix or an agreed deadline. This is the professional norm, and the process is formalized in ISO/IEC 29147 (disclosure) and ISO/IEC 30111 (handling) **●●●** |
| **Full disclosure** | Publish details immediately so everyone can act. Rare and controversial; carries legal and ethical risk |
| **Non-disclosure** | Keep it to yourself or sell it. Selling to exploit brokers or criminals is unethical, and may be illegal |

Deadlines are a negotiation. A 90-day window is common in industry (Google Project Zero popularized it), with flexibility if the vendor is working on a fix. **●●○**

### If you stumble on something

1. **Stop** as soon as you realize the system is not yours or the access is unintended.
2. **Do not go further.** No pivoting, no browsing records, no "proof" beyond the minimum.
3. **Record** what you did and saw, with timestamps, for your own protection.
4. **Do not keep data.** If you already retrieved any, secure it and delete it once reported.
5. **Find the reporting channel.** Look for a published policy or a `security.txt` file (RFC 9116 defines `/.well-known/security.txt`). Otherwise contact the organization's security or IT team.
6. **Report factually** and offer help; never demand payment. An unsolicited request for money can be read as extortion.
7. **Consider a coordinator.** In Colombia, ColCERT (under MinTIC) coordinates response to cyber incidents, and national CERTs in other countries do the same. The CERT/CC *Guide to Coordinated Vulnerability Disclosure* describes the process in detail.

### Bug bounty programs

A program's policy is your authorization. Read it fully before sending a request: scope, forbidden actions (denial of service, social engineering, data access beyond proof), required reporting format, rules on disclosure and payment. Safe-harbor language in a policy is a contractual promise from the company; it is only as strong as the company and does not bind prosecutors. Outside the scope you have no cover at all. More on how programs work is in the [professional phase of the roadmap](../../roadmap/phase-4-professional/README.md#bug-bounty).

## Handling the data you meet

Testing often exposes personal or confidential data. Handle it as a custodian.

- Collect the minimum needed to prove the issue; screenshots with redactions are enough.
- Store evidence encrypted, with access limited to those who need it, and delete it at the agreed time.
- Redact personal data and secrets in reports, writeups and screenshots before sharing.
- Never publish credentials, tokens or customer data, even from a lab you built using real-looking data.

## Reporting a crime or an incident in Colombia

- **Report a crime:** the Policía Nacional receives complaints about computer crimes through its cyber channels, and serious cases go to the Fiscalía General de la Nación.
- **Report a personal-data incident or complaint:** the Superintendencia de Industria y Comercio (SIC), the data protection authority.
- **Coordination of cyber incidents:** ColCERT, part of MinTIC.

Channels and portals change; confirm them on the official sites.

## A short ethical code

Professional bodies publish codes of ethics, such as the ISC2 Code of Ethics (protect society and the common good, act honorably, provide diligent service, advance the profession) and the ACM Code of Ethics. They agree on the same basics.

- Get authorization in writing and stay inside it.
- Protect the data and systems you touch as if they were your own.
- Report honestly, including your own mistakes.
- Do not use your skills to harm, intimidate or surveil anyone.
- If an action would embarrass you when made public, do not do it.
- When unsure whether something is legal or ethical, stop and ask first.

## What to do with this

- [ ] Read the full text of articles 269A to 269J in the official source.
- [ ] Write a one-page rules-of-engagement template for your own lab exercises, using the table above.
- [ ] Check the terms of every platform you use: what is allowed, what you may publish.
- [ ] Find the `security.txt` of three websites and read their reporting rules.
- [ ] Keep notes about active content in your private repository, never in the public one.

## Key references

ACM Code of Ethics · CERT Guide to CVD · ISC2 Code of Ethics · ISO/IEC 29147 · ISO/IEC 30111 · Ley 1273 de 2009 · Ley 1581 de 2012 · Ley 1928 de 2018 · Ley 2502 de 2025 · RFC 9116 · Sentencia C-224 de 2019 · US DOJ CFAA policy (2022). Full list in [References](../15-references.md).

<!-- navigation -->
[← Adversaries and attack frameworks](04-adversaries-and-attack-frameworks.md) · [Index](../00-start-here.md) · [Linux for security →](../02-systems/01-linux-for-security.md)
