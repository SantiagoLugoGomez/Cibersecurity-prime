# Track deep dive: Offensive security (12 weeks)

For the student who chose offensive security as their primary track. This is a 12-week curriculum that takes you from the Phase 2 baseline to being able to compromise realistic multi-host environments and write a professional report, which is the bar for a junior penetration tester.

**Prerequisites:** Phase 2 complete, especially the machines and AD module.
**Main platform:** [HTB Academy Penetration Tester path](https://academy.hackthebox.com/preview/certifications) (Student plan, $10/month with an academic email) plus [Hack The Box](https://www.hackthebox.com/) machines. Free alternatives noted per week.
**Certification target:** HTB CPTS, TCM PNPT or OSCP+ (see [Phase 4](../phase-4-professional/README.md#stage-3-track-certification-one-in-your-primary-track)).

## Weeks 1-2: Professional methodology and reconnaissance

**Read/study:** the penetration testing process and information-gathering modules of the HTB Academy path; the [PTES](http://www.pentest-standard.org/) phases; a public pentest report from [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports) each week.
**Practice:** passive and active recon against lab targets and authorized scope only; master `nmap` scripting, `ffuf` for content discovery, and subdomain/asset enumeration.
**Deep practice:** full recon of a retired HTB box, producing a structured enumeration document before any exploitation.
**English:** study the structure of two professional reports; start a personal "report phrasing" bank.
**Deliverable:** a reusable recon checklist and one structured enumeration document.

## Weeks 3-5: Web and service exploitation at depth

**Read/study:** the web attack modules (SQLi, file inclusion, upload, command injection, SSRF, deserialization) and common service attacks (SMB, databases, mail) in the HTB path; [HackTricks](https://book.hacktricks.xyz/) per service.
**Practice:** one retired HTB machine or TryHackMe room per week that centers on web-to-shell; PortSwigger expert labs in your weakest topic.
**Deep practice:** chain a web vulnerability to a foothold on three different machines; write a full finding for each.
**English:** write each finding to report standard.
**Deliverable:** three web-to-foothold writeups.

## Weeks 6-7: Post-exploitation and privilege escalation

**Read/study:** the Linux and Windows privilege-escalation modules; [GTFOBins](https://gtfobins.github.io/) and [LOLBAS](https://lolbas-project.github.io/); pivoting and tunneling.
**Practice:** `linpeas`/`winpeas` on varied machines; practice manual verification of what the scripts flag (never trust a tool blindly in a report).
**Deep practice:** two machines per week where the privesc is the hard part; document each vector and its fix.
**English:** write the "recommendations" section for each, in prioritized order.
**Deliverable:** a privilege-escalation techniques catalog with fixes.

## Weeks 8-10: Active Directory and multi-host environments

**Read/study:** the full AD attack chain in the HTB path; [BloodHound CE](https://github.com/SpecterOps/BloodHound); [[Impacket](https://github.com/fortra/impacket)] tooling.
**Practice:** [GOAD](https://github.com/Orange-Cyberdefense/GOAD) in your lab, or the HTB AD labs; one multi-host chain per week.
**Deep practice:** over the three weeks, compromise a full lab domain from external foothold to Domain Admin, documenting the whole path with evidence and a defender's detection view.
**English:** write the engagement as a narrative report with an attack-path diagram.
**Deliverable:** one full internal-network engagement report against your lab.

## Weeks 11-12: Capstone engagement and report

**Deep practice:** treat a small set of retired machines or a lab environment as a client engagement with a defined scope and rules of engagement. Run the full process (recon, exploitation, post-exploitation, lateral movement), keep professional notes throughout, and deliver one complete penetration test report: executive summary, scope, methodology, findings ranked by severity with CVSS, evidence, remediation, and an appendix.
**English:** the report is the deliverable; apply the full [writing-reports.md](../../english/writing-reports.md) checklist and have a peer or tool review it.
**Deliverable:** a portfolio-grade penetration test report (redacted as needed), published in your repo.

## You are ready for the certification when...

- [ ] You can go from an unknown external IP to Domain Admin in a lab environment unaided.
- [ ] Your reports are clear enough that a developer could fix every finding from them alone.
- [ ] You verify and explain every tool finding rather than pasting output.
- [ ] You can scope an engagement and stay inside rules of engagement.
- [ ] You have at least five machine writeups and one full engagement report in your portfolio.

**Free-only path:** TryHackMe free rooms + retired HTB machines with [IppSec](https://ippsec.rocks/) + GOAD in your lab cover most of this without the Academy subscription; the Academy path mainly adds structure and the CPTS voucher.
