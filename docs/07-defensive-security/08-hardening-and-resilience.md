# Hardening and resilience

> [!TIP]
> **In short:** every page before this one in the knowledge base assumes an attacker eventually gets somewhere. **Hardening** reduces how far that gets them and how easily, by removing what is unused, tightening what remains, and applying defense in depth so no single control failure is fatal. **Resilience** accepts that some incident will eventually succeed anyway and asks the next question: can the organization keep operating, and can it get back to normal, specifically including when the attacker's goal was to destroy or encrypt your ability to recover at all? Backups are the one control that must survive the same incident it is meant to recover from, which is why they get special treatment here.

## Hardening: shrink the attack surface, then raise the cost of what remains

Hardening is not one action; it is the accumulation of specific, boring decisions, each closing one small door.

| Principle | In practice |
|---|---|
| **Remove what you do not use** | Uninstall unused software and services; disable unused protocols (see the list of legacy protocols in [Active Directory](../02-systems/03-active-directory.md) and [Kerberos, NTLM and enterprise identity](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md)); close unused ports |
| **Apply least privilege everywhere** | Covered at the account and permission level throughout [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md) and [Privilege escalation](../06-offensive-security/04-privilege-escalation.md); the same idea applies to services, network paths and firewall rules |
| **Segment** | A flat network lets one compromised host reach everything; segmentation (network, identity tiers, cloud account boundaries) contains a breach to where it started |
| **Patch on a schedule you can actually sustain** | See [Vulnerability and exposure management](07-vulnerability-and-exposure-management.md) |
| **Use secure, repeatable configuration** | Infrastructure as code and golden images mean every new system starts hardened, instead of being hardened by hand after the fact and drifting |
| **Verify against a baseline, continuously** | A hardening effort that is not checked for drift decays silently |

### Baselines: do not invent your own

Writing a hardening checklist from scratch, system by system, is slow and easy to get wrong. Established baselines exist and are free to use:

| Baseline | Covers |
|---|---|
| **CIS Benchmarks** | Detailed, consensus-built configuration guidance for operating systems, cloud platforms, containers and common software; published and updated on an ongoing basis, so check the current catalog at the CIS website rather than a cached version number |
| **CIS Controls** (already introduced in [Adversaries and attack frameworks](../01-foundations/04-adversaries-and-attack-frameworks.md)) | A prioritized, higher-level set of safeguards, with **Implementation Group 1** as a practical minimum for smaller organizations |
| **Vendor hardening guides** | Microsoft, cloud providers and major software vendors publish their own baselines, sometimes stricter or more current than third-party ones for their own products |
| **DISA STIGs** | Highly detailed US government configuration standards, widely used as a reference even outside government contexts |

A practical workflow: pick the baseline matching your platform, apply it in a test environment first (some settings break legitimate functionality), measure compliance with a scanner, and track exceptions explicitly rather than silently skipping settings that are inconvenient.

### Hardening by layer

| Layer | Key moves | Where the detail lives |
|---|---|---|
| **Identity** | MFA everywhere, least privilege, tiered administration, no shared accounts | [Passwords and MFA](../04-cryptography-and-identity/04-passwords-and-mfa.md), [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md) |
| **Endpoints** | Application control, EDR, disk encryption, automatic patching, removal of local administrator rights from daily accounts | [Memory and exploit mitigations](../02-systems/04-memory-and-exploit-mitigations.md) |
| **Network** | Segmentation, default-deny firewall rules, disabling legacy protocols, require signing where available | [Network defense architecture](../03-networking/04-network-defense-architecture.md) |
| **Active Directory** | Tiered administration, protected tier 0, delegation limits, certificate template review | [Active Directory](../02-systems/03-active-directory.md), [Active Directory attacks](../06-offensive-security/05-active-directory-attacks.md) |
| **Applications** | Secure defaults, the OWASP Top 10 controls, dependency hygiene | [OWASP Top 10:2025](../05-application-security/02-owasp-top-10-2025.md), [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md) |
| **Cloud** | Least-privilege IAM, no public storage by default, logging enabled everywhere | [Cloud security fundamentals](../08-cloud-and-infrastructure/01-cloud-security-fundamentals.md) |

## Defense in depth, revisited

Hardening is effective because no single control is assumed to be perfect. The same idea from [Security principles](../01-foundations/02-security-principles.md) applies operationally: an attacker who defeats one layer (a phished password) should meet another (MFA), and another (anomalous sign-in detection), and another (least-privilege limiting what that account can actually reach). Design each layer assuming the one before it has already failed, not as a redundant copy of it.

## Resilience: staying up, and getting back up

Resilience is what hardening leaves for when prevention and detection both fail anyway, which eventually happens to every organization regardless of maturity.

