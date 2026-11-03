# Privacy and data protection

> [!TIP]
> **In short:** privacy and security are related but distinct: security protects data from unauthorized access and misuse; privacy decides, in the first place, what data should be collected at all, for what purpose, and who gets a say in that. [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md) already covers Colombia's criminal statute on unauthorized access to systems (Ley 1273 de 2009); this page covers the separate body of law and practice governing **personal data itself**, Colombia's Ley 1581 de 2012 at the center, plus the privacy-engineering techniques (anonymization, pseudonymization, data minimization) that make compliance actually achievable rather than a paperwork exercise layered on top of unchanged practice.

## Privacy is not the same question as security

| Question | Discipline |
|---|---|
| Is this data protected from unauthorized access? | Security (everything in sections 2 through 9 of this knowledge base) |
| Should this data have been collected at all? | Privacy |
| Does the person it describes know, and did they agree? | Privacy |
| Is it being used only for what it was collected for? | Privacy |
| Is it kept only as long as actually needed? | Privacy |
| Can the person see, correct, or ask for deletion of it? | Privacy |

A perfectly secured database of data that should never have been collected is still a privacy failure. A privacy-respecting data collection practice with no security controls around it is a breach waiting to happen. The two disciplines need each other, and a mature program treats them as connected, not as the same checkbox.

## Common principles across data protection law

Most modern data protection regimes, Colombia's included, converge on a similar set of principles, even where the specific wording and enforcement differ:

| Principle | Meaning |
|---|---|
| **Purpose limitation** | Collect data for a specific, stated purpose, and do not quietly repurpose it for something else later |
| **Data minimization** | Collect only what the stated purpose actually requires, not everything that might someday be useful |
| **Consent and legal basis** | Have a legitimate basis for processing, consent being the most familiar but not the only one |
| **Transparency** | Tell people what is collected, why, and what happens to it, in terms they can actually understand |
| **Accuracy** | Keep data correct and current where it matters |
| **Storage limitation** | Keep data only as long as the purpose requires, then delete or properly anonymize it |
| **Security** | Protect it proportionate to its sensitivity, which is where this principle hands off directly to the rest of this knowledge base |
| **Accountability** | Be able to demonstrate compliance, not just claim it, echoing the audit-evidence discipline from [Policies, audit and third-party risk](03-policies-audit-and-third-party-risk.md) |

The EU's **GDPR** is the most globally influential expression of these principles and is worth knowing even outside the EU, because many organizations design one global privacy program to its standard rather than maintaining separate, weaker ones per jurisdiction; but it is not the law that governs Colombia, which is where the rest of this page focuses.

## Colombia: Ley 1581 de 2012 and habeas data

Colombia's data protection framework rests on a constitutional right (**habeas data**, the right to know, update and correct personal information held by others, recognized in Article 15 of the Constitution) given statutory detail by **Ley Estatutaria 1581 de 2012**, with **Decreto 1377 de 2013** regulating its implementation. The enforcement authority is the **Superintendencia de Industria y Comercio (SIC)**, acting through its Delegatura for data protection.

| Concept | Meaning under Colombian law |
|---|---|
| **Titular** | The person the data is about, holding the rights described below |
| **Responsable del tratamiento** | The party who decides what data is processed and why (the controller) |
| **Encargado del tratamiento** | The party who processes data on behalf of the responsable (the processor) |
| **Dato personal** | Any information linked or linkable to an identified or identifiable natural person |
| **Dato sensible** | A narrower, more protected category: health, sexual orientation, political opinions, religious or philosophical beliefs, union membership, biometric and genetic data among others; processing it generally requires explicit consent and, for some categories, is only permitted for specific purposes |
| **Autorización** | The legal basis requirement: processing personal data generally requires the titular's prior, express and informed authorization, with specific exceptions set out in the law |

### Rights the law gives the titular

| Right | In practice |
|---|---|
| Access their own data held by a responsable | Request and receive a copy |
| Update or correct inaccurate data | A correction request process must exist |
| Request deletion ("suprimir") | Subject to legal retention requirements that may override it |
| Revoke authorization previously given | Where no legal obligation requires continued processing |
| Be informed of the use their data will be put to | At the point of collection, not buried in unrelated terms |
| Lodge a complaint with the SIC | The regulatory escalation path if the responsable does not resolve a request |

### Obligations on organizations

| Obligation | Detail |
|---|---|
| **Register databases with the RNBD** (Registro Nacional de Bases de Datos) | Required of responsables above the thresholds set by regulation, with periodic update windows (commonly cited as within the first 15 business days of February and August each year for registry updates); verify current thresholds and windows against the SIC's own current guidance, since these details are implemented through SIC circulars that are updated over time |
| **Have a privacy policy (política de tratamiento de datos)** | Publicly available, describing what is collected, why, and the titular's rights |
| **Report security incidents affecting personal data to the SIC** | Within a window commonly cited as 15 business days of becoming aware, though you should confirm the figure currently in force against the SIC's own circulars before relying on it for a real compliance deadline, as covered already in [Incident response](../07-defensive-security/04-incident-response.md#legal-and-regulatory-notification) |
| **Implement security measures** | The law requires "necessary security measures," without prescribing specific technical controls, which is where the rest of this knowledge base and frameworks such as MinTIC's MSPI (below) fill in the detail |

### A regulatory bill to watch

A bill to reform Ley 1581 de 2012 has been under discussion in the Colombian Congress, aimed at strengthening SIC oversight and updating sanctions; its progress and final content were not settled at the time of writing, so check the Congress's own bill-tracking resources for its current status before relying on any specific provision attributed to it. **◇**

