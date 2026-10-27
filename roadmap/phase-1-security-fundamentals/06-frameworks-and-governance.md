# Module 1.6: Frameworks, vulnerability management and governance (weeks 14-16)

Security is also an organizational discipline. This module gives you the frameworks and the risk vocabulary that every role touches, with a Colombian focus so it is relevant where you will work.

**Main resources:** [NIST CSF 2.0](https://www.nist.gov/cyberframework), [CIS Controls v8.1](https://www.cisecurity.org/controls/v8-1), [FIRST (CVSS and EPSS)](https://www.first.org/), [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), Colombian regulations (see [legal-and-ethics.md](../../legal-and-ethics.md)).

## Week 14: Frameworks and controls

**Goal:** describe a security program with NIST CSF 2.0 and implement it with concrete controls.

**R. Read and study (75 min)**
- [NIST CSF 2.0 (CSWP 29)](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf): the six functions and the tiers/profiles concept.
- [CIS Controls v8.1](https://www.cisecurity.org/controls/v8-1): the 18 controls and Implementation Group 1.
- Notes: the six CSF functions (Govern, Identify, Protect, Detect, Respond, Recover) and why Govern is central; what a CSF profile and tier are; how CIS Controls IG1 maps to CSF outcomes; the idea of ISO/IEC 27001 (an ISMS) and 27002's 93 controls in four themes.
- Flashcards: the six CSF functions, what Govern added in 2.0, what IG1 is, ISO 27001 vs 27002.

**P. Guided practice (90 min)**
- Take the fictional 20-person accounting firm in Bogotá and write a CSF 2.0 current profile: for each of the six functions, one or two sentences on where they are today.
- Map five CIS IG1 safeguards to the CSF functions they support.

**D. Deep practice (3 h)**
- Write a target profile and a short roadmap for the same firm: for each function, the target state and the two or three concrete steps (drawn from CIS IG1) to get there, prioritized. Keep it to two pages, management-readable.
- This is exactly the deliverable a GRC analyst or vCISO produces.

**E. English (60 min)**
- Read the CSF 2.0 "Govern" function description. Explain, in English, why governance was elevated to its own function in 2.0, in 150 words.

**Check yourself**
1. Name the six CSF 2.0 functions and what each covers.
2. What is a CSF profile, and what is the difference between current and target?
3. How do the CIS Controls relate to the CSF?
4. What is the difference between ISO/IEC 27001 and 27002?
5. Why is "Govern" at the center of CSF 2.0?

**Deliverable:** the current and target CSF 2.0 profiles with a prioritized roadmap for the fictional firm.

## Week 15: Vulnerability management and prioritization

**Goal:** understand how organizations find, score and prioritize vulnerabilities, because drowning in findings is the real-world problem.

**R. Read and study (75 min)**
- [FIRST CVSS v4.0](https://www.first.org/cvss/v4-0/) specification overview, and [EPSS](https://www.first.org/epss/).
- [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) and how it is used.
- Notes: CVE vs CVSS vs EPSS vs KEV and what each tells you; why CVSS alone over-prioritizes; how EPSS (probability of exploitation) and KEV (confirmed exploited) sharpen prioritization; the vulnerability management lifecycle (discover, assess, prioritize, remediate, verify).
- Flashcards: CVE vs CVSS vs EPSS vs KEV, CVSS base vs temporal vs environmental, what the KEV catalog means for a vuln.

**P. Guided practice (90 min)**
- Take ten real recent CVEs. For each, record the CVSS score, the EPSS probability and whether it is in the KEV catalog. Then rank them for a hypothetical company and justify the top three.
- Run a vulnerability scan in your lab (e.g. with [Prowler](https://github.com/prowler-cloud/prowler) on a cloud account, or `pip-audit`/`npm audit` on a project) and triage the output.

**D. Deep practice (3 h)**
- Write a one-page "prioritization policy": given a stream of findings, how should this fictional company decide what to fix first, using CVSS, EPSS, KEV and asset exposure together? Apply it to your ten CVEs and produce a ranked remediation list with reasons.
- This is a frequent interview topic and a real daily task.

**E. English (60 min)**
- Read the EPSS FAQ. Write three sentences, in English, explaining to a manager why a CVSS 9.8 vulnerability might be lower priority than a CVSS 7.5 one.

**Check yourself**
1. What is the difference between a CVE, a CVSS score, an EPSS score and the KEV catalog?
2. Why is prioritizing purely by CVSS a mistake?
3. What does EPSS add that CVSS does not?
4. What does inclusion in the KEV catalog tell you?
5. What are the stages of the vulnerability management lifecycle?

**Deliverable:** the prioritization policy and the ranked remediation list for your ten CVEs.

## Week 16: Governance, compliance and Colombian context

**Goal:** understand the regulatory and governance environment you will actually work in.

**R. Read and study (75 min)**
- Re-read [legal-and-ethics.md](../../legal-and-ethics.md) for the Colombian laws.
- Read about the Colombian public-sector security model (MinTIC's MSPI, updated in 2025 to align with ISO/IEC 27001:2022) and, for the financial sector, the Superintendencia Financiera's cybersecurity circular (CE 007 de 2018).
- Notes: what an ISMS and a security policy framework are; the roles of risk owner, control owner and auditor; how Ley 1581 (data protection) and sector rules translate into controls; incident reporting obligations in Colombia.
- Flashcards: ISMS, MSPI, who enforces Ley 1581, what CE 007 de 2018 requires at a high level.

**P. Guided practice (90 min)**
- Build a risk register for the fictional firm: ten risks, each with description, owner, likelihood, impact, inherent rating, treatment decision (accept/mitigate/transfer/avoid) and residual rating.
- Map three of the risks to the specific Colombian obligation they relate to (e.g. personal-data exposure to Ley 1581).

**D. Deep practice (3 h)**
- Write two one-page policies the firm needs: an acceptable use policy and an information security policy, aligned with NIST CSF 2.0 and referencing the relevant Colombian law. Make them realistic and enforceable, not boilerplate.
- This is GRC portfolio material and useful even if you go technical, because you will have to read and satisfy such policies.

**E. English (60 min)**
- Write the information security policy in English (the acceptable use policy can be in Spanish). Practice the formal-but-clear register these documents require.

**Check yourself**
1. What is an ISMS, and what does ISO/IEC 27001 require of one?
2. Who enforces Ley 1581 de 2012, and what can they impose?
3. What is a risk register, and what does "residual risk" mean?
4. What are the four risk treatment options?
5. What does the MSPI require of Colombian public entities, at a high level?

**Deliverable:** the risk register and the two policies, with Colombian legal references.

## End of Phase 1

You should now be able to reason about how any system fails and which control addresses it, and to speak the language of both engineers and management. Confirm the mastery checklist in the [Phase 1 overview](README.md).

Next: [Phase 2, guided practice](../phase-2-guided-practice/README.md).
