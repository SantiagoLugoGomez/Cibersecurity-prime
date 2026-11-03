# Security principles

> [!TIP]
> **In short:** a handful of design principles, most of them written down in 1975, explain a surprising share of real vulnerabilities. Default to **deny**, check **every** access, give each party the **least** privilege that works, keep mechanisms **small**, do not rely on **secrecy of the design**, and plan for the day one layer **fails**. When you review a design or a finding, ask which principle it breaks. The answer usually names the fix.

## Where the principles come from

In 1975 Jerome Saltzer and Michael Schroeder published *The Protection of Information in Computer Systems*, which listed design principles for protection mechanisms in multi-user operating systems (Saltzer and Schroeder, 1975). **●●●** The paper is about timesharing computers, yet the list has outlasted every technology it was written for, because it describes how people make mistakes, not how machines work. Later guidance from NIST, OWASP and CISA restates the same ideas in current vocabulary.

## The eight classic principles

| Principle | Statement | The test to apply |
|---|---|---|
| **Economy of mechanism** | Keep the design as simple and small as possible | Can one person read and understand the whole security-relevant part? |
| **Fail-safe defaults** | Base access decisions on permission, not exclusion; when in doubt, deny | If the rule set were empty, would the system be open or closed? |
| **Complete mediation** | Check every access to every object, every time | Is there any path that skips the check, or caches an old answer? |
| **Open design** | The design is not a secret; only keys and passwords are | Would the system still hold if the attacker had the source code? |
| **Separation of privilege** | Require more than one condition to grant access | Does one stolen credential unlock the whole thing? |
| **Least privilege** | Give each actor only the rights needed for the task, and only for as long as needed | If this account were stolen, what is the worst it could do? |
| **Least common mechanism** | Minimize shared mechanisms between users of different trust | What resource do two unrelated tenants or processes share? |
| **Psychological acceptability** | The secure way must be the easy way, or people will bypass it | Do users work around this control? |

### Economy of mechanism

More code means more bugs, and more features mean more code. Security-critical components should be small enough to review thoroughly. Heartbleed (CVE-2014-0160) is the textbook case: a missing bounds check in the rarely used TLS *heartbeat* extension of OpenSSL let a remote client read up to 64 KB of server memory per request, including private keys and session data. A feature that almost nobody needed carried a flaw that affected a large share of the internet. **●●●**

**Apply it:** disable unused features, remove unused services and dependencies, prefer a well-reviewed standard component to a clever custom one.

### Fail-safe defaults

The default answer must be *no*. Allowlists beat blocklists because you cannot enumerate everything bad, but you can enumerate what you need. A related habit is to **fail closed**: if the authorization service is down, deny rather than allow.

**Violations you will meet:** default credentials on routers and cameras (Mirai spread by trying a short list of factory defaults), cloud storage created public by default, firewall rules ending in "allow all", exception handlers that return the admin view on error. Compare the OWASP 2025 category *Mishandling of Exceptional Conditions*, which is this principle seen at the application layer (see [OWASP Top 10:2025](../05-application-security/02-owasp-top-10-2025.md)).

### Complete mediation

Every request must pass through the check, and the check must be repeated. Hiding a button in the interface is not mediation; the request can be sent without the interface. A cached authorization decision is not mediation if permissions can change.