## The public sector layer: MSPI

For Colombian public entities specifically, **MinTIC's Modelo de Seguridad y Privacidad de la Información (MSPI)** sets the operational security and privacy requirements, most recently updated by **Resolución 02277 de 2025** (updating the earlier Resolución 500 de 2021). It is built to align with ISO/IEC 27001 and gives public entities a structured implementation path covering both security controls and the privacy obligations under Ley 1581. Private organizations are not bound by MSPI directly, but it is a useful, free, Spanish-language reference model regardless. **●●●**

## Privacy engineering: techniques, not just policy

Policy says what should happen; these techniques are how data minimization and reduced risk actually get built into systems.

| Technique | What it does | Limitation |
|---|---|---|
| **Data minimization by design** | Collect and retain only fields the actual feature needs; do not collect "just in case" | Requires discipline during design, not a retrofit |
| **Pseudonymization** | Replace a direct identifier with a token, keeping the mapping separately secured | The data is still personal data if the mapping can be reversed; it reduces exposure, it does not remove the legal obligation |
| **Anonymization** | Remove or alter data so no individual can reasonably be re-identified, even combined with other available data | Genuinely robust anonymization is harder than it looks; naive approaches (just removing a name) are frequently reversible through combination with other datasets |
| **k-anonymity** | Ensures each record is indistinguishable from at least *k-1* others on the attributes that could identify someone | Vulnerable to certain attacks when the sensitive attribute is uniform within a group, or when an attacker has outside knowledge; a conceptual building block, already encountered in a different form in [Passwords and MFA](../04-cryptography-and-identity/04-passwords-and-mfa.md#checking-against-breached-passwords) via the Have I Been Pwned k-anonymity API design |
| **Differential privacy** | Adds calibrated statistical noise so that including or excluding any one individual's data barely changes the output, with a formal, provable privacy guarantee | Reduces the precision of aggregate results; implementation detail matters enormously, and a poorly implemented version can fail to deliver its theoretical guarantee |
| **Encryption at rest and in transit** | Already covered in depth in [Cryptography foundations](../04-cryptography-and-identity/01-cryptography-foundations.md) and [TLS in depth](../04-cryptography-and-identity/03-tls-in-depth.md) | Protects against unauthorized access, not against authorized misuse, which is a privacy question these techniques alone do not answer |
| **Access control and purpose-binding** | Technically restrict personal data access to the specific systems and people whose stated purpose requires it | Only as good as the authorization discipline in [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md) |

**Practical implication:** "we encrypted it" answers a security question, not a privacy one. A system can encrypt personal data perfectly and still violate purpose limitation if it then uses that data for something the person was never told about.

## Privacy by design, concretely

| Practice | In practice |
|---|---|
| **Privacy impact assessment** for new features or systems that touch personal data | A structured review, before building, of what is collected, why, and what risk it creates, the privacy equivalent of the threat modeling discipline in [Threat modeling](../01-foundations/03-threat-modeling.md) |
| **Default to the most private setting** | Opt-in rather than opt-out for anything beyond what is strictly necessary |
| **Build deletion in from the start** | Retrofitting "right to deletion" into a system never designed to support it is far harder than building it in from the first schema design |
| **Minimize logging of personal data** | Already covered as a logging-specific concern in [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md#privacy-and-legal-handling-of-logs) |
| **Data flow mapping** | Know where personal data actually goes, across every system and every third party, well enough to answer a titular's access request completely and correctly |

## Connecting this to the rest of the knowledge base

| This page's concept | Where it is applied elsewhere |
|---|---|
| Breach notification timelines | [Incident response](../07-defensive-security/04-incident-response.md#legal-and-regulatory-notification) |
| Minimizing personal data in logs | [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md) |
| The criminal law side of unauthorized data access | [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md) |
| Security measures that implement the law's protection requirement | Nearly every technical page in sections 2 through 9 |

## Practice

1. Write a data flow map for one real application you have access to (even a personal project): every category of personal data it collects, why, where it is stored, who can access it, and how long it is kept.
2. Draft a short, plain-language privacy notice for that same application, covering what Ley 1581's transparency principle would require, and compare it against the application's actual current privacy policy if one exists.
3. Pick one field your application collects and ask, honestly, whether its stated purpose actually requires it; if not, remove it, as a direct exercise in data minimization.
4. Implement a simple pseudonymization scheme for one dataset (replace a direct identifier with a token, store the mapping separately) and explain, specifically, what it does and does not protect against.
5. Read the SIC's current public guidance on RNBD registration and incident reporting timelines, and note the exact current figures alongside the date you checked them.

These support the [GRC track](../../roadmap/phase-3-specialization/track-grc.md) of the roadmap and [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md).

## What to do with this

- [ ] Explain the difference between privacy and security clearly enough to give an example where one is satisfied and the other is not.
- [ ] Name the core principles shared across data protection regimes and give a concrete example of each.
- [ ] Explain the Colombian titular's rights and the responsable's main obligations under Ley 1581 de 2012.
- [ ] Explain the difference between pseudonymization and anonymization, and why the legal treatment of each differs.
- [ ] Build one real data flow map and one real privacy notice for something you actually run.

## Key references

Decreto 1377 de 2013 · Ley 1581 de 2012 · MinTIC Resolución 02277 de 2025 (MSPI) · Sweeney (2002), k-anonymity · Dwork (2006), differential privacy. Full list in [References](../15-references.md).