| Practice | Purpose |
|---|---|
| **Business continuity planning** | Keep critical functions running, in some form, during a disruption |
| **Disaster recovery planning** | The specific technical plan to restore systems and data after a disruption |
| **Defined recovery objectives** | **RTO** (recovery time objective: how long can this system be down?) and **RPO** (recovery point objective: how much data loss, measured in time, is acceptable?), set per system based on its actual importance, not assumed to be "zero" for everything |
| **Tested failover and recovery** | A disaster recovery plan that has never been exercised is a hypothesis, not a capability |
| **Redundancy for critical paths** | No single point of failure for the functions that matter most |

RTO and RPO targets should come from the business impact of downtime for that specific system, not a blanket policy; a marketing website and a payment processing system do not deserve the same number.

## Backups: the control that must survive the attack

Backups deserve their own section because modern ransomware specifically targets them. An attacker who can encrypt your production data and also delete or encrypt your backups has removed your only clean path back, which is exactly why backup destruction is now a routine step in ransomware operations before the visible encryption even happens.

### The 3-2-1 rule, extended

| Element | Meaning |
|---|---|
| **3** copies of important data | The original plus at least two backups |
| **2** different media or storage types | Reduces the chance a single failure mode (a storage system bug, a ransomware strain targeting one platform) destroys everything |
| **1** copy offsite | Protects against a site-level disaster, physical or digital |
| **+1 immutable or air-gapped** copy | A copy an attacker with full administrative access to your live environment still cannot modify or delete, because it is write-once storage or genuinely disconnected |
| **+0 errors on verified recovery** | A backup that has never been tested for restoration is a belief, not a backup |

The extended version (sometimes called 3-2-1-1-0) exists specifically because ransomware operators learned to hunt for and destroy ordinary backups before encrypting production; **immutability is what the extra "1" buys you**, and it is the single most consequential addition for ransomware resilience specifically. **●●○** (The underlying rule is a long-standing, vendor-neutral industry practice; the immutability extension is now widely recommended across the backup industry, though framed by vendors selling the capability, so verify specifics against neutral guidance such as CISA's ransomware readiness material as well.)

### Making backups survive a determined attacker

| Control | Why |
|---|---|
| **Separate credentials for backup infrastructure**, not reusable from the production domain | An attacker with domain administrator rights should not automatically have backup administrator rights too |
| **Immutable or offline copies**, not just "another server on the network" | Network-reachable backups with reusable credentials are not meaningfully separate from production for an attacker who already has a foothold |
| **Test restoration regularly**, not just backup completion | A backup job reporting "success" says the data was written, not that it can be read back into a working system |
| **Monitor backup infrastructure like tier 0** | Deletion or modification of backup jobs and retention settings is a high-value detection signal, not routine administrative noise |
| **Keep an offline, printed or otherwise out-of-band copy of the recovery procedure itself** | If the system that documents how to recover is also encrypted, you have lost the instructions along with the data |

## Tabletop exercises for resilience

The same tabletop method introduced in [Incident response](04-incident-response.md) applies directly here: walk through "our primary data center is unreachable" or "our backups were found to be encrypted too" as a discussion exercise, before it happens for real. The questions that surface (who has the offline credentials, how long would restoration actually take, does anyone remember the manual procedure) are exactly the gaps a resilience program exists to close.

## Measuring hardening and resilience

| Metric | What it shows |
|---|---|
| **Baseline compliance percentage**, per asset class | How consistently hardening is actually applied, not just documented |
| **Patch and configuration drift over time** | Whether hardening holds after initial deployment |
| **Backup restoration test success rate** | Whether recovery would actually work, not just whether backups run |
| **RTO/RPO achieved in exercises versus targets** | Whether stated resilience objectives are real or aspirational |

## Practice

1. Apply a CIS Benchmark to a VM in your lab, measure compliance before and after with a free scanner, and document every setting you had to adjust because it broke something legitimate.
2. Design a backup scheme for your own important files following the extended 3-2-1-1-0 model, including at least one copy you deliberately cannot reach from your main account's credentials.
3. Test a full restoration from your own backup, from scratch, onto a clean system, and time how long it actually takes versus how long you assumed it would take.
4. Write RTO and RPO targets for three systems in your lab or personal setup, with your reasoning for each number.
5. Run a 20-minute tabletop exercise with a study partner: "your primary machine and its backups are both encrypted overnight." What do you actually have left, and what would you change today to make that scenario less catastrophic?

These support [Module 1.5](../../roadmap/phase-1-security-fundamentals/05-network-defense-monitoring.md) and the [defensive track](../../roadmap/phase-3-specialization/track-defensive.md) of the roadmap.

## What to do with this

- [ ] Apply a recognized hardening baseline to at least one system you control and measure the result.
- [ ] Build a backup scheme that would survive an attacker who already has full access to your main account.
- [ ] Actually restore from a backup once, rather than assuming it would work.
- [ ] Write RTO and RPO targets for something you are responsible for.
- [ ] Run one resilience tabletop exercise and act on what it reveals.

## Key references

CIS Benchmarks and CIS Controls · CISA ransomware readiness guidance · NIST SP 800-34 (contingency planning). Full list in [References](../15-references.md).
