# Phase 3: Specialization

**Duration:** 20 weeks: 12 weeks sampling six tracks (2 weeks each), then 8 weeks going deeper in the one you choose.
**When:** Semesters 5 and 6, with one break used for the deep dive.
**Prerequisites:** Phase 2 complete.

Nobody is hired as "cybersecurity". People are hired as SOC analysts, penetration testers, application security engineers, cloud security engineers, GRC analysts. This phase gives you enough direct experience with each track to choose based on what you enjoy doing for hours, not on what sounds impressive.

## Objectives

1. Spend two focused weeks on each of six tracks and produce one small artifact per track.
2. Understand what each role does day to day, what it pays attention to, and how people actually get hired into it.
3. Choose a **primary** track and a **secondary** track using the decision matrix below.
4. Complete an 8-week deep dive in the primary track that ends with a portfolio project.

## The six tracks at a glance

| Track | Typical roles | What the work looks like | Most common way in |
|---|---|---|---|
| Offensive | Penetration tester, red team operator | Testing systems against an agreed scope, then writing reports | Junior pentester at a consultancy, after a strong portfolio and a practical certification |
| Defensive | SOC analyst, detection engineer, incident responder, DFIR analyst | Triage alerts, investigate, contain, tune detections | SOC analyst level 1, one of the most common entry jobs in the field |
| Web security | Application security engineer, web pentester, bug bounty hunter | Reviewing designs and code, testing web apps and APIs, working with developers | From software development, or from web pentesting |
| Malware analysis | Malware analyst, reverse engineer, threat intelligence analyst | Taking samples apart, extracting indicators, writing detection rules and reports | From SOC or DFIR work, plus reverse engineering skills built on the side |
| Cloud security | Cloud security engineer, cloud security architect | IAM design, guardrails, posture findings, securing pipelines and infrastructure as code | From cloud, DevOps or platform engineering |
| GRC | GRC analyst, IT auditor, risk analyst, compliance specialist | Policies, risk assessments, control testing, audits, vendor risk | Audit and consulting firms, internal control teams |

## Track details

