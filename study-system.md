# The study system

This roadmap only works if the hours you put in actually stick. This page explains how to run the four weekly sessions, take notes that you will reuse, and review so you do not forget. Read it once at the start (it is week 1 of Phase 0) and come back when a habit slips.

## The four sessions

Every week in every phase has the same four sessions. Keeping the format fixed removes the daily "what should I do?" decision.

### R: Read and study (75 min)

Reading passively does almost nothing. Read actively:

1. **Preview (5 min):** read the headings and the summary first. Ask: what should I be able to do after this?
2. **Read in chunks (50 min):** after each section, look away and say the main idea in your own words. If you cannot, reread that section.
3. **Make flashcards (20 min):** turn the key facts into questions (see below). Aim for 5 to 15 cards, not 50. Fewer, well-chosen cards beat a dump.

Write notes in your own words. Copied notes feel productive and teach little.

### P: Guided practice (90 min)

Structured exercises with a known answer: labs, CTF levels, drills. The point is repetition and feedback. If you get one wrong, redo it until it is automatic. Keep a one-line record of what each exercise taught.

### D: Deep practice (3 h)

One longer, open problem: a machine, a build, a tool, an investigation. This is where real skill forms, because you have to combine things and get stuck. Rules:

- Work from the week's method, not from a walkthrough.
- When stuck for 45 minutes with no progress, take one hint, then close it.
- Keep notes *as you go*, not after. Screenshots, commands, what worked and what did not.
- End with a short writeup. The [writeup template](writeups/TEMPLATE.md) is the target.

### E: English (60 min)

Same topic as the week, but in English: read a source, write a note or finding, or explain something out loud. The [english track](english/README.md) says exactly what to do each week. Do not skip it; technical English is a career multiplier and it is easiest to build on material you already understand.

## Notes: the two-repo system

Keep two separate places:

- **This public repo (portfolio):** polished writeups, reports, tools and your progress. Things you are happy for an employer to see.
- **A private `security-notes` repo:** raw notes, flashcard decks, lab command history, and anything you must not publish (solutions to active or graded content). The [`.gitignore`](.gitignore) here excludes `private/` as a backup, but keep genuinely private material in the private repo.

Structure your private notes one file per week, named like `phase-0/week-02.md`, following the [weekly note template](templates/weekly-note.md). Future-you will search these constantly.

## Flashcards and spaced repetition

Memory fades on a predictable curve. Spaced repetition beats that curve by showing you a card just before you would forget it.

- Use [Anki](https://apps.ankiweb.net/) (the desktop app is free) or any spaced-repetition tool.
- Write **atomic** cards: one fact per card, phrased as a question. "What does event ID 4625 mean?" not "Windows event logs".
- Write cards in your own words, from understanding, never copied.
- Review daily, 10 minutes. It is the highest-return habit in this whole roadmap.
- Put commands, definitions, port numbers, framework items and your-own-mistakes on cards. Put skills (exploiting, investigating) in practice sessions, not cards.

## The check-yourself questions

Every week ends with questions to answer **from memory**, out loud or on paper. They are the gate to the next week:

- Answer all of them cleanly → move on.
- More than two shaky → repeat that week's R session and the weak practice before advancing.

Do not lie to yourself here. The questions mirror what an interviewer or an exam will ask.

## Weekly and monthly review

- **End of each week (part of the Sunday slot in [weekly-plan.md](weekly-plan.md)):** answer the check-yourself questions, commit your deliverable, update [progress.md](progress.md), and plan the next week. Use the [weekly review template](templates/weekly-review.md).
- **End of each month:** reread your month's writeups, re-answer a sample of old check-yourself questions, and note any topic that has gone stale to refresh with a few flashcards.
- **End of each phase:** confirm the phase mastery checklist honestly before moving on.

## When you get stuck (and you will)

Being stuck is the job, not a failure. A routine for it:

1. Re-read the task or error carefully. Most blocks are a missed detail.
2. Enumerate again. On machines, 90% of blocks are missed enumeration.
3. Check your notes and flashcards for something similar.
4. Search the specific error or symptom, not the whole problem.
5. After 45 minutes with no progress, take one hint, then continue and note what you missed.
6. If a whole topic is not landing, drop back a level (an easier box, a more basic lab) and build up again.

## Protecting the habit

- A fixed weekly schedule beats motivation. Put the deep-practice block in your calendar as an appointment.
- Consistency over intensity: four steady hours a week for a year beats occasional marathons.
- Track streaks in [progress.md](progress.md); a visible chain is motivating.
- One rest day a week with no security work is part of the plan.
- During exam season, drop to the maintenance plan in [weekly-plan.md](weekly-plan.md) rather than stopping entirely.
