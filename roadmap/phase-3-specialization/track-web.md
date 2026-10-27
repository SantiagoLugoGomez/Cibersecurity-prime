# Track deep dive: Web and application security (12 weeks)

For the student who chose web/application security (AppSec engineer, web pentester, bug bounty). Web skills have the widest reach and the clearest path to bug bounty income. This curriculum takes you from the Phase 2 web baseline to expert-level web and API testing and secure code review.

**Prerequisites:** Phase 2 complete, especially the web labs module.
**Main platform:** [PortSwigger Web Security Academy](https://portswigger.net/web-security) (free, all the way to expert), plus [Hacker101](https://www.hacker101.com/), [PortSwigger research](https://portswigger.net/research), and bug bounty platforms.
**Certification target:** Burp Suite Certified Practitioner (BSCP) or HTB CWES (see [Phase 4](../phase-4-professional/README.md#stage-3-track-certification-one-in-your-primary-track)).

## Weeks 1-3: Expert-level web vulnerabilities

**Read/study:** the PortSwigger expert-level topics (advanced SQLi, server-side template injection, web cache poisoning, HTTP request smuggling, prototype pollution, advanced XSS); read the matching [PortSwigger research](https://portswigger.net/research) posts.
**Practice:** all practitioner and expert labs in one hard topic per week (request smuggling, SSTI, then cache poisoning or prototype pollution).
**Deep practice:** write a deep-dive explainer for each topic with a working lab exploit and the exact fix. These become reference material and portfolio content.
**English:** each explainer in clear technical English.
**Deliverable:** three expert-topic explainers with working exploits.

## Weeks 4-5: APIs and modern app architectures

**Read/study:** [OWASP API Security Top 10](https://owasp.org/API-Security/); testing GraphQL and REST; JWT attacks; the [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) methodology.
**Practice:** PortSwigger API and JWT labs; test the Juice Shop and a GraphQL target in your lab.
**Deep practice:** full API assessment of a lab target following the WSTG, focusing on broken object-level authorization (BOLA) and mass assignment; write findings.
**English:** write an API assessment report section.
**Deliverable:** one API assessment with findings.

## Weeks 6-8: Secure code review

**Read/study:** how to read code for vulnerabilities (data flow from source to sink); the [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/); common sink patterns per language.
**Practice:** review intentionally vulnerable open-source apps in your lab; use [Semgrep](https://semgrep.dev/) (open source) to find candidates, then verify each by hand.
**Deep practice:** full secure code review of one real open-source project (small, in your lab): trace user input to dangerous sinks, find real issues, and propose patches with diffs. This is the core AppSec-engineer skill.
**English:** write the code review as a report with findings and suggested patches.
**Deliverable:** one secure code review with patches, portfolio-grade.

## Weeks 9-11: Bug bounty practice

**Read/study:** Real-World Bug Hunting (Yaworski) and Bug Bounty Bootcamp (Li), both No Starch Press (reference); read disclosed reports on [HackerOne](https://www.hackerone.com/) and [Intigriti](https://www.intigriti.com/) to learn what accepted findings look like.
**Practice:** finish the [Hacker101 CTF](https://www.hacker101.com/); then pick one real program with a wide scope and work it for the three weeks (read the whole policy first; stay in scope).
**Deep practice:** reconnaissance and testing on your chosen program. Expect duplicates and "not applicable" at first; treat it as training. Write every candidate finding as a full report before submitting.
**English:** your submitted reports are the English deliverable; clarity directly affects payout.
**Deliverable:** at least one submitted report to a real program (accepted or not), written to professional standard.

## Week 12: Capstone and portfolio

**Deep practice:** produce one polished web application security assessment of a deliberately vulnerable modern app, combining everything: methodology, a range of findings across OWASP categories, a secure-code-review appendix for one finding, and clear remediation. This is your centerpiece portfolio piece and BSCP preparation.
**English:** full report with the self-review checklist applied.
**Deliverable:** a capstone web assessment report.

## You are ready for the certification when...

- [ ] You can solve PortSwigger practitioner labs quickly and make progress on expert ones.
- [ ] You can read code and trace user input to a vulnerable sink.
- [ ] You can test an API for BOLA and mass assignment and explain the fix.
- [ ] You have submitted at least one real bug bounty report following the program's rules.
- [ ] You have a code review, an API assessment and a capstone web report in your portfolio.

**Note on BSCP:** the exam requires an active Burp Suite Professional license (paid) in addition to the $99 exam fee. Prepare by completing every practitioner lab first.

**Free-only path:** the entire Web Security Academy, Hacker101, Juice Shop, Semgrep and public disclosed reports make this the most free-friendly track; only the BSCP exam and Burp Pro cost money.
