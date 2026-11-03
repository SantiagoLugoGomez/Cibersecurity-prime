# Glossary

> [!TIP]
> **In short:** about 280 terms used across this knowledge base, defined the way they are actually used here, with a link to the page that treats each one in depth. Use this page to look a term up quickly; use the linked page when you need the reasoning, the evidence and the practice behind it. Terms that are easy to confuse with one another (MAC address versus Mandatory Access Control; authentication versus authorization) are cross-referenced explicitly so the distinction is not lost in a quick lookup.

## How to use this page

Entries are alphabetical. A term defined fully on its own linked page is kept short here on purpose; read the link for depth, evidence markers and practice. Acronyms are listed at their spelled-out alphabetical position and also as a bare acronym where it is the more common form.

## A

**ABAC (Attribute-Based Access Control).** An authorization model where access decisions depend on attributes of the subject, resource, action and environment (device managed, time of day, data sensitivity) rather than a fixed role. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Access control.** The general discipline of deciding and enforcing who may do what to which resource. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Accountability.** The property that actions can be traced to the responsible party, usually through logging and identity. See [Logging and telemetry](07-defensive-security/01-logging-and-telemetry.md).

**ACME (Automatic Certificate Management Environment).** The protocol (RFC 8555) behind automated certificate issuance services such as Let's Encrypt. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**ACL (Access Control List).** A list of permissions attached to an object, stating which principals may perform which actions on it. In Active Directory, ACLs on directory objects are a major privilege-escalation surface. See [Active Directory](02-systems/03-active-directory.md).

**Active Directory (AD).** Microsoft's directory service combining an LDAP database, Kerberos and NTLM authentication, DNS and Group Policy for Windows domain networks. See [Active Directory](02-systems/03-active-directory.md).

**AD CS (Active Directory Certificate Services).** Microsoft's PKI role for issuing certificates inside a domain; a common privilege-escalation surface when templates are misconfigured. See [Active Directory](02-systems/03-active-directory.md).

**Adversary emulation.** Reproducing a specific, documented threat actor's techniques to test defenses realistically. See [Red teaming and adversary emulation](06-offensive-security/06-red-teaming-and-adversary-emulation.md).

**Adware.** Software that generates revenue through unwanted advertising, often bundled with other installs. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**AES (Advanced Encryption Standard).** The standard symmetric block cipher (FIPS 197), almost always used in an authenticated mode such as GCM. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Agent (AI).** A system that loops: reads context, plans, calls tools and acts, often with delegated authority. See [LLM and AI application security](05-application-security/07-llm-and-ai-application-security.md).

**AiTM (Adversary-in-the-Middle).** A phishing technique where a proxy sits between victim and real site, relaying credentials and session tokens in real time. See [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md).

**Allowlist (also: allowlisting).** A security control that permits only explicitly approved items (IP addresses, applications, algorithms) and denies everything else by default. See [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md).

**AMSI (Antimalware Scan Interface).** Not covered as a standalone page; a Windows interface letting security products inspect script content before execution.

**Anonymization.** Altering data so no individual can reasonably be re-identified, even combined with other data; stronger and legally different from pseudonymization. See [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md).

**APT (Advanced Persistent Threat).** A sophisticated, usually well-resourced threat actor (often state-linked) that maintains long-term, stealthy access to a target. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**ARP (Address Resolution Protocol).** Resolves an IP address to a MAC address on a local network segment; ARP spoofing abuses its lack of authentication. See [Models and addressing](03-networking/01-models-and-addressing.md).

**ASLR (Address Space Layout Randomization).** An exploit mitigation that randomizes where code and data load in memory. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

**Asset.** Anything of value to be protected: data, a system, a process, reputation. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**Asymmetric cryptography.** Cryptography using a mathematically linked key pair (public and private) instead of one shared secret; the basis of PKI and digital signatures. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**ATT&CK.** See MITRE ATT&CK.

**Attack path.** A chained sequence of weaknesses an attacker can follow from a starting point to a goal; computed explicitly by graph-based tools in both Active Directory and cloud IAM. See [Active Directory attacks](06-offensive-security/05-active-directory-attacks.md) and [Cloud IAM and attack paths](08-cloud-and-infrastructure/02-cloud-iam-and-attack-paths.md).

**Attack surface.** Every point where an attacker could attempt to enter or extract data from a system. See [What security is](01-foundations/01-what-security-is.md).

**Attack tree.** A diagram decomposing a high-level attack goal into the specific sub-goals and conditions that achieve it. See [Threat modeling](01-foundations/03-threat-modeling.md).

**Attack vector.** The specific path or method used to deliver an attack. See [What security is](01-foundations/01-what-security-is.md).

**Audit (security).** An independent check of whether controls exist, are implemented, and actually operated as claimed. See [Policies, audit and third-party risk](10-governance-risk-and-compliance/03-policies-audit-and-third-party-risk.md).

