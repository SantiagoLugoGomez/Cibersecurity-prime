# <Box or challenge name>

| Field | Value |
|---|---|
| Platform | <TryHackMe / Hack The Box / picoCTF / OverTheWire / other> |
| Type | <Machine / Web / Crypto / Forensics / Reversing / Pwn> |
| Difficulty | <Easy / Medium / Hard> |
| Date solved | <YYYY-MM-DD> |
| Time spent | <hours> |
| Hints used | <none / one hint at step X / walkthrough for privesc> |
| Tags | <e.g. linux, sqli, suid, active-directory> |

> Authorization: this target is a lab or platform that authorizes testing. See [../legal-and-ethics.md](../legal-and-ethics.md). Do not publish writeups for active Hack The Box content or anything a platform's rules forbid sharing.

## Summary

Two or three sentences: what the target was, the path to the goal, and the single most important lesson. Written so a classmate who has not touched the box understands what happened.

## Reconnaissance

What you found and how. Commands and their relevant output, trimmed to what mattered.

```bash
# example
nmap -sC -sV -oN nmap/initial.txt 10.10.10.10
```

| Port | Service | Version | Note |
|---|---|---|---|
| 22 | SSH | OpenSSH 8.9 | |
| 80 | HTTP | nginx 1.24 | Login page |

## Enumeration

Services explored in more depth: directories found, technologies identified, users enumerated. Keep the hypotheses visible, including the ones that led nowhere.

## Exploitation

The path that worked, step by step, with enough detail to reproduce. For each step say what you did, what you expected and what happened.

```bash
# example payload or command
```

Include evidence (a trimmed response, a screenshot reference). Do not paste full credentials or secrets if you plan to publish; redact them.

## Privilege escalation

How you moved from initial access to the goal (root, SYSTEM, the flag). Same level of detail.

## Proof

The flag or final evidence, redacted if the platform requires it (for example `HTB{re...ed}`).

## Root cause and fixes

The part that matters most for your growth and for a reader.

| Finding | Root cause | Fix | Reference |
|---|---|---|---|
| <what was wrong> | <why it was possible> | <what the administrator or developer should change> | <OWASP / ATT&CK / CVE link> |

## ATT&CK mapping (for machines and intrusions)

| Tactic | Technique | Where in this box |
|---|---|---|
| Initial Access | T1190 Exploit Public-Facing Application | <step> |

## Lessons learned

- What you will do faster or differently next time.
- A tool or technique you want to practice more.
- One thing you did not understand and need to read about.

## References

- <links to docs, advisories, writeups you used>
