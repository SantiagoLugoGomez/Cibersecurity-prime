# Module 0.3: Bash scripting (week 5)

Security work is full of small repetitive tasks: parsing output, checking many hosts, collecting evidence. Bash is the fastest way to automate them on any Linux machine.

## Week 5: Scripts that save you time

**Goal:** write readable Bash scripts with arguments, conditions, loops, functions and error handling.

**R. Read and study (75 min)**
- The Linux Command Line: "Writing Your First Script", "Starting a Project", "Flow Control: Branching with if", "Reading Keyboard Input", "Flow Control: Looping with while/until", "Positional Parameters", "Flow Control: Looping with for".
- Notes: the shebang line, exit codes and `$?`, `[[ ]]` vs `[ ]`, quoting rules (why `"$var"` and not `$var`), `set -euo pipefail`, functions and `local`.
- Flashcards: `$0`, `$1`, `$#`, `$@`; `-f`, `-d`, `-z`, `-n` tests; `&&` and `||`.

**P. Guided practice (90 min)**
- Write these four scripts, each under 40 lines, with a usage message when arguments are missing:
  1. `backup-notes.sh <dir>`: creates a dated `.tar.gz` of a directory and keeps only the five newest.
  2. `ping-sweep.sh <prefix>`: pings `.1` to `.254` of a `/24` in your lab once each and prints the hosts that answered.
  3. `log-summary.sh <file>`: prints line count, first and last timestamp, and top five source IPs.
  4. `check-tools.sh`: checks that `nmap`, `curl`, `jq`, `python3` and `git` are installed and prints what is missing.
- Run [ShellCheck](https://www.shellcheck.net/) on each script and fix every warning.

**D. Deep practice (3 h)**
- Build `host-report.sh`, a script you run on any Linux VM that writes a Markdown report with: hostname and OS version, users with a login shell, members of `sudo` or `wheel`, listening TCP ports with their processes, setuid files outside `/usr`, cron jobs for all users, and the last ten logins.
- Run it on two different VMs and compare the reports. This is the core of what both an administrator auditing a server and an incident responder triaging one do first.
- Commit it to your notes repo with a README explaining every section.

**E. English (60 min)**
- Write the README for `host-report.sh` in English: purpose, usage, sample output, limitations. Use the [writing guide](../../english/writing-reports.md) style rules.

**Check yourself**
1. Why does `set -euo pipefail` make scripts safer, and when can it surprise you?
2. What breaks if you write `rm $file` instead of `rm "$file"` and the name contains a space?
3. How do you make a script fail with a useful message when an argument is missing?
4. What is the difference between `$@` and `$*` inside quotes?
5. Why is the "listening ports" section of `host-report.sh` useful during an incident?

**Deliverable:** the four practice scripts and `host-report.sh`, all passing ShellCheck, committed to your notes repo.

**Stretch:** "Strings and Numbers" and "Arrays" from The Linux Command Line; add a `--json` option to `host-report.sh` using `jq`.