**Authentication (authn).** Proving who you are. Contrast with authorization. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Authenticity.** Assurance that information or a message genuinely comes from its claimed source. See [What security is](01-foundations/01-what-security-is.md).

**Authorization (authz).** Deciding and enforcing what an authenticated principal may do; also used for the legal permission required before security testing. Contrast with authentication. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md) and [Legal limits and ethics](01-foundations/05-legal-and-ethics.md).

**Availability.** One of the three classic CIA properties: systems and data are accessible when needed. See [What security is](01-foundations/01-what-security-is.md).

## B

**Backdoor.** A hidden or undocumented means of bypassing normal authentication to access a system. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**Beacon / beaconing.** Regular, often low-volume check-ins from malware or a C2 implant to attacker infrastructure. See [Traffic analysis and scanning](03-networking/05-traffic-analysis-and-scanning.md).

**BGP (Border Gateway Protocol).** The routing protocol that exchanges reachability information between networks across the internet. See [TCP, UDP and routing](03-networking/02-tcp-udp-and-routing.md).

**Blocklist (also: blocklisting).** A control that denies explicitly listed items and allows everything else; generally weaker than allowlisting. See [Injection and XSS](05-application-security/03-injection-and-xss.md).

**BOLA (Broken Object Level Authorization).** An API failure where changing an object identifier returns or alters another user's data; the top entry in the OWASP API Security Top 10. See [API security](05-application-security/05-api-security.md).

**Bug bounty.** A program paying independent researchers for valid vulnerability reports within a defined scope. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md) and [Portfolio and writing](11-learning-and-career/06-portfolio-and-writing.md).

**Buffer overflow.** Writing past the end of allocated memory, corrupting adjacent data; the classic memory-safety vulnerability. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

**Business continuity.** Planning to keep critical functions operating through a disruption. See [Hardening and resilience](07-defensive-security/08-hardening-and-resilience.md).

## C

**C2 (Command and Control).** Infrastructure and protocol a compromised host uses to receive instructions from an attacker. See [Red teaming and adversary emulation](06-offensive-security/06-red-teaming-and-adversary-emulation.md).

**CA (Certificate Authority).** An entity trusted to issue digital certificates binding a public key to an identity. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**Capability (Linux).** A fine-grained unit of privilege that can be granted to a process independently of full root access. See [Privilege escalation](06-offensive-security/04-privilege-escalation.md).

**CAPEC.** A catalog of common attack patterns maintained alongside CWE. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**CFG (Control Flow Guard).** A Windows exploit mitigation restricting indirect call targets. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

**Chain of custody.** A continuous, documented record of who possessed a piece of evidence, from collection onward, needed for it to be trusted later. See [Digital forensics](07-defensive-security/05-digital-forensics.md).

**CIA triad.** Confidentiality, integrity and availability: the three classic properties security protects. See [What security is](01-foundations/01-what-security-is.md).

**CIDR (Classless Inter-Domain Routing).** The notation and method for allocating and summarizing IP address blocks (for example `10.0.0.0/24`). See [Models and addressing](03-networking/01-models-and-addressing.md).

**CIS Benchmarks.** Detailed, consensus-built configuration hardening guides per platform, from the Center for Internet Security. See [Hardening and resilience](07-defensive-security/08-hardening-and-resilience.md).

**CIS Controls.** A free, prioritized set of safeguards grouped into Implementation Groups; IG1 is a practical minimum baseline. See [Frameworks and standards](10-governance-risk-and-compliance/02-frameworks-and-standards.md).

**Cipher suite.** The negotiated combination of key exchange, authentication, encryption and integrity algorithms used in a TLS connection. See [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md).

**Ciphertext.** The output of encryption; unreadable without the key. Contrast with plaintext. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Clickjacking.** Tricking a user into clicking something different from what they perceive, usually via an invisible overlaid frame. See [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md).

**Cloud security posture management (CSPM).** Tooling that continuously checks cloud configuration against known-good baselines. See [Cloud security fundamentals](08-cloud-and-infrastructure/01-cloud-security-fundamentals.md).

**Confidentiality.** One of the three classic CIA properties: information is accessible only to those authorized. See [What security is](01-foundations/01-what-security-is.md).

**Container.** A process isolated by kernel namespaces and cgroups, sharing the host kernel. See [Containers, Kubernetes and IaC](08-cloud-and-infrastructure/03-containers-kubernetes-and-iac.md).

**Control.** A measure that reduces the likelihood or impact of a risk. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**CORS (Cross-Origin Resource Sharing).** A mechanism letting a server opt in to having other origins read its responses, relaxing the same-origin policy. See [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md).

**CRL (Certificate Revocation List).** A published list of revoked certificates, largely superseded by OCSP. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**CSP (Content Security Policy).** A response header restricting which sources of scripts and other resources a page may load, the primary mitigation layered behind XSS fixes. See [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md).

