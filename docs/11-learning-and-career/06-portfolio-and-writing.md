# Portfolio and writing

> [!TIP]
> **In short:** in a field this hands-on, a public portfolio of real, documented work outweighs a CV line almost every time a technical reviewer is involved. A portfolio is built from the same writeups and projects this roadmap already asks you to produce every week; the only extra work is **curating and writing them well enough that a stranger can follow them**, and **checking, before publishing, what each one actually reveals** about you, an employer, or a target you tested. This page is about doing that curation and that check well; the specific list of recommended portfolio projects and the bug bounty platforms to use lives in [Phase 4 of the roadmap](../../roadmap/phase-4-professional/README.md#portfolio-projects), which this page does not repeat.

## Why a portfolio matters more here than in most fields

Security hiring, especially for technical roles, is unusually skeptical of credentials alone, for a good reason: a certification or a degree can be earned without ever having actually broken, defended, or investigated a real system end to end. A portfolio answers the question a resume cannot: **can this person actually do the work, and can they explain what they did clearly enough for someone else to trust the result?** This repository, kept public and current, is itself the portfolio this roadmap builds toward, one writeup and one project at a time.

## What belongs in the portfolio, and what does not

| Belongs here (public) | Stays in your private notes |
|---|---|
| A finished, reviewed writeup of a machine, a CTF challenge, or a lab exercise | Raw command history and half-finished notes from getting there |
| A completed project with a README, a diagram, and an explanation of what it demonstrates | Solutions to active or currently graded challenges (see the etiquette note in [Community](07-community.md)) |
| A tool you built and documented for others to use | Credentials, API keys, or anything else that must never be committed to any repository, public or private, as covered in [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md#secrets-management) |
| A GRC artifact (a policy set, a risk register, a framework mapping) built for a realistic, clearly fictional scenario | Real data, real client names, or real findings from any engagement you were not explicitly authorized to publish |

The two-repository structure already described in [the study system](02-the-study-system.md#notes-the-two-repository-system) exists specifically to make this split automatic rather than a judgment call made under pressure every time you finish something.

## What makes a writeup actually good

A writeup is not a transcript of everything you typed; it is a **report** written for a reader who was not in the room, exactly the standard already set in [the writeup template](../../writeups/TEMPLATE.md) and the finding structure in [Penetration testing methodology](../06-offensive-security/01-penetration-testing-methodology.md#anatomy-of-a-finding).

| Quality | What it looks like |
|---|---|
| **A clear methodology, not just a solution** | Show *how* you found the path, including the dead ends that taught you something, not only the sequence of commands that worked |
| **Explained reasoning, not narrated keystrokes** | "This suggested the service might be vulnerable to X, so I checked Y" beats a bare list of commands with no connecting logic |
| **Evidence, not just claims** | Screenshots, command output, and specific artifact references that let a skeptical reader verify what you are describing |
| **An honest account of what did not work** | What you tried and ruled out is often as informative to a reader as what succeeded, and it is more honest than presenting only the clean final path |
| **A clean structure, used consistently** | The same template every time means a reader who liked your first writeup knows exactly where to find what they want in your next one |
| **Concise, correct English** | The specific standard and the common mistakes Spanish speakers make are covered in [writing-reports.md](../../english/writing-reports.md); technical writing quality is itself part of what a portfolio demonstrates |

A writeup that explains your reasoning clearly is also, not incidentally, direct practice for the technical interview, where you will be asked to explain your reasoning out loud under real-time pressure; writing it down first is rehearsal.

## Before you publish: an OSINT self-audit

Publishing a portfolio means applying, to yourself, the same information-gathering discipline covered in [Reconnaissance and enumeration](../06-offensive-security/02-reconnaissance-and-enumeration.md): assume a stranger, including a future employer, a current employer, or someone with less friendly intentions, will read everything you publish, and check what it actually reveals before it goes live, not after.

| Check | Why |
|---|---|
| **Does this reveal anything about a real employer, client, or system I was not explicitly authorized to disclose?** | Even an anonymized description can be identifiable from enough detail; when in doubt, ask before publishing, or build a fictional equivalent instead |
| **Does this contain a flag, solution, or answer to an active, currently gradable challenge?** | Publishing live CTF flags or graded coursework solutions is a community and academic integrity violation, not just a bad look; wait until a challenge is retired, or write generically about the technique instead of the specific answer |
| **Does this expose a credential, key, internal hostname, or personal data that slipped into a screenshot or log excerpt?** | Redact before publishing, every time, even in your own lab work; the habit of checking matters more than any single instance |
| **Does this reasonably look like it targets a real organization without authorization?** | Keep offensive-technique writeups clearly scoped to your own lab, a training platform, or an authorized engagement, consistent with [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md) |
| **Would I be comfortable with this being the first thing a recruiter or a future colleague reads about me?** | A portfolio is a long-lived, searchable public record; write accordingly |

This is not paranoia; it is the same professional discipline a working security practitioner applies to their own public footprint every day, and building the habit now, while the stakes of a mistake are lower, pays off for the rest of your career.

## Presenting the portfolio beyond the repository itself

| Surface | What to do |
|---|---|
| **This repository's README** | Keep it current as the front door: a short, honest summary of where you are, what you have built, and links to your best work, not an exhaustive list of everything |
| **A CV** | Link directly to specific writeups or projects relevant to the role, rather than only a bare repository URL a reader may never actually open |
| **LinkedIn or an equivalent professional profile** | A short post when you finish a significant project or pass a certification, linking back to the actual writeup, builds visibility over time far better than a resume update nobody sees until you apply |
| **A technical interview** | Bring your own portfolio into the conversation proactively ("I ran into exactly this pattern when I was working on..."); it is far stronger evidence than describing a skill in the abstract |

## Writing in English, deliberately

Every piece of portfolio writing is also English practice, and the reverse is equally true: the [English track](../../english/README.md) exists because most of the field's hiring, documentation, and professional community operates in English, and a portfolio written in clear, correct technical English reaches a global audience a Spanish-only portfolio does not. Write your best, most significant work in English first; a Spanish version, if you want one, is easy to add afterward, but writing the reverse direction and hoping to translate up to professional quality later rarely works as well.

## Practice

1. Take your single best completed lab or CTF solution so far and rewrite it as a formal writeup using the template, applying every quality criterion above, specifically adding the reasoning and the dead ends you did not originally bother to document.
2. Run the OSINT self-audit checklist against every piece of your current portfolio, including anything already published, and fix or remove whatever fails a check.
3. Rewrite your repository's README as a short, honest front door, linking to your three best pieces of work rather than listing everything.
4. Write one short professional-network post about a recent project, linking back to the full writeup, and notice how it feels different from writing the writeup itself.

These support [Module 4 of the roadmap](../../roadmap/phase-4-professional/README.md#portfolio-projects) and the [English track](../../english/writing-reports.md).

## What to do with this

- [ ] Keep your two-repository split (public portfolio, private notes) enforced on every piece of work, not just the finished ones.
- [ ] Apply the quality checklist to every writeup before publishing it, not only your best ones.
- [ ] Run the OSINT self-audit on every single publish, as a fixed habit, not an occasional afterthought.
- [ ] Keep your repository's README current as a short, honest front door to your best work.
- [ ] Write your most significant work in English first.

## Key references

OWASP Web Security Testing Guide (report-writing appendix) · SANS report-writing guidance. Full list in [References](../15-references.md).

<!-- navigation -->
[← Certification strategy](05-certification-strategy.md) · [Index](../00-start-here.md) · [Community →](07-community.md)
