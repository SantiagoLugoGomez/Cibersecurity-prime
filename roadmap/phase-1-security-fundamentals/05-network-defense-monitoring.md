# Module 1.5: Network security and monitoring (weeks 12-13)

Having built and attacked, now learn to watch. This module introduces the defensive view: capturing traffic, generating and finding detections, and understanding how attacks look from the SOC.

**Main resources:** [Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/), [Zeek](https://zeek.org/) and [Suricata](https://suricata.io/), your lab's Wazuh stack, [MITRE ATT&CK](https://attack.mitre.org/).

## Week 12: Traffic analysis and network detection

**Goal:** read network traffic for signs of attack and understand how an IDS works.

**R. Read and study (75 min)**
- Wireshark User's Guide: display filters, following streams, statistics and expert info.
- Read about [Suricata](https://suricata.io/) (signature IDS) and [Zeek](https://zeek.org/) (network metadata logging) and how they complement each other.
- Notes: how to spot a port scan, a brute-force attempt and data exfiltration in a capture; signature vs anomaly detection; what Zeek logs (conn, dns, http, ssl) vs what Suricata alerts on.
- Flashcards: three Wireshark display filters you will reuse, IDS vs IPS, signature vs anomaly detection, what a Zeek conn.log row tells you.

**P. Guided practice (90 min)**
- Analyze a provided malicious pcap (from [malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/), which publishes training captures) or one you generate: identify the suspicious host, the protocol abused and the indicators.
- In your lab, run an Nmap scan from Kali against the Docker host and capture it; identify the scan signature in the traffic.

**D. Deep practice (3 h)**
- In your lab, generate three activities (a port scan, an SSH brute force, and a large file transfer out), capture each, and write a short "what the network shows" analysis for each with the key packets highlighted and the indicators listed. This is the raw skill behind network detection.

**E. English (60 min)**
- Write one "network detection note" in English: the activity, how it appears in traffic, and what a defender should alert on.

**Check yourself**
1. Write a Wireshark display filter to show only traffic to or from one host on port 445.
2. How does a port scan look different from normal traffic?
3. What is the difference between what Zeek and Suricata each give you?
4. What is the difference between an IDS and an IPS?
5. What indicators would suggest data exfiltration in a capture?

**Deliverable:** three network-activity analyses with captures, and one detection note.

## Week 13: Logs, SIEM and the SOC view

**Goal:** collect logs centrally, write detections, and map activity to ATT&CK the way a SOC does.

**R. Read and study (75 min)**
- Your lab's [Wazuh](https://documentation.wazuh.com/current/quickstart.html) documentation: how agents, decoders, rules and alerts work.
- Read about the [Sigma](https://github.com/SigmaHQ/sigma) generic detection rule format and [MITRE ATT&CK](https://attack.mitre.org/) tactics and techniques (recall ATT&CK v19 split Defense Evasion into Stealth and Defense Impairment).
- Notes: log sources that matter (auth, Sysmon, web, firewall); what a detection rule is; true/false positives; how a SOC triages an alert; the ATT&CK tactic order.
- Flashcards: Wazuh agent vs manager, what a Sigma rule is, false positive vs false negative, the ATT&CK tactics in order.

**P. Guided practice (90 min)**
- In Wazuh, generate the three activities from last week on monitored hosts and find the resulting alerts. Read the rule that fired for each.
- Read two [Sigma](https://github.com/SigmaHQ/sigma) rules and explain, in your notes, exactly what each detects.

**D. Deep practice (3 h)**
- Pick one intrusion report from [The DFIR Report](https://thedfirreport.com/). Build an [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) layer of the techniques used, then for the three earliest techniques write how you would detect each in your lab (which log source, which condition). Where you can, implement one as a Wazuh custom rule or a Sigma rule and trigger it.
- This is the core loop of detection engineering.

**E. English (60 min)**
- Read a section of the chosen DFIR report closely (Module reading method in [reading-professional-material.md](../../english/reading-professional-material.md)). Note the narrative verbs ("the actor then", "which allowed"). Summarize the intrusion in five sentences.

**Check yourself**
1. What is the path of a log from an endpoint to an alert in a SIEM?
2. What does a Sigma rule describe, and why is a vendor-neutral format useful?
3. Given a failed-then-successful login burst, what do you check first?
4. Map a brute-force-then-login intrusion to ATT&CK tactics.
5. What makes a detection rule noisy, and how would you tune it?

**Deliverable:** the ATT&CK Navigator layer for a real intrusion, with detection ideas for the earliest techniques and at least one rule implemented and triggered in your lab.

**Stretch:** read about [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) and run one atomic test against a lab host, then confirm it fires your detection.
