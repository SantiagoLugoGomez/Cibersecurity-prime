# Frameworks and standards

> [!TIP]
> **In short:** frameworks and standards exist so organizations do not each have to invent, from scratch, what "good security" means. They differ in what they are for: some describe **a management system** (how a security program is run and improved), some give **a certifiable, auditable control set**, some give **a free, prioritized starting list**, and some are **required by a specific industry or contract**. Knowing which is which, and how they map to each other, is what lets you answer "which framework should we use?" with "it depends what you need it to do," rather than a brand preference.

## Why more than one framework exists

| Need | The right kind of framework |
|---|---|
| "How should our security program be governed and continuously improved?" | A management system standard (ISO/IEC 27001) |
| "What specific technical and organizational controls should we have?" | A control catalog (NIST SP 800-53, ISO/IEC 27002, CIS Controls) |
| "We have almost no resources; what should we do first?" | A prioritized, free starting point (CIS Controls Implementation Group 1) |
| "A customer or regulator requires a specific certification" | Whatever that customer or regulator specifies (SOC 2, PCI DSS, an industry-specific requirement) |
| "How do we talk about cybersecurity risk at the leadership and board level?" | A risk-communication framework (NIST CSF 2.0) |

Most mature organizations end up using several together: a management system to govern the program, a control catalog to populate it, and a risk framework to communicate about it, mapped to whatever a specific customer or regulator additionally requires.

## NIST Cybersecurity Framework 2.0

