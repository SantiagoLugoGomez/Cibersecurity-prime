# The study system

> [!TIP]
> **In short:** this roadmap only works if the hours you put in actually stick. Every week in every phase runs the same four sessions (Read, guided Practice, Deep practice, English), so you never sit down wondering what to do, and every technique below (active reading, atomic flashcards, check-yourself questions answered from memory) is chosen because the evidence in [Learning science](01-learning-science.md) says it works, not because it is traditional. Read this page once at the start, in week 1 of Phase 0, and come back whenever a habit slips.

## The four sessions

Every week in every phase uses the same fixed format, described in [the roadmap's weekly session format](../../roadmap/README.md#the-weekly-session-format). Keeping it fixed removes the daily "what should I do?" decision, which is itself a form of discipline worth protecting.

### R: Read and study (75 min)

Reading passively does almost nothing; this is retrieval practice applied to reading, as explained in [Learning science](01-learning-science.md#retrieval-practice-testing-yourself-is-studying).

1. **Preview (5 min).** Read the headings and the summary first. Ask: what should I be able to do after this?
2. **Read in chunks (50 min).** After each section, look away and say the main idea in your own words, from memory, not while rereading the text. If you cannot, reread that section once, then try again.
3. **Make flashcards (20 min).** Turn the key facts into questions. Aim for 5 to 15 cards, not 50; fewer, well-chosen cards reviewed consistently beat a large dump reviewed sporadically.

Write notes in your own words. Copied notes feel productive and teach very little, because copying requires no retrieval at all.

### P: Guided practice (90 min)

Structured exercises with a known answer: labs, CTF levels, drills. The point is repetition with feedback. If you get one wrong, redo it until it is automatic rather than moving on while it is still shaky. Keep a one-line record of what each exercise taught you, which becomes raw material for flashcards later.

### D: Deep practice (3 h)

One longer, open problem: a machine, a build, a tool, an investigation. This is where real skill forms, because you have to combine several things at once and get genuinely stuck, which is exactly the desirable-difficulty condition described in [Learning science](01-learning-science.md#desirable-difficulty-struggle-is-a-signal-not-a-warning). Rules:

- Work from the week's method, not from a walkthrough.
- When stuck for 45 minutes with no progress, take one hint, then continue and note exactly what you missed.
- Keep notes **as you go**, not after. Screenshots, commands, what worked and what did not.
- End with a short writeup. The [writeup template](../../writeups/TEMPLATE.md) is the target format.

### E: English (60 min)

Same topic as the week, but in English: read a source, write a note or finding, or explain something out loud. The [English track](../../english/README.md) specifies exactly what to do each week. Do not skip it; technical English is a career multiplier (see [Your degree and security](04-your-degree-and-security.md) and [Portfolio and writing](06-portfolio-and-writing.md)), and it is easiest to build on material you already understand from the same week's R and P sessions.

## Notes: the two-repository system

Keep two separate places for what you write:

| Repository | Contents | Visibility |
|---|---|---|
| **This repository (your portfolio)** | Polished writeups, reports, tools and your tracked progress: things you are happy for an employer to see | Public |
| **A private `security-notes` repository** | Raw notes, flashcard decks, lab command history, and anything that must not be published (solutions to active or graded content) | Private |

Structure the private notes one file per week, named consistently (for example `phase-0/week-02.md`), following the [weekly note template](../../templates/weekly-note.md). Future you will search these constantly, so name and organize them for searching, not just for writing once.

## Flashcards and spaced repetition

Memory fades on a predictable curve; spaced repetition beats that curve by showing you a card just before you would otherwise forget it, the mechanism explained in [Learning science](01-learning-science.md#spacing-distribute-practice-over-time).

| Practice | Detail |
|---|---|
| **Tool** | [Anki](https://apps.ankiweb.net/) (free desktop app) or any spaced-repetition tool |
| **Card design** | **Atomic**: one fact per card, phrased as a question. "What does Windows event ID 4625 mean?" rather than "Windows event logs" |
| **Source of cards** | Write them in your own words, from understanding; never copy-paste the source material directly |
| **Cadence** | Review daily, about 10 minutes; it is the single highest-return habit in this entire roadmap |
| **What goes on a card** | Commands, definitions, port numbers, framework items, and your own past mistakes |
| **What does not go on a card** | Skills such as exploiting or investigating; those belong in practice sessions, not flashcards, because a card tests recall, not the ability to perform a multi-step task |

## The check-yourself questions

Every week ends with questions to answer **from memory**, out loud or on paper, exactly the retrieval-practice principle from [Learning science](01-learning-science.md) applied as a weekly gate rather than a daily habit:

- Answer all of them cleanly: move on to next week.
- More than two shaky: repeat that week's R session and the weakest practice before advancing.

Do not lie to yourself here. The questions mirror what an interviewer or an exam will actually ask, and a false "yes, I know this" now is a worse outcome than an honest "not yet" and one more pass.

## Weekly and monthly review

| Cadence | What to do |
|---|---|
| **End of each week** | Answer the check-yourself questions, commit your deliverable, update [progress.md](../../roadmap/progress.md), and plan the next week using the [weekly review template](../../templates/weekly-review.md); this is the Sunday slot in [Study load modes](03-study-load-modes.md) |
| **End of each month** | Reread the month's writeups, re-answer a sample of old check-yourself questions, and refresh any topic that has gone stale with a few new flashcards |
| **End of each phase** | Confirm the phase's mastery checklist honestly before moving on; a checklist you tick without re-testing yourself defeats its own purpose |

## When you get stuck, and you will

Being stuck is the job, not a failure; it is the desirable-difficulty condition working as intended. A routine for it:

1. Re-read the task or error carefully. Most blocks are a missed detail, not a missing skill.
2. Enumerate again. On machines and investigations alike, most blocks come from missed enumeration, not from needing a cleverer technique.
3. Check your notes and flashcards for something similar you have already solved.
4. Search the specific error or symptom, not the whole problem.
5. After 45 minutes with no progress, take one hint, then continue and note what you missed for your flashcards.
6. If a whole topic is not landing, drop back a level (an easier machine, a more basic lab) and build back up, rather than forcing your way through a gap in the foundation.

## Protecting the habit

- A fixed weekly schedule beats motivation. Put the deep-practice block in your calendar as a real appointment, not an intention.
- Consistency over intensity: four steady hours a week for a year outperforms occasional marathons, which is also the direct lesson of the spacing research in [Learning science](01-learning-science.md).
- Track streaks in [progress.md](../../roadmap/progress.md); a visible chain of completed weeks is motivating in its own right.
- One rest day a week with no security work is part of the plan, not a lapse.
- During exam season, drop to the **Red** mode in [Study load modes](03-study-load-modes.md) rather than stopping entirely; a very light week is far easier to recover from than a full stop.

## Practice

1. Run one full week of this system exactly as described, including the check-yourself questions answered honestly from memory, and note which session felt easiest to skip; that is the one to protect most deliberately next week.
2. Build your first 15 flashcards from this week's material, following the atomic-card rule, and review them daily for two weeks before adding more.
3. Set up the two-repository structure (a public portfolio repository and a private notes repository) before your next deep-practice session, so you are not deciding where things go while also trying to focus on the work.
4. At the end of your first month, run the monthly review exactly as described and write down, honestly, what has already gone stale.

These support the [roadmap's weekly format](../../roadmap/README.md#the-weekly-session-format) and connect directly to [Learning science](01-learning-science.md).

## What to do with this

- [ ] Run the four weekly sessions, in format, for at least one full month before changing anything about the system.
- [ ] Build and maintain a flashcard deck using the atomic-card rule.
- [ ] Answer every week's check-yourself questions from memory, honestly, before moving on.
- [ ] Keep the two-repository structure from week one, not as an afterthought once the private repository is already a mess.
- [ ] Have a specific, time-boxed routine ready for the next time you get stuck, rather than improvising frustration in the moment.

## Key references

Dunlosky et al. (2013) · Roediger and Karpicke (2006). Full list in [References](../15-references.md).

<!-- navigation -->
[← Learning science](01-learning-science.md) · [Index](../00-start-here.md) · [Study load modes →](03-study-load-modes.md)
