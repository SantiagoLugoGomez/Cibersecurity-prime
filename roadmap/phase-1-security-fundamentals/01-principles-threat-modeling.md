# Module 1.1: Principles and threat modeling (weeks 1-2)

Before tools, you need a way of thinking. These two weeks give you the vocabulary and the mental models that every later topic hangs on.

**Main resources:** [Professor Messer Security+ SY0-701](https://www.professormesser.com/sy0-701-certification-course/) (free), [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling), [Ross Anderson, Security Engineering, 3rd ed.](https://www.cl.cam.ac.uk/~rja14/book.html) (free online).

## Week 1: Core principles and the vocabulary

**Goal:** use the CIA triad and the core security principles precisely, and stop confusing vulnerability, threat, risk and exploit.

**R. Read and study (75 min)**
- Professor Messer SY0-701: the "General Security Concepts" section.
- Security Engineering, chapter 1 (What Is Security Engineering?).
- Notes: CIA triad plus authenticity, non-repudiation and accountability; the principles of least privilege, defense in depth, separation of duties, fail-safe defaults, complete mediation, and keep-it-simple; the precise difference between asset, threat, vulnerability, risk, exploit and control.
- Flashcards: one per term above, each with a one-line definition and an example. Use the [glossary](../../english/glossary.md) as the source of truth.

**P. Guided practice (90 min)**
- For five recent breaches you find in the news, classify each: which CIA property was violated, which principle failed, and which single control would most likely have prevented it. Write one row per breach in a table.

**D. Deep practice (3 h)**
- Take one system you know (your university portal, a bank app, your home lab) and write an asset inventory: what data and functions exist, who should access each, and what the impact would be if confidentiality, integrity or availability were lost. Rate each impact low/medium/high with a one-line justification.
- This is the input to threat modeling next week.

**E. English (60 min)**
- Read the definitions section of [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) or the glossary. Write precise one-sentence definitions, in English, of risk, threat and vulnerability that a non-technical manager would understand.

**Check yourself**
1. Give a real example where availability was attacked but confidentiality was not.
2. State the difference between a vulnerability, a threat and a risk in one sentence each.
3. What is the difference between least privilege and need to know?
4. What does "defense in depth" mean, and why does one control failing not end the game?
5. Why is "fail-safe defaults" a security principle?

**Deliverable:** the five-breach classification table and the asset inventory with impact ratings.

## Week 2: Threat modeling with STRIDE

**Goal:** systematically find what could go wrong with a system before building or attacking it.

**R. Read and study (75 min)**
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling) and the [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html).
- Notes: the four questions (what are we working on, what can go wrong, what will we do, did we do a good job); STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) and which CIA property each attacks; data-flow diagrams and trust boundaries.
- Flashcards: each STRIDE category with an example and its matching defense.

**P. Guided practice (90 min)**
- Draw a data-flow diagram (Mermaid is fine) of a simple web app: browser, web server, database, and an external login provider. Mark the trust boundaries.
- For each element and data flow, list at least one STRIDE threat.

**D. Deep practice (3 h)**
- Produce a full STRIDE threat model of OWASP Juice Shop (or your own small app): data-flow diagram, a threat table (element, STRIDE category, threat, likelihood, impact, mitigation), and the three threats you would fix first with reasons.
- Keep this; you will test several of these threats in Phase 2.

**E. English (60 min)**
- Write the executive summary of your threat model in English: three paragraphs a manager could read, naming the top risks and recommended actions, no jargon.

**Check yourself**
1. What are the four questions of threat modeling?
2. Which CIA property does each STRIDE letter threaten?
3. What is a trust boundary, and why do the most interesting threats cross one?
4. Why model threats before writing code or testing, not after?
5. Given a login form, name one spoofing and one elevation-of-privilege threat.

**Deliverable:** the Juice Shop STRIDE threat model with diagram, threat table and prioritized fixes, committed to your notes repo.

**Stretch:** read Security Engineering chapter 3 (Psychology and Usability) on why people are the weakest link.