CSF 2.0 (February 2024) organizes cybersecurity activity into six functions, already introduced from the incident-response angle in [Incident response](../07-defensive-security/04-incident-response.md#from-phases-to-functions):

| Function | Question it answers |
|---|---|
| **Govern** | Is there oversight, strategy and accountability for cybersecurity risk? (Added in 2.0, reflecting that the earlier five functions do not run themselves) |
| **Identify** | What do we have, and what risk does it carry? |
| **Protect** | What safeguards are in place? |
| **Detect** | How would we notice something wrong? |
| **Respond** | What do we do once we notice? |
| **Recover** | How do we get back to normal, and improve from it? |

Underneath the six functions sit categories and subcategories (106 subcategories in total), each a specific outcome statement, not a prescribed technical control; CSF deliberately leaves *how* to achieve each outcome open, which is why organizations commonly pair it with a control catalog that fills in the specifics. **●●●** CSF also introduces **Community Profiles** (the same mechanism behind NIST's revised incident response guidance, SP 800-61 Revision 3) and **Organizational Profiles**, which let an organization describe its current and target state against the framework and track the gap between them, which is often the most directly useful artifact CSF produces for a management conversation.

## ISO/IEC 27001 and 27002

**ISO/IEC 27001:2022** is a certifiable **management system standard**: it specifies requirements for establishing, implementing, maintaining and continually improving an information security management system (ISMS), built on a risk-based, plan-do-check-act cycle. Its **Annex A** lists 93 controls across four themes (organizational, people, physical, technological), and **ISO/IEC 27002:2022** provides the detailed implementation guidance for each. **●●●**

| Point | Detail |
|---|---|
| **Certifiable** | An accredited external auditor can certify an organization against it, which is why it appears frequently in vendor and contract requirements |
| **Risk-based scope** | Organizations select and justify which Annex A controls apply to them through their own risk assessment, documented in a **Statement of Applicability**; not every control is mandatory for every organization |
| **The 2022 update** | Restructured from 2013's 114 controls across 14 domains into 93 controls across 4 themes, adding 11 new controls (including explicit coverage of threat intelligence and cloud security) reflecting a decade of changed practice |
| **Transition** | Organizations certified under the 2013 edition had until October 2025 to transition; if you encounter a certificate that still cites 2013, that is now a stale reference worth questioning |

## NIST SP 800-53

A far more granular **control catalog**, developed for US federal information systems but used well beyond that context as a detailed reference. It organizes hundreds of controls into families (access control, audit and accountability, incident response, and many more) and supports tailored baselines by impact level (low, moderate, high), making it the natural choice when you need prescriptive technical and procedural detail rather than the outcome-level statements of CSF or the more implementation-flexible Annex A controls of ISO 27002.

## CIS Controls and CIS Benchmarks

Already introduced in [Adversaries and attack frameworks](../01-foundations/04-adversaries-and-attack-frameworks.md) and [Hardening and resilience](../07-defensive-security/08-hardening-and-resilience.md): the **CIS Controls** (version 8.1) are a free, prioritized set of safeguards grouped into **Implementation Groups**, with **IG1** specifically designed as "essential cyber hygiene," a practical, resource-light starting point for an organization with no mature program yet. The **CIS Benchmarks** are the detailed, platform-specific configuration guidance that operationalizes hardening in practice. Of everything in this page, CIS Controls IG1 is the most defensible answer to "we have almost nothing; where do we start?"

## SOC 2

A **SOC 2** report is an independent auditor's attestation, not a certification against a fixed control list, that an organization's controls meet the **Trust Services Criteria** (security, and optionally availability, processing integrity, confidentiality and privacy) relevant to the service it provides. It is the report most commonly requested of a software or cloud service vendor by its own business customers, and it comes in two types:

| Type | Covers |
|---|---|
| **Type I** | Whether controls are suitably designed, at a single point in time |
| **Type II** | Whether those controls actually operated effectively over a period (typically 6 to 12 months) |

A Type II report is the far stronger signal, since it reflects sustained operation rather than a design on paper.

## PCI DSS

Already introduced in [Penetration testing methodology](../06-offensive-security/01-penetration-testing-methodology.md): the **Payment Card Industry Data Security Standard** (currently version 4.0.1) is a mandatory, contractually enforced standard for any organization that stores, processes or transmits payment card data, set by the card brands rather than a government or standards body. It specifies prescriptive technical and procedural requirements across twelve requirement areas, with compliance validated through self-assessment or formal audit depending on transaction volume, and carries real contractual and financial consequences (fines, increased transaction fees, and in serious cases, loss of the ability to process cards) for non-compliance, which sets it apart from the largely voluntary frameworks elsewhere on this page.

## Sector and regional frameworks, briefly

| Framework | Scope |
|---|---|
| **HIPAA Security Rule** | US health information |
| **DORA** (Digital Operational Resilience Act) | EU financial sector operational resilience, including the threat-led penetration testing requirements already introduced in [Penetration testing methodology](../06-offensive-security/01-penetration-testing-methodology.md) |
| **NIS2 Directive** | EU critical infrastructure and essential services cybersecurity obligations |
| **Colombia's MSPI, SFC and sector-specific requirements** | Covered in detail in [Colombian regulatory landscape](05-colombian-regulatory-landscape.md) |

## Mapping frameworks to each other

Because so many frameworks ultimately describe overlapping, sensible security practice, mapping tables between them (CSF to ISO 27001 Annex A, CIS Controls to NIST SP 800-53, and similar) are published and widely used, so that implementing one well typically covers much of another, with the remaining gap being about documentation and specific wording rather than genuinely different practice. **Practical implication:** do not implement the same control five separate times to satisfy five frameworks' different names for it; implement it once, well, and document the mapping.

## Choosing and combining, in practice

| Situation | A reasonable approach |
|---|---|
| Small organization, no existing program | Start with CIS Controls IG1; add CSF 2.0 for leadership communication once the basics are in place |
| Needs to sell to enterprise customers | SOC 2 Type II is often the specific, concrete requirement; build toward it using CIS Controls or ISO 27002 as the underlying control set |
| Handles payment cards | PCI DSS compliance is mandatory, not optional, regardless of what else is in use |
| Operating in a regulated sector or specific country | The sector or national requirement sets the floor; general frameworks fill in what it does not specify |
| Wants external certification as a market signal | ISO/IEC 27001 |
| Needs a detailed, prescriptive technical baseline | NIST SP 800-53, tailored to an appropriate impact level |

## Practice

1. Pick an organization you know (even informally, such as a small business or club) and draft a CSF 2.0 Organizational Profile for it: a rough current-state and target-state statement for each of the six functions.
2. Map the CIS Controls IG1 safeguards against ISO/IEC 27002's control themes and identify which ISO controls are substantially satisfied by implementing IG1 well.
3. Read a real SOC 2 Type II report (several vendors publish redacted or summary versions publicly) and identify which Trust Services Criteria it covers and what the auditor actually tested.
4. Write a one-page explanation, in plain language for a non-technical manager, of why PCI DSS compliance is not optional for an organization that accepts card payments, using the mandatory-versus-voluntary distinction from this page.
5. For one framework from this page, find its current official source document and confirm the version and date you are citing, rather than relying on a secondary summary.

These support the [GRC track](../../roadmap/phase-3-specialization/track-grc.md) of the roadmap.

## What to do with this

- [ ] Explain the difference between a management system standard, a control catalog, a free prioritized list, and a mandatory industry standard, with one example of each.
- [ ] Explain what CSF 2.0's Govern function adds that was missing from the original five-function framework.
- [ ] Explain the difference between a SOC 2 Type I and Type II report and why the distinction matters to whoever is relying on it.
- [ ] Recommend a starting framework for a small organization with no existing program, and justify it.
- [ ] Find and read the current official text of one framework mentioned on this page, rather than relying only on this summary.

## Key references

CIS Controls v8.1 · ISO/IEC 27001:2022 and 27002:2022 · NIST CSF 2.0 · NIST SP 800-53 · PCI DSS 4.0.1 · SOC 2 Trust Services Criteria (AICPA). Full list in [References](../15-references.md).

<!-- navigation -->
[← Risk management](01-risk-management.md) · [Index](../00-start-here.md) · [Policies, audit and third-party risk →](03-policies-audit-and-third-party-risk.md)
