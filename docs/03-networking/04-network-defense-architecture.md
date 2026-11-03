# Network defense architecture

> [!TIP]
> **In short:** the old model of a hard perimeter around a soft interior no longer matches how organizations work, because users, apps and data are everywhere. Modern network defense combines **segmentation** (limit how far an intruder can move), **filtering** at several layers, **encrypted and authenticated access** (VPNs, zero trust), **monitoring** and **resilient design**. A design is good when the compromise of one host is a small incident rather than a total one. The tools differ by vendor; the architecture patterns are what you need to learn.

## From perimeter to segments

The traditional design had an outside (internet), a **DMZ** (servers that must be reachable) and an inside (everything else), separated by a firewall. Inside, everything could talk to everything. That is why one phished laptop could lead to the file servers, the domain controllers and the backups.

The modern idea is to divide the network into **zones** by function and trust, and to control the flows between zones explicitly.

| Zone | Contains | Rules of thumb |
|---|---|---|
| **Internet-facing / DMZ** | Reverse proxies, web servers, mail gateways, VPN endpoints | Only required ports inbound; no direct path to internal databases |
| **User networks** | Workstations, printers, Wi-Fi | No inbound from other user subnets; outbound through a proxy or filter |
| **Server networks** | Application and file servers | Reachable only from the services that need them |
| **Data / database tier** | Databases, storage | Only the application tier can connect; no internet access |
| **Management network** | Hypervisors, switches, out-of-band controllers, jump hosts | Access only from privileged workstations; strongly authenticated |
| **Identity tier (Tier 0)** | Domain controllers, PKI, secrets stores | The most restricted zone (see [Active Directory](../02-systems/03-active-directory.md)) |
| **Guest / IoT / OT** | Visitor Wi-Fi, cameras, building and industrial systems | Isolated; internet only, or specific vendor paths |

Segmentation is implemented with **VLANs and subnets plus firewall rules**, with **host-based firewalls**, with **micro-segmentation** in virtual and cloud environments, or with **identity-aware proxies**. The question to ask of any flow is "does this need to exist?".

**Practical implication:** the single highest-value network change in many organizations is blocking workstation-to-workstation traffic (SMB, RDP, WinRM). It removes the main route for lateral movement and ransomware spread, and few legitimate workflows need it.

## Firewalls and filtering

| Technology | What it examines | Strengths | Limits |
|---|---|---|---|
| **Packet filter / ACL** | Source, destination, port, protocol, per packet | Fast, simple | No connection memory |
| **Stateful firewall** | Packets plus the state of the connection | Allows replies to permitted outbound sessions; the baseline | Does not understand applications |
| **Next-generation firewall (NGFW)** | Applications, users, URL categories, sometimes TLS inspection and IPS | Policy by application and identity | Complexity; inspection of encrypted traffic is intrusive and costly |
| **Web application firewall (WAF)** | HTTP requests and responses | Blocks common web attack patterns; virtual patching | Bypassable; not a substitute for fixing the application |
| **Host firewall** | Traffic to and from one machine | Works where the network cannot see | Needs central management |
| **DNS filtering / secure web gateway** | Domains and URLs | Cheap, effective against known-bad destinations and phishing | Evaded by new infrastructure |

### Writing good rules

- **Default deny**, then allow what is needed (see [Security principles](../01-foundations/02-security-principles.md), *fail-safe defaults*).
- **Filter egress as well as ingress.** Outbound controls limit command-and-control and data exfiltration. A database server rarely needs to initiate connections to the internet.
- Name rules after their purpose and owner, and review them regularly. Old "temporary" rules accumulate.
- Log denied traffic at the boundaries; unusual denials are a detection signal.
- Block unnecessary protocols between internal zones: SMB, RDP, SSH and database ports are the usual suspects.

## Remote access: VPNs and beyond

| Option | How it works | Notes |
|---|---|---|
| **IPsec** (RFC 4301) | Network-layer tunnels (IKEv2 for keys, ESP for data) | Common for site-to-site links and some clients; complex to configure |
| **WireGuard** | Small, modern UDP-based tunnel with fixed, modern cryptography | Simple configuration, fast, easy to audit |
| **OpenVPN / TLS-based VPNs** | User-space tunnel over TLS | Widely supported; flexible |
| **Clientless / reverse proxy access** | Applications published through an authenticating proxy | Reduces network-level exposure |

