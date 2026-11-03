# Active Directory

> [!TIP]
> **In short:** Active Directory (AD) is the directory and authentication service behind most corporate Windows networks. It combines an LDAP database of users, computers and groups with Kerberos and NTLM authentication, DNS and Group Policy. Whoever controls it controls every machine and account that trusts it, so it is the main target of ransomware crews and red teams and the most valuable thing to defend. Learn its structure, the permissions that create attack paths, and the tiering model that contains them.

## What AD is made of

| Component | Role |
|---|---|
| **Domain controller (DC)** | A server that holds a writable copy of the directory and authenticates logons. Multiple DCs replicate with each other |
| **Domain** | An administrative unit with its own accounts and policies, for example `corp.example.com` |
| **Forest** | One or more domains that share a schema and configuration. **The forest is the security boundary**, not the domain |
| **Organizational unit (OU)** | A container used to organize objects and to apply policy and delegate administration |
| **Global catalog (GC)** | A partial replica of every domain's objects for forest-wide searches |
| **Site** | A set of well-connected subnets; controls replication and which DC clients use |
| **NTDS.dit** | The directory database file on each DC, containing all account password hashes |
| **SYSVOL** | A replicated share on every DC holding Group Policy files and logon scripts |

Five **FSMO roles** (flexible single master operations) are held by particular DCs: Schema Master and Domain Naming Master (one per forest), and PDC Emulator, RID Master and Infrastructure Master (one per domain). The PDC Emulator matters most day to day: it handles password changes, account lockouts and time synchronization.

### Ports a DC exposes

| Port | Service |
|---|---|
| 53 TCP/UDP | DNS (AD depends on it: clients find DCs through SRV records) |
| 88 | Kerberos |
| 135, and dynamic RPC ports | RPC endpoint mapper and services |
| 389 / 636 | LDAP / LDAP over TLS (LDAPS) |
| 445 | SMB (SYSVOL, NETLOGON, remote administration) |
| 464 | Kerberos password change |
| 3268 / 3269 | Global catalog / global catalog over TLS |
| 5985 / 5986 | WinRM (PowerShell remoting) |
| 9389 | Active Directory Web Services |

## Objects and the attributes that matter

Everything in AD is an object with attributes. The security-relevant ones are worth memorizing.

| Object | Attributes and notes |
|---|---|
| **User** | `sAMAccountName`, `userPrincipalName`, `memberOf`, `servicePrincipalName` (SPN), `userAccountControl`, `pwdLastSet`, `lastLogon` |
| **Computer** | Name ends in `$`; its password is random and changes by default every 30 days; it is a security principal like a user |
| **Group** | Scope domain local, global or universal; security groups grant access, distribution groups do not |
| **GPO** | Group Policy Object: settings plus a container in AD and files in SYSVOL |
| **Service principal name** | Maps a service (`MSSQLSvc/db01.corp.example.com:1433`) to the account that runs it; used by Kerberos |

`userAccountControl` is a bit field whose flags drive many attacks and checks:

| Flag | Hex | Meaning |
|---|---|---|
| `ACCOUNTDISABLE` | 0x2 | Account is disabled |
| `PASSWD_NOTREQD` | 0x20 | Account may have an empty password |
| `DONT_EXPIRE_PASSWORD` | 0x10000 | Password never expires |
| `TRUSTED_FOR_DELEGATION` | 0x80000 | **Unconstrained delegation** |
| `NOT_DELEGATED` | 0x100000 | Account cannot be delegated |
| `DONT_REQ_PREAUTH` | 0x400000 | Kerberos pre-authentication not required (AS-REP roastable) |
| `TRUSTED_TO_AUTH_FOR_DELEGATION` | 0x1000000 | Constrained delegation with protocol transition |

## Permissions on AD objects

Every AD object has an ACL, just like a file. Misconfigured ACLs are one of the most common ways a low-privileged user reaches domain dominance, because permissions chain: right A on object X gives you control of X, which holds right B on Y, and so on. The rights that deserve attention:

| Right on a target object | What it allows |
|---|---|
| `GenericAll` | Full control |
| `GenericWrite` | Write most attributes (for example add an SPN or script path) |
| `WriteDACL` | Change the object's permissions, so grant yourself anything |
| `WriteOwner` | Take ownership, then `WriteDACL` |
| `ForceChangePassword` | Reset the user's password without knowing it |
| `AddMember` / `Self` on a group | Add accounts to the group |
| `DS-Replication-Get-Changes` and `-All` on the domain | Replicate password data from a DC (**DCSync**) |

