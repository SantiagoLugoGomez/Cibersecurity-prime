# Module 2.1: CTF foundations and methodology (weeks 1-4)

Capture The Flag challenges are the gym of security. This module builds breadth across the five classic categories and, more importantly, the habit of a repeatable method and a writeup for every solve.

**Main resources:** [CyLab Security Academy / picoGym](https://cylabacademy.org/) (free, formerly picoCTF), [CTFtime](https://ctftime.org/), [CryptoHack](https://cryptohack.org/), [pwn.college](https://pwn.college/).

## The method you will use for everything

Write this on a card and follow it on every challenge and machine from now on:

1. **Enumerate** everything before touching anything.
2. **Form hypotheses**, most likely first.
3. **Test one at a time**, recording results including failures.
4. **Exploit**, then re-enumerate from the new position.
5. **Understand the root cause** and the fix.
6. **Write it up** within 48 hours.

**Hint rule:** stuck with no progress for 45 minutes, read one hint, close it, continue. Note what you missed.

## Week 1: General skills and the toolkit

**Goal:** get comfortable with the CTF workflow and the everyday tools.

**R. Read and study (75 min)**
- picoGym / CyLab: the "Getting Started" material. Skim writeups for two easy challenges to see what a good solve looks like.
- Notes: encoding (hex, Base64, URL), the Linux tools you will reuse (`file`, `strings`, `xxd`, `grep`, `nc`, `curl`), and what each CTF category tests.
- Flashcards: `file`, `strings`, `xxd`, `base64 -d`, `nc`, what each of the five categories means.

**P. Guided practice (90 min)**
- picoGym "General Skills": solve at least eight challenges. Write the method for each.

**D. Deep practice (3 h)**
- Solve a mixed set of ten easy picoGym challenges across categories. For each, fill a short entry: category, what it tested, how you solved it, one lesson. Start your writeup habit here.

**E. English (60 min)**
- Read one published picoCTF/CyLab writeup. Note the structure and the verbs. Write your own writeup for one challenge in that style.

**Check yourself**
1. Decode this in your head or with one tool: what is `aGVsbG8=`?
2. When do you reach for `strings` vs `xxd`?
3. What does each of the five CTF categories test?
4. What is your six-step method?
5. Why write up a challenge you already solved?

**Deliverable:** ten solved challenges with short writeups.

## Week 2: Cryptography challenges

**Goal:** apply Module 1.2 crypto knowledge to break flawed implementations.

**R. Read and study (75 min)**
- CryptoHack: revisit "Introduction" and "Symmetric Ciphers" theory.
- Notes: the misuses you will exploit (ECB, reused nonces, weak RSA parameters, bad randomness).
- Flashcards: how to spot ECB, what a reused nonce leaks, small-exponent RSA, padding oracle idea.

**P. Guided practice (90 min)**
- CryptoHack: "General" and the start of "Symmetric Ciphers" and "RSA" categories.

**D. Deep practice (3 h)**
- Work a harder CryptoHack set (or picoGym crypto) until you have five solves that each required writing a Python script. Keep the scripts; this is applied crypto and applied Python together.

**E. English (60 min)**
- Write a writeup for the most interesting crypto solve, explaining the flaw to someone who knows the basics. Precision matters here.

**Check yourself**
1. How do you detect ECB from ciphertext alone?
2. Why does a small RSA public exponent with no padding leak the message?
3. What does nonce reuse in a stream cipher let you do?
4. Why is writing a script better than solving by hand here?
5. Which degree course does this reinforce, and how?

**Deliverable:** five scripted crypto solves with writeups.

## Week 3: Forensics and reverse engineering

**Goal:** pull hidden data out of files and understand what a binary does.

**R. Read and study (75 min)**
- Notes: file carving and metadata (`binwalk`, `exiftool`, `foremost`); packet-capture forensics (Wireshark, recall Module 1.5); what a disassembler and decompiler do ([Ghidra](https://github.com/NationalSecurityAgency/ghidra)); static vs dynamic analysis.
- Flashcards: `binwalk`, `exiftool`, `strings` on a binary, what Ghidra shows, static vs dynamic.

**P. Guided practice (90 min)**
- picoGym "Forensics": five challenges (steganography, pcap, disk images).
- picoGym "Reverse Engineering": three easy challenges, using Ghidra on at least one.

**D. Deep practice (3 h)**
- Forensics: work a pcap-based challenge end to end and extract the flag/evidence, writing a timeline of what happened in the capture.
- Reversing: take one simple crackme, open it in Ghidra, find the check, and explain in your notes what the program does and how you defeated it.

**E. English (60 min)**
- Write the reversing writeup: describe the program's logic and your approach in clear prose, not just screenshots.

**Check yourself**
1. What does `binwalk` look for, and when does it help?
2. How do you extract files transferred inside a pcap?
3. What is the difference between a disassembler and a decompiler?
4. What is the difference between static and dynamic analysis?
5. How did you locate the check in your crackme?

**Deliverable:** one forensics timeline and one reversing writeup with Ghidra.

## Week 4: Binary exploitation intro and first online CTF

**Goal:** meet memory-corruption basics and play a real timed CTF with others.

**R. Read and study (75 min)**
- [pwn.college](https://pwn.college/): the program-interaction and introductory assembly dojos (start them).
- Notes: the stack, calling conventions, what a buffer overflow overwrites, what a shellcode is at a high level. Connect to Module 0.6 (memory) and the DSA course ([degree-connections.md](../../degree-connections.md)).
- Flashcards: stack frame, return address, buffer overflow, what `pwntools` is for.

**P. Guided practice (90 min)**
- pwn.college: the first program-interaction levels. Install [pwntools](https://docs.pwntools.com/) and solve a trivial "talk to the program" challenge with it.

**D. Deep practice (3 h)**
- Play one beginner-friendly online CTF from [CTFtime](https://ctftime.org/), ideally with one or two classmates. Aim to solve at least two challenges in categories you are comfortable with. Afterward, write a team retro: what you solved, what you missed, what to study.

**E. English (60 min)**
- Join a CTF team chat (Discord) and read how people coordinate in English. Write one clear, specific help request about a challenge (even if you solve it yourself).

**Check yourself**
1. What does a buffer overflow overwrite, and why is the return address the prize?
2. What is a calling convention?
3. What does `pwntools` automate for you?
4. How did your team divide work in the CTF?
5. Which category do you most need to practice, based on the CTF?

**Deliverable:** pwn.college intro levels done, one online CTF played, and a team retro note.

**Stretch:** continue pwn.college assembly; read the "Smashing the Stack" classic for background.