**CSR (Certificate Signing Request).** A request, including a public key, submitted to a CA to obtain a certificate. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**CSRF (Cross-Site Request Forgery).** An attack that uses a victim's browser, and its automatically attached cookies, to make an unwanted state-changing request to a site the victim is logged into. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**CTEM (Continuous Threat Exposure Management).** Gartner's five-stage cycle (scoping, discovery, prioritization, validation, mobilization) for managing exposure continuously, beyond traditional CVE-only vulnerability management. See [Vulnerability and exposure management](07-defensive-security/07-vulnerability-and-exposure-management.md).

**CVE (Common Vulnerabilities and Exposures).** A unique identifier for a specific publicly known vulnerability. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**CVSS (Common Vulnerability Scoring System).** A standardized severity score for vulnerabilities, currently version 4.0. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**CWE (Common Weakness Enumeration).** A catalog of the types of weaknesses that cause vulnerabilities (for example CWE-79, cross-site scripting). See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

## D

**DAC (Discretionary Access Control).** An access model where the resource owner grants rights to others at their own discretion, as in Unix file permissions. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**DAST (Dynamic Application Security Testing).** Testing a running application for vulnerabilities by attacking it like a user would. See [Secure development and supply chain](05-application-security/06-secure-development-and-supply-chain.md).

**DCSync.** A technique abusing directory replication rights to extract password hashes from a domain controller without logging on to it directly. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**DDoS (Distributed Denial of Service).** A denial-of-service attack launched from many sources at once.

**Decompiler.** A tool that approximates higher-level source code from compiled machine code. Contrast with disassembler. See [Reverse engineering basics](09-malware-and-reverse-engineering/05-reverse-engineering-basics.md).

**Deep practice.** The roadmap's term for a longer, open-ended practice session where real skill forms through struggle and combination of ideas. See [The study system](11-learning-and-career/02-the-study-system.md).

**Defense in depth.** Layering independent controls so that one layer's failure does not cause total compromise. See [Security principles](01-foundations/02-security-principles.md).

**DEP/NX (Data Execution Prevention / No-Execute).** A mitigation marking memory as non-executable to block simple shellcode injection. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

**Desirable difficulty.** A learning-science finding that conditions making initial learning feel harder often produce better long-term retention. See [Learning science](11-learning-and-career/01-learning-science.md).

**Detection engineering.** Writing, testing, deploying and maintaining detection logic as disciplined, validated work rather than ad hoc rules. See [Detection engineering](07-defensive-security/02-detection-engineering.md).

**DFIR (Digital Forensics and Incident Response).** The combined discipline of investigating and responding to security incidents. See [Incident response](07-defensive-security/04-incident-response.md) and [Digital forensics](07-defensive-security/05-digital-forensics.md).

**DHCP (Dynamic Host Configuration Protocol).** The protocol that automatically assigns IP addresses and network configuration to hosts. See [Models and addressing](03-networking/01-models-and-addressing.md).

**Diamond Model.** An intrusion-analysis model relating adversary, capability, infrastructure and victim for a given event. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**Differential privacy.** A technique adding calibrated statistical noise so that including or excluding any one individual barely changes an aggregate result, with a formal privacy guarantee. See [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md).

**Digital signature.** A cryptographic proof that a message was signed by the holder of a specific private key and has not been altered. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**Disassembler.** A tool that converts machine code into human-readable assembly instructions. Contrast with decompiler. See [Reverse engineering basics](09-malware-and-reverse-engineering/05-reverse-engineering-basics.md).

**DMZ (Demilitarized Zone).** A network segment exposing specific services to a less trusted network while isolating the rest of the internal network. See [Network defense architecture](03-networking/04-network-defense-architecture.md).

**DNS (Domain Name System).** The distributed system that resolves human-readable names to IP addresses. See [DNS, HTTP and the web stack](03-networking/03-dns-http-and-the-web-stack.md).

**DNSSEC.** Cryptographic signing of DNS records to prevent tampering and spoofing. See [DNS, HTTP and the web stack](03-networking/03-dns-http-and-the-web-stack.md).

**DoH / DoT (DNS over HTTPS / DNS over TLS).** Protocols that encrypt DNS queries in transit. See [DNS, HTTP and the web stack](03-networking/03-dns-http-and-the-web-stack.md).

**DPoP (Demonstrating Proof of Possession).** An OAuth extension (RFC 9449) binding a token to a client-held key so a stolen token alone is useless. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

## E

**EDR (Endpoint Detection and Response).** Software monitoring endpoint behavior (process, file, network, memory) and enabling response actions. See [Detection engineering](07-defensive-security/02-detection-engineering.md).

**Encapsulation (networking).** Wrapping data from a higher protocol layer inside the header and structure of a lower one. See [Models and addressing](03-networking/01-models-and-addressing.md).

