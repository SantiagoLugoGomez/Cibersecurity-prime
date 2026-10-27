# Track deep dive: Defensive security (12 weeks)

For the student who chose defense (SOC, blue team, DFIR). SOC analyst is one of the most common entry points in the field, and this curriculum takes you from the Phase 2 baseline to being able to detect, investigate and respond like a level 1 to 2 analyst.

**Prerequisites:** Phase 2 complete, especially the blue team module.
**Main platform:** [HTB Academy SOC Analyst path](https://academy.hackthebox.com/preview/certifications) (Student plan) plus your lab's Wazuh/Splunk and [CyberDefenders](https://cyberdefenders.org/blue-team-labs/). Free alternatives noted.
**Certification target:** BTL1, HTB CDSA, Microsoft SC-200 or CompTIA CySA+ (see [Phase 4](../phase-4-professional/README.md#stage-3-track-certification-one-in-your-primary-track)).

## Weeks 1-2: The SOC, logging and the attacker's playbook

**Read/study:** the SOC fundamentals and security monitoring modules of the HTB path; [MITRE ATT&CK](https://attack.mitre.org/) in depth (tactics, techniques, the v19 Stealth/Defense Impairment split).
**Practice:** map every attack you ran in Phase 2 to ATT&CK; for each, list the log source that would reveal it.
**Deep practice:** build a complete logging baseline in your lab: Wazuh agents on all hosts, Sysmon with a tuned config ([olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular)), and confirm you can see process, network and auth events from every host.
**English:** write a one-page "what we log and why" document.
**Deliverable:** a fully instrumented lab and an ATT&CK-to-log-source map.

## Weeks 3-4: Detection engineering

**Read/study:** the [Sigma](https://github.com/SigmaHQ/sigma) rule format; detection-as-code concepts; the HTB detection modules.
**Practice:** write ten detections for techniques you can execute, using [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) to trigger each and confirm it fires.
**Deep practice:** build a small detection library in your repo: each rule with its ATT&CK mapping, the atomic test that validates it, and its false-positive profile.
**English:** document each detection in English (what it catches, how to tune it).
**Deliverable:** ten validated detections mapped to ATT&CK, in your portfolio.

## Weeks 5-6: Alert triage and SOC operations

**Read/study:** the incident-handling and triage modules; how to write a clear ticket and when to escalate.
**Practice:** [LetsDefend](https://letsdefend.io/) free tier and CyberDefenders alert-based labs; triage dozens of alerts.
**Deep practice:** run a "shift" in your lab: generate a stream of mixed benign and malicious activity (script it), then work the alert queue cold, triaging and documenting each with a verdict.
**English:** write five professional triage tickets.
**Deliverable:** a shift log with triaged alerts and tickets.

## Weeks 7-9: Digital forensics and incident response

**Read/study:** the DFIR modules; Windows forensic artifacts; the tools ([Eric Zimmerman's tools](https://ericzimmerman.github.io/), [Volatility 3](https://github.com/volatilityfoundation/volatility3), [Hayabusa](https://github.com/Yamato-Security/hayabusa), [Chainsaw](https://github.com/WithSecureLabs/chainsaw)).
**Practice:** one CyberDefenders DFIR lab per week (disk, memory, and multi-source).
**Deep practice:** full investigations. Week 7 endpoint/disk, week 8 memory with Volatility, week 9 a combined case. Each ends with an incident report.
**English:** write each incident report to professional standard; practice the investigative narrative.
**Deliverable:** three incident reports across disk, memory and combined evidence.

## Weeks 10-11: Threat hunting and threat intelligence

**Read/study:** hypothesis-driven threat hunting; reading threat intel ([The DFIR Report](https://thedfirreport.com/), vendor reports); turning intel into detections.
**Practice:** load the [Splunk BOTS v3](https://github.com/splunk/botsv3) dataset and hunt for specific techniques; run [Hayabusa](https://github.com/Yamato-Security/hayabusa)/[Chainsaw](https://github.com/WithSecureLabs/chainsaw) over collected logs.
**Deep practice:** pick a threat actor or malware family from public intel, extract its TTPs, write detections for them, and hunt for them in the BOTS dataset or your lab.
**English:** write a threat intelligence brief relevant to Colombia or Latin America from public sources, with TTPs and detection ideas.
**Deliverable:** one threat-intel brief and a hunt report.

## Week 12: Capstone and response exercise

**Deep practice:** run a full incident end to end in your lab: have a peer (or a script) execute an attack chain, then detect it, triage, investigate across network and endpoint, contain, and write a complete incident report with a timeline, ATT&CK mapping, IOCs, root cause and lessons learned. This mirrors a real IR engagement and the practical exams (BTL1, CDSA).
**English:** the report is the deliverable; executive summary plus full technical detail.
**Deliverable:** a capstone incident report, portfolio-grade.

## You are ready for the certification when...

- [ ] You can take raw logs and reach a defensible verdict on whether an incident occurred.
- [ ] You can write and validate a detection, and tune it to reduce false positives.
- [ ] You can investigate across network, disk and memory and build a timeline.
- [ ] You can write an incident report a manager and an engineer can both act on.
- [ ] You have a detection library, three incident reports and a threat brief in your portfolio.

**Free-only path:** Wazuh + Splunk Free + Sysmon in your lab, CyberDefenders free labs, LetsDefend free tier, the BOTS dataset and the open-source DFIR tools cover this track end to end without a subscription.
