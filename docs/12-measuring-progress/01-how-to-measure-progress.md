# How to measure progress

> [!TIP]
> **In short:** a checked box in [progress.md](../../roadmap/progress.md) tells you that you did the work, not that the work actually built durable skill. Real progress has to be measured in ways that are hard to fool yourself with: can you explain the concept from memory, cold, weeks later; can you apply it to a problem that looks different from the one you practiced on; would an honest, skeptical interviewer be convinced? This page gives you that second, harder layer of measurement, on top of the simple completion tracking the roadmap already does.

## Why completion is not the same as competence

Finishing a week's sessions proves you spent the time; it does not prove the time produced lasting skill, because, as [Learning science](../11-learning-and-career/01-learning-science.md) explains, the methods that *feel* most productive (rereading, following a walkthrough step by step) are often the ones that build the least durable retention. A checklist that only tracks completion will happily let you check every box while quietly accumulating a gap between what you can recognize and what you can actually do unaided, a gap that stays invisible until an interview or a real incident exposes it.

## The calibration problem

**Calibration** is how well your own confidence matches your actual ability. Two failure modes are both common and both dangerous in different ways:

| Failure mode | What it looks like | Why it is dangerous |
|---|---|---|
| **Overconfidence** | "I understand this" after one read-through, with no retrieval test | You stop reviewing material you have not actually retained, and the gap surfaces at the worst possible moment: an interview, an exam, a real incident |
| **Underconfidence** | Genuine competence paired with persistent doubt, often worse for people newer to a field who can see how much they do not yet know | You avoid opportunities (an interview, a bug bounty submission, a conference talk) you are actually ready for |

Both are corrected the same way: with **objective, retrieval-based tests** of what you actually know, rather than a subjective feeling in either direction. The check-yourself questions in [the study system](../11-learning-and-career/02-the-study-system.md#the-check-yourself-questions) exist specifically to replace "do I feel like I know this?" with "can I actually produce this, cold, right now?"

## Signals that measure something real

| Signal | What it actually tells you | How to generate it |
|---|---|---|
| **Cold recall, days or weeks later** | Whether a concept actually stuck, as opposed to being fluent only immediately after studying it | Re-answer old check-yourself questions, unprompted, during your monthly review |
| **Explaining it to someone else** | Whether your understanding is deep enough to survive someone else's questions, not just your own | Explain a concept to a study partner, a classmate, or out loud to an empty room, and notice exactly where you stumble |
| **Applying it to an unfamiliar problem** | Whether you learned the underlying idea or just the specific example | A new machine, an unfamiliar codebase, or a CTF category you have not drilled specifically |
| **Teaching it in writing** | Whether you can organize and sequence the idea clearly for a reader who was not there | A writeup, as described in [Portfolio and writing](../11-learning-and-career/06-portfolio-and-writing.md) |
| **A timed, simulated interview question** | Whether you can produce a correct, clear answer under the mild pressure a real interview will add | Have a study partner (or an AI tool, used as a quizzing partner rather than a source of answers) ask you a technical question and time your response |
| **A completed, working build or exploit from scratch** | Whether you can execute a full chain of reasoning end to end without a walkthrough | The deep-practice sessions in [the study system](../11-learning-and-career/02-the-study-system.md), specifically done "from the week's method, not from a walkthrough" |

**Practical implication:** if a measurement can be satisfied just by re-reading your own notes with the material open, it is measuring recognition, not the competence you actually need. Prefer signals that would be hard or impossible to fake without the real skill underneath them.

## Tracking progress across different timescales

| Timescale | What to track | Where |
|---|---|---|
| **Weekly** | Sessions completed, check-yourself questions answered from memory, the deliverable committed | [progress.md](../../roadmap/progress.md), as already described in [the study system](../11-learning-and-career/02-the-study-system.md) |
| **Monthly** | Cold recall of a sample of older check-yourself questions; which topics have gone stale and need a flashcard refresh | The monthly review already described in [the study system](../11-learning-and-career/02-the-study-system.md#weekly-and-monthly-review) |
| **Per phase** | The phase's mastery checklist, re-tested honestly, not just re-read and assumed | Each phase's own README in [the roadmap](../../roadmap/README.md) |
| **Per year or per major milestone** | Portfolio growth (new projects, writeups, a certification, a bug bounty result), and a genuine, honest self-assessment against where you were a year earlier | A yearly review you write yourself, kept alongside your portfolio |

## A simple self-interview, run periodically

Twice a semester, run this short, honest exercise, ideally written down so you can compare it to the previous time you ran it:

1. Pick three topics from the last few months at random, not your favorites.
2. For each, write, from memory, a two- or three-sentence explanation good enough that a classmate unfamiliar with the topic would understand it.
3. Check your explanation against the actual source material. Note every gap or mistake honestly.
4. Ask yourself: if this came up in a technical interview right now, would my answer have been convincing? If not, what specifically was missing?
5. Turn every gap you found into new flashcards or a scheduled re-study session, immediately, while it is fresh.

This single exercise, run consistently, catches the overconfidence failure mode before it becomes a bad moment in a real interview or engagement.

## Where portfolio evidence fits

A portfolio, built as described in [Portfolio and writing](../11-learning-and-career/06-portfolio-and-writing.md), is itself a progress measurement, and often the most externally convincing one: a growing, genuinely understood body of writeups and projects is harder to produce by accident than a checklist of completed weeks, precisely because writing a clear explanation for a stranger exposes gaps that a private checklist does not. If you cannot write a clear writeup about something you supposedly finished, that is itself a signal the underlying skill is not yet where the checklist suggests it is.

## When the signals disagree with each other

Sometimes you will feel confident but fail a cold-recall test, or feel shaky but explain something perfectly to a study partner. Trust the **objective, retrieval-based signal** over the subjective feeling every time; the entire point of this page is that feelings about your own competence are exactly the thing that needs independent verification, not the thing to verify against.

## Practice

1. Run the self-interview exercise above right now, on three topics from the last month, and write down what it reveals honestly, including anything uncomfortable.
2. Pick one topic you are certain you already understand well, and try to explain it, out loud, to someone with no security background, timing yourself; note exactly where you hesitate or simplify past something you cannot actually explain.
3. Compare your subjective confidence rating (1 to 10) on five recent topics against your actual performance re-answering their check-yourself questions cold, and note the size and direction of any gap.
4. Build a standing, recurring calendar reminder for the monthly and per-phase reviews, so they happen on schedule rather than only when you happen to remember.

These support [the study system](../11-learning-and-career/02-the-study-system.md) and connect to [Troubleshooting](02-troubleshooting.md) for what to do when a measurement reveals a real gap.

## What to do with this

- [ ] Explain the difference between completion tracking and competence measurement clearly enough to catch yourself relying only on the first.
- [ ] Run the self-interview exercise at least twice this semester, on randomly chosen topics, not your favorites.
- [ ] Track your own calibration (confidence versus actual cold-recall performance) at least once, and notice which direction you tend to err.
- [ ] Treat a gap revealed by an honest measurement as useful information, not a reason for discouragement, and act on it immediately.
- [ ] Use your portfolio itself as evidence, checking whether you can actually explain what it claims you did.

## Key references

Dunlosky et al. (2013) · Roediger and Karpicke (2006). Full list in [References](../15-references.md).
