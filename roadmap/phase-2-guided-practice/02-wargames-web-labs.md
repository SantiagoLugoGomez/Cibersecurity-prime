# Module 2.2: Wargames and web application labs (weeks 5-10)

Six weeks of structured, progressively harder practice: the OverTheWire wargames to cement Linux and web basics, then a deep pass through the PortSwigger practitioner labs and Juice Shop.

**Main resources:** [OverTheWire](https://overthewire.org/wargames/), [PortSwigger Web Security Academy](https://portswigger.net/web-security), [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), [HackTricks](https://book.hacktricks.wiki/) and [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) as references.

## Week 5: OverTheWire Bandit finish and Natas start

**Goal:** finish the Linux wargame and begin the web wargame.

**R. Read and study (75 min)**
- Skim [HackTricks](https://book.hacktricks.wiki/) Linux privilege-escalation checklist to see how professionals organize enumeration.
- Notes: the Bandit techniques you have met (cron, git, setuid, services), and what Natas will teach (server-side web logic).
- Flashcards: three privesc checks from HackTricks, what Natas levels are about.

**P. Guided practice (90 min)**
- OverTheWire Bandit: finish through level 25 if not already done.
- OverTheWire Natas: levels 0 to 6.

**D. Deep practice (3 h)**
- Natas levels 7 to 12, writing down the web flaw behind each (LFI, command injection, weak session, etc.) and which OWASP 2025 category it maps to.

**E. English (60 min)**
- Write a short writeup of the most interesting Natas level, naming the vulnerability class and the fix.

**Check yourself**
1. Which Bandit levels used a setuid binary or a cron job, and how?
2. What web flaw does each Natas level you solved demonstrate?
3. How does HackTricks structure a privesc check?
4. Map three Natas levels to OWASP categories.
5. What is local file inclusion, and how is it abused?

**Deliverable:** Bandit complete, Natas 0-12 with per-level vulnerability notes.

## Week 6: Natas finish and Leviathan

**Goal:** complete the web wargame and practice small binary/Linux puzzles.

**R. Read and study (75 min)**
- Notes: session handling and server-side validation flaws from the later Natas levels.
- Flashcards: command injection, SSRF, insecure deserialization reminders.

**P. Guided practice (90 min)**
- Natas: levels 13 to 20.
- Leviathan: levels 0 to 4.

**D. Deep practice (3 h)**
- Finish Natas (up to the level you can reach) and Leviathan. Write one consolidated note: the five web flaw classes Natas taught you and how each maps to a PortSwigger topic you will deepen next.

**E. English (60 min)**
- Rehearse out loud: explain command injection and how to prevent it, in two minutes.

**Check yourself**
1. What server-side mistakes made the later Natas levels exploitable?
2. How do you move from a found flaw to reading a file you should not?
3. Which Natas levels map to injection, and which to access control?
4. What did Leviathan add that Natas did not?
5. Which web topic do you most need to deepen?

**Deliverable:** Natas and Leviathan progress with the consolidated five-classes note.

## Weeks 7-8: PortSwigger practitioner labs

**Goal:** go beyond apprentice level in the highest-value web topics.

**R. Read and study (75 min each week)**
- PortSwigger: the practitioner-level material for SQL injection, access control, authentication, SSRF and XSS (split across the two weeks).
- Notes: the advanced techniques (blind and out-of-band SQLi, second-order flaws, filter bypasses).
- Flashcards: out-of-band SQLi, second-order injection, DOM XSS sources and sinks, SSRF filter bypass tricks.

**P. Guided practice (90 min each week)**
- Complete practitioner labs: aim for all practitioner labs in two topics in week 7 and two more in week 8.

**D. Deep practice (3 h each week)**
- Each week, take the hardest lab you solved and write a full professional finding with the [template](../../writeups/TEMPLATE.md). By the end you have four strong findings.
- Reference [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) for payloads, but understand every payload before using it.

**E. English (60 min each week)**
- Write the findings in English. Focus one week on the "impact" sections and one week on "remediation", using the [writing guide](../../english/writing-reports.md).

**Check yourself (end of week 8)**
1. How do you exploit SQLi when there is no visible output?
2. What is a second-order injection?
3. What are the source and sink in DOM-based XSS?
4. Name three ways to bypass an SSRF filter.
5. Which practitioner topic felt hardest, and why?

**Deliverable:** practitioner labs complete in four topics, and four professional findings.

## Weeks 9-10: Juice Shop challenge run

**Goal:** apply everything to a realistic modern app, under your own direction.

**R. Read and study (75 min each week)**
- Notes: plan which Juice Shop challenge categories to attack; review the [WSTG](https://owasp.org/www-project-web-security-testing-guide/) phases.
- Flashcards: refresh the OWASP categories you are weakest on.

**P. Guided practice (90 min each week)**
- Juice Shop: solve challenges across categories, 15 in week 9 and 15 in week 10, including at least five rated three stars or higher. Run it in your lab.

**D. Deep practice (3 h each week)**
- Week 9: focus on injection and XSS challenges; write findings for the two hardest.
- Week 10: focus on access control and business-logic challenges; write findings for the two hardest, and produce a short "Juice Shop assessment" summary tying your findings to OWASP 2025.

**E. English (60 min each week)**
- Keep writing findings in English. By now aim for a native-reviewer-only-fixes-content standard.

**Check yourself (end of week 10)**
1. Which Juice Shop challenge taught you the most, and why?
2. For a three-star challenge you solved, what made it hard?
3. How does Juice Shop's modern stack change where bugs live versus Natas?
4. Which OWASP category are you now strongest and weakest in?
5. Could a classmate reproduce your findings from your writeups alone?

**Deliverable:** 30 Juice Shop solves, at least eight findings total across the two weeks, and a short assessment summary.

**Stretch:** try [DVWA](https://github.com/digininja/DVWA) on "impossible" security level to read how each fix is implemented in code.