Tools such as **BloodHound** collect these relationships into a graph and compute the shortest path from any account to a target like Domain Admins. Defenders should run the same analysis against their own domain before an attacker does.

## Privileged groups and Tier 0

Built-in groups with wide power: **Enterprise Admins**, **Domain Admins**, **Schema Admins**, **Administrators**, and the operators groups (Account, Backup, Server, Print operators), plus **DnsAdmins** and Group Policy Creator Owners. Members of protected groups have their ACLs reset on a schedule (the AdminSDHolder process, by default every 60 minutes), which prevents casual permission changes from sticking.

The more useful concept is **Tier 0**: everything that can control the identity system. That includes the DCs and the accounts and groups that administer them, but also anything with a path to them:

- AD CS certificate authorities,
- the Microsoft Entra Connect server and AD FS, which bridge to the cloud,
- backup and virtualization platforms that store or can restore DCs,
- management tooling that runs as SYSTEM on DCs.

If an attacker controls any Tier 0 asset, treat the whole forest as compromised.

## Trusts

A trust lets one domain's users authenticate to resources in another. Domains in the same forest trust each other transitively. Cross-forest and external trusts are explicit. Direction matters (who trusts whom), and **SID filtering** blocks a trusted domain from claiming privileged SIDs it should not hold. Trusts widen the blast radius: a compromised domain with weak filtering can be a bridge into its partners.

## Group Policy

GPOs apply to sites, domains and OUs in the order *local, site, domain, OU* (LSDOU), with later settings overriding earlier ones. Control of a GPO is control of every machine it applies to, so permissions on GPOs are Tier 0 permissions. Two legacy hazards still turn up:

- **Group Policy Preferences passwords.** Older GPOs could set local account passwords and stored them in SYSVOL files (`cpassword`) encrypted with a published key. Microsoft patched the creation of new ones in 2014 (MS14-025), but old files remain in many domains. Any authenticated user can read SYSVOL, so any such password is public. **●●●**
- **Logon scripts with embedded credentials** in NETLOGON.

## Active Directory Certificate Services

AD CS issues certificates that can be used to authenticate to AD (PKINIT). Researchers showed in 2021 that misconfigured certificate templates and CA settings give attackers a route to impersonate any user, including domain admins, and that the technique persists even after passwords change (Schroeder and Christensen, 2021). **●●●** The weaknesses were numbered ESC1 onward, and more have been found since. A typical one (ESC1) is a template that lets the requester supply the subject name and allows client authentication, so a low-privileged user can request a certificate as an administrator.

Defenses: inventory templates and CAs, remove dangerous enrollment rights, require manager approval where appropriate, keep the CA patched and move toward the strong certificate mapping enforcement that Microsoft has been rolling out on DCs (KB5014754).

## Hybrid identity

Most organizations also run Microsoft Entra ID (formerly Azure AD). Accounts are synchronized from AD by Entra Connect, and authentication happens through password hash sync, pass-through authentication or federation. Consequences:

- An attacker with control of on-premises AD, or of the Entra Connect server, may reach cloud resources.
- Cloud-side admin roles must be protected with phishing-resistant MFA and Conditional Access, separate from on-premises accounts.
- Treat the sync server as Tier 0.

## Containing AD: the administrative model

The central defensive idea is **credential hygiene by tier**: powerful credentials must never be exposed on less trusted systems, because anything that can steal a credential from a machine can then use it.

| Practice | Effect |
|---|---|
| **Separate admin accounts** per tier; no daily-use account with admin rights | Phishing a user does not yield an admin |
| **No Tier 0 logons on workstations or servers** (enforced with "deny log on" policies and authentication silos) | Prevents domain admin credentials from landing where they can be stolen |
| **Privileged access workstations (PAWs)** for administration | A clean, dedicated device for sensitive tasks |
| **Just-in-time and just-enough administration** | Rights exist only while needed |
| **Windows LAPS** | Unique, rotating local admin password on every machine |
| **gMSA** for services | Strong, auto-rotating service passwords that resist offline cracking |
| **Protected Users group** and authentication policies | No NTLM or weak Kerberos for privileged accounts; short tickets |
| **Credential Guard** | Secrets in LSASS not readable even by SYSTEM |

