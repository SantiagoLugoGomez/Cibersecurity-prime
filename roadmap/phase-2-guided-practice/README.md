# Phase 2: Guided practice

**Duration:** 16 weeks: about 7 hours per week during the semester, with a faster pace during one break (see [weekly-plan.md](../../weekly-plan.md)).
**When:** Semesters 3 and 4.
**Prerequisites:** Phase 0 complete; Phase 1 at least through the OWASP block.

Practice is where knowledge turns into skill. This phase uses structured platforms, where the targets are legal, scoped and designed to teach, and adds the habit that separates professionals from hobbyists: documenting every solve to a standard someone else could follow.

## Objectives

By the end of this phase you can:

1. Solve beginner CTF challenges across general skills, web, cryptography, forensics and reverse engineering.
2. Finish the core OverTheWire wargames (Bandit, Natas, Leviathan) without walkthroughs for most levels.
3. Find and exploit common web vulnerabilities in deliberately vulnerable applications, and explain the fix for each.
4. Compromise easy-rated machines on TryHackMe or Hack The Box following a repeatable methodology.
5. Investigate basic blue team scenarios (phishing email, suspicious login, packet capture) and reach a justified conclusion.
6. Write professional writeups using the [template](../../writeups/TEMPLATE.md).

## Plan

| Weeks | Block | Main output |
|---|---|---|
| 1-4 | Beginner CTFs | 40 challenges on CyLab Security Academy (picoGym) across five categories |
| 5-7 | Wargames | Bandit finished, Natas 0-15, Leviathan finished |
| 8-11 | Web labs | All Web Security Academy apprentice labs; 30 Juice Shop challenges in your lab |
| 12-14 | Machines | 6 easy machines on TryHackMe or Hack The Box |
| 15-16 | Blue team labs and review | 4 investigations on CyberDefenders or Blue Team Labs Online; writeup backlog cleared |

Join one beginner-friendly online CTF per month from [CTFtime](https://ctftime.org/) throughout the phase, ideally with classmates.

## Methodology for machines and challenges

Use the same loop every time and write it down as you go:

1. **Scope:** confirm what is in scope and what the platform allows.
2. **Reconnaissance and enumeration:** identify services, versions, technologies and users. Enumerate more than feels necessary.
3. **Hypothesis:** list possible weaknesses for each service, most likely first.
4. **Test:** check one hypothesis at a time and record the result, including failures.
5. **Exploit and escalate:** gain access, then repeat the loop from the new position.
6. **Root cause and fix:** for every step, write why it worked and what would have prevented it.
7. **Write up** within 48 hours, while it is still fresh.

**Hint rule:** if you have made no progress for 45 minutes, read one hint or the first section of a writeup, then close it and continue. Note in your writeup what you missed and why.

## Resources

### Beginner CTFs

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [CyLab Security Academy](https://cylabacademy.org/) (formerly picoCTF and picoGym) | Free | Hundreds of graded practice challenges by Carnegie Mellon. picoCTF moved here on May 8, 2026; old accounts still work. The annual picoCTF competition continues. |
| 2 | [CTFtime](https://ctftime.org/) | Free | Calendar of online CTFs and team rankings |
| 3 | [Root-Me](https://www.root-me.org/?lang=en) | Free for personal use | 600+ challenges grouped by category, many in web and network |
| 4 | [CryptoHack](https://cryptohack.org/) | Free | Continue from Phase 1 for cryptography challenges |

### Wargames

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [OverTheWire](https://overthewire.org/wargames/) | Free | Bandit, then Natas (web), Leviathan (Linux binaries), Krypton (classical crypto) |
| 2 | [pwn.college](https://pwn.college/) | Free | After Linux Luminarium, continue with the introductory dojos for program interaction and assembly |

### Web labs

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Free | The best free web security curriculum; every topic has labs |
| 2 | [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) | Free, self-hosted | Modern vulnerable application with 100+ challenges; run it in your [home lab](../../homelab/README.md) |
| 3 | [DVWA](https://github.com/digininja/DVWA) | Free, self-hosted | Classic vulnerabilities at adjustable difficulty; good for seeing how a fix changes behavior |
| 4 | [Hacker101](https://www.hacker101.com/) | Free | HackerOne's video lessons and CTF; progress can lead to private bug bounty invitations |

### Network and system labs

| # | Resource | Cost (October 2026) | Why |
|---|---|---|---|
| 1 | [TryHackMe free rooms](https://tryhackme.com/free-rooms) | Free: 650+ rooms, 1 hour of AttackBox per day, OpenVPN access | Guided rooms with explanations; use OpenVPN from your own Kali VM to avoid the AttackBox limit |
| 2 | [Hack The Box Academy](https://academy.hackthebox.com/) | Tier 0 modules free; Student plan $10/month (academic email added as secondary), covers modules up to Tier II | Deep, text-based modules. With a university email, this is the best value in this phase. Price confirmed in the [HTB help center](https://help.hackthebox.com/en/articles/13677074-academy-subscriptions). |
| 3 | [Hack The Box Labs](https://www.hackthebox.com/hacker/pricing) | Free: 20 active machines and 80+ active challenges. VIP $14/month adds retired machines. | Unguided machines. Retired machines have public writeups and video walkthroughs to learn from after you try. |
| 4 | [IppSec](https://ippsec.rocks/) | Free | Searchable index of IppSec's video walkthroughs of retired HTB machines, by technique |

### Blue team labs

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [CyberDefenders](https://cyberdefenders.org/blue-team-labs/) | Free labs; Pro labs paid | Realistic investigations: packet captures, disk and memory images, logs |
| 2 | [Blue Team Labs Online](https://blueteamlabs.online/) | Free challenges; PRO subscription for investigations | Short blue team challenges with a scoreboard |
| 3 | [LetsDefend](https://letsdefend.io/) | Free tier with limited content | Simulated SOC alert queue |

## Required hands-on practice

- **CTF:** 40 picoGym challenges, at least 5 in each of General Skills, Web Exploitation, Cryptography, Forensics and Reverse Engineering.
- **Wargames:** Bandit complete, Natas 0-15, Leviathan complete.
- **Web:** all Web Security Academy apprentice labs; practitioner labs in SQL injection, access control and authentication. 30 Juice Shop challenges, including at least five rated 3 stars or higher.
- **Machines:** 6 easy machines, at least 2 of them Windows, without a full walkthrough.
- **Blue team:** 4 investigations, including one packet capture and one phishing email.
- **Events:** at least 3 online CTFs, one of them with a team.
- **Writeups:** 10 complete writeups using the template. Publish at least 3 in [writeups/](../../writeups/) that the platform's rules allow you to share (see [writeups/README.md](../../writeups/README.md)).

## You've mastered this phase when...

- [ ] You can compromise an easy machine you have never seen in under 4 hours, without a walkthrough.
- [ ] You have 40 or more picoGym solves spread across five categories.
- [ ] You finished Bandit, Natas 0-15 and Leviathan.
- [ ] You finished every Web Security Academy apprentice lab and can explain the root cause and fix of each vulnerability class.
- [ ] You can explain, for each machine you solved, what the administrator should change, in order of priority.
- [ ] You can investigate a phishing email and a packet capture and write a conclusion with evidence.
- [ ] You have 10 writeups that a classmate could follow from start to finish.
- [ ] You have played at least 3 online CTFs.

Next: [Phase 3, specialization](../phase-3-specialization/README.md).
