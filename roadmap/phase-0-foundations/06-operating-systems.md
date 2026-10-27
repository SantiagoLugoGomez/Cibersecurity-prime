# Module 0.6: How operating systems work (weeks 13-15)

You cannot exploit or defend what you do not understand. This module builds a mental model of what an operating system actually does, which underlies privilege escalation, malware, forensics and detection.

**Main resources:** [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) (free, "OSTEP"), the [Linux man-pages project](https://man7.org/linux/man-pages/) (sections 2, 5, 7), your own VMs for observation.

## Week 13: Processes, system calls and the kernel boundary

**Goal:** understand what a process is, how it is created, and how user space asks the kernel for things.

**R. Read and study (75 min)**
- OSTEP: "A Dialogue on Virtualization", "The Abstraction: The Process", "Interlude: Process API".
- Man pages: `fork(2)`, `execve(2)`, `wait(2)`, intro to `syscalls(2)`.
- Notes: the process life cycle; `fork` then `execve`; the difference between user mode and kernel mode; what a system call is and why it is the security boundary; file descriptors.
- Flashcards: `fork` vs `exec`, process states, what a PID and PPID are, what a system call does.

**P. Guided practice (90 min)**
- `strace -f ls` and `strace -f curl https://example.com` on a VM. Identify `execve`, `openat`, `read`, `write`, `connect`. Write what each does.
- Inspect a running process: `cat /proc/<pid>/status`, `/proc/<pid>/maps`, `/proc/<pid>/fd/`. Explain what you see.

**D. Deep practice (3 h)**
- Write a tiny C program (or Python with `os.fork`) that forks a child, has the child `exec` another program, and the parent `wait` for it. Run it under `strace` and map every syscall to a line of your code.
- Then write a page in your notes: "How a shell runs a command", tracing `fork`, `execve`, `wait` and file descriptors for input/output redirection. This directly explains how reverse shells and command injection work later.

**E. English (60 min)**
- Read `man 2 execve` (the DESCRIPTION). Rewrite it in your own plain English in 100 words.

**Check yourself**
1. What is the difference between `fork` and `execve`, and why are they separate?
2. What makes a system call different from a normal function call?
3. What is in `/proc/<pid>/maps`, and why is it useful in forensics?
4. How does a shell redirect a command's output to a file, in terms of file descriptors?
5. What is the boundary between user mode and kernel mode protecting?

**Deliverable:** the fork/exec program with its annotated strace, and the "how a shell runs a command" note.

## Week 14: Memory, scheduling and concurrency

**Goal:** understand virtual memory and concurrency well enough to grasp memory-corruption bugs and race conditions later.

**R. Read and study (75 min)**
- OSTEP: "Address Spaces", "Memory API", "Address Translation" (concept level), and "Concurrency: An Introduction" and "Interlude: Thread API".
- Notes: virtual vs physical memory and why each process sees its own address space; the stack vs the heap; what a segmentation fault is; what a race condition and a deadlock are; why shared mutable state needs locks.
- Flashcards: stack vs heap, virtual address space, what causes a segfault, race condition, mutex.

**P. Guided practice (90 min)**
- Write a program with two threads incrementing a shared counter without a lock; show the wrong result; add a lock; show it fixed. Explain the race.
- Trigger and read a segmentation fault: write a program that dereferences a null or out-of-bounds pointer, run it, and inspect the crash (and a core dump if enabled).

**D. Deep practice (3 h)**
- Study a time-of-check-to-time-of-use (TOCTOU) race conceptually: write a script where one process checks a file then acts on it, and another process swaps the file in between, and show how the check can be defeated. Explain in your notes why setuid programs that do this are exploitable.
- Write a note connecting this module to the degree's DSA course ([degree-connections.md](../../degree-connections.md)): stack, heap, and why a buffer overflow corrupts adjacent memory.

**E. English (60 min)**
- Read the Wikipedia or OSTEP description of a race condition. Explain, out loud and recorded, what a race condition is and give one security example, in two minutes.

**Check yourself**
1. Why does each process have its own virtual address space?
2. What is the difference between the stack and the heap?
3. What is a race condition, and how is TOCTOU one?
4. Why does concurrent access to shared state need a lock?
5. What is a segmentation fault, in terms of memory access?

**Deliverable:** the threading race demo (broken and fixed), the segfault demo, and the TOCTOU note.

## Week 15: File systems, permissions model and OS security

**Goal:** understand how data is stored and how the OS enforces access, the basis of forensics and hardening.

**R. Read and study (75 min)**
- OSTEP: "File System Implementation" (concept level), "Interlude: Files and Directories".
- Man pages: `inode(7)`, `credentials(7)`, `capabilities(7)`.
- Notes: inodes, hard vs symbolic links, what "deleting" a file really does (and why recovery is possible); the real/effective/saved UID model; Linux capabilities as finer-grained than root; mount options like `noexec` and `nosuid`.
- Flashcards: inode, hard link vs symlink, real vs effective UID, one capability (e.g. `CAP_NET_RAW`), what `noexec` does.

**P. Guided practice (90 min)**
- Create a file, make a hard link and a symlink to it, delete the original, and observe what survives and why. Inspect inodes with `ls -i` and `stat`.
- Find files with capabilities set: `getcap -r / 2>/dev/null`. Explain why a capability can be a privilege-escalation path, just like setuid.

**D. Deep practice (3 h)**
- Forensics primer: create a file in a small disk image or a loopback filesystem, delete it, and recover it with a tool such as `extundelete` or by carving with `strings`/`photorec` in your lab. Write up what "deleted" means at the filesystem level.
- Connect this to incident response: why an attacker who deletes logs may not actually erase them, and why responders image disks.

**E. English (60 min)**
- Read `man 7 capabilities` (the overview). Summarize in 120 words why capabilities are safer than "run as root".

**Check yourself**
1. What is an inode, and what metadata does it hold?
2. What is the difference between a hard link and a symbolic link?
3. What really happens when you delete a file, and why can it be recovered?
4. What is the difference between the real and effective UID of a process?
5. How does a Linux capability differ from full root, and why does that matter for least privilege?

**Deliverable:** the links/inode experiment, your capability inventory with explanations, and the file-recovery writeup.

**Stretch:** OSTEP "Paging" chapters, and read how AppArmor or SELinux adds mandatory access control on top of the permission model.