VPN gateways are exposed, high-privilege devices, and their vulnerabilities have been among the most exploited by ransomware crews and state actors in recent years (CISA's Known Exploited Vulnerabilities catalog lists many). Patch them first, require MFA and monitor their logs. **●●○**

### Zero trust in practice

NIST describes zero trust as an architecture in which no request is trusted because of its network location; every access is authenticated and authorized using identity, device health and context, and it is evaluated per session (NIST SP 800-207). **●●●** The components are:

- a **policy engine** that decides,
- a **policy enforcement point** (an access proxy, firewall or agent) that applies the decision,
- **signals** about the user, the device (patched, encrypted, managed) and the request.

You can adopt it gradually: put MFA and device checks in front of applications, replace broad VPN access with per-application access, segment the network, and log everything the policy engine decides. It is a direction of travel, not a purchase.

## Wireless

| Standard | Notes |
|---|---|
| **WEP** | Broken; never use |
| **WPA2-Personal (PSK)** | Acceptable with a long passphrase, but a captured handshake can be cracked offline, so weak passphrases fall |
| **WPA3-Personal (SAE)** | Resists offline guessing and gives forward secrecy; use where supported |
| **WPA2/WPA3-Enterprise (802.1X, EAP)** | Per-user or per-device credentials via a RADIUS server; the right choice for organizations; prefer certificate-based EAP-TLS |

Other points: isolate guest networks, disable WPS, watch for rogue access points and "evil twin" networks, and avoid shared passphrases for staff. Public Wi-Fi is hostile territory; a VPN and TLS everywhere are the personal defense.

## Detection and visibility

You cannot defend traffic you cannot see. Core sources:

| Source | Shows |
|---|---|
| **Firewall and proxy logs** | Allowed and denied connections, URLs, volumes |
| **DNS logs** | Every name looked up, a rich signal for malware and tunneling |
| **NetFlow / IPFIX** | Metadata about flows (who talked to whom, how much) at low cost |
| **IDS/IPS** (Suricata, Snort) | Signature-based alerts on known-bad patterns |
| **Network security monitoring** (Zeek) | Detailed per-protocol logs (connections, DNS, HTTP, TLS, files) for investigation and hunting |
| **Full packet capture** | The ultimate evidence; expensive, so used at choke points and on demand |

Zeek and Suricata complement each other: Suricata alerts on known signatures, Zeek writes rich logs you can search after the fact. Both are free and are included in Security Onion. See [Traffic analysis and scanning](05-traffic-analysis-and-scanning.md) and [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md).

**Encrypted traffic** limits payload inspection. Defenders compensate with metadata (domains, certificates, JA3/JA4 TLS fingerprints, volume and timing patterns), endpoint telemetry and, where policy and law allow, controlled TLS inspection at a gateway. Newer protocol features, such as Encrypted Client Hello (RFC 9849), further reduce what a network observer sees, which pushes defense toward the endpoint and identity. **●●○**

## Resilience

Availability needs design, not hope.

- **Redundancy** for links, devices and sites; no single point of failure for critical paths.
- **DDoS protection**: anycast CDNs and scrubbing services for internet-facing assets, rate limiting, capacity planning.
- **Backups and recovery** that are offline or immutable and tested (see [Hardening and resilience](../07-defensive-security/08-hardening-and-resilience.md)).
- **Out-of-band management** so you can fix the network when it is down.
- **Documented, rehearsed failover.**

## A reference design for a small organization

Even with a small budget, you can apply the principles.

1. Separate **guest**, **staff**, **servers** and **management** into different VLANs with a firewall between them.
2. Allow **no inbound** connections from the internet except through a reverse proxy or a VPN with MFA.
3. Block **SMB, RDP and WinRM** between workstations; allow admin access only from a management host.
4. Send **DNS** through a filtering resolver and block direct outbound DNS from other devices.
5. Use **WPA3** or WPA2/3-Enterprise for staff Wi-Fi.
6. Log firewall, DNS and authentication events centrally and review alerts.
7. Keep **offline backups** and test a restore twice a year.

Build this in your lab with OPNsense as described in the [home lab guide](../../homelab/README.md) and [Module 0.4, week 9](../../roadmap/phase-0-foundations/04-networking.md).

## What to do with this

- [ ] Draw a network zone diagram for a small company and mark every allowed flow between zones.
- [ ] Write a firewall rule set in OPNsense for the zones in your lab, default deny, and test it with Nmap.
- [ ] Explain the difference between a stateless filter, a stateful firewall and a WAF in two sentences each.
- [ ] Review three of your own accounts or devices for Wi-Fi and VPN settings and fix one.
- [ ] Read the executive summary of NIST SP 800-207 and list three zero trust practices you can apply to your lab.

## Key references

CISA KEV Catalog · Donenfeld (2017) · NIST SP 800-41 Rev. 1 · NIST SP 800-207 · RFC 4301 · RFC 9849. Full list in [References](../15-references.md).

<!-- navigation -->
[← DNS, HTTP and the web stack](03-dns-http-and-the-web-stack.md) · [Index](../00-start-here.md) · [Traffic analysis and scanning →](05-traffic-analysis-and-scanning.md)