Each track below has: what the job is like day to day, the core skills, how people get in, a two-week sampler using free resources, and the artifact to produce. Certifications for each track are in [Phase 4](../phase-4-professional/README.md#certifications-in-order).

### 1. Offensive security (pentesting, red team)

**Day to day.** A penetration tester works on engagements of one to three weeks. A typical week starts with a scoping or kickoff call, then testing a web application, internal network or cloud environment within written rules of engagement. Testing is methodical and repetitive more often than dramatic: enumerate, verify, document with evidence, move on. A large share of the time goes into notes, screenshots and the final report, followed by a readout call and later a retest of the fixes. Red team operators run longer, objective-based campaigns that emulate a specific adversary, care about stealth, and coordinate with defenders in purple team exercises. Red team roles usually go to people with several years of pentesting.

**Core skills.** Networking, Linux and Windows internals, Active Directory, web application testing, scripting, and clear technical writing.

**How people get in.** Junior roles at security consultancies and internal security teams, typically after a visible portfolio (writeups, a home lab, CTF results) and one practical certification. Moving from a SOC or system administration role into pentesting is also common.

**Two-week sampler.**
- Hack The Box Academy Penetration Tester path: the free Tier 0 modules, then the first Tier I modules if you have the Student plan.
- Two retired machines with Active Directory, then watch the [IppSec](https://ippsec.rocks/) walkthrough after your attempt.
- Read two public pentest reports from [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports).

**Artifact.** A short mock pentest report (3-5 pages) of a target in your home lab, using [english/writing-reports.md](../../english/writing-reports.md).

### 2. Defensive security (SOC, blue team, DFIR)

**Day to day.** A level 1 SOC analyst works an alert queue in a SIEM and EDR console: decides whether each alert is a true or false positive, gathers context, escalates real incidents and documents everything in tickets. Many SOCs, especially managed security providers, run 24/7 with shifts. Level 2 and 3 analysts investigate escalations, hunt for threats that did not trigger alerts, and write and tune detections. DFIR analysts are called in when something serious happens: they acquire evidence, build timelines from disk, memory and logs, determine scope and root cause, and report to technical teams, management and sometimes lawyers.

**Core skills.** Log analysis, Windows event logs, networking, SIEM queries, knowledge of attacker techniques (ATT&CK), forensics tools, calm communication under pressure.

**How people get in.** SOC analyst level 1 roles at banks, telecoms, large companies and managed security providers. Hands-on blue team labs, a home detection lab and a defensive certification help an application stand out.

**Two-week sampler.**
- Build the Wazuh stage of the [home lab](../../homelab/README.md) and generate your own alerts.
- Three investigations on [CyberDefenders](https://cyberdefenders.org/blue-team-labs/) or [Blue Team Labs Online](https://blueteamlabs.online/).
- Read the [Sigma](https://github.com/SigmaHQ/sigma) rule format and write two rules for activity you generated in the lab.

**Artifact.** An incident report for an attack you ran and then investigated in your own lab, with a timeline and ATT&CK mapping.

### 3. Web security (AppSec, web testing, bug bounty)

**Day to day.** An application security engineer works with development teams: reviews designs and threat models, triages findings from code scanners and dependency checks, reviews risky pull requests, tests features before release, and teaches developers to avoid recurring bugs. Web pentesters do focused testing engagements on applications and APIs. Bug bounty hunters work independently on public and private programs, with income that depends on findings and can vary a lot from month to month.

**Core skills.** HTTP in depth, JavaScript and at least one backend language, authentication and authorization models, API design, code review, and communicating with developers without antagonizing them.

**How people get in.** Software developers who move into security are the most common AppSec profile. Web pentesting roles at consultancies are the other route. Bug bounty results are strong evidence of skill for both.

**Two-week sampler.**
- Web Security Academy practitioner labs in two topics you have not done.
- Read the Juice Shop source code for one challenge you solved and locate the vulnerable line.
- Skim the [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) and test one Juice Shop feature against its authentication requirements.

**Artifact.** A secure code review of one module of an open-source app (in your lab) with findings and suggested patches.

### 4. Malware analysis and reverse engineering

**Day to day.** A malware analyst receives samples from incidents, threat feeds or customers. Work includes quick triage (what is it, is it known, what does it do), static analysis of the file, dynamic analysis in an isolated sandbox, deeper reverse engineering in a disassembler or decompiler, extracting configuration and indicators, writing YARA rules and detection guidance, and reporting findings to SOC and threat intelligence teams. These roles are concentrated in security vendors, large SOCs and threat intelligence teams, and there are fewer junior openings than in the SOC.

**Core skills.** x86-64 assembly, Windows internals and APIs, C, a disassembler such as Ghidra, debugging, patience, and precise writing.

**How people get in.** Usually from SOC, DFIR or threat intelligence roles, after building reverse engineering skills through CTF reversing challenges, courses and personal analysis blogs.

**Two-week sampler.**
- [OpenSecurityTraining2](https://ost2.fyi/) assembly and reverse engineering classes (free).
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) on the reverse engineering challenges you solved in Phase 2.
- Build the malware analysis enclave in the [home lab](../../homelab/README.md#stage-4-malware-analysis-enclave) with [REMnux](https://docs.remnux.org/) and [FLARE-VM](https://github.com/mandiant/flare-vm). Analyze only well-documented samples, only inside that isolated enclave.

**Artifact.** A short analysis report of one well-documented sample: hashes, behavior, persistence, indicators and one YARA rule.

### 5. Cloud security

**Day to day.** A cloud security engineer reviews and designs IAM policies and roles, sets organization-wide guardrails, triages findings from posture management tools, secures CI/CD pipelines and infrastructure-as-code templates, manages secrets, and helps investigate incidents using cloud audit logs. Much of the work is preventing misconfiguration at scale, so automation and code are central.

**Core skills.** One major cloud provider in depth (AWS or Azure is a reasonable first choice), IAM, networking in the cloud, Linux, Python, Terraform or another IaC tool, logging.

**How people get in.** Most cloud security engineers were cloud, DevOps or platform engineers first. Security engineers who learn cloud deeply are the other route.

**Two-week sampler.**
- [flaws.cloud](http://flaws.cloud/) and [flaws2.cloud](http://flaws2.cloud/): free, hosted AWS challenges, no account needed.
- [Wiz CTF challenges](https://www.wiz.io/ctf), starting with The Big IAM Challenge.
- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) in your own AWS account. New AWS accounts on the free plan get $100 in credits plus up to $100 more for completing onboarding tasks, valid for 6 months ([announcement](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/)). Set an AWS Budget alert before you deploy anything, and destroy the scenario when you finish.
- [Azure for Students](https://azure.microsoft.com/en-us/free/students/): $100 credit for 12 months with a university email and no credit card.

**Artifact.** A short review of a Terraform or IAM policy you wrote, with the misconfigurations you found and fixed.

### 6. Governance, risk and compliance (GRC)

**Day to day.** GRC analysts write and maintain security policies and standards, run risk assessments, map controls to frameworks (ISO/IEC 27001, NIST CSF, CIS Controls, PCI DSS), collect and review evidence for audits, assess third-party vendors, track remediation, and report risk to management. In Colombia this also includes compliance with Ley 1581 de 2012 on personal data (see [legal-and-ethics.md](../../legal-and-ethics.md)) and sector rules from regulators such as the Superintendencia Financiera for banks. The work is less hands-on technically, but people who understand the technology behind the controls are more effective and more valued.

**Core skills.** Frameworks and standards, risk methods, writing, interviewing, presenting to non-technical audiences, enough technical depth to know when a control is real and when it only exists on paper.

**How people get in.** Audit and consulting firms, internal control and compliance teams, and internal transfers from IT. Strong writing in both Spanish and English is a clear advantage for multinational employers.

**Two-week sampler.**
- Revisit the CSF 2.0 profile from Phase 1 and extend it with [CIS Controls v8.1](https://www.cisecurity.org/controls/v8-1) Implementation Group 1 safeguards.
- Read the structure of [ISO/IEC 27001](https://www.iso.org/standard/27001) (the standard is paid; the overview page is free) and list which clauses your fictional company would struggle with.
- Write an acceptable use policy and a password policy aligned with NIST SP 800-63B-4.

**Artifact.** A risk register with ten risks, owners, ratings and treatment decisions for the fictional company.

## Choosing your track

Score each track from 1 to 5 after its sampler. Be honest about the first column: enjoyment predicts persistence better than anything else.

| Track | Enjoyed the work | Made progress | Job market I can reach | Fits my degree strengths | Total |
|---|---|---|---|---|---|
| Offensive | | | | | |
| Defensive | | | | | |
| Web security | | | | | |
| Malware analysis | | | | | |
| Cloud security | | | | | |
| GRC | | | | | |

Pick the highest total as primary and a complementary track as secondary. Combinations that work well together:

- Offensive and web security
- Defensive and cloud security
- Defensive and malware analysis
- Web security and cloud security
- GRC and cloud security

## Deep dive (8 weeks)

Spend 8 weeks on the primary track:

1. Weeks 1-2: finish the core learning path for the track on one platform (for example the HTB Academy Penetration Tester or SOC Analyst path).
2. Weeks 3-6: build the portfolio project for the track from [Phase 4](../phase-4-professional/README.md#portfolio-projects).
3. Weeks 7-8: write it up, publish it in this repo, and present it to classmates or at a local meetup.

## You've mastered this phase when...

- [ ] You completed all six samplers and have one artifact for each.
- [ ] You can describe a normal working week in each track, including the boring parts.
- [ ] You filled in the decision matrix and chose a primary and a secondary track with a written reason.
- [ ] You finished the 8-week deep dive and published its project in this repo.
- [ ] You can explain to an interviewer why you chose your track and what you have done in it.

Next: [Phase 4, professional level](../phase-4-professional/README.md).
