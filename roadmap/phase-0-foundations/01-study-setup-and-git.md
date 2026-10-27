# Module 0.1: Study setup and Git (week 1)

Set up the tools you will use every day for the next four years, and learn Git well enough to manage this repo through branches and pull requests.

## Week 1: Your workstation, your notes and Git

**Goal:** a working study environment, a private notes repo, and the core Git workflow in your hands.

**R. Read and study (75 min)**
- [study-system.md](../../study-system.md) in full. It explains how every session in this roadmap works.
- [Pro Git](https://git-scm.com/book/en/v2), chapter 1 (Getting Started) and chapter 2 (Git Basics).
- Notes to write: what a commit, a branch, `HEAD`, the staging area and a remote are, each in one or two sentences of your own.
- Flashcards: one card per Git concept above, plus `git status`, `git diff`, `git log --oneline --graph`.

**P. Guided practice (90 min)**
1. Install Git, configure `user.name` and `user.email`, and create an SSH key with `ssh-keygen -t ed25519`. Add the public key to GitHub.
2. Complete the "Introduction Sequence" and "Ramping Up" levels in [Learn Git Branching](https://learngitbranching.js.org/).
3. Clone this repo, create a branch named `progress/week-01`, tick the first boxes in [progress.md](../../progress.md), commit, push and open a pull request against your own `main`.

**D. Deep practice (3 h)**
- Create a **private** repository called `security-notes`. This is where your raw notes, solutions and anything you must not publish will live. Structure it like this:

  ```
  security-notes/
    phase-0/      one Markdown file per week
    cards/        flashcard exports
    labs/         lab configs and command history
    private/      solutions to active or graded content
  ```

- Install a Markdown editor ([Obsidian](https://obsidian.md/license) is free for all uses; any editor works) and a flashcard app ([Anki](https://apps.ankiweb.net/) desktop is free).
- Pro Git chapter 3 (Git Branching): create two branches in `security-notes`, change the same line in both, merge them, and resolve the conflict by hand. Write down exactly what Git showed you.

**E. English (60 min)**
- Read the GitHub Docs page [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). List ten verbs it uses for collaboration (propose, review, merge, ...).
- Write the description of your week 1 pull request in English: what changed and why, in four sentences.

**Check yourself**
1. What is the difference between `git add` and `git commit`?
2. What happens to `HEAD` when you check out a different branch?
3. When does a merge conflict happen, and what do the `<<<<<<<` and `>>>>>>>` markers mean?
4. Why must solutions to active Hack The Box machines never go in this public repo?
5. What is the difference between your public portfolio repo and your private notes repo?

**Deliverable:** a merged pull request in this repo that updates `progress.md`, and a private `security-notes` repo with the folder structure above.

**Stretch:** Pro Git chapter 7.1 to 7.3 (revision selection, interactive staging, stashing).