**Violations you will meet:** insecure direct object references (changing `/invoice/1041` to `/invoice/1042` and reading someone else's data), time-of-check to time-of-use races, and microservices that trust any request coming from "inside" the network. The most common web vulnerability class, broken access control, is a failure of this principle (see [Access control, SSRF and logic flaws](../05-application-security/04-access-control-ssrf-and-logic-flaws.md)).

### Open design

Auguste Kerckhoffs stated the cryptographic version in 1883: a system should remain secure even if everything about it except the key is public (Kerckhoffs, 1883). Shannon restated it as "the enemy knows the system" (Shannon, 1949). **●●●** Secret algorithms get leaked, reverse-engineered or brute-forced, and they never get the public scrutiny that finds flaws. Keys can be changed after a leak; designs cannot.

**What it does not say:** that you should publish everything. Hiding details such as software versions or internal addresses is a legitimate, cheap *delay*. It is only a problem when it is the *only* protection.

### Separation of privilege

A protection that depends on one secret is brittle. Requiring two independent conditions, such as a password plus a hardware key, or two approvers for a sensitive change, means one failure does not grant access. Multi-factor authentication, split cryptographic keys and "two-person" rules for production data are all instances. Independence matters: two factors that can both be phished on the same fake page are weaker than they look (see [Passwords and MFA](../04-cryptography-and-identity/04-passwords-and-mfa.md)).

### Least privilege

Every account, process and API key should have the minimum rights needed. The point is to bound the damage when something is compromised, which it eventually will be. Typical applications:

- Service accounts that run one service, not the domain administrator.
- Cloud roles scoped to specific resources and actions instead of wildcards.
- Linux `sudo` rules for specific commands rather than a full shell.
- Database accounts that can read and write rows but not drop tables.
- Time-bound elevation (just-in-time access) instead of permanent admin rights.

**Practical implication:** audit rights by asking what the worst action is that an account could take, not what it is *supposed* to do.

### Least common mechanism

Anything shared between parties is a potential channel between them: a shared directory, a shared kernel, a shared CPU cache. Containers share the host kernel, so a kernel flaw can cross the container boundary; virtual machines share a hypervisor and hardware, which is why speculative-execution attacks such as Spectre and Meltdown mattered for cloud tenants. The principle does not forbid sharing, it asks you to notice it and treat it as a trust boundary.

### Psychological acceptability

If the secure path is painful, people will route around it: shared accounts, passwords on sticky notes, disabled controls "just for this release". Designers must account for the human who has a deadline. Password-rotation rules that force a new password every 90 days are a classic failure; current NIST guidance dropped forced rotation and composition rules for this reason (NIST SP 800-63B-4). **●●●** The corollary is that good security usually improves the experience: passkeys are both stronger and quicker than passwords.

## Two more factors from the same paper

Saltzer and Schroeder also listed two ideas that they considered borrowed from physical security.

- **Work factor.** Compare the cost of defeating a control with the resources of the attacker you expect. This is why password hashes are made deliberately expensive and why key sizes are chosen against a time horizon.
- **Compromise recording.** Sometimes it is better to reliably record that a breach happened than to prevent it. Tamper-evident logs and audit trails are the modern form.

## Principles added since 1975

| Principle | Idea | Where it shows up |
|---|---|---|
| **Defense in depth** | Several independent layers, so that no single failure is fatal | Network segmentation plus host hardening plus detection |
| **Zero trust** | No implicit trust from network location; authenticate and authorize every request | NIST SP 800-207; identity-aware proxies; device posture checks |
| **Assume breach** | Design and operate as if an attacker is already inside | Segmentation, least privilege, monitoring, tested recovery |
| **Minimize attack surface** | Every exposed interface is a place to attack | Closing ports, removing features, fewer dependencies |
| **Separate code and data** | Never let data be interpreted as instructions | Parameterized queries, output encoding; the root cause of injection |
| **Secure by default and by design** | The vendor ships the safe configuration and owns the outcome | CISA's Secure by Design initiative; hardened baselines |
| **Fail securely** | Errors must not weaken protection or leak details | Generic error messages, deny on failure |
| **Privacy by design** | Build data protection in from the start | Data minimization, purpose limits, retention limits |

Two caveats on these.

- **Defense in depth is only as good as the independence of the layers.** Five controls that all depend on the same credential are one control. The "Swiss cheese" picture works because holes rarely line up; make sure yours do not.
- **Zero trust is a strategy, not a product.** NIST describes it as a set of principles for architecture in which trust is evaluated per request, using identity, device state and context (NIST SP 800-207). **●●●** Vendors sell products labelled "zero trust"; judge them against the principles.

## Using the principles in a review

When you look at a design, a configuration or a finding, run this short list.

1. **Default:** what happens if nothing is configured? (fail-safe defaults)
2. **Check:** where exactly is the access decision made, and can it be skipped? (complete mediation)
3. **Blast radius:** if this credential, host or component is compromised, what else falls? (least privilege, assume breach)
4. **Secrets:** does the design depend on something remaining unknown other than a key? (open design)
5. **Single point:** does one condition grant everything? (separation of privilege)
6. **Shared:** what do parties of different trust share? (least common mechanism)
7. **Size:** is there a feature here nobody needs? (economy of mechanism)
8. **Human:** will a busy person bypass this? (psychological acceptability)

If you can answer all eight for a system, you can produce a useful review of it, and the answers feed directly into a threat model (see [Threat modeling](03-threat-modeling.md)).

## What to do with this

- [ ] Memorize the eight classic principles and their one-line tests.
- [ ] Take one finding from a lab you solved and name the principle it violated.
- [ ] Review your own home lab with the eight-question list and write down three improvements.
- [ ] Read the first sections of Saltzer and Schroeder's paper; it is short and still readable.

## Key references

CISA Secure by Design · Kerckhoffs (1883) · NIST SP 800-63B-4 · NIST SP 800-207 · Saltzer and Schroeder (1975) · Shannon (1949). Full list in [References](../15-references.md).

<!-- navigation -->
[← What security is](01-what-security-is.md) · [Index](../00-start-here.md) · [Threat modeling →](03-threat-modeling.md)
