# Module 1.4: Web security and the OWASP Top 10 (weeks 8-11)

The web is the largest attack surface in the world, and web skills transfer to almost every security role. This module works through the OWASP Top 10:2025 with hands-on labs for each class.

**Main resources:** [OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/), [PortSwigger Web Security Academy](https://portswigger.net/web-security) (free, the backbone of this module), [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) in your lab, [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/).

**Note on currency:** the 2025 list added A03 Software Supply Chain Failures and A10 Mishandling of Exceptional Conditions, and folded SSRF into A01. Many courses still teach the 2021 list; use the 2025 one.

## Week 8: How the web works for attackers, and injection

**Goal:** set up Burp Suite, understand the HTTP request/response as an attacker, and exploit injection.

**R. Read and study (75 min)**
- PortSwigger: "Getting started", the Burp Suite basics, and the [SQL injection](https://portswigger.net/web-security/sql-injection) topic.
- Notes: how a proxy intercepts and modifies requests; parameterized queries vs concatenation; types of SQLi (in-band, blind, out-of-band); OS command injection; the general injection defense (treat input as data, not code).
- Flashcards: what Burp Repeater and Intruder do, union-based vs blind SQLi, the fix for SQLi, OWASP A05 Injection.
- Read the A05 Injection page of the 2025 Top 10.

**P. Guided practice (90 min)**
- Set up Burp Community with your browser. Complete the SQL injection apprentice labs and start the practitioner ones.
- Reproduce the authentication-bypass SQLi from the [example writeup](../../writeups/2026-example-juice-shop-login-sqli.md) against Juice Shop in your lab.

**D. Deep practice (3 h)**
- Work the OS command injection and (time permitting) a practitioner SQLi lab end to end. For each, write a full finding using the [writeup template](../../writeups/TEMPLATE.md): description, impact, reproduction, root cause, fix. Build the habit now.

**E. English (60 min)**
- Read the OWASP [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). Write the "remediation" paragraph for your SQLi finding in precise English.

**Check yourself**
1. What does intercepting a request in Burp let you do that a browser does not?
2. How does a parameterized query stop SQL injection?
3. What is blind SQL injection, and how do you detect it without visible output?
4. Why is input validation alone an incomplete defense against injection?
5. Which OWASP 2025 category covers injection, and what moved into or out of it?

**Deliverable:** two complete injection findings (SQLi and command injection) using the template.

## Week 9: Broken access control, XSS and SSRF

**Goal:** exploit the two highest-impact web classes: access control (now including SSRF) and cross-site scripting.

**R. Read and study (75 min)**
- PortSwigger: [Access control](https://portswigger.net/web-security/access-control), [SSRF](https://portswigger.net/web-security/ssrf), and [Cross-site scripting](https://portswigger.net/web-security/cross-site-scripting).
- Read the A01 Broken Access Control page of the 2025 Top 10 (note SSRF is now here).
- Notes: IDOR and privilege escalation; horizontal vs vertical access control; SSRF and why cloud metadata endpoints make it severe; reflected vs stored vs DOM XSS; the XSS defenses (output encoding, CSP).
- Flashcards: IDOR, horizontal vs vertical privilege escalation, SSRF impact in cloud, the three XSS types, what CSP does.

**P. Guided practice (90 min)**
- PortSwigger: access control apprentice labs, one SSRF apprentice lab, and reflected and stored XSS apprentice labs.

**D. Deep practice (3 h)**
- Pick one access-control lab and one XSS lab and write full findings. For the XSS, include a proof-of-concept payload and explain the exact fix (which output context needs which encoding, and how CSP would have helped).
- In Juice Shop, find and document one access-control flaw yourself, without a walkthrough.

**E. English (60 min)**
- Write the impact sections for your access-control and XSS findings. Practice stating impact in business terms ("an attacker can read any user's private messages").

**Check yourself**
1. What is the difference between horizontal and vertical privilege escalation?
2. Why is SSRF especially dangerous in a cloud environment?
3. Explain the difference between reflected, stored and DOM-based XSS.
4. What is the primary defense against XSS, and what does CSP add?
5. Why is broken access control consistently the number one web risk?

**Deliverable:** three findings (access control, SSRF or XSS lab, and a self-found Juice Shop access-control flaw).

## Week 10: The rest of the Top 10

**Goal:** cover the remaining categories so you recognize all ten in the wild.

**R. Read and study (75 min)**
- Read the 2025 Top 10 pages for A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions.
- Notes: one concrete example and the primary fix for each category. Connect A04 to Module 1.2 and A07 to Module 1.3.
- Flashcards: one card per category, "example -> fix".

**P. Guided practice (90 min)**
- PortSwigger: one lab each from information disclosure (A02), insecure deserialization intro (A08) and business logic (A06).
- Run [`pip-audit`](https://pypi.org/project/pip-audit/) on one of your Python projects and explain each dependency finding (A03).

**D. Deep practice (3 h)**
- Build a single reference table in your notes: all ten 2025 categories, each with a one-line definition, a real-world example, the primary fix, and the lab or exercise where you saw it. This becomes your revision sheet and interview prep.
- In Juice Shop, find one verbose-error or fail-open behavior (A10) and write up the root cause.

**E. English (60 min)**
- Read the A03 Software Supply Chain Failures page. Summarize in English why this was added in 2025 and give one real incident it reflects.

**Check yourself**
1. Name all ten 2025 categories from memory.
2. Give a concrete example and the fix for A02, A03 and A10.
3. Why were A03 and A10 added in 2025?
4. How does A04 connect to what you learned about crypto?
5. What is the difference between insecure design (A06) and misconfiguration (A02)?

**Deliverable:** the complete OWASP Top 10:2025 reference table and the A10 finding.

## Week 11: APIs and a consolidation project

**Goal:** apply web skills to APIs and pull the module together into one portfolio piece.

**R. Read and study (75 min)**
- [OWASP API Security Top 10](https://owasp.org/API-Security/) (2023 edition): read the list and note how it differs from the web Top 10 (BOLA, broken authentication, excessive data exposure).
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) introduction: how professionals structure a web test.
- Notes: why APIs shift risk toward authorization (BOLA/IDOR at scale); how to test an API with Burp and the WSTG methodology.
- Flashcards: BOLA, mass assignment, the difference between the web and API Top 10 focus.

**P. Guided practice (90 min)**
- PortSwigger: the API testing labs (or the Juice Shop REST API). Enumerate endpoints and test one for broken object-level authorization.

**D. Deep practice (3 h)**
- Consolidation project: perform a structured mini web assessment of Juice Shop following the WSTG phases (information gathering, authentication, authorization, input validation), find at least five issues across different OWASP categories, and write a single professional report (not separate findings) with an executive summary, methodology, findings table and detailed findings. This is a portfolio centerpiece and rehearsal for Phase 4.

**E. English (60 min)**
- Write the executive summary and methodology section of the report in English, following [writing-reports.md](../../english/writing-reports.md). Have the self-review checklist open.

**Check yourself**
1. What is BOLA, and why is it the top API risk?
2. How does testing an API differ from testing a web page?
3. What are the phases of a structured web test per the WSTG?
4. Why does one consolidated report beat ten separate findings for a client?
5. Which five Juice Shop issues did you find, and which categories do they map to?

**Deliverable:** a single, professional mini-assessment report of Juice Shop, published in your `writeups/` or notes repo.

**Stretch:** read about the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) and [MITRE ATLAS](https://atlas.mitre.org/) if AI security interests you.