**Encryption.** Transforming plaintext into ciphertext using an algorithm and a key, reversible only with the correct key. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Enumeration.** Systematically extracting detail from a discovered service or system: versions, accounts, shares, configuration. See [Reconnaissance and enumeration](06-offensive-security/02-reconnaissance-and-enumeration.md).

**EPSS (Exploit Prediction Scoring System).** A score estimating the probability a given CVE will be exploited in the wild soon. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**Exploit.** Code or a technique that takes advantage of a vulnerability. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**Exposure management.** The broadened discipline of managing every path an attacker could use (misconfigurations, excess permissions, weak credentials), not only CVE-tracked software flaws. See [Vulnerability and exposure management](07-defensive-security/07-vulnerability-and-exposure-management.md).

## F

**Fail-safe defaults.** A security principle: default to denial, and grant access only through an explicit, positive decision. See [Security principles](01-foundations/02-security-principles.md).

**False positive / false negative.** A detection firing on legitimate activity, versus a detection failing to fire on real malicious activity. See [Detection engineering](07-defensive-security/02-detection-engineering.md).

**Federation.** Letting one identity provider vouch for a user's identity to another system or organization. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**FIDO2 / WebAuthn.** A standard for phishing-resistant, public-key-based authentication, the basis of security keys and passkeys. See [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md).

**Firewall.** A device or software that controls network traffic based on defined rules. See [Network defense architecture](03-networking/04-network-defense-architecture.md).

**Forward secrecy.** A TLS property ensuring that compromise of a long-term private key does not expose past session traffic. See [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md).

**Fuzzing.** Feeding a program random or mutated input to find crashes and vulnerabilities. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

## G

**GDPR (General Data Protection Regulation).** The EU's data protection regulation, globally influential as a reference standard. See [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md).

**GNAP (Grant Negotiation and Authorization Protocol).** A newer authorization protocol (RFC 9635), not backward-compatible with OAuth 2.0. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Golden ticket.** A forged Kerberos ticket-granting ticket created with a stolen `krbtgt` key, valid for any user in the domain. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**GPO (Group Policy Object).** A Windows domain mechanism for pushing configuration to many computers at once. See [Active Directory](02-systems/03-active-directory.md).

**GRC (Governance, Risk and Compliance).** The combined discipline of program oversight, risk management and meeting external requirements. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

## H

**Habeas data.** The constitutional right, in Colombia and several other countries, to know, update and correct personal information held by others. See [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md).

**Hardening.** Reducing attack surface and raising the cost of attack through configuration, removal of unused components, and baseline compliance. See [Hardening and resilience](07-defensive-security/08-hardening-and-resilience.md).

**Hash function.** A one-way function mapping arbitrary input to a fixed-size output, used for integrity checking and password storage. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**HMAC.** A construction for message authentication using a hash function and a secret key. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Honeypot / honeytoken.** A decoy system or credential designed to detect and study unauthorized access attempts. See [Reconnaissance and enumeration](06-offensive-security/02-reconnaissance-and-enumeration.md).

**HSTS (HTTP Strict Transport Security).** A header instructing browsers to use HTTPS only for a given host. See [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md).

**HTTP / HTTPS.** The application-layer protocol underlying the web, and its encrypted form over TLS. See [DNS, HTTP and the web stack](03-networking/03-dns-http-and-the-web-stack.md).

## I

**IaaS / PaaS / SaaS.** Infrastructure, platform and software as a service; cloud service models with different shared-responsibility boundaries. See [Cloud security fundamentals](08-cloud-and-infrastructure/01-cloud-security-fundamentals.md).

**IaC (Infrastructure as Code).** Describing infrastructure in version-controlled text files applied by tooling, enabling review and scanning before deployment. See [Containers, Kubernetes and IaC](08-cloud-and-infrastructure/03-containers-kubernetes-and-iac.md).

**IAM (Identity and Access Management).** The systems and processes managing identities and their permissions, especially in cloud platforms. See [Cloud IAM and attack paths](08-cloud-and-infrastructure/02-cloud-iam-and-attack-paths.md).

**IDOR (Insecure Direct Object Reference).** A vulnerability where changing an object identifier grants access to another user's data; a near-synonym of BOLA in API contexts. See [Access control, SSRF and logic flaws](05-application-security/04-access-control-ssrf-and-logic-flaws.md).

**IDS / IPS (Intrusion Detection / Prevention System).** A system that detects, and in the prevention case blocks, malicious network or host activity matching known patterns. See [Network defense architecture](03-networking/04-network-defense-architecture.md).

**IMDS (Instance Metadata Service).** A cloud service reachable only from inside a running instance, providing configuration and temporary credentials; a frequent SSRF target. See [Cloud security fundamentals](08-cloud-and-infrastructure/01-cloud-security-fundamentals.md).

**Incident response.** The structured process of detecting, containing, eradicating and recovering from a security incident. See [Incident response](07-defensive-security/04-incident-response.md).

**Indicator of compromise (IOC).** A technical artifact (a hash, domain, address) associated with malicious activity. See [Threat intelligence and hunting](07-defensive-security/06-threat-intelligence-and-hunting.md).

