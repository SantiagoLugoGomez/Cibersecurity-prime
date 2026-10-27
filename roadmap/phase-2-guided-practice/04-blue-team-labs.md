# Module 2.4: Blue team labs (weeks 17-20)

Having attacked for sixteen weeks, spend four weeks defending. Even if you choose an offensive track, understanding detection and response makes you far better at both. This module uses realistic investigation platforms and your own lab.

**Main resources:** [CyberDefenders](https://cyberdefenders.org/blue-team-labs/) (free labs), [Blue Team Labs Online](https://blueteamlabs.online/) (free challenges), [LetsDefend](https://letsdefend.io/) (free tier), [Splunk BOTS v3](https://github.com/splunk/botsv3) dataset, your lab's Wazuh.

## Week 17: Log analysis and alert triage

**Goal:** work an alert queue and decide true vs false positive with evidence.

**R. Read and study (75 min)**
- Notes: the SOC analyst workflow (triage, investigate, escalate, document); what to check for each alert type (failed logins, malware, suspicious process); writing a clear ticket.
- Flashcards: triage steps, true vs false positive, what to record in a ticket, escalation criteria.

**P. Guided practice (90 min)**
- LetsDefend free tier or a CyberDefenders beginner lab: triage several alerts, documenting the decision for each.

**D. Deep practice (3 h)**
- In your lab, generate a mix of benign and malicious activity (normal logins plus a brute force, a normal download plus a suspicious one). Working only from the Wazuh alerts, triage each, investigate the real ones, and write tickets. Then check yourself against what you actually did.

**E. English (60 min)**
- Write one alert ticket in English to a professional standard: what fired, what you found, your verdict, and the recommended action.

**Check yourself**
1. What is your first step when an alert fires?
2. How do you distinguish a true positive from a false positive for a failed-login burst?
3. When do you escalate rather than close?
4. What belongs in a triage ticket?
5. What is the risk of closing a real alert as a false positive?

**Deliverable:** at least five triaged alerts with tickets, three from a platform and two from your lab.

## Week 18: Packet and network investigation

**Goal:** investigate an incident from network evidence.

**R. Read and study (75 min)**
- Notes: the network investigation method (identify the suspicious host, the protocol, the indicators, the timeline); extracting files and credentials from a capture.
- Flashcards: Wireshark statistics views, how to extract an object from HTTP, signs of C2 traffic (beaconing).

**P. Guided practice (90 min)**
- CyberDefenders: a pcap-based network forensics lab. Answer every question with evidence.
- Practice on a capture from [malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/).

**D. Deep practice (3 h)**
- Take one full network forensics case (CyberDefenders or a traffic-analysis exercise) and write a complete incident report: timeline, affected hosts, what the attacker did, indicators of compromise, and recommendations. Follow the [report style](../../english/writing-reports.md).

**E. English (60 min)**
- Write the incident report in English. Practice the past-tense investigative narrative ("the host then connected to...").

**Check yourself**
1. How do you spot beaconing C2 traffic in a capture?
2. How do you extract a file transferred over HTTP?
3. What indicators would you hand to the rest of the team?
4. How do you build a timeline from a pcap?
5. What distinguishes an incident report from a pentest report?

**Deliverable:** one full network incident report.

## Week 19: Endpoint forensics and DFIR tooling

**Goal:** investigate a compromised endpoint from logs and artifacts.

**R. Read and study (75 min)**
- Notes: Windows forensic artifacts (event logs, prefetch, registry run keys, scheduled tasks, Amcache/Shimcache); the DFIR tools ([Eric Zimmerman's tools](https://ericzimmerman.github.io/), [Hayabusa](https://github.com/Yamato-Security/hayabusa), [Chainsaw](https://github.com/WithSecureLabs/chainsaw) for event logs).
- Flashcards: three persistence locations, what prefetch shows, what Hayabusa/Chainsaw do, event ID 4688.

**P. Guided practice (90 min)**
- Run [Hayabusa](https://github.com/Yamato-Security/hayabusa) or [Chainsaw](https://github.com/WithSecureLabs/chainsaw) over the event logs from your Module 2.3 AD attack, and see which of your own attack steps it flags.
- A CyberDefenders endpoint/DFIR lab if time allows.

**D. Deep practice (3 h)**
- Take the Windows machine or AD attack you performed in Module 2.3, collect the endpoint evidence, and write the investigation from the defender's side: reconstruct what the attacker did using only the artifacts, and note where you (as attacker) left traces you did not expect. This before/after perspective is rare and valuable.

**E. English (60 min)**
- Write the endpoint investigation in English, with a clear timeline and an indicators section.

**Check yourself**
1. Name three places Windows persistence hides.
2. What does prefetch tell an investigator?
3. How did Hayabusa/Chainsaw flag your attack, and what did it miss?
4. What is the value of Shimcache/Amcache in an investigation?
5. As the attacker, which trace surprised you?

**Deliverable:** one endpoint investigation reconstructing your own earlier attack from artifacts.

## Week 20: Splunk, a capstone investigation, and phase review

**Goal:** use a real SIEM dataset and consolidate the phase.

**R. Read and study (75 min)**
- Notes: the Splunk search language basics (search, stats, table, timechart); how analysts pivot through a dataset.
- Flashcards: `stats count by`, `table`, `timechart`, how to narrow a search.

**P. Guided practice (90 min)**
- Load the [Splunk BOTS v3](https://github.com/splunk/botsv3) dataset into Splunk Free in your lab and work through a set of its questions.

**D. Deep practice (3 h)**
- Capstone: pick a CyberDefenders scenario or the BOTS dataset and run a full investigation end to end, producing one polished incident report (executive summary, timeline, technical detail, IOCs, recommendations). This is your blue-team portfolio piece.
- Then review the whole phase: tick the Phase 2 mastery checklist and list your three weakest areas to revisit.

**E. English (60 min)**
- Write the capstone report's executive summary and recommendations in English to a standard you would send to a manager.

**Check yourself**
1. Write a Splunk search that counts events by source IP.
2. How do you pivot from one indicator to the full scope of an incident?
3. What are the sections of a strong incident report?
4. Across the phase, are you stronger at attack or defense, and why?
5. Which three areas will you revisit before Phase 3?

**Deliverable:** one capstone incident report, and a phase-review note with your weak areas.

## End of Phase 2

You can now compromise easy machines unaided and investigate incidents to a conclusion, and you have a body of writeups. Confirm the mastery checklist in the [Phase 2 overview](README.md), then choose where to go deep.

Next: [Phase 3, specialization](../phase-3-specialization/README.md).
