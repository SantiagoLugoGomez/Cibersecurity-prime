# Reading professional material

Advisories, CVE descriptions, threat intelligence and incident reports, and RFCs are written in a dense, precise register. Reading them fluently is a C2 skill in itself, and it is also how you stay current in the field. This page gives you a method and real sources to practice on.

## Why this register is hard

Professional security writing packs a lot into short sentences and leans on patterns that general English courses skip:

- **Hedging and conditionals.** "An attacker *could* obtain code execution *if* the service is exposed and *provided that* authentication is misconfigured." The meaning lives in the modal verbs and conditions. Misreading "could" as "will" changes the severity.
- **Passive voice and nominalization.** "Exploitation of this vulnerability may lead to unauthorized disclosure of information." The actor disappears and verbs become nouns ("exploitation", "disclosure"). This is normal here, not bad writing.
- **Precise verbs.** *Mitigate*, *remediate*, *disclose*, *coordinate*, *escalate*, *chain*, *leverage*, *bypass* each mean something specific.
- **Standardized structure.** Once you know the shape of each document type, you can read it fast.

## A method for reading any security text

1. **Identify the type and its structure first.** An advisory, a CVE and an RFC are built differently (see below). Knowing the shape tells you where the answer to "what, how bad, what do I do" lives.
2. **First pass for the gist.** Read the summary or abstract and the headings only. Answer in one sentence: what is affected and why does it matter?
3. **Second pass for precision.** Read fully. Pay attention to every modal verb (*may*, *could*, *must*, *should*) and condition (*if*, *when*, *provided that*, *unless*). These set the real severity and the prerequisites for an attack.
4. **Extract the actionable core.** For an advisory: affected versions, impact, prerequisites, fix. For a report: initial access, actions, impact, detections.
5. **Mine it for language.** Pick three to five expressions you understood but could not have produced, and add them to your personal glossary with the exact sentence. Target the verbs and collocations, not just nouns.
6. **Summarize in your own words**, in English, in two or three sentences. If you cannot, you did not fully understand it; go back to step 3.

Do steps 1-4 on everything you read for labs anyway. Do steps 5-6 on two texts per week deliberately.

## Document types and where to practice

### Security advisories

Vendor or government notices that a vulnerability exists and what to do. Structure: summary, affected products and versions, impact, prerequisites, remediation, references.

- [CISA advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) and the [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog): the catalog is a running list of vulnerabilities confirmed to be exploited in the wild. Start here; the writing is clear and consistent.
- [Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide) and vendor advisories from the products you use.

Language to watch: "an unauthenticated, remote attacker", "under certain conditions", "successful exploitation could allow", "customers are advised to update".

### CVE descriptions

A CVE is a single standardized paragraph: the identifier, the affected product, the weakness, and the impact, often in one long sentence. Severity is scored separately with CVSS.

- [CVE Program](https://www.cve.org/) and the [NVD](https://nvd.nist.gov/vuln) for the CVSS score and weakness (CWE) mapping.
- Practice by reading the CVEs referenced in the advisories above, then restating each as: *who* can do *what*, *where*, under *which conditions*.

Language to watch: the standard frame "A \<weakness> in \<product> \<version> allows \<attacker> to \<impact> via \<vector>."

### Threat intelligence and incident reports

Longer narrative documents describing a real intrusion or a threat actor: timeline, techniques (usually mapped to MITRE ATT&CK), indicators, and recommendations.

- [The DFIR Report](https://thedfirreport.com/): detailed, well-structured real intrusions. Excellent for both the technical content and the writing.
- Annual reports such as the [Verizon Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) and vendor threat reports (for example Mandiant M-Trends). These teach the register used to describe trends and statistics.
- [MITRE ATT&CK](https://attack.mitre.org/) technique pages: short, precise descriptions of how a technique works.

Language to watch: sequence and causation ("the actor then", "which allowed", "as a result"), and the past-tense narrative voice of an investigation.

### RFCs and standards

The documents that define how protocols work. Dense but exact. The key skill is the precise meaning of the requirement words.

- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) defines MUST, SHOULD and MAY. Read it once; it unlocks every other RFC and most standards. In security writing, "MUST" is an absolute requirement and "SHOULD" means recommended but with room for judgment.
- Good first RFCs: [RFC 9116 (security.txt)](https://www.rfc-editor.org/rfc/rfc9116) is short and relevant; [RFC 8446 (TLS 1.3)](https://www.rfc-editor.org/rfc/rfc8446) is long, so read only the overview sections.
- NIST publications such as [SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) use the same requirement language and are very readable.

Language to watch: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, REQUIRED, and the difference between "is" (description) and "shall" (requirement).

## A weekly routine

- Read one CISA advisory or CVE closely (10 minutes). Restate it in one sentence.
- Read one section of a DFIR or threat report (20 minutes). Note three expressions.
- Once a fortnight, read a short RFC or one section of a NIST document.
- Keep adding to your personal glossary. By the end of a semester you will have a vocabulary list built entirely from real professional English, which is exactly the register interviews and reports require.
