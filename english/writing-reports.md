# Writing professional reports and writeups in English

Writing is the deliverable in much of security work. A penetration test is sold as a report; a bug bounty finding is paid on the quality of its write-up; an incident is closed with a post-incident report. Clear English writing is a direct career advantage, and for a Spanish speaker it is a learnable, high-return skill.

## What a professional report does

A good finding answers four questions in order, fast:

1. **What is wrong?** A specific, titled finding.
2. **How bad is it?** Impact and severity, in business terms where possible.
3. **How do I reproduce it?** Exact, numbered steps with evidence.
4. **How do I fix it?** Concrete remediation, not "improve security."

The reader is often busy and non-technical at the top (a manager who reads only the summary) and technical lower down (an engineer who reproduces the steps). Write for both: an executive summary in plain language, then technical detail.

## Structure of a finding

```
Title:            Short, specific. "SQL injection in the login endpoint",
                  not "Security issue".
Severity:         Critical / High / Medium / Low / Informational, with a
                  CVSS score if the engagement uses one.
Affected asset:   The exact URL, host, parameter or component.
Description:      What the vulnerability is and why it exists.
Impact:           What an attacker can do, and what it means for the business.
Steps to reproduce: Numbered, exact, with requests, payloads and evidence.
Remediation:      The specific fix, with a reference.
References:       OWASP, CWE, vendor docs.
```

The [writeup template](../writeups/TEMPLATE.md) and the [worked example](../writeups/2026-example-juice-shop-login-sqli.md) follow this shape.

## Register and style

- **Lead with the conclusion.** English technical writing is top-down: state the finding, then explain. Do not build up to it the way an essay might.
- **Short sentences.** One idea per sentence. If a sentence has three clauses, split it.
- **Prefer the active voice for instructions**, the passive for describing impact. "Validate the input" (instruction) but "Customer data could be disclosed" (impact).
- **Be specific and measurable.** "The server returned the full query in a 500 error" beats "the server behaved insecurely."
- **No drama, no filler.** Avoid "catastrophic", "hacker's paradise", "easily". State the fact and let severity speak.
- **Consistent terminology.** Pick one term per concept and keep it. Do not alternate between "flaw", "bug", "issue" and "vulnerability" at random.
- **Define an acronym on first use**, then use it: "cross-site scripting (XSS)".

## Mistakes Spanish speakers make most

These are the errors a reviewer sees again and again from strong Spanish-speaking writers. Fixing them moves your writing from "clearly non-native" to "native-level".

### Vocabulary and false friends

| Instead of | Write | Why |
|---|---|---|
| "encript", "encripted" | "encrypt", "encrypted" | "Encriptar" leads here; the English verb is *encrypt*. *Cipher*, not "cypher". |
| "the password is encrypted" (when hashed) | "the password is hashed" | Hashing is one-way; encryption is reversible. See the [glossary](glossary.md). |
| "actually" (meaning "currently") | "currently" / "at the moment" | "Actual" in Spanish means current; English "actually" means "in fact". |
| "eventually" (meaning "possibly") | "possibly" / "if needed" | "Eventual" in Spanish means possible; English "eventually" means "in the end". |
| "sensible data" | "sensitive data" | "Sensible" is a false friend; English *sensible* means reasonable. |
| "assist to the meeting" | "attend the meeting" | "Asistir a" is *attend*, not "assist". |
| "realize" (meaning "carry out") | "perform" / "carry out" / "conduct" | "Realizar" is to perform; English "realize" means to become aware. |
| "exploit a vulnerability" ✓ but "explode" ✗ | "exploit" | "Explotar" covers both; keep *exploit* for security. |
| "informatic" / "informatics" | "computing" / "IT" / "computer" | "Informática" has no everyday English equivalent; say "the IT systems", "computer security". |
| "comprise of" | "comprise" / "consist of" | *Comprise* takes no "of". |

### Grammar

- **Article use.** English needs "the" and "a" where Spanish often drops them, and omits them where Spanish keeps them. "Attacker can access the database" should be "An attacker can access the database." Abstract and plural nouns usually take no article: "Encryption protects data", not "The encryption protects the data".
- **Subject-verb agreement with "data".** In formal writing "data" is often plural, but in security writing treating it as a mass noun ("data is encrypted") is widely accepted. Pick one and be consistent.
- **False cognate verb patterns.** "allows to do" is wrong; write "allows an attacker to do" or "allows doing". English *allow* needs an object before the infinitive.
- **Gerund vs infinitive.** "We recommend to update" is wrong; write "We recommend updating" or "We recommend that you update".
- **Prepositions.** "vulnerable to", "depends on", "consists of", "results in", "protect against", "susceptible to". These are fixed; learn them as whole phrases.
- **Word order of adjectives.** English adjectives come before the noun: "a critical remote vulnerability", not "a vulnerability critical remote".
- **Overusing the present continuous.** "The function is returning the password" (ongoing) vs "The function returns the password" (general fact). Reports usually want the simple present for facts.

### Punctuation and formatting

- **No space before a colon or semicolon**, unlike French-influenced habits. One space after.
- **Capitalize** the first word of every bullet and sentence; it is easy to forget in a hurry.
- **Numbers and units.** "a 500 error", "port 443", "15 characters". Be consistent with digits vs words.
- **Do not translate Spanish quotation or dash conventions.** Use standard English quotation marks.

### Tone

- Spanish technical writing can be more elaborate and formal. English prefers plain and direct. A sentence like "It would be of the utmost importance to proceed with the remediation of the aforementioned vulnerability" should be "Fix this vulnerability."
- Avoid apologizing or hedging about your own work ("I think maybe this could possibly be a problem"). State the finding and your confidence level directly: "This is exploitable. I confirmed it with the proof of concept below."

## A self-review checklist

Before you submit any report or publish any writeup, read it once for each line:

- [ ] Does the title name the specific vulnerability?
- [ ] Can a busy manager understand the summary without technical knowledge?
- [ ] Can an engineer reproduce every finding from the steps alone?
- [ ] Is every finding's impact stated in terms of what an attacker gains?
- [ ] Is the remediation specific and actionable, with a reference?
- [ ] One idea per sentence; no sentence longer than about 25 words?
- [ ] No false friends (encript, actual, sensible, assist, realize)?
- [ ] "allow someone to do", "recommend doing", correct prepositions?
- [ ] Consistent terminology for each concept?
- [ ] No drama, no filler, no apology?
- [ ] Acronyms defined on first use?

## How to improve fastest

1. Study real reports. The [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports) collection has reports from top firms. Notice their structure and phrasing.
2. Read the official [OffSec exam report guidance](https://help.offsec.com/) and a template such as [SysReptor's OSCP template](https://docs.syslifters.com/) to see the expected format.
3. Keep a personal list of phrases from good reports ("an unauthenticated attacker can", "we recommend enforcing", "this finding is exploitable under the following conditions").
4. Write a real writeup for every lab you solve. Volume with review is what builds fluency.
5. Have a tool or a peer check grammar, but study each correction so you stop making it.