**Infostealer.** Malware that harvests credentials, cookies and other sensitive data from an infected host. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**Insider threat.** Risk originating from someone with legitimate access, whether malicious, negligent or compromised. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**Integrity.** One of the three classic CIA properties: data has not been altered without authorization. See [What security is](01-foundations/01-what-security-is.md).

**Interleaving.** A learning technique mixing different topics or skills in practice rather than completing one before starting the next. See [Learning science](11-learning-and-career/01-learning-science.md).

**IOC.** See indicator of compromise.

## J

**JWT (JSON Web Token).** A compact, signed (and optionally encrypted) token format widely used for authentication and authorization claims. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

## K

**KDF (Key Derivation Function).** A function deriving one or more cryptographic keys from a password or other secret, such as PBKDF2, scrypt or Argon2id. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Kerberoasting.** Requesting Kerberos service tickets for accounts with service principal names and cracking the resulting material offline to recover the account's password. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**Kerberos.** A ticket-based network authentication protocol used by default in Active Directory, built on a trusted third party (the KDC). See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**Kernel.** The core of an operating system, running with full hardware privilege. See [Windows internals for security](02-systems/02-windows-internals-for-security.md) and [Linux for security](02-systems/01-linux-for-security.md).

**Key (cryptography).** A piece of secret or public information that parameterizes a cryptographic algorithm's operation. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Kill chain.** A model dividing an intrusion into sequential stages, from reconnaissance to actions on objectives. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**k-anonymity.** A privacy property ensuring each record is indistinguishable from at least *k*-1 others on identifying attributes. See [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md).

**KPI / KEV.** KEV, the CISA Known Exploited Vulnerabilities catalog, lists CVEs with confirmed real-world exploitation. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**krbtgt.** The Active Directory account whose key protects every Kerberos ticket-granting ticket in the domain; the single most sensitive secret in a domain. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**Kubernetes.** An orchestration platform for managing containers across many machines. See [Containers, Kubernetes and IaC](08-cloud-and-infrastructure/03-containers-kubernetes-and-iac.md).

## L

**LAPS (Local Administrator Password Solution).** A Windows feature giving every computer a unique, rotating local administrator password. See [Active Directory](02-systems/03-active-directory.md).

**Lateral movement.** Using an initial foothold to reach additional hosts or accounts within a network. See [Active Directory attacks](06-offensive-security/05-active-directory-attacks.md).

**LDAP (Lightweight Directory Access Protocol).** The protocol used to query and modify directory services such as Active Directory. See [Active Directory](02-systems/03-active-directory.md).

**Least privilege.** A security principle: grant only the minimum access needed to perform a task. See [Security principles](01-foundations/02-security-principles.md).

**LLM (Large Language Model).** A machine learning model that processes and generates text, increasingly embedded in applications and agents. See [LLM and AI application security](05-application-security/07-llm-and-ai-application-security.md).

**LOLBAS / GTFOBins.** Catalogs of signed, legitimate binaries that can be abused for execution, download or privilege escalation, on Windows and Unix respectively. See [Privilege escalation](06-offensive-security/04-privilege-escalation.md).

## M

**MAC address (Media Access Control address).** A hardware identifier for a network interface, used at the link layer. Not to be confused with Mandatory Access Control. See [Models and addressing](03-networking/01-models-and-addressing.md).

**Malware.** Software designed to cause harm, gain unauthorized access, or operate against the interest of the system's owner. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**Mandatory Access Control (MAC).** An access model where a central policy, not the resource owner, enforces labels on subjects and objects. Not to be confused with a MAC address. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**MFA (Multi-Factor Authentication).** Authentication combining factors from different categories (something you know, have, are). See [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md).

**MITM (Man-in-the-Middle).** An attack where the adversary secretly relays or alters communication between two parties who believe they are talking directly.

**MITRE ATT&CK.** A knowledge base of adversary tactics and techniques organized by stage, used as a shared vocabulary for detection, intelligence and emulation. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**mTLS (Mutual TLS).** TLS where both client and server authenticate each other with certificates. See [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md).

## N

**NAT (Network Address Translation).** Mapping private IP addresses to a shared public one for outbound connectivity. See [Models and addressing](03-networking/01-models-and-addressing.md).

**N-day.** A vulnerability with a known fix available, exploited because patching lagged. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**Non-repudiation.** Assurance that a party cannot later deny having performed an action, usually via signatures or logs. See [What security is](01-foundations/01-what-security-is.md).

**NTLM.** A challenge-response authentication protocol family predating and still coexisting with Kerberos in Windows networks, vulnerable to relay and hash-based attacks. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

## O