Microsoft's current guidance generalizes the older three-tier model into an *enterprise access model* with control, management and workload planes; the principle is unchanged: control-plane assets are isolated from everything below them. **●●○**

## Common weaknesses and what to do

| Weakness | Why it matters | Fix |
|---|---|---|
| Service accounts with SPNs and weak passwords | Kerberoasting: any user can request tickets and crack the password offline | Use gMSA; long random passwords; AES-only encryption types |
| Accounts with "do not require pre-authentication" | AS-REP roasting without credentials | Remove the flag; strong passwords |
| Unconstrained delegation on non-DC hosts | Compromising the host yields tickets for anyone who connects to it | Remove; use constrained or resource-based delegation; put sensitive users in Protected Users |
| Domain admins logging on to workstations and servers | Their credentials are stolen from memory | Tiering and PAWs |
| Shared local administrator password | One compromise opens every machine | Windows LAPS |
| Weak ACLs, stale privileged accounts, nested groups | Hidden paths to Domain Admins | Regular ACL reviews with BloodHound or PingCastle; remove unused accounts |
| LLMNR, NBT-NS and mDNS enabled; SMB and LDAP signing off | Name poisoning and relay attacks | Disable; require signing; enable channel binding |
| Old `krbtgt` password | Forged tickets remain valid | Rotate twice (with replication in between) on a schedule and after an incident |
| Print spooler or other coercible services on DCs | Authentication coercion for relay | Disable the spooler on DCs; patch |
| Misconfigured AD CS | Certificate-based impersonation | Audit with a purpose-built tool; fix templates and CAs |
| Credentials in descriptions, scripts or SYSVOL | Free secrets | Search for them and rotate |

## Detecting trouble: key events

Many AD attacks leave events on the DCs if the relevant audit policies are on (notably *Audit Directory Service Access* and *Audit Directory Service Changes*).

| Event | Meaning | Use |
|---|---|---|
| **4662** with replication GUIDs | An operation on a directory object; with `DS-Replication-Get-Changes(-All)` GUIDs, a replication request | DCSync detection when the source is not a DC |
| **4769** with RC4 ticket encryption for a service account | Service ticket request | Kerberoasting indicator |
| **4768** with pre-authentication type 0 | TGT request without pre-authentication | AS-REP roasting indicator |
| **4728 / 4732 / 4756** | Member added to a group | Alert on privileged groups |
| **4720 / 4738 / 4742** | User created or changed; computer account changed | New or altered privileged accounts |
| **5136** | A directory object was modified | ACL, SPN and script path changes |
| **4624** with unusual logon type for an admin | Where privileged accounts log on | Tier violations |
| **1102 / 104** | Audit log cleared | Defense impairment |

Microsoft Defender for Identity monitors these signals natively. For hygiene reviews, **PingCastle** and **Purple Knight** score the domain's configuration, and **BloodHound Community Edition** maps attack paths.

## How this connects

- The mechanics of Kerberos and NTLM, which underlie most of these attacks, are in [Kerberos, NTLM and enterprise identity](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).
- The attacker's view of the same weaknesses is in [Active Directory attacks](../06-offensive-security/05-active-directory-attacks.md).
- To practice safely, build the domain in your [home lab](../../homelab/README.md) and follow [Module 2.3 of the roadmap](../../roadmap/phase-2-guided-practice/03-machines-and-ad.md).

## What to do with this

- [ ] Draw your lab domain: DCs, OUs, privileged groups, service accounts, trusts.
- [ ] List every account with an SPN and every account with `DONT_REQ_PREAUTH` in your lab.
- [ ] Run BloodHound against the lab and find the shortest path to Domain Admins.
- [ ] Enable the directory service audit policies on the lab DC and trigger event 5136.
- [ ] Write a tiering plan for the lab: which accounts may log on where.

## Key references

BloodHound documentation · Microsoft Learn: Active Directory security best practices · Microsoft Learn: Enterprise access model · MS14-025 · NIST SP 800-53 Rev. 5 · PingCastle · Schroeder and Christensen (2021). Full list in [References](../15-references.md).

<!-- navigation -->
[← Windows internals for security](02-windows-internals-for-security.md) · [Index](../00-start-here.md) · [Memory, corruption bugs and exploit mitigations →](04-memory-and-exploit-mitigations.md)
