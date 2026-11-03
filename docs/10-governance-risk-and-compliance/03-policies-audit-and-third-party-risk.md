# Policies, audit and third-party risk

> [!TIP]
> **In short:** a **policy** states what must be true; a **control** is what makes it true in practice; an **audit** checks whether the control actually worked, with evidence. Most organizations have the first and skip straight to assuming the third, which is how a policy document and reality quietly drift apart for years until an incident or an actual audit reveals the gap. **Third-party risk** is the same discipline applied past your own boundary: a vendor's security failure becomes your incident the moment their access or your data is involved, so the diligence and audit habits on this page apply to vendors as much as to your own organization.

## Policies, standards, procedures and guidelines

These four terms are often used loosely; a mature program keeps them distinct, because they carry different authority and change at different speeds.

| Document type | What it does | Example | Changes how often |
|---|---|---|---|
| **Policy** | States a requirement and who it applies to, at a level leadership approves | "All production systems must have multi-factor authentication for administrative access" | Rarely |
| **Standard** | Specifies the measurable detail that satisfies a policy | "Administrative MFA must use a phishing-resistant method" | Occasionally |
| **Procedure** | The step-by-step instructions to actually do it | "To enroll a new administrator's security key, follow these seven steps" | As tooling changes |
| **Guideline** | A recommended, non-mandatory practice | "Consider rotating API keys every 90 days as good hygiene" | Flexibly |

A policy with no standard is unenforceable, because nobody can tell what satisfies it. A procedure with no policy behind it is just documentation, with no authority to require anyone follow it. Keep the hierarchy intact, and write policies to **outcomes**, not specific products, so they do not need rewriting every time the tooling changes underneath them.

## What a security policy set typically covers

| Area | Core question the policy answers |
|---|---|
| **Acceptable use** | What may employees do with organizational systems and data? |
| **Access control** | Who gets access to what, how it is requested, approved and reviewed? |
| **Data classification and handling** | What categories of data exist, and what protection does each require? |
| **Incident response** | Who does what when something goes wrong (see [Incident response](../07-defensive-security/04-incident-response.md)) |
| **Vendor and third-party management** | What due diligence and ongoing oversight applies to external parties |
| **Change management** | How changes to production systems are proposed, reviewed and approved |
| **Business continuity and disaster recovery** | What keeps the organization running through disruption (see [Hardening and resilience](../07-defensive-security/08-hardening-and-resilience.md)) |
| **Remote work and device use** | What security expectations apply outside a traditional office |

A policy that is never read does nothing. Distribute policies as part of onboarding, require acknowledgment, and revisit them on a schedule, not only when something goes wrong.

## Auditing: internal, external and continuous

| Type | Who performs it | Purpose |
|---|---|---|
| **Internal audit** | Staff or a team inside the organization, ideally independent of the function being audited | Ongoing assurance that controls work as intended, catching gaps before an external party does |
| **External audit** | An independent third party | Required for certifications (ISO/IEC 27001), attestations (SOC 2), and often by regulation or contract |
| **Regulatory examination** | A government or sector regulator | Compliance with a specific legal requirement |
| **Continuous control monitoring** | Automated tooling | Checks a control's state constantly rather than at a single point in time, closing the gap between "we have a policy" and "it is actually true right now" |

### What auditors actually look for

An auditor does not take "we have a policy that says X" as evidence that X is true. The standard pattern, worth internalizing because it is also how you should evaluate your own controls before an auditor ever shows up:

1. **The control exists and is documented.** A policy or procedure describes what should happen.
2. **The control is actually implemented.** A configuration, a system setting, or a completed process step demonstrates it is in place, not just described.
3. **The control operated consistently over the relevant period.** Evidence (logs, tickets, sign-offs, sampled records) shows it worked repeatedly, not just once, around the time someone remembered to check.

This three-part pattern is exactly why SOC 2 Type II (operation over a period) is a stronger signal than Type I (design at one point in time), as introduced in [Frameworks and standards](02-frameworks-and-standards.md).

### Common audit findings

| Finding pattern | Root cause |
|---|---|
| "Policy requires X, but the system is configured to allow not-X" | Policy and implementation drifted apart over time |
| "Access reviews are supposed to happen quarterly; the last one on record is from fourteen months ago" | A control that exists on paper but has stopped actually running |
| "Terminated employees retained system access past their last working day" | Offboarding process gap, often between HR and IT systems that do not talk to each other automatically |
| "No evidence the control operated; the responsible team says it happens but nothing documents it" | A real control with no audit trail, which an auditor cannot distinguish from a control that does not happen at all |

