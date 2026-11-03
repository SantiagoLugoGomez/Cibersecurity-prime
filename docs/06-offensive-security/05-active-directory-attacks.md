# Active Directory attacks

> [!TIP]
> **In short:** an Active Directory compromise is rarely one exploit. It is a **path**: a low-privilege foothold, enumeration of a directory that any authenticated user can mostly read, the cheapest available credentials, then one of a short list of well-known escalation routes (permissions on objects, delegation, certificate services, group policy) to a domain controller. Every step abuses a *design feature* configured too generously, not a bug. The defense is the same path read backwards, which is why defenders run the same mapping tools attackers do: find the shortest routes to tier 0 before someone else does, and close them.

> [!CAUTION]
> Everything on this page is for your own isolated lab (see [Home lab](../../homelab/README.md)) or an engagement with written authorization. Touching an organization's directory without permission is a crime under Ley 1273 de 2009. This page stays conceptual on purpose; build the lab and practice the mechanics there, under supervision of the roadmap modules and licensed training content, not from a copy-pasted command sequence.

## The stages, at a glance

| Stage | What it means | Where the mechanics are covered | Main defense |
|---|---|---|---|
| **Foothold** | Getting a first set of credentials or a first authenticated session with no prior access | Relay and poisoning basics in [Kerberos, NTLM and enterprise identity](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md#relay-and-coercion); spraying in [Passwords and MFA](../04-cryptography-and-identity/04-passwords-and-mfa.md) | Disable legacy name resolution, require signing, MFA, smart lockout |
| **Enumeration** | Reading the directory to find accounts, groups, permissions and relationships | Below | Reduce what is readable, tier accounts, watch query volume |
| **Credential access** | Turning a foothold into usable credentials for more accounts | Kerberoasting and AS-REP roasting in the [Kerberos doc](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md#what-goes-wrong) | gMSA and AES-only accounts, Credential Guard, LSA protection |
| **Lateral movement** | Using credentials to reach more hosts | Pass-the-hash and pass-the-ticket in the [Kerberos doc](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md#what-goes-wrong) | Unique local admin passwords (LAPS), network segmentation |
| **Privilege escalation** | Climbing from one account or host to broader rights over the directory | Below | Permission reviews, delegation limits, certificate template hardening |
| **Domain and tier 0 compromise** | Reaching the systems and secrets that control every credential in the domain | Golden/silver tickets and delegation in the [Kerberos doc](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md#what-goes-wrong) | Protect tier 0 as one unit; see [Active Directory](../02-systems/03-active-directory.md) |

This page focuses on the two stages that are not already covered elsewhere in detail: **enumeration** and the **escalation routes** that link an ordinary account to control over the directory.

## Enumeration: the directory maps itself

By default, any authenticated user can read most of the directory over LDAP: users, groups, computers, group policy objects, trust relationships, service principal names, delegation flags and the permissions set on each object. Because these relationships form a graph, the practical question is never "is there a vulnerability?" but "**what is the shortest path from where I am to where the keys are?**"

Graph-based auditing tools (BloodHound is the best known; collectors exist for Windows, Linux and Entra ID) answer exactly that question, for attackers and defenders alike. They model relationships such as group membership, administrative rights on a computer, an active logon session, and the permission types in the table below, then compute the shortest path between any two nodes.

**Defender's use.** Run one of these tools against your own domain on a schedule, not only during a test. Treat every short path into a privileged group as a finding to remediate, the same way you would treat an open port: nested groups that quietly grant more than intended, stale administrative sessions on shared jump hosts, and service accounts with forgotten rights are the recurring findings in real audits. Automated domain-hardening checkers such as PingCastle or Purple Knight give a scored report covering the same ground and are a reasonable starting point if you are new to this.

Beyond the graph, a directory audit should also look at:

| Area | What to check |
|---|---|
| **Shares** | `SYSVOL` and `NETLOGON` scripts for embedded credentials; old Group Policy Preferences files, which can carry a recoverable password (MS14-025) |
| **Attributes** | Passwords accidentally left in a user's `description` field |
| **Account hygiene** | Accounts with passwords that have never changed, service accounts with interactive-logon rights, disabled accounts still in privileged groups |
| **Delegation flags** | Any computer or service configured for unconstrained delegation outside the domain controllers |

## Escalation routes: how one account becomes many

Once inside with ordinary rights, the routes that most often lead further are permission misconfigurations rather than software bugs. Understanding *why* each one works is the point; the operational detail belongs in a supervised lab, not in a reference document.

| Route | The underlying design feature | Why it is dangerous when misconfigured | Primary defense |
|---|---|---|---|
| **Object permissions (ACLs)** | Active Directory lets any object owner, or anyone granted rights, control who can modify that object, including sensitive rights like resetting a password or adding group members | Rights granted broadly (often by delegation wizards or old migrations) can let a low-privileged account eventually control a privileged one, several hops away in the graph | Regular permission reviews; avoid broad delegation; let graph-based auditing surface unintended paths |
| **Kerberos delegation** | Lets a service act on a user's behalf toward another service | Unconstrained delegation on a non-domain-controller host collects the credentials of anyone who connects to it; misconfigured constrained or resource-based delegation can let a compromised host impersonate arbitrary users | Remove unconstrained delegation outside domain controllers; keep delegation lists minimal; see the [delegation table in the Kerberos doc](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md#delegation) |
| **Active Directory Certificate Services** | Certificates can authenticate as the subject they are issued to, which is powerful by design | Templates that let a low-privileged requester supply their own subject name, or that grant enrollment rights too broadly, let that requester obtain a certificate that authenticates as someone else, including a domain administrator | Audit every certificate template and enrollment permission (tools such as Certipy or PingCastle's certificate module read them); remove requester-supplied subject names from templates that do not need them; restrict enrollment rights |
| **Group Policy** | GPOs can push settings, including local group membership and scheduled tasks, to every computer they apply to | Write or link permissions on a GPO let the holder affect every machine downstream of it, often without needing administrative rights on any single one of them first | Restrict who can edit or link GPOs; monitor GPO changes |
| **Trust relationships** | Domains and forests can trust each other so users can access resources across the boundary | A compromise on one side of a trust can be a path to the other, depending on trust direction and filtering | Understand your trusts; apply SID filtering where appropriate; treat a trusted domain as part of your attack surface |

**Practical implication:** none of these routes is a flaw in Active Directory. Each is a legitimate feature that becomes a problem only when permissions are wider than the task requires. The fix is almost always the same sentence: find out who has more than they need, and take it away.

## Why tier 0 compromise is final

The domain controllers, the `krbtgt` account, the certificate authority and the identity federation servers are collectively called **tier 0**: whoever controls any one of them can, in effect, mint valid credentials for any user in the domain. That is why a confirmed tier 0 compromise is treated as total: the response is not "remove the attacker's access" but "assume every credential and every trust relationship may be forged," which typically means rotating the domain's core secrets and rebuilding from clean systems rather than trying to clean the existing one. The full reasoning is in [Active Directory](../02-systems/03-active-directory.md#containing-ad-the-administrative-model) and the [Kerberos doc](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

## A tiered administration model

The structural defense against this entire chapter is keeping tier 0 small, separate and watched, so that compromising an ordinary workstation or a line-of-business server never gets an attacker closer to it.

| Practice | Effect |
|---|---|
| **Separate administrator accounts** from day-to-day user accounts, with no email or web browsing on the privileged one | A phished workstation does not hand over a privileged credential |
| **Privileged access workstations** for tier 0 administration | Administrative sessions never touch a machine that also runs general software |
| **No credential of a higher tier ever logs on to a lower tier** | Breaks the "harvest a session, climb the tier" pattern entirely |
| **Unique local administrator passwords** (Windows LAPS) | One compromised machine does not unlock every other machine |
| **Minimal, audited group membership** for Domain Admins and equivalent groups | Shrinks the target and makes additions noticeable |
| **Regular graph-based audits** (BloodHound, PingCastle, Purple Knight) against your own domain | Finds the unintended short paths before an attacker's enumeration does |

## Detection themes

| Signal | What it tends to mean |
|---|---|
| A burst of LDAP queries pulling full object and ACL detail from one account in a short time | Enumeration consistent with a graph-collection tool |
| Group membership changes to privileged groups outside change windows | Escalation or persistence |
| Certificate issuance to an unusual subject name, or from a template rarely used | AD CS abuse |
| A new or modified GPO affecting a sensitive OU | Escalation through policy |
| Authentication or replication traffic from a host that is not a domain controller | Possible tier 0 abuse |

These pair with the Kerberos-specific detections (events 4768, 4769, 4771, 4662) already covered in the [Kerberos and enterprise identity doc](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md#detection) and the broader logging approach in [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md).

## Practice

1. Build the lab environment described in [Home lab](../../homelab/README.md) or a small multi-VM Active Directory of your own, and work through a structured, licensed course end to end (Hack The Box Academy's Active Directory modules, or an equivalent) rather than assembling a chain from scattered sources. A guided course pairs every technique with the reasoning and the fix.
2. Run a graph-based audit tool against your lab domain and identify the shortest path to Domain Admins. Fix the single permission or delegation setting that creates it, then re-run the audit and confirm the path is gone.
3. Run PingCastle or Purple Knight against the same lab domain and work through its findings one by one.
4. For every finding in steps 2 and 3, write the detection rule that would have caught it being abused, using the event sources above.
5. Document your hardened lab's tiering model: which accounts are tier 0, which workstations may touch them, and how you verified no lower tier can reach them.

These map to [Module 2.3](../../roadmap/phase-2-guided-practice/03-machines-and-ad.md) of the roadmap, which sequences the licensed courses and lab platforms this topic deserves.

## What to do with this

- [ ] Explain, in your own words, why Active Directory attacks are described as a path rather than a single exploit.
- [ ] Name the four escalation routes in the table above and say what legitimate feature each one abuses.
- [ ] Run a graph-based audit against your lab domain and fix the shortest path it finds.
- [ ] Explain what makes tier 0 different from every other tier, and why its compromise usually means a rebuild.
- [ ] Write the tiered administration model for a domain you control.

## Key references

BloodHound documentation · Microsoft Enterprise Access Model · MITRE ATT&CK · PingCastle documentation · RFC 4120. Full list in [References](../15-references.md).

<!-- navigation -->
[← Privilege escalation](04-privilege-escalation.md) · [Index](../00-start-here.md) · [Red teaming and adversary emulation →](06-red-teaming-and-adversary-emulation.md)
