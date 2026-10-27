# Phase 2: Guided practice

**Duration:** 20 weeks at about 7.5 hours per week (around 150 hours).
**When:** Semesters 3 and 4, with one break used to accelerate.
**Prerequisites:** Phase 0 complete; Phase 1 at least through the web module.

Practice turns knowledge into skill. This phase uses platforms where the targets are legal, scoped and built to teach, and builds the habit that separates professionals from hobbyists: documenting every solve to a standard someone else could follow. Each module is a separate file with the full week-by-week plan.

## Modules

| Module | Weeks | Topic |
|---|---|---|
| [2.1 CTF foundations and methodology](01-ctf-foundations.md) | 1-4 | The five CTF categories, a repeatable method, first online CTF |
| [2.2 Wargames and web labs](02-wargames-web-labs.md) | 5-10 | OverTheWire, PortSwigger practitioner labs, Juice Shop |
| [2.3 Machines and Active Directory](03-machines-and-ad.md) | 11-16 | Full Linux and Windows machines, then a small AD attack and detect |
| [2.4 Blue team labs](04-blue-team-labs.md) | 17-20 | Alert triage, network and endpoint forensics, a SIEM capstone |

## The method, used everywhere

1. Enumerate everything first.
2. Form hypotheses, most likely first.
3. Test one at a time, recording failures too.
4. Exploit, then re-enumerate from the new position.
5. Understand the root cause and the fix.
6. Write it up within 48 hours.

**Hint rule:** no progress for 45 minutes, read one hint, close it, continue, and note what you missed.

## What you may publish

Your own lab, Juice Shop, DVWA, picoGym, OverTheWire (method, not stored passwords) and **retired** HTB machines are fine to write up. Active HTB machines are not; keep those notes in your private repo. Some CTFs forbid writeups until they end. See [writeups/README.md](../../writeups/README.md).

## Objectives

By the end of this phase you can:

1. Solve beginner CTF challenges across all five categories and play online CTFs with a team.
2. Finish the core OverTheWire wargames and the PortSwigger practitioner labs in the key topics.
3. Compromise easy Linux and Windows machines unaided, and run a basic Active Directory attack.
4. Investigate alerts, network captures and endpoints to a justified conclusion.
5. Write professional writeups and incident reports, and see both the attacker's and defender's view of the same event.

## You've mastered this phase when...

- [ ] You can compromise an easy machine you have never seen in under four hours, without a walkthrough.
- [ ] You have 40+ CTF solves across five categories and have played at least three online CTFs.
- [ ] You finished Bandit, Natas and Leviathan, and the PortSwigger practitioner labs in four topics.
- [ ] You solved at least six machines (Linux and Windows) with writeups, and ran one full AD attack-and-detect.
- [ ] You can triage alerts and investigate a network capture and an endpoint to a written conclusion.
- [ ] You have a body of writeups and at least one polished incident report and one web assessment, all shareable.

Track these in [progress.md](../../progress.md).

Next: [Phase 3, specialization](../phase-3-specialization/README.md).
