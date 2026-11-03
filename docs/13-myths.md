# Common myths

> [!TIP]
> **In short:** cybersecurity attracts more folk wisdom than most technical fields, partly because popular media gets it wrong constantly, and partly because some myths used to be true and the field moved on without updating the common wisdom. Each entry below names the myth, states the reality plainly, and points to the page in this knowledge base that covers it properly. If you are about to repeat one of these in an interview, this page is worth a read first.

## "Hacking is mostly about writing clever exploits"

In practice, most real intrusions succeed through misconfiguration, stolen or reused credentials, and known, unpatched vulnerabilities, not novel zero-day exploits. Verizon's annual Data Breach Investigations Report has for years listed credential theft and vulnerability exploitation among the top initial-access methods; custom exploit development is a specialized, comparatively rare skill within the field, not the default path in. **●●●** See [Reconnaissance and enumeration](06-offensive-security/02-reconnaissance-and-enumeration.md) and [Privilege escalation](06-offensive-security/04-privilege-escalation.md), both of which are overwhelmingly about finding what was configured too loosely, not about writing new exploit code.

## "A VPN makes you anonymous and secure online"

A VPN moves trust from your internet provider to the VPN provider; it does not remove trust from the equation, and it does nothing about a phishing page, a weak password, malware already on your device, or a website that tracks you through cookies and browser fingerprinting regardless of your IP address. See [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md) for what encryption in transit actually protects, and notice how little of a real threat model it addresses on its own.

## "Strong passwords need numbers, symbols and capital letters"

Current guidance (NIST SP 800-63B-4) explicitly reversed this: **length** matters far more than character-class complexity, composition rules should not be imposed, and periodic forced rotation should not be required either. `Summer2026!` satisfies every classic composition rule and is cracked in seconds, because attackers try exactly these predictable patterns first. **●●●** See [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md) for the entropy math behind this.

## "Incognito or private browsing mode makes me anonymous"

It stops your own browser from saving history and cookies locally; it does nothing to hide your activity from your network, your employer's network monitoring, or the websites you visit, which can still see your IP address and fingerprint your browser exactly as they would otherwise. It is a local privacy feature, not an anonymity tool.

## "I need to be a great programmer before I can start in security"

Programming skill helps, especially for the offensive, application security and malware tracks, but Phase 0 of this roadmap deliberately starts with Linux, networking and only then Python, because a huge share of real security work (log analysis, configuration review, network defense, GRC) depends far more on systems and protocol understanding than on advanced software engineering. See [Linux for security](02-systems/01-linux-for-security.md) and [Models and addressing](03-networking/01-models-and-addressing.md) for where the roadmap actually begins.

## "Certifications guarantee a job"

A certification is evidence that can support a job search; it is not a guarantee, and a certification earned without the underlying hands-on skill behind it is often exposed within minutes of a real technical interview. See [Certification strategy](11-learning-and-career/05-certification-strategy.md) for how certifications actually function as signals, and to whom.

## "If I don't get caught, it's not illegal"

Getting caught and breaking the law are entirely separate questions. Ley 1273 de 2009 criminalizes unauthorized access regardless of whether anyone ever notices, and "I was only testing" or "I didn't cause damage" are not defenses to the offense itself. **●●●** See [Legal limits and ethics](01-foundations/05-legal-and-ethics.md) for the actual statute and what authorization genuinely requires.

## "HTTPS means a website is safe and legitimate"

HTTPS, via TLS, means the connection to that specific server is encrypted and the certificate was issued to whoever controls that domain name; it says nothing about whether the site's operator is trustworthy, honest, or free of malicious intent. Phishing pages routinely use valid HTTPS certificates, often from the same free, automated certificate authorities legitimate sites use. See [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md) for exactly what the padlock icon does and does not claim.

## "A firewall stops most attacks"

A traditional firewall controls which network connections are allowed; it does nothing about a malicious attachment a user opens, a vulnerable web application exposed through an allowed port, a phished credential, or an attacker who is already inside the perimeter. Modern defense is layered across identity, endpoints, applications and detection, not concentrated in one network device. See [Network defense architecture](03-networking/04-network-defense-architecture.md) for where a firewall actually fits among many other controls.

## "Only large, famous companies get breached"

Smaller organizations are attacked constantly, often specifically because they are assumed to have weaker defenses; many ransomware and business email compromise operations deliberately target small and mid-sized businesses at scale precisely because the economics favor volume over famous targets. The absence of small-business breaches in the news reflects weaker reporting requirements and less media interest, not lower actual risk.

## "Hiding your software's version number is real security"

Obscuring a banner or version string (**security through obscurity**) can slightly slow down casual reconnaissance, but it is not a substitute for actually patching and configuring the system correctly, and a determined attacker has other ways to fingerprint software regardless. Saltzer and Schroeder's open design principle, covered in [Security principles](01-foundations/02-security-principles.md), states this directly: security should not depend on the secrecy of the design or implementation, only on the secrecy of specific keys or credentials.

