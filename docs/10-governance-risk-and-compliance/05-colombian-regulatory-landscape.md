# Colombian regulatory landscape

> [!TIP]
> **In short:** Colombia's cybersecurity regulation is built in layers that arrived at different times for different reasons: a national policy line (the CONPES documents) that evolved from pure state defense toward shared, economy-wide risk management; a criminal law ([Ley 1273 de 2009](../01-foundations/05-legal-and-ethics.md)) and a data protection law ([Ley 1581 de 2012](04-privacy-and-data-protection.md)), both covered in depth elsewhere; a specific, binding technical regime for the financial sector; and an institutional architecture that splits state cyber defense, criminal investigation and civilian coordination across three different bodies. This page is the map connecting those layers; the two statutes get their own dedicated, close treatment on the pages already linked above.

## The policy line: CONPES documents

**CONPES** (Consejo Nacional de Política Económica y Social) documents are national policy guidance, not law, but they shape what later becomes law, regulation and institutional structure. Three in this area matter, and tracking how the scope widened across them tells the story of the whole field in Colombia:

| Document | Year | Scope | Shift from the previous one |
|---|---|---|---|
| **CONPES 3701** | 2011 | Ciberseguridad y ciberdefensa: the state's own defense of national interests in cyberspace | The starting point; created coordination mechanisms and the role that became the national digital security coordinator |
| **CONPES 3854** | 2016 | Política Nacional de Seguridad Digital: risk management extended to all of society and the economy, not just the state | Reframed digital security from a defense problem to a shared risk-management responsibility across all stakeholders, with an explicitly preventive rather than reactive posture |
| **CONPES 3995** | 2020 | Política Nacional de Confianza y Seguridad Digital | Added **digital trust** as an explicit goal alongside security, and pushed to strengthen governance, which the document itself identified as still underdeveloped |

A later, narrower document, **CONPES 4144 (2025)**, addresses the responsible development and adoption of artificial intelligence specifically; MinTIC has aligned its AI-specific security and privacy guidance with it, but it should not be read as a fourth general digital-security CONPES in the same line as the three above. **◇** Verify its current scope and status against DNP's own published document before citing it for anything beyond AI policy.

**Decreto 338 de 2022** followed on from this policy line to establish the actual governance **model and instances** for digital security at the national level, giving the earlier CONPES documents' coordination concepts a formal institutional structure.

## The institutional architecture

Colombia splits cyber-related state functions across three distinct bodies, each with a different mandate; confusing them is a common mistake worth avoiding deliberately.

| Body | Mandate | Reports to |
|---|---|---|
| **colCERT** | National coordination for cybersecurity and cyberdefense incidents; the country's national computer emergency response coordination point | Positioned within the national digital security system under the governance structure set out in Decreto 338 de 2022 |
| **Comando Conjunto Cibernético (CCOC)** | Military cyberdefense: protecting national interests in cyberspace from a defense posture | The Comando General de las Fuerzas Militares |
| **Centro Cibernético Policial (CCP)**, including its **CAI Virtual** | Prevention, citizen reporting, and criminal investigation of cybercrime (the enforcement side of [Ley 1273 de 2009](../01-foundations/05-legal-and-ethics.md)) | Policía Nacional |

In practice these three coordinate: the CCP commonly handles the largest volume of citizen-facing incident response alongside colCERT, while CCOC's mandate is specifically military and national-security focused rather than ordinary cybercrime. If you are reporting an ordinary cybercrime as a citizen or a business, the CCP's channels are the relevant starting point; a national-level, cross-sector incident affecting critical infrastructure is where colCERT's coordination role becomes central. Verify current reporting channels and institutional detail directly against MinTIC's and the Policía Nacional's own current published guidance, since this architecture has evolved through several decrees and is reasonably likely to continue evolving.

## The public sector security model: MSPI