**OAuth 2.0.** A framework for delegated authorization, letting an application act on a user's behalf without receiving their password. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**OCSP (Online Certificate Status Protocol).** A protocol for checking in real time whether a certificate has been revoked. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**OIDC (OpenID Connect).** An identity layer built on OAuth 2.0, letting a client learn who signed in. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Open design.** A security principle: security should not depend on secrecy of design or implementation, only of specific keys. See [Security principles](01-foundations/02-security-principles.md).

**OSINT (Open Source Intelligence).** Gathering information from publicly available sources. See [Reconnaissance and enumeration](06-offensive-security/02-reconnaissance-and-enumeration.md).

**OWASP (Open Worldwide Application Security Project).** A nonprofit community producing widely used free application security resources, including the Top 10. See [The OWASP Top 10:2025](05-application-security/02-owasp-top-10-2025.md).

## P

**Packing.** Compressing or encrypting a program's real code behind a small decompression stub, used legitimately and to defeat static malware analysis. See [Static analysis](09-malware-and-reverse-engineering/03-static-analysis.md).

**Pass-the-hash.** Authenticating using a stolen password hash directly, without needing to crack it. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**Pass-the-ticket.** Reusing a stolen Kerberos ticket to authenticate as its original holder. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**Passkey.** A FIDO-based credential replacing passwords, phishing-resistant by design. See [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md).

**Patch management.** The process of applying software updates in a prioritized, timely and tested manner. See [Vulnerability and exposure management](07-defensive-security/07-vulnerability-and-exposure-management.md).

**Payload.** The part of an exploit or malicious file that performs the actual intended action once delivered. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**PCI DSS (Payment Card Industry Data Security Standard).** A mandatory technical standard for organizations handling payment card data. See [Frameworks and standards](10-governance-risk-and-compliance/02-frameworks-and-standards.md).

**Pentest (penetration test).** An authorized, scoped engagement to find and demonstrate exploitable weaknesses. See [Penetration testing methodology](06-offensive-security/01-penetration-testing-methodology.md).

**Persistence.** Mechanisms an attacker uses to maintain access across reboots or credential changes. See [Privilege escalation](06-offensive-security/04-privilege-escalation.md).

**PKI (Public Key Infrastructure).** The system of certificate authorities, certificates and trust relationships supporting public-key cryptography at scale. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**Plaintext.** Readable, unencrypted data. Contrast with ciphertext. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

**Playbook / runbook.** A written, repeatable procedure for handling a specific type of alert or incident. See [Security operations and the SIEM](07-defensive-security/03-security-operations-and-siem.md).

**Post-quantum cryptography.** Cryptographic algorithms believed to resist attacks from sufficiently powerful quantum computers, such as ML-KEM and ML-DSA. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**Privilege escalation.** Gaining higher (vertical) or peer-level different (horizontal) privileges than originally held. See [Privilege escalation](06-offensive-security/04-privilege-escalation.md).

**Prompt injection.** Crafted input that changes a language model's behavior by exploiting its inability to reliably separate instructions from data. See [LLM and AI application security](05-application-security/07-llm-and-ai-application-security.md).

**Proxy / reverse proxy.** An intermediary forwarding requests on behalf of a client, or on behalf of a server, respectively. See [Network defense architecture](03-networking/04-network-defense-architecture.md).

**Pseudonymization.** Replacing a direct identifier with a token while keeping the mapping separately secured; weaker and legally different from anonymization. See [Privacy and data protection](10-governance-risk-and-compliance/04-privacy-and-data-protection.md).

**Pyramid of Pain.** A model ranking indicator types by how costly they are for an attacker to change, from hashes (trivial) to TTPs (hardest). See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

## Q

**QUIC.** A UDP-based, encrypted transport protocol underlying HTTP/3. See [DNS, HTTP and the web stack](03-networking/03-dns-http-and-the-web-stack.md).

## R

**Race condition.** A bug where the outcome depends on the relative timing of concurrent operations, exploitable when a check and its use are not atomic. See [Access control, SSRF and logic flaws](05-application-security/04-access-control-ssrf-and-logic-flaws.md).

**Ransomware.** Malware that denies access to data or systems for extortion, increasingly combined with data theft (double extortion). See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**RAT (Remote Access Trojan).** Malware giving an attacker persistent, interactive remote access to a host. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**RBAC (Role-Based Access Control).** An access model assigning permissions to roles, which are then assigned to users. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**ReBAC (Relationship-Based Access Control).** An access model deriving permissions from relationships in a graph (for example, "editors of a folder can edit its documents"). See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Reconnaissance.** Gathering information about a target before active engagement, passively or actively. See [Reconnaissance and enumeration](06-offensive-security/02-reconnaissance-and-enumeration.md).

**Red team.** An exercise testing whether a realistic adversary would succeed and be detected, usually goal-based and organization-wide. See [Red teaming and adversary emulation](06-offensive-security/06-red-teaming-and-adversary-emulation.md).

**Residual risk.** The risk remaining after controls have been applied. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**Retrieval practice.** A learning technique of actively recalling information from memory rather than passively re-reading it. See [Learning science](11-learning-and-career/01-learning-science.md).

