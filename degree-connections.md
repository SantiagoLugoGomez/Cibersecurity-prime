# Degree connections

Most of what the degree teaches in the first semesters shows up in security work, often in places that are not obvious. This page maps each course to where it appears in the field and gives one or two exercises that reinforce both at the same time.

| Course | Where it shows up in security | Roadmap phase |
|---|---|---|
| Linear Algebra | Classical and post-quantum cryptography, cryptanalysis, machine-learning detection | 1, 2, 3 |
| Data Structures and Algorithms (Python) | Attack path analysis, detection engines, parsers, performance and denial-of-service bugs, every script you write | 0 to 4 |
| Differential Calculus | Brute-force and entropy math, rate-based detection, gradient-based machine learning | 1, 3 |
| Physics I | Side channels, wireless, fault injection, measurement discipline | 3 |
| Fundamentals of Cybersecurity | The vocabulary and principles behind Phase 1 | 1 |
| Networking (later in the degree) | Every attack and every detection crosses a network | 0, 2, 3 |

## Linear Algebra

**Where it appears**

- **Classical ciphers.** The Hill cipher is matrix multiplication modulo 26. Decryption needs the modular inverse of the key matrix, which exists only if its determinant is invertible mod 26. It is a standard first cryptanalysis exercise: with enough known plaintext, you can solve for the key with a linear system.
- **Linear structure breaks crypto.** Anything that is linear over GF(2), the field with two elements where addition is XOR, can be attacked with Gaussian elimination. Linear feedback shift registers and the internal state of Python's default random number generator (the Mersenne Twister) are both linear over GF(2), which is why their outputs can be predicted from enough observed values and why security code must use `secrets` instead of `random`.
- **Post-quantum cryptography.** ML-KEM, standardized by NIST in FIPS 203 in August 2024, is built on module lattices and the learning-with-errors problem: vectors, matrices and noise over a ring. Reading the standard is much easier once you are comfortable with matrix-vector products.
- **Lattice attacks.** Many CTF cryptography challenges are solved with lattice reduction (LLL), for example recovering RSA or ECDSA secrets from partial leaks. CryptoHack has a dedicated category.
- **Machine learning for detection.** Log events and network flows become feature vectors. Cosine similarity, projections and principal component analysis (PCA) are used to cluster behavior and flag anomalies.

**How to reinforce it**

- Implement the Hill cipher with NumPy: key generation that checks invertibility mod 26, encryption, decryption, and a known-plaintext attack that recovers a 2x2 key.
- Solve a system of linear equations over GF(2) in Python (rows as integers, XOR as addition) and use it to recover the state of a small LFSR from its output.
- Do the CryptoHack lattices introduction once your course covers bases and linear independence.
- Free support: [3Blue1Brown's Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) for geometric intuition and [MIT OCW 18.06SC](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) for depth.

## Data Structures and Algorithms (Python)

**Where it appears**

| Structure or idea | Security use |
|---|---|
| Hash tables | Fast lookups of indicators of compromise; also a target: hash-flooding attacks force collisions to degrade servers to quadratic time, which is why many languages randomize string hashing |
| Graphs, BFS and shortest paths | Active Directory attack path tools model users, groups and computers as a graph and search for the shortest path to high privilege; defenders use the same graph to find and cut those paths |
| Trees | Merkle trees protect integrity in Git and in Certificate Transparency logs; parsers build syntax trees, and parser confusion causes request smuggling and injection bugs |
| Tries and multi-pattern matching (Aho-Corasick) | Intrusion detection systems match thousands of signatures against traffic in one pass |
| Heaps and priority queues | Alert triage and scheduling by severity |
| Sorting and binary search | Log analysis, timeline building in forensics |
| Complexity analysis | Algorithmic complexity attacks, including regular expression denial of service (ReDoS), where a crafted input makes a backtracking regex run in exponential time |
| Recursion and backtracking | Fuzzers, parsers, and the reason ReDoS happens |

**How to reinforce it**

- Model a toy Active Directory as a Python dictionary graph (users, groups, computers, "can administer" edges) and write a BFS that finds the shortest path from a normal user to Domain Admins. Then remove one edge and show the path disappears. That is the core idea behind both attacking and hardening AD.
- Implement a trie that matches a list of indicator strings against a log file, and compare its speed with a naive loop over all indicators.
- Time the regex `^(a+)+$` in Python against strings of `a` followed by `!` of increasing length, plot the times, and explain the exponential growth. Run this only on your own machine.
- Write a script that merges two sorted log files into one timeline in O(n) time.

## Differential Calculus

**Where it appears**

- **Exponential growth and logarithms.** A password of length *n* over an alphabet of size *k* has *k^n* possibilities. Entropy in bits is *n* log2 *k*, which is why each extra character matters more than an extra character class. This is the math behind the NIST SP 800-63B-4 move to a 15-character minimum for single-factor passwords.
- **Approximations.** The birthday bound (collisions appear after about the square root of the space) comes from approximating 1 - *x* by *e^-x*, a first-order Taylor expansion. It explains why a 64-bit value collides after about 2^32 samples and why hash outputs are at least 256 bits.
- **Rates of change.** Detection rules often fire on a rate: failed logins per minute, bytes out per hour. Thinking in derivatives (how fast is this changing, is it accelerating) leads to better thresholds than fixed counts.
- **Optimization.** Machine-learning detection models are trained by gradient descent. Adversarial examples, which fool classifiers with tiny input changes, are found by following the gradient in the other direction.
- **Asymptotics.** Limits and growth rates are the language of algorithm complexity and of cryptographic security levels.

**How to reinforce it**

- Write a function that computes password entropy and the time to exhaust the space at a given guess rate, then plot entropy against length for different alphabets.
- Derive the birthday bound approximation by hand and check it with a Python simulation using truncated SHA-256 outputs of 24 to 32 bits.
- Using the failed login log from Phase 0, compute a moving rate per minute and compare a rate-based threshold with a fixed-count threshold.

## Physics I

**Where it appears**

- **Side channels.** Power consumption, electromagnetic emissions, sound and timing can leak secrets from hardware and software. Side-channel analysis treats them as physical signals.
- **Fault injection.** Glitching a chip's voltage or clock at the right moment can skip a security check. It is an applied physics problem in timing and energy.
- **Wireless.** Wi-Fi, Bluetooth and radio security depend on signal propagation, frequency and power.
- **Measurement discipline.** Error analysis and careful measurement transfer directly to timing attacks, benchmarking and incident timelines, where you must separate signal from noise.

**How to reinforce it**

- Measure the response time of a string comparison in Python that returns early on the first wrong character, over many trials, and show statistically that timing leaks how many characters are correct. Then switch to `hmac.compare_digest` and show the leak disappears.

## Fundamentals of Cybersecurity

Use the course as the theory track for [Phase 1](roadmap/phase-1-security-fundamentals/README.md). For each course unit, do the matching Phase 1 lab the same week. Concepts stick when you have both the definition from class and the experience of exploiting or defending the thing.

## Networking

The degree's networking course will revisit [Phase 0](roadmap/phase-0-foundations/README.md) in more depth. When it starts:

- Rebuild the four Phase 0 packet captures and add an analysis of each layer's headers.
- Configure the OPNsense router in the [home lab](homelab/README.md) with VLANs or separate segments, firewall rules and logging, and test the rules from Kali.
- Capture and explain an ARP exchange, a DHCP lease and a traceroute, and connect each to an attack it enables (ARP spoofing, rogue DHCP, network mapping) and its defense.