**Practical implication:** build evidence generation into the control itself, not as a separate step performed later. A control that automatically logs its own execution is auditable by design; a control that depends on someone remembering to screenshot it for the auditor eventually fails exactly when it matters most.

## Third-party and supply chain risk

Introduced briefly in [Risk management](01-risk-management.md): any vendor, contractor, or partner with access to your systems or data carries risk that remains yours to manage, because your customers, regulators and your own leadership will not distinguish "we were breached" from "our vendor was breached and that is how they reached us."

### Due diligence before the relationship starts

| Step | What it checks |
|---|---|
| **Security questionnaire or review** | The vendor's own controls, matched to the sensitivity of what they will access |
| **Request existing attestations** | A current SOC 2 report or ISO/IEC 27001 certificate often answers most of a questionnaire at once, and is stronger evidence than self-reported answers |
| **Scope the access precisely** | What data, systems and permissions does this relationship actually require, kept to the minimum, consistent with the least-privilege principle running through this entire knowledge base |
| **Contract terms** | Security obligations, breach notification timelines to you specifically, audit rights, data handling and deletion requirements, liability |
| **Data location and sub-processors** | Where data will actually be stored and processed, and whether the vendor itself uses further vendors (sub-processors) that extend the chain |

### Ongoing oversight, not a one-time check

| Practice | Why |
|---|---|
| **Re-assess on a schedule**, tiered by how critical the vendor is | A vendor's security posture changes; a point-in-time review at onboarding goes stale |
| **Monitor for the vendor's own incidents** | Public breach disclosures, security advisories, and news coverage relevant to vendors you depend on |
| **Review access periodically** | Confirm the vendor still has only what it currently needs, not what it was granted at onboarding and never revisited |
| **Have an offboarding plan** | When the relationship ends, access, data and credentials need a clean, verified termination, the same discipline as employee offboarding |
| **Tier vendors by criticality** | A vendor with deep access to sensitive data or core systems deserves far more scrutiny and more frequent review than one with trivial, low-risk access; treating every vendor identically wastes effort on low-risk ones and under-scrutinizes the ones that matter |

### Supply chain risk beyond vendors in the traditional sense

The software and infrastructure supply chain risks already covered in depth in [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md#the-software-supply-chain) are a specific, technical instance of this same third-party risk discipline: an open-source dependency, a build tool, or a CI action is, in risk terms, exactly a vendor you did not formally onboard but whose compromise still becomes your incident.

## Connecting this to the rest of the knowledge base

| This page's concept | Where it is applied elsewhere |
|---|---|
| Policy and control gap | The specific technical controls throughout sections 2 through 9 are what a policy here would actually require |
| Audit evidence discipline | [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md) is largely what makes a control's operation provable |
| Third-party due diligence | [Cloud security fundamentals](../08-cloud-and-infrastructure/01-cloud-security-fundamentals.md) for cloud providers specifically |
| Vendor incidents becoming your incident | [Incident response](../07-defensive-security/04-incident-response.md) |

## Practice

1. Write one real policy (not a template copied unread) for something you actually manage, following the policy-standard-procedure-guideline hierarchy: one policy statement, the standard that makes it measurable, and the procedure that implements it.
2. Pick one control you believe you already have in place and apply the three-part auditor test to it: does it exist and is it documented, is it actually implemented, and can you produce evidence it operated consistently over the last few months? Identify the weakest of the three.
3. List every third party with access to something you are responsible for (cloud providers, software vendors, contractors), and tier each by the sensitivity of what they can reach.
4. For your highest-tier third party, find whatever attestation or security documentation they publish and read it critically: what does it actually demonstrate, and what gap remains that it does not cover?
5. Design an offboarding checklist, for either an employee or a vendor relationship, that leaves no access, credential, or data copy unaccounted for.

These support the [GRC track](../../roadmap/phase-3-specialization/track-grc.md) of the roadmap.

## What to do with this

- [ ] Explain the difference between a policy, a standard, a procedure and a guideline, and why conflating them causes problems.
- [ ] Apply the three-part auditor test to one of your own controls and identify its weakest link.
- [ ] Build evidence generation into one control you run, so it documents its own operation automatically.
- [ ] Tier your own third parties by criticality and apply proportionate scrutiny to each tier.
- [ ] Write one complete, real offboarding checklist and use it.

## Key references

AICPA Trust Services Criteria · ISO/IEC 27001:2022 (management review and internal audit requirements) · NIST SP 800-53 (supply chain risk management family). Full list in [References](../15-references.md).