**Reverse engineering.** Analyzing compiled code to understand its behavior without original source, using disassemblers, decompilers and debuggers. See [Reverse engineering basics](09-malware-and-reverse-engineering/05-reverse-engineering-basics.md).

**Risk.** The combination of likelihood and impact if a threat exploits a vulnerability against an asset. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**Risk appetite.** How much risk an organization is willing to accept in pursuit of its objectives. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**Risk register.** A living, owned document tracking identified risks, their ratings, treatments and owners. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**Rootkit.** Malware operating at a privileged level specifically to hide the presence of other malicious activity. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**ROP (Return-Oriented Programming).** An exploitation technique chaining existing code fragments to execute arbitrary logic without injecting new code, used to bypass DEP/NX. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

**RPO (Recovery Point Objective).** The maximum acceptable data loss, measured in time, after a disruption. See [Hardening and resilience](07-defensive-security/08-hardening-and-resilience.md).

**RTO (Recovery Time Objective).** The maximum acceptable downtime for a system after a disruption. See [Hardening and resilience](07-defensive-security/08-hardening-and-resilience.md).

## S

**SAML (Security Assertion Markup Language).** An older, XML-based standard for single sign-on, still common in enterprise federation. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Sandbox.** An isolated environment for safely running untrusted or malicious code to observe its behavior. See [Safe analysis lab setup](09-malware-and-reverse-engineering/02-safe-analysis-lab.md).

**SAST (Static Application Security Testing).** Analyzing source code for vulnerabilities without running it. See [Secure development and supply chain](05-application-security/06-secure-development-and-supply-chain.md).

**SBOM (Software Bill of Materials).** An inventory of the components (libraries, dependencies) that make up a piece of software. See [Secure development and supply chain](05-application-security/06-secure-development-and-supply-chain.md).

**SCA (Software Composition Analysis).** Scanning dependencies against vulnerability databases. See [Secure development and supply chain](05-application-security/06-secure-development-and-supply-chain.md).

**Same-origin policy.** The browser's core isolation rule: a page from one origin may not read data from another origin without explicit opt-in. See [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md).

**SIEM (Security Information and Event Management).** A platform centralizing, normalizing and correlating logs to support detection and investigation. See [Security operations and the SIEM](07-defensive-security/03-security-operations-and-siem.md).

**Silver ticket.** A forged Kerberos service ticket created with a stolen service account key, bypassing the KDC entirely for that service. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**Session.** Server-side state, or a token, linking a sequence of requests to an authenticated principal. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**Shellcode.** Small machine code, often injected by an exploit, intended to run a shell or perform an attacker's immediate action. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

**SOAR (Security Orchestration, Automation and Response).** Tooling automating repeatable steps of triage and response. See [Security operations and the SIEM](07-defensive-security/03-security-operations-and-siem.md).

**SOC (Security Operations Center).** The function and team monitoring, triaging and investigating security events continuously. See [Security operations and the SIEM](07-defensive-security/03-security-operations-and-siem.md).

**SOC 2.** An auditor's attestation that an organization's controls meet defined Trust Services Criteria, commonly requested of vendors. See [Frameworks and standards](10-governance-risk-and-compliance/02-frameworks-and-standards.md).

**Social engineering.** Manipulating people, rather than systems, into taking an action that compromises security. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**Spaced repetition.** Reviewing material at increasing intervals timed to just before it would be forgotten. See [Learning science](11-learning-and-career/01-learning-science.md) and [The study system](11-learning-and-career/02-the-study-system.md).

**SPN (Service Principal Name).** The name Kerberos uses to map a service to the account that runs it. See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**SSH (Secure Shell).** An encrypted protocol for remote command-line access and tunneling.

**SSO (Single Sign-On).** Authenticating once to access multiple, separate systems or applications. See [Authorization, sessions and federation](04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

**SSRF (Server-Side Request Forgery).** A flaw letting an attacker make the server send a request to a destination the attacker chooses, including internal and cloud metadata addresses. See [Access control, SSRF and logic flaws](05-application-security/04-access-control-ssrf-and-logic-flaws.md).

**STIX / TAXII.** Standards for structuring (STIX) and exchanging (TAXII) threat intelligence between systems. See [Threat intelligence and hunting](07-defensive-security/06-threat-intelligence-and-hunting.md).

**STRIDE.** A threat-modeling mnemonic: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. See [Threat modeling](01-foundations/03-threat-modeling.md).

**Subnet.** A logically segmented portion of an IP network. See [Models and addressing](03-networking/01-models-and-addressing.md).

**SUID.** A Unix file permission bit causing a program to run with its owner's privileges regardless of who executes it; a common privilege-escalation surface when misused. See [Privilege escalation](06-offensive-security/04-privilege-escalation.md).

**Supply chain attack.** Compromising a target through a trusted upstream dependency, build process or vendor rather than directly. See [Secure development and supply chain](05-application-security/06-secure-development-and-supply-chain.md).

**Symmetric cryptography.** Cryptography using the same secret key for both encryption and decryption. See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md).

