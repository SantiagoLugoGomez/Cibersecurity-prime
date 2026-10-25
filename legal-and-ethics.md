# Legal limits and ethics

Read this before you touch any system you do not own. The skills in this roadmap are the same whether they are used to defend or to attack; the law and your ethics are what separate a security professional from a criminal. In Colombia, computer crimes carry real prison sentences, and being a student is not a defense.

This page is a practical summary for a student practitioner. It is not legal advice. When in doubt, do not act, and consult a qualified lawyer.

## The one rule that keeps you safe

**Only test systems you own or have explicit, written authorization to test.**

Everything else follows from this. Your home lab, deliberately vulnerable apps you host yourself, and platforms that authorize testing (TryHackMe, Hack The Box, picoCTF, OverTheWire, bug bounty targets within their stated scope) are all fine. A website, app, network or device that does not fall in one of those categories is off limits, no matter how easy the vulnerability looks or how good your intentions are.

"I was just looking" and "I didn't change anything" are not defenses under Colombian law. Unauthorized access is itself the crime.

## Colombian law

### Ley 1273 de 2009: computer crimes

Ley 1273 de 2009 added a chapter titled "protection of information and data" to the Penal Code (Código Penal, Ley 599 de 2000). It defines distinct computer crimes, each with prison terms stated in months and fines in current monthly minimum wages (salarios mínimos mensuales legales vigentes, SMMLV). Official text: [Secretaría del Senado](http://www.secretariasenado.gov.co/senado/basedoc/ley_1273_2009.html) and [Función Pública](https://www.funcionpublica.gov.co/eva/gestornormativo/norma_pdf.php?i=34492).

| Article | Conduct | Penalty |
|---|---|---|
| 269A | Abusive access to a computer system (accessing without authorization, or staying against the owner's will) | 48 to 96 months prison, 100 to 1000 SMMLV fine |
| 269B | Illegitimate obstruction of a system or network | 48 to 96 months, 100 to 1000 SMMLV |
| 269C | Interception of computer data without a court order | 36 to 72 months |
| 269D | Computer damage (destroy, damage, delete, alter data) | 48 to 96 months, 100 to 1000 SMMLV |
| 269E | Use of malicious software (produce, traffic, acquire, distribute, sell, send, introduce malware) | 48 to 96 months, 100 to 1000 SMMLV |
| 269F | Violation of personal data (obtain, compile, sell, send, buy, divulge personal data for gain, without authorization) | 48 to 96 months, 100 to 1000 SMMLV |
| 269G | Website spoofing to capture personal data (phishing pages, malicious links and pop-ups) | 48 to 96 months, 100 to 1000 SMMLV |
| 269H | Aggravating circumstances | Penalties above increase by one-half to three-quarters |
| 269I | Theft by computer means | Penalties of theft (art. 240 of the Penal Code) |
| 269J | Non-consensual transfer of assets (computer fraud) | 48 to 120 months, 200 to 1500 SMMLV |

The aggravating circumstances in 269H raise the penalty when, among other things, the conduct targets state or official systems or the financial sector, is committed by someone abusing a position of trust, or uses another person as an unwitting tool. Several of these articles apply directly to exactly the techniques you learn in this roadmap: a port scan plus login attempt against a system you were not authorized to test can be abusive access (269A); running malware outside an isolated lab can implicate 269E; a phishing page built "for practice" against a real site can be 269G.

Colombia also approved the Council of Europe Convention on Cybercrime (the Budapest Convention) through **Ley 1928 de 2018**, upheld by the Constitutional Court in judgment C-224 of 2019. This strengthens international cooperation, which means cross-border "practice" against foreign systems is not a way around the law.

### Ley 1581 de 2012: personal data protection

Ley 1581 de 2012 is Colombia's general personal data protection law. It is enforced by the Superintendencia de Industria y Comercio (SIC). Official text: [SUIN-Juriscol](https://www.suin-juriscol.gov.co/viewDocument.asp?ruta=Leyes/1684507) and [Secretaría del Senado](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html); its main regulation is Decreto 1377 de 2013.

What matters for a security practitioner:

- **Consent and purpose.** Personal data may be processed only with the owner's prior, informed consent and only for the stated purpose. If you capture personal data during testing (a database dump, logs with real users), you are now handling regulated data.
- **Security principle (art. 4 g).** Those who process personal data must apply the technical, human and administrative measures needed to protect records against adulteration, loss, unauthorized or fraudulent access or use. Weak security is not only bad practice; it can be a breach of this duty.
- **Duty to report (art. 17 k).** Data controllers must inform the SIC when security codes are violated and there are risks in managing the owners' information. Breach handling is a legal obligation, not only a technical one.
- **Penalties (art. 23).** The SIC can impose fines of up to **2,000 SMMLV** per violation, and the fines can be repeated while the non-compliance continues. These sanctions apply to private parties.

Sensitive data (health, biometrics, political views and similar) and children's data have stronger protection. A breach that exposes personal data can trigger both Ley 1273 (the crime) and Ley 1581 (regulatory sanctions and the duty to notify).

### Where to report

- **Report a crime:** the Policía Nacional's cybercrime unit (Centro Cibernético Policial) receives citizen reports; serious cases go to the Fiscalía General de la Nación.
- **Report a data incident or complaint:** the SIC, as the data protection authority.
- **National incident coordination:** ColCERT, under the Ministry of Information and Communications Technologies (MinTIC), coordinates response to cyber incidents at the national level.

Confirm the current reporting channels on the official sites, since government portals change.

## Practicing legally

| Allowed without extra permission | Never without explicit written authorization |
|---|---|
| Your own home lab and VMs | Any website, app or API you do not own |
| Juice Shop, DVWA and other apps you host yourself | Your university's systems, including the Wi-Fi and the portal |
| TryHackMe, Hack The Box, picoCTF, OverTheWire and similar platforms | A friend's or employer's systems "to help" |
| CTF competitions you entered | Any government, bank or company system |
| Bug bounty targets, strictly within the published scope | A device or network you connected to but do not control |

Testing a classmate's project, scanning the campus network, or "checking" a company's site are all unauthorized access, even with good intentions.

## Responsible disclosure and bug bounty

If you find a vulnerability in a system you were not authorized to test, you are in a difficult legal position: finding it may already have required unauthorized access. The safe path is to practice only where you are authorized, so you never get there.

When you are authorized (your own systems, or a program that invites testing), responsible disclosure is the professional standard:

1. **Confirm you are in scope.** Read the program policy or the organization's `security.txt` file before testing. [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116) defines `security.txt`, a file at `/.well-known/security.txt` where organizations publish how to report vulnerabilities.
2. **Report privately first.** Send a clear report to the vendor or program: affected asset, impact, reproducible steps, evidence, and a suggested fix. Use the [report-writing guidance](english/writing-reports.md).
3. **Do no harm.** Do not access more data than needed to prove the issue, do not run denial-of-service, do not pivot to other systems, and delete any data you had to retrieve.
4. **Give time to fix.** Coordinate a disclosure timeline. Public disclosure happens only with agreement, usually after a patch.
5. **Stay inside the rules.** A program's safe harbor protects you only while you follow its policy. Step outside the scope and that protection is gone.

The [CERT Guide to Coordinated Vulnerability Disclosure](https://vuls.cert.org/confluence/display/CVD) is the standard reference for how this process works. How bug bounty programs operate in practice is covered in [Phase 4](roadmap/phase-4-professional/README.md#bug-bounty).

## A short ethical code

- Get authorization in writing, and stay inside its scope.
- Protect the data and systems you touch as if they were your own.
- Report what you find honestly, including your mistakes.
- Do not use your skills to harm, intimidate or spy on anyone.
- If an action would embarrass you if it were public, do not do it.
- When unsure whether something is legal or ethical, stop and ask first.
