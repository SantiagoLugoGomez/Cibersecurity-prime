# Module 0.5: Python for security (weeks 10-12)

Python is the lingua franca of security tooling. This module assumes your degree's Data Structures and Algorithms course gives you the language basics, and focuses on the standard library and patterns you will use to automate security tasks.

**Main resources:** your DSA course, [Automate the Boring Stuff with Python, 3rd edition](https://automatetheboringstuff.com/) (free online), the [official Python docs](https://docs.python.org/3/) for `socket`, `ssl`, `hashlib`, `re`, `argparse`, `subprocess` and `requests`.

## Week 10: Files, text, regex and the CLI

**Goal:** process files and text, parse with regular expressions, and build clean command-line tools.

**R. Read and study (75 min)**
- Automate the Boring Stuff: "Reading and Writing Files", "Organizing Files", "Pattern Matching with Regular Expressions".
- Python docs: `argparse` tutorial, `re` how-to (first half).
- Notes: opening files with context managers, reading large files line by line, raw strings, the regex metacharacters you will use most (`\d`, `\w`, `\s`, `+`, `*`, `?`, groups, anchors).
- Flashcards: `re.search` vs `re.match` vs `re.findall`; capturing groups; `argparse` positional vs optional arguments.

**P. Guided practice (90 min)**
- Rework [`failed_logins.py`](exercises/failed_logins.py): add `--since` to filter by timestamp and `--json` for machine-readable output, as the exercise README asks.
- Write `extract-iocs.py`: given a text file, extract all IPv4 addresses, domains and URLs with regex and print each unique one with a count.

**D. Deep practice (3 h)**
- Build `logparse.py`, a small log-analysis tool: it reads an SSH or web log, and with subcommands (`argparse` subparsers) reports top IPs, top targeted users or URLs, and a timeline histogram per hour. Handle missing files and malformed lines without crashing.
- Test it on the sample log and on logs you generate in your lab.

**E. English (60 min)**
- Read the `argparse` tutorial's examples. Write `--help` output text for `logparse.py` in clear English, then implement it.

**Check yourself**
1. Why use a `with open(...)` block instead of `open` and `close`?
2. Write a regex that matches an IPv4 address (approximately) and explain its parts.
3. What is the difference between `re.findall` and `re.finditer`?
4. How do you read a 2 GB log without loading it all into memory?
5. How do `argparse` subcommands work?

**Deliverable:** the upgraded `failed_logins.py`, `extract-iocs.py` and `logparse.py`, committed with a README.

## Week 11: Networking and the web in Python

**Goal:** script network and HTTP interactions, the core of most security tooling.

**R. Read and study (75 min)**
- Automate the Boring Stuff: "Making Web Requests with the requests Module" and "Downloading from the Web".
- Python docs: `socket` (the intro and the TCP example), `ssl` (client examples), `http.client` basics.
- Notes: sockets vs higher-level libraries; timeouts; why you validate TLS certificates; sending and parsing HTTP with `requests`.
- Flashcards: `socket.create_connection`, `ssl.create_default_context`, `requests.get` vs `.post`, response `.status_code`, `.headers`, `.json()`.

**P. Guided practice (90 min)**
- Rework [`port_check.py`](exercises/port_check.py) to scan concurrently with `concurrent.futures.ThreadPoolExecutor`, and time it against the serial version on a lab /24.
- Write `banner-grab.py`: connect to a host/port, send a minimal request and print the service banner.

**D. Deep practice (3 h)**
- Build `web-recon.py` for authorized targets only: given a base URL in your lab, it requests the page, lists the security headers (reuse [`http_headers.py`](exercises/http_headers.py)), finds linked pages on the same host, and checks `/robots.txt` and `/.well-known/security.txt`. Respect a configurable rate limit.
- Run it only against Juice Shop or DVWA in your own lab.

**E. English (60 min)**
- Read the `requests` library quickstart. Write three sentences on the difference between a GET and a POST, using the correct verbs.

**Check yourself**
1. Why set a timeout on every socket and HTTP request?
2. What does `ssl.create_default_context()` give you that a raw socket does not?
3. When is `requests` the right tool and when do you need raw `socket`?
4. Why should a scanner respect a rate limit, even in a lab?
5. How does a thread pool speed up a port scan, and what is the risk of too many threads?

**Deliverable:** the concurrent `port_check.py` with timing comparison, `banner-grab.py` and `web-recon.py`.

## Week 12: Crypto, subprocess and packaging a tool

**Goal:** use cryptographic primitives correctly from Python, run external tools, and package a script others can use.

**R. Read and study (75 min)**
- Python docs: `hashlib`, `hmac`, `secrets`, `subprocess` (the `run` function and security notes).
- Notes: why `secrets` and not `random` for anything security-related; hashing vs HMAC; the danger of `shell=True` in `subprocess`; virtual environments.
- Flashcards: `hashlib.sha256`, `hmac.compare_digest` (and why constant-time), `secrets.token_hex`, `subprocess.run([...], capture_output=True)`, why `shell=True` is risky.

**P. Guided practice (90 min)**
- Write `hashid-check.py`: given a file, print its MD5, SHA-1 and SHA-256, and optionally compare against an expected hash using `hmac.compare_digest`.
- Write a wrapper that runs `nmap` via `subprocess` (no `shell=True`), parses the output and prints a clean table. Run against your lab only.

**D. Deep practice (3 h)**
- Take your best tool so far (`logparse.py` or `web-recon.py`) and package it properly: a virtual environment, a `requirements.txt` or `pyproject.toml`, a `--version` flag, a real README with examples, and a `-I`-safe entry point. Install it fresh in a new venv to prove it works.
- Run a linter (`ruff` or `flake8`) and fix every issue.

**E. English (60 min)**
- Write the project README in English: purpose, install, usage, examples, limitations, and a short "security notes" section. This is portfolio material.

**Check yourself**
1. Why must you use `secrets` instead of `random` to generate a token?
2. What is the difference between a hash and an HMAC, and when do you need each?
3. Why is `subprocess.run(cmd, shell=True)` with user input dangerous?
4. Why compare secrets with `hmac.compare_digest` instead of `==`?
5. What does a virtual environment isolate, and why does it matter?

**Deliverable:** one packaged, linted, documented tool installed from a clean venv, committed to your notes repo and ready to feature in your portfolio.

**Stretch:** read the [pwntools](https://docs.pwntools.com/) intro; you will use it in Phase 2 for binary challenges.