Already introduced in [Privacy and data protection](04-privacy-and-data-protection.md#the-public-sector-layer-mspi): MinTIC's **Modelo de Seguridad y Privacidad de la Información**, most recently updated by **Resolución 02277 de 2025**, is the operational security and privacy model Colombian public entities are expected to implement, built to align with ISO/IEC 27001. For a private organization, it is not a binding obligation, but it is a free, Spanish-language, locally relevant reference model worth knowing regardless of sector, and it is frequently the framework cited in Colombian public-sector security documentation you may encounter working with or for government clients.

## The financial sector's binding technical regime

Unlike the general policy line above, the financial sector has a specific, binding, technical cybersecurity regulation from its own regulator, independent of the general CONPES policy guidance:

| Instrument | Content |
|---|---|
| **Superintendencia Financiera de Colombia, Circular Externa 007 de 2018** | Minimum requirements for information security and cybersecurity risk management for supervised entities, incorporated into the Circular Básica Jurídica; covers governance, risk management stages, and requires business continuity plans to explicitly address cyber risk response, recovery and restoration |
| **Circular Externa 033 de 2020** | Built on the 2018 circular, adding a unified incident taxonomy and standardized reporting of security metrics and incidents |

This is the regime that explains why Colombian banks and other supervised financial entities run mature security programs, bug bounty relationships, and formal incident reporting well beyond what the general CONPES policy line requires of other sectors: for them, it is not voluntary good practice, it is supervised compliance with specific, binding instructions from their prudential regulator. Confirm the current, consolidated text and any subsequent amendments directly against the Superintendencia Financiera's own published Circular Básica Jurídica before relying on specific requirement details.

## How the pieces fit together

| If you are... | The layer that applies |
|---|---|
| Any individual or organization, regarding unauthorized access to systems | [Ley 1273 de 2009](../01-foundations/05-legal-and-ethics.md) (criminal law) |
| Any organization processing personal data | [Ley 1581 de 2012](04-privacy-and-data-protection.md) and SIC oversight |
| A Colombian public entity | MSPI, under the governance structure of Decreto 338 de 2022 |
| A financial entity supervised by the SFC | Circular Externa 007 de 2018 and 033 de 2020, in addition to everything above |
| Reporting a cybercrime as a citizen or business | The Centro Cibernético Policial (CCP) |
| Involved in a national-level, cross-sector incident | colCERT's coordination role |
| Building AI systems in or for Colombia | MinTIC's AI security and privacy guidance, aligned with CONPES 4144 |

## The civil society and professional landscape

Beyond law and regulation, Colombia has an active professional security community worth connecting with early, covered in more depth in [Community](../11-learning-and-career/07-community.md): local OWASP chapters in Bogotá and Medellín, national conferences such as DragonJAR Security Conference and BSides Colombia, and a growing number of organizations (including some of the country's largest banks) running public bug bounty programs. This professional layer is where the formal regulatory structure above actually gets implemented day to day, and it is the fastest way to learn how these rules are applied in practice rather than only on paper.

## A caution on currency

Every specific figure, circular number, decree number, and institutional detail on this page reflects research current as of this writing. Colombian digital security regulation has changed meaningfully several times over the past fifteen years (three CONPES documents in under a decade, a reform bill to Ley 1581 under active discussion, resolutions updating MSPI), and nothing here should be treated as a substitute for checking the current, official source before a decision that actually depends on it: DNP's CONPES document registry, MinTIC's Gobierno Digital portal, the SIC's data protection guidance, and the Superintendencia Financiera's Circular Básica Jurídica are the authoritative places to verify anything this page summarizes.

## Practice

1. Read the actual text (not a summary) of one CONPES document from the policy-line table and identify, in your own words, what specifically changed from the one before it.
2. Find colCERT's, the CCP's and the CCOC's own current official descriptions of their mandates, and write a one-paragraph explanation of how they divide responsibility, checking your explanation against this page's table.
3. If you work with or plan to work with a Colombian financial entity, read the current consolidated text of Circular Externa 007 de 2018 as amended, and map its required risk management stages against the control families you have already learned in [Frameworks and standards](02-frameworks-and-standards.md).
4. Check the current status of the Ley 1581 reform bill against the Congress's own tracking tools, and note what, if anything, has changed since this page was written.
5. Explain, to someone unfamiliar with Colombian regulation, why a Colombian bank's cybersecurity program and a Colombian retailer's cybersecurity program are not held to the same binding technical standard, even though both must comply with Ley 1273 and Ley 1581 equally.

These support the [GRC track](../../roadmap/phase-3-specialization/track-grc.md) of the roadmap.

## What to do with this

- [ ] Explain the shift across CONPES 3701, 3854 and 3995 without notes.
- [ ] Correctly identify which of colCERT, CCOC or the CCP handles a given scenario.
- [ ] Explain why the financial sector's cybersecurity obligations differ from the general policy line, and name the instrument that creates that difference.
- [ ] Find and bookmark the current, official sources for every instrument named on this page.
- [ ] Explain the connection between this page and the two statutes it deliberately does not duplicate, [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md) and [Privacy and data protection](04-privacy-and-data-protection.md).

## Key references

CONPES 3701, 3854, 3995 and 4144 (DNP) · Decreto 338 de 2022 · MinTIC MSPI (Resolución 02277 de 2025) · Superintendencia Financiera de Colombia, Circular Externa 007 de 2018 and 033 de 2020. Full list in [References](../15-references.md).

<!-- navigation -->
[← Privacy and data protection](04-privacy-and-data-protection.md) · [Index](../00-start-here.md) · [Learning science →](../11-learning-and-career/01-learning-science.md)
