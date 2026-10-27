# Module 2.3: Machines and Active Directory (weeks 11-16)

Full-machine compromise is the skill most people mean by "hacking": enumerate a host you have never seen, find a way in, and escalate to full control. This module builds it on Linux, Windows and a small Active Directory.

**Main resources:** [TryHackMe](https://tryhackme.com/) free rooms and [Hack The Box](https://www.hackthebox.com/) (free tier plus Academy Student plan), [IppSec](https://ippsec.rocks/) video index, [HackTricks](https://book.hacktricks.wiki/), [GTFOBins](https://gtfobins.github.io/), [LOLBAS](https://lolbas-project.github.io/).

**Rule:** only retired HTB machines may be written up publicly. Keep active-machine notes in your private repo.

## Week 11: Enumeration and the methodology on Linux

**Goal:** a repeatable enumeration process, and your first full Linux machine.

**R. Read and study (75 min)**
- HackTricks: the "Pentesting Methodology" page and the Linux privilege-escalation checklist.
- Notes: a service-by-service enumeration checklist (web, SMB, SSH, FTP, databases); from a foothold, the Linux privesc vectors (sudo rules, setuid, cron, capabilities, kernel).
- Flashcards: enumeration order, five Linux privesc checks, what `sudo -l` tells you, GTFOBins idea.

**P. Guided practice (90 min)**
- TryHackMe: a guided easy Linux room (connect with OpenVPN from your Kali VM to avoid the AttackBox time limit).
- Run `linpeas` on a lab VM and read what it flags.

**D. Deep practice (3 h)**
- Compromise one easy Linux machine end to end (TryHackMe or a retired HTB box) without a full walkthrough. Follow the six-step method. Write a complete writeup including a root-cause-and-fix section and an ATT&CK mapping.

**E. English (60 min)**
- Write the writeup in English. Add a "lessons learned" section naming what slowed you down.

**Check yourself**
1. What is your enumeration order when you see ports 22, 80 and 445 open?
2. What does `sudo -l` reveal, and how can a single allowed command lead to root?
3. How does a setuid binary on GTFOBins become a privesc?
4. What did `linpeas` flag that you would have missed?
5. What would the administrator change to stop your path?

**Deliverable:** one full Linux machine writeup with root cause and ATT&CK mapping.

## Week 12: Windows machines and privilege escalation

**Goal:** apply the method to Windows, where enumeration and privesc differ.

**R. Read and study (75 min)**
- HackTricks: the Windows local privilege-escalation checklist.
- Notes: Windows enumeration (SMB shares, services, scheduled tasks, registry); privesc vectors (unquoted service paths, weak service permissions, token privileges, stored credentials); living-off-the-land binaries ([LOLBAS](https://lolbas-project.github.io/)).
- Flashcards: `winpeas`, unquoted service path, `SeImpersonatePrivilege`, where Windows stores creds, what a LOLBin is.

**P. Guided practice (90 min)**
- TryHackMe: a guided easy Windows room.
- Run `winpeas` on your Windows 11 lab VM and interpret the output.

**D. Deep practice (3 h)**
- Compromise one easy Windows machine end to end without a full walkthrough. Writeup with root cause, ATT&CK mapping, and the defender's view: which event logs (recall Module 0.7) would have recorded each step.

**E. English (60 min)**
- Rehearse out loud: explain one Windows privesc technique and its detection, in two minutes.

**Check yourself**
1. How does Windows enumeration differ from Linux?
2. What is an unquoted service path, and how is it abused?
3. What does `SeImpersonatePrivilege` enable?
4. What is a LOLBin, and why are they useful to attackers?
5. Which event IDs would reveal your privesc?

**Deliverable:** one full Windows machine writeup with the defender's view.

## Weeks 13-14: More machines, building range and speed

**Goal:** solve four more machines across OSes to build pattern recognition.

**R. Read and study (75 min each week)**
- Watch one [IppSec](https://ippsec.rocks/) walkthrough of a retired box *after* you attempt it, and note techniques you did not know.
- Notes: a growing personal "techniques seen" list, grouped by enumeration, foothold and privesc.
- Flashcards: new techniques from each box.

**P. Guided practice (90 min each week)**
- One easy machine per week with light hint use, focusing on speed and clean notes.

**D. Deep practice (3 h each week)**
- One machine per week fully on your own (no walkthrough until done). Two boxes per week total across guided and deep. Writeups for the self-solved ones.
- By the end of week 14 you should have six machines total since week 11.

**E. English (60 min each week)**
- Keep writing English writeups. Vary the audience: one for a technical reader, one explaining the key bug to a beginner.

**Check yourself (end of week 14)**
1. What enumeration step most often unlocks the foothold for you?
2. Which privesc techniques have you now used more than once?
3. How much faster are you than on your first box, and where is the time going now?
4. What class of machine still blocks you?
5. Could you solve a box like these in an exam setting in four hours?

**Deliverable:** six machines total since week 11, at least four with full writeups, plus your growing techniques list.

## Weeks 15-16: Active Directory

**Goal:** understand and attack a small Windows domain, the core of enterprise pentesting.

**R. Read and study (75 min each week)**
- HackTricks: the Active Directory methodology overview.
- Notes: AD concepts (domain, forest, users, groups, Kerberos, NTLM); the common attack chain (initial access, enumeration with BloodHound, Kerberoasting, lateral movement, domain dominance); why these work.
- Flashcards: Kerberoasting, AS-REP roasting, pass-the-hash, what [BloodHound](https://github.com/SpecterOps/BloodHound) maps, DCSync.

**P. Guided practice (90 min each week)**
- TryHackMe or HTB Academy AD modules (the AD content in the Penetration Tester path, free Tier 0 where available).
- Stand up [GOAD-Light](https://github.com/Orange-Cyberdefense/GOAD) in your lab, or use your own DC from Module 0.7.

**D. Deep practice (3 h each week)**
- Over the two weeks, run one full attack path against your lab domain: enumerate with BloodHound, get a foothold, Kerberoast a service account, move laterally, and reach Domain Admin. Document every step.
- Then switch seats: for each step, identify the Windows event or Sysmon log that recorded it (Module 0.7 and 1.5). This purple-team writeup is a strong portfolio piece and the seed of a Phase 4 project.

**E. English (60 min each week)**
- Write the AD attack path as a professional report in English, with an attack narrative and a detection table.

**Check yourself (end of week 16)**
1. What is Kerberoasting, and why does it work?
2. What does BloodHound compute that manual enumeration cannot easily?
3. What is the difference between pass-the-hash and pass-the-ticket?
4. How does an attacker go from one user to Domain Admin in your lab?
5. Which detections would catch the attack earliest?

**Deliverable:** one full AD attack-and-detect writeup against your lab domain.

**Stretch:** read about [Impacket](https://github.com/fortra/impacket) tools and use two of them (e.g. `GetUserSPNs`, `secretsdump`) against your own lab.
