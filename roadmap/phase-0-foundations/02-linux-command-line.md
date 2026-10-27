# Module 0.2: Linux and the command line (weeks 2-4)

Most servers, security tools and lab targets run Linux. By the end of this module the terminal should feel faster than a GUI for everyday work.

**Main resources:** [pwn.college Linux Luminarium](https://pwn.college/linux-luminarium), [OverTheWire Bandit](https://overthewire.org/wargames/bandit/), [The Linux Command Line](https://linuxcommand.org/tlcl.php) (free PDF). Chapter titles below are from the free edition; the 2026 third print edition renumbers some chapters, so use the titles.

**Environment:** an Ubuntu or Kali VM (see [homelab](../../homelab/README.md), stage 1), or WSL on Windows for the first two weeks.

## Week 2: Navigation, files and the shell

**Goal:** move around the file system, manipulate files and understand how the shell interprets what you type.

**R. Read and study (75 min)**
- The Linux Command Line: "What Is the Shell?", "Navigation", "Exploring the System", "Manipulating Files and Directories".
- Notes: the Filesystem Hierarchy Standard directories that matter in security (`/etc`, `/var/log`, `/home`, `/tmp`, `/proc`, `/usr/bin`, `/opt`) and what each holds.
- Flashcards: absolute vs relative paths, `.` and `..`, hidden files, `ls -la` output columns, wildcards `*`, `?`, `[ ]`.

**P. Guided practice (90 min)**
- Linux Luminarium: the "Hello Hackers", "Pondering Paths" and "Comprehending Commands" modules.
- Bandit levels 0 to 5. For each level, write in your notes the command that solved it and *why* it worked.

**D. Deep practice (3 h)**
- On your VM, without a GUI, recreate this tree and populate it with files using only the shell: `~/lab/{recon,loot,notes}/`, three files per folder, one hidden file per folder.
- Use `find` to list every file modified in the last 10 minutes, every hidden file, and every file larger than 1 KB.
- Explore `/etc` and `/var/log`: identify five configuration files and three log files, and write one line on what each is for.

**E. English (60 min)**
- Read the `man` page for `ls` and `find` (`man ls`, `man find`). Note how options are described ("lists", "prints", "excludes"). Write a 5-sentence explanation of `find` for a classmate.

**Check yourself**
1. What does `cd -` do? And `cd ~`?
2. How do you list hidden files, and why do they matter when searching a compromised machine?
3. What is the difference between `rm -r` and `rmdir`?
4. Where would you look for system-wide configuration, and where for logs?
5. What does the shell do with `*.txt` before the command runs?

**Deliverable:** `phase-0/week-02.md` in your notes repo with the Bandit 0-5 explanations and the `/etc` and `/var/log` inventory.

## Week 3: Redirection, permissions and users

**Goal:** chain commands, and understand Linux permissions well enough to spot a dangerous one.

**R. Read and study (75 min)**
- The Linux Command Line: "Working with Commands", "Redirection", "Seeing the World as the Shell Sees It", "Permissions".
- Notes: stdin, stdout and stderr; `>`, `>>`, `2>`, `|`; octal and symbolic permissions; setuid, setgid and the sticky bit; `umask`.
- Flashcards: what `chmod 4755`, `chmod 1777` and `chmod 600` mean; what `/etc/passwd` and `/etc/shadow` contain and who can read each.

**P. Guided practice (90 min)**
- Linux Luminarium: "Digesting Documentation", "File Globbing", "Practicing Piping" and "Perceiving Permissions".
- Bandit levels 6 to 12.

**D. Deep practice (3 h)**
- As root on your VM, create three users and two groups. Build a shared folder where group members can write but cannot delete each other's files (hint: sticky bit plus group ownership). Prove it works by logging in as each user.
- Find every setuid binary on the system: `find / -perm -4000 -type f 2>/dev/null`. Pick three and explain in your notes why each one needs setuid.
- Explain in one paragraph why a setuid binary that lets the user run arbitrary commands is a privilege escalation risk. Look up one of your binaries on [GTFOBins](https://gtfobins.github.io/) to see how defenders and testers document this class of misconfiguration.

**E. English (60 min)**
- Write a short "permissions policy" for your shared folder in English (who can read, write, delete, and why). Use *must*, *may* and *must not* precisely.

**Check yourself**
1. What is the difference between `>` and `>>`? How do you send only errors to a file?
2. Read this aloud and explain it: `-rwsr-xr-x 1 root root`.
3. Why can every user read `/etc/passwd` but not `/etc/shadow`?
4. What does the sticky bit do on a directory such as `/tmp`?
5. Why is a world-writable script that runs as root dangerous?

**Deliverable:** the shared-folder setup documented step by step, plus your setuid inventory with explanations.

## Week 4: Processes, services, packages, SSH and text processing

**Goal:** manage what runs on a system, administer it remotely and process text fast.

**R. Read and study (75 min)**
- The Linux Command Line: "Processes", "The Environment", "Package Management", "Networking" (the SSH section), "Regular Expressions", "Text Processing".
- Notes: process states, signals (`SIGTERM` vs `SIGKILL`), `systemctl` and unit files, `journalctl`, environment variables and `PATH`, public-key authentication.
- Flashcards: `ps aux` columns, `kill -9` vs `kill -15`, `grep -E`, `cut`, `sort | uniq -c`, `sed 's/a/b/g'`, `awk '{print $1}'`.

**P. Guided practice (90 min)**
- Linux Luminarium: "Processes and Jobs", "Untangling Users", "Chaining Commands", "Pondering PATH" and the remaining modules.
- Bandit levels 13 to 20.

**D. Deep practice (3 h)**
- Set up an SSH server on your VM. Configure key-only login: disable password authentication and root login in `sshd_config`, restart the service and confirm with `ssh -v` from your host.
- Generate failed logins against your own VM (wrong passwords from your host), then use `grep`, `awk`, `sort` and `uniq -c` on `/var/log/auth.log` (or `journalctl -u ssh`) to count attempts per source IP. Compare the result with [`failed_logins.py`](exercises/failed_logins.py).
- Write a systemd unit that runs a small script every boot, enable it, reboot and confirm it ran with `journalctl`.

**E. English (60 min)**
- Write a 200-word "SSH hardening checklist" in English for a teammate, in imperative voice ("Disable password authentication.").

**Check yourself**
1. How do you find which process is listening on port 22 and which user owns it?
2. What is the difference between `systemctl stop`, `disable` and `mask`?
3. Why is key-based SSH authentication stronger than passwords?
4. What happens if a directory you control appears early in root's `PATH`?
5. Write from memory a pipeline that prints the ten most frequent IPs in a log.

**Deliverable:** your hardened `sshd_config` diff, the log-analysis pipeline, and Bandit 13-20 notes.

**Stretch:** finish Bandit up to level 25 and read "Searching for Files" and "Archiving and Backup".