## T

**TAXII.** See STIX / TAXII.

**TCP (Transmission Control Protocol).** A connection-oriented, reliable transport-layer protocol. See [TCP, UDP and routing](03-networking/02-tcp-udp-and-routing.md).

**Testing effect.** The learning-science finding that actively testing recall produces stronger retention than passive review. See [Learning science](11-learning-and-career/01-learning-science.md).

**Threat.** A potential cause of an unwanted incident. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

**Threat actor.** An individual or group responsible for, or capable of, a security event. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**Threat hunting.** Proactively searching for intrusions that existing detections have not caught, starting from a hypothesis. See [Threat intelligence and hunting](07-defensive-security/06-threat-intelligence-and-hunting.md).

**Threat intelligence.** Information about adversaries, analyzed enough to change a decision. See [Threat intelligence and hunting](07-defensive-security/06-threat-intelligence-and-hunting.md).

**Threat modeling.** A structured process for identifying what could go wrong in a system and deciding what to do about it. See [Threat modeling](01-foundations/03-threat-modeling.md).

**Ticket (Kerberos).** An encrypted, time-limited credential issued by the KDC, proving authentication (TGT) or authorizing access to a specific service (service ticket). See [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

**TLP (Traffic Light Protocol).** A shorthand marking how far shared information may travel. See [Threat intelligence and hunting](07-defensive-security/06-threat-intelligence-and-hunting.md).

**TLS (Transport Layer Security).** The protocol encrypting and authenticating most secure network traffic, including HTTPS. See [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md).

**TOTP (Time-Based One-Time Password).** A one-time code algorithm (RFC 6238) used by authenticator apps. See [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md).

**TTP (Tactics, Techniques and Procedures).** A description of adversary behavior at increasing levels of specificity; the most durable thing to detect against, per the Pyramid of Pain. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

## U

**UDP (User Datagram Protocol).** A connectionless, unreliable transport-layer protocol. See [TCP, UDP and routing](03-networking/02-tcp-udp-and-routing.md).

**Unified Kill Chain.** A model combining and extending the Lockheed Martin kill chain and MITRE ATT&CK into a single, longer sequence. See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

**Use-after-free.** A memory-safety bug where freed memory is used again, often exploitable for code execution. See [Memory and exploit mitigations](02-systems/04-memory-and-exploit-mitigations.md).

## V

**VDP (Vulnerability Disclosure Program).** A program accepting vulnerability reports, usually without paying a bounty. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**VLAN (Virtual Local Area Network).** A logically separated network segment on shared physical infrastructure. See [Network defense architecture](03-networking/04-network-defense-architecture.md).

**VPN (Virtual Private Network).** An encrypted tunnel extending a private network across an untrusted one.

**Vulnerability.** A weakness that a threat can exploit to violate a security property. See [Risk management](10-governance-risk-and-compliance/01-risk-management.md).

## W

**WAF (Web Application Firewall).** A filter inspecting and blocking malicious HTTP traffic based on rules or patterns; a compensating control, not a substitute for fixing the underlying flaw. See [Injection and XSS](05-application-security/03-injection-and-xss.md).

**Wiper.** Malware designed to destroy data or systems with no extortion motive. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

**Worm.** Malware that spreads automatically to other systems without repeated human action. See [The malware landscape](09-malware-and-reverse-engineering/01-malware-landscape.md).

## X

**X.509.** The standard format for public-key certificates. See [Public-key cryptography and PKI](04-cryptography-and-identity/02-public-key-cryptography-and-pki.md).

**XSS (Cross-Site Scripting).** Injection of attacker-controlled script into a page, executed in a victim's browser under the site's own origin. See [Injection and XSS](05-application-security/03-injection-and-xss.md).

## Y

**YARA.** A pattern-matching rule format and tool used to identify and classify malware samples by file characteristics. See [Static analysis](09-malware-and-reverse-engineering/03-static-analysis.md).

## Z

**Zero-day (0-day).** A vulnerability exploited, or known to an attacker, before a fix is available. See [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md).

**Zero trust.** A security model that never trusts a connection based on network location alone, verifying identity and context for every request. See [Network defense architecture](03-networking/04-network-defense-architecture.md).

## What to do with this

- [ ] Read through one letter section a day until you have covered the whole glossary at least once.
- [ ] For any term you cannot define from memory after reading its linked page, add it to your flashcard deck.
- [ ] Notice and internalize the three deliberately disambiguated pairs on this page (MAC address versus Mandatory Access Control; authentication versus authorization; pseudonymization versus anonymization).
- [ ] Add a term you encounter elsewhere that is missing here to your own private notes, with a definition in your own words.

## Key references

Every linked page's own Key references line. Full list in [References](15-references.md).
