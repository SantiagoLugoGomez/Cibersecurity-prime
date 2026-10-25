# Speaking and listening practice

Writing you can revise; speaking you cannot. In an interview or a meeting you have one take, so fluency about attacks and defenses has to be rehearsed until the words come without searching. This page gives you a method to practice speaking, a bank of interview questions to rehearse, and listening sources that train your ear to the field's accents and vocabulary.

## Why speaking is the hardest part

You already read and write English well, but producing precise technical English in real time is a different skill. The gap shows up as: hunting for a word mid-sentence, falling back on vague terms ("the thing that checks the password"), or freezing on a question you could answer easily in writing. The fix is deliberate spoken practice, not more reading.

## A method for speaking practice

### The two-minute explanation drill

Pick one concept and explain it out loud for two minutes, to an imaginary non-technical colleague, with no notes. Record yourself on your phone. Then listen back and note: where you paused to search for a word, where you used a vague term, where grammar slipped. Do one concept per session.

Good concepts to start with:

- How SQL injection works and how to prevent it.
- The difference between hashing and encryption.
- What multi-factor authentication protects against, and what it does not.
- What happens, step by step, when you load an HTTPS website.
- How a SOC analyst decides whether an alert is a real incident.
- What least privilege means and why it matters.

Then do the same drill for a technical listener, where you can use the exact terms. Being able to switch between the two audiences is a C2 register skill.

### The teach-back

Explain something you just learned to a classmate, a study group or a camera, in English. Teaching forces you to produce the vocabulary actively. If you run a study group or a CTF team, make English the working language for one session a week.

### Think-aloud during labs

While solving a machine or a challenge, narrate what you are doing in English, as if streaming: "I am enumerating the web server, I found an upload form, I will test whether it validates the file type." This builds the exact fluency a technical interview or a live readout call needs.

### Shadowing

Play a sentence from a talk or podcast, pause, and repeat it aloud, copying the rhythm and stress. Thirty seconds of a clear speaker, repeated, trains pronunciation and the natural phrasing of the field far faster than reading.

## Technical interview questions to rehearse

Rehearse each out loud until you can answer in under a minute without stalling. These are common entry-level and track-specific questions.

### General and behavioral

1. Walk me through what happens when you type a URL and press enter.
2. Explain the CIA triad with an example of each.
3. What is the difference between a vulnerability, an exploit and a threat?
4. How do you keep up with security news? Name a recent vulnerability and why it mattered.
5. Tell me about a machine or challenge you solved. What was the hardest part?
6. You find a serious vulnerability in a system you were not asked to test. What do you do?
7. Why cybersecurity, and why this track?

### Offensive

8. Describe your methodology for a box you have never seen.
9. What is the difference between a reverse shell and a bind shell?
10. Explain three ways to escalate privileges on Linux.
11. What is pass-the-hash and why does it work?
12. How would you explain a critical finding to a client who is not technical?

### Defensive

13. An alert fires for multiple failed logins followed by a success. Walk me through your triage.
14. What is the difference between a SIEM and an EDR?
15. How do you tell a false positive from a real incident?
16. Explain the phases of incident response.
17. What is MITRE ATT&CK and how would you use it in a SOC?

### Web

18. Explain the difference between stored, reflected and DOM-based XSS.
19. How does a parameterized query prevent SQL injection?
20. What is CSRF and how do anti-CSRF tokens stop it?
21. How would you review a login function for security problems?

### Cloud and GRC

22. What is the principle of least privilege in cloud IAM, and how is it commonly broken?
23. What is the difference between a policy, a standard and a procedure?
24. How would you explain a risk to management so they can decide whether to accept it?

Rehearse the general set in both English and Spanish. For Colombian employers you may interview in Spanish, but for multinationals and remote roles the technical interview is usually in English.

## Listening: podcasts, talks and channels

Listening trains your ear to native pace, idiom and the real vocabulary of the field. Aim for a few hours a week, passively while commuting and actively (with the shadowing drill) for short bursts.

### Podcasts

| Podcast | What it is | Why it helps |
|---|---|---|
| [Darknet Diaries](https://darknetdiaries.com/) | Narrative stories of real hacks and investigations | Clear narration, rich vocabulary, and genuinely engaging; the best starting point |
| [Risky Business](https://risky.biz/) | Weekly security news and interviews | Fast, idiomatic industry conversation; trains you for real discussions |
| [SANS Internet Storm Center StormCast](https://isc.sans.edu/podcast.html) | A short daily briefing, around five minutes | Current threats in a compact, technical register; good for a daily habit |

### Talks

| Source | What it is | Why it helps |
|---|---|---|
| [Black Hat YouTube channel](https://www.youtube.com/@BlackHatOfficialYT) | Recorded conference briefings | Formal technical presentation English; note that talks appear months after the event |
| [DEF CON media and YouTube](https://www.youtube.com/@DEFCONConference) | Conference talks archive | A wide range of speakers, accents and styles |
| [IppSec](https://www.youtube.com/@ippsec) | Hack The Box machine walkthroughs | Think-aloud technical English while hacking; model your own narration on it |
| [13Cubed](https://www.youtube.com/@13Cubed) | DFIR and forensics tutorials | Clear, measured explanation of defensive topics |

### How to use video

- First watch for content, subtitles on.
- Second watch, subtitles off, and pause to summarize each section aloud in English.
- Pick one or two segments for the shadowing drill.
- Add new terms to your [personal glossary](glossary.md) with the sentence you heard them in.

## A weekly speaking and listening routine

- One two-minute explanation drill, recorded and reviewed (15 minutes).
- Rehearse three interview questions aloud (10 minutes).
- One podcast episode while commuting or exercising (passive).
- One short talk segment with the shadowing drill (10 minutes).
- Once a week, narrate a full lab in English, or run a study-group session in English.

Over a semester this turns reading-level English into speaking-level English, which is the part that actually gets tested in an interview.