## "Removing someone's name makes data anonymous"

Removing a direct identifier like a name is a start, not an end point; re-identification from the remaining fields (a birth date, a postal code, a handful of purchases) is a well-documented, repeatedly demonstrated risk. Robust anonymization is a harder technical problem than it first appears, which is exactly why [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md) treats pseudonymization and genuine anonymization as different things with different legal consequences, not interchangeable synonyms.

## "AI will make security jobs obsolete" and, in the opposite direction, "AI tools are safe to trust blindly"

Both overstate the current reality. Language models accelerate parts of both attack and defense work, but they introduce a genuinely new, still largely unsolved vulnerability class of their own (prompt injection), and a model's output still requires human judgment, verification and accountable decisions. See [LLM and AI application security](05-application-security/07-llm-and-ai-application-security.md) for why neither extreme holds up.

## "Zero trust means you don't need a firewall or a network perimeter anymore"

Zero trust, as covered in [Network defense architecture](03-networking/04-network-defense-architecture.md), means never trusting a connection based on network location alone, and verifying identity and context for every request; it is an addition to network controls and segmentation, not a replacement for them. Organizations that heard "zero trust" as "no more network security" generally learn the difference the hard way.

## "An air-gapped system can't be hacked"

Physical isolation from a network removes remote attack paths, but not all of them: removable media, supply chain compromise before the system was ever isolated, insider access, and even side channels (covered conceptually in [Your degree and security](11-learning-and-career/04-your-degree-and-security.md#physics-i)) have all been used against genuinely air-gapped systems in documented, real-world incidents, Stuxnet being the best known example.

## "SMS-based two-factor authentication is just as good as any other MFA"

SMS codes are phishable and vulnerable to SIM-swapping attacks that bypass the code entirely by taking over the phone number. [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md) ranks authentication methods explicitly by phishing resistance; SMS sits near the bottom, well below an authenticator app, and far below a hardware security key or passkey.

## "You need expensive tools and a powerful lab to start learning"

Nearly every topic in this entire knowledge base has a free, legitimate path: free-tier platforms, open-source tools, and a modest virtual machine setup, all catalogued in [Reading and resource list](16-resources.md). Expensive tools and advanced hardware become relevant much later, for specific specializations, not as a barrier to starting.

## "Offensive security people are smarter or more skilled than defensive ones, or the reverse"

This is a false hierarchy. Effective offense and effective defense require overlapping but genuinely different skills, and the strongest practitioners in either direction (and the best purple-team work, covered in [Red teaming and adversary emulation](06-offensive-security/06-red-teaming-and-adversary-emulation.md)) tend to respect and understand the other side rather than dismiss it.

## "A CVSS score alone tells you how urgently to fix something"

CVSS measures technical severity in the abstract; it says nothing about whether a vulnerability is actually being exploited in the wild, whether the affected system is exposed to the internet, or how valuable that system is. [Vulnerability and exposure management](07-defensive-security/07-vulnerability-and-exposure-management.md) explains why real prioritization combines CVSS with exploitation data (EPSS, the CISA KEV catalog) and business context, never CVSS in isolation.

## "Open-source software is automatically more secure because anyone can review the code"

The availability of source code makes review *possible*; it does not make review *guaranteed to happen*, and the field has repeatedly been reminded of this by incidents like the Heartbleed vulnerability sitting unnoticed in a widely used library for years, and the 2024 xz utils backdoor inserted by a trusted maintainer over a long social-engineering campaign. See [Secure development and supply chain](05-application-security/06-secure-development-and-supply-chain.md) for the realistic picture of open-source supply chain risk.

## "Real hackers look like the movies"

The field's day-to-day work is reading documentation, writing careful notes, enumerating patiently, and communicating findings clearly in a report, far more often than the dramatic, fast-typing, dark-room scenes popular culture depicts. If this knowledge base's own emphasis on methodology, writeups and English technical writing feels unglamorous compared to that image, that gap is itself informative about what the job actually is.

## Practice

1. Pick three myths from this page that you held, even partially, before reading this knowledge base, and write a short note explaining the reality in your own words with a citation to the page that corrects it.
2. The next time you hear one of these myths repeated, by a classmate, in a forum, or in casual conversation, practice correcting it briefly and accurately rather than letting it pass uncorrected; this is also direct practice for the technical-communication skill this whole knowledge base is building.
3. Find one additional myth not listed here, from your own experience or reading, and write it up in the same format: myth, reality, and a link to the page that supports the correction.

## What to do with this

- [ ] Recognize every myth on this page quickly enough to correct it in conversation without needing to look it up.
- [ ] Explain, for at least five of these myths, the specific page and evidence that corrects it.
- [ ] Catch yourself the next time you are about to repeat one of these out of habit.
- [ ] Add at least one new myth you encounter yourself to your own private notes, with its correction.

## Key references

NIST SP 800-63B-4 · Saltzer and Schroeder (1975) · Verizon DBIR. Full list in [References](15-references.md).
