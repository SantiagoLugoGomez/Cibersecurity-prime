# Reconnaissance and enumeration

> [!TIP]
> **In short:** most of a test's success is decided before any exploit runs. **Reconnaissance** maps what an organization exposes: domains, hosts, services, people, technologies, forgotten assets. **Enumeration** then extracts detail from each exposed service: versions, accounts, shares, endpoints, misconfigurations. Work from **passive** (no contact with the target) to **active** (probing it), keep an organized map, and notice what is *unexpected*, because the forgotten test server or the exposed admin console is usually the way in. Defenders can run the same techniques first and close what they find.

> [!CAUTION]
> Passive research on public information is low risk. Active scanning and enumeration touch someone's systems and need written authorization. Keep personal data you encounter (employee names, leaked credentials, exposed records) inside the scope and the rules of engagement, and report open exposures instead of exploring them. See [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md).

## Passive and active

| | Passive | Active |
|---|---|---|
| **Contact with target** | None, or only normal public requests | Probes sent to the target's systems |
| **Examples** | Certificate logs, DNS records from public sources, search engines, code repositories, internet scan databases | Port scans, directory brute force, banner grabbing, authentication attempts |
| **Detectable by the target** | Rarely | Often (logs, IDS, rate limits) |
| **Authorization** | Still follows scope and law | Required in writing |

ATT&CK groups these steps under the **Reconnaissance** tactic (TA0043). **●●●**

## Passive reconnaissance

| Source | What it reveals | Tools |
|---|---|---|
| **Domain registration** (WHOIS, RDAP) | Name servers, registrar, dates; the registrant is often redacted | `whois`, registry lookups |
| **DNS** | Hosts and their roles: A, AAAA, MX, NS, CNAME, TXT, SRV. TXT records disclose mail providers (SPF) and SaaS in use (domain-verification strings) | `dig`, `host`, `dnsx` |
| **Certificate Transparency logs** | Every publicly trusted certificate issued for the domain, including **internal-looking subdomain names**; the logs are public by design (RFC 6962) | crt.sh, Censys, `subfinder` |
| **Internet scan databases** | Exposed services, banners, versions and certificates collected by continuous scanning | Shodan, Censys (free tiers exist and change; check current limits) |
| **Search engines** | Exposed files and login pages through operators (`site:`, `filetype:`, `inurl:`, `intitle:`); the Google Hacking Database collects examples | Search operators, GHDB |
| **Code and document leaks** | Keys, endpoints and internal names in public repositories, packages, paste sites, public API workspaces, container images, open storage buckets | GitHub code search, secret scanners |
| **Document metadata** | Author names, software versions, internal paths in PDFs, Office files and images | `exiftool` |
| **Web archives** | Old pages, removed endpoints and files | Wayback Machine |
| **Network ownership** | IP ranges owned by the organization (autonomous system numbers); in Latin America registrations come from LACNIC | BGP toolkits, regional registry |
| **Job postings and press** | Technology stack, vendors, projects | Reading |
| **People** | Naming conventions for e-mail, roles, exposure to social engineering | Only when explicitly in scope |
| **Breach corpora** | Whether the organization's addresses appear in leaks | Have I Been Pwned for domain owners |

A first pass on a domain **you own or are authorized to test**:

```bash
whois example.com
dig +short NS example.com
dig +short MX example.com
dig +short TXT example.com
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sort -u
subfinder -d example.com -silent
```

Frameworks that combine sources include OWASP Amass, theHarvester, Recon-ng and SpiderFoot. For people-oriented OSINT, Bazzell's book is the standard text (Bazzell, 2023). Treat what the tools return as leads to **verify**, not as facts.

## Active reconnaissance

### Hosts and ports

Discovery and port scanning with Nmap are covered in [Traffic analysis and scanning](../03-networking/05-traffic-analysis-and-scanning.md). The principle: start broad and cheap (which hosts are alive?), then go deep and targeted (all ports on interesting hosts; versions and scripts on open ports), and save every output.

### DNS

| Technique | Notes |
|---|---|
| **Zone transfer** (`AXFR`) | A misconfigured name server returns the entire zone to anyone who asks: `dig axfr example.com @ns1.example.com`. Rare today, instant jackpot when found |
| **Subdomain brute force** | Resolve candidate names from a wordlist; detect wildcard DNS first, or every name appears to exist |
| **Reverse lookups** | Resolve IP ranges back to names |
| **Virtual host discovery** | One IP serves many sites by `Host` header; fuzz the header to find hidden ones |

### Web content

1. **Fingerprint** the technology: response headers, cookie names, error pages, default files, favicon hashes (`whatweb`, browser extensions).
2. **Read what the site volunteers**: `/robots.txt`, `/sitemap.xml`, `/.well-known/`, `/security.txt`, HTML comments, **JavaScript files and source maps** (endpoints, API paths, keys), API descriptions (`/openapi.json`, `/swagger.json`).
3. **Discover content** that is not linked, with wordlists such as [SecLists](https://github.com/danielmiessler/SecLists):

```bash
ffuf -u http://10.10.20.50/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -mc 200,204,301,302,307,401,403 -rate 50
ffuf -u http://10.10.20.50/ -H "Host: FUZZ.lab.local" -w subdomains.txt -fs 1234
```

4. **Map parameters, roles and workflows** by using the application normally through an intercepting proxy before you fuzz anything.

Control your request rate. Aggressive fuzzing against a fragile or shared server is a form of denial of service.

## Service enumeration

For each open port, learn what runs, which version, and whether it is configured safely. Run these only against your lab or authorized targets.

| Port | Service | What to check | Example (lab) |
|---|---|---|---|
| 21 | FTP | Anonymous login, writable directories, version | `nmap --script ftp-anon -p21 HOST` |
| 22 | SSH | Version, password authentication allowed, weak algorithms | `ssh-audit HOST` |
| 25, 587 | SMTP | Banner, user enumeration (`VRFY`, `EXPN`), open relay, STARTTLS | `nmap --script smtp-commands -p25 HOST` |
| 53 | DNS | Zone transfer, recursion, version | `dig axfr example.com @HOST` |
| 80, 443, 8080 | HTTP(S) | Technology, content, admin consoles (Tomcat, Jenkins, Jupyter), TLS settings | see above; `testssl.sh HOST` |
| 88 | Kerberos | Indicates a domain controller; user existence can be checked | `nmap -p88 --script krb5-enum-users ...` |
| 111, 2049 | RPC, NFS | Exported shares, `no_root_squash` | `showmount -e HOST` |
| 135, 139, 445 | RPC, NetBIOS, SMB | Null or guest sessions, shares, signing required, SMBv1, OS version | `smbclient -L //HOST -N`, `nxc smb HOST` |
| 161 (UDP) | SNMP | Default community strings; system, process and network data | `snmpwalk -v2c -c public HOST` |
| 389, 636, 3268 | LDAP | Anonymous bind, naming contexts, users and groups | `ldapsearch -x -H ldap://HOST -s base namingContexts` |
| 1433, 3306, 5432, 1521 | SQL databases | Exposure, default credentials, version | `nmap -sV -p PORT HOST` |
| 6379, 27017, 9200 | Redis, MongoDB, Elasticsearch | Unauthenticated access to data | `nmap --script redis-info -p6379 HOST` |
| 3389 | RDP | Network Level Authentication enabled, exposure | `nmap --script rdp-enum-encryption -p3389 HOST` |
| 5985, 5986 | WinRM | Exposure of remote management | `nmap -p5985,5986 HOST` |
| 2375, 6443, 10250 | Docker API, Kubernetes API and kubelet | Unauthenticated access is typically critical | `nmap -sV -p PORT HOST` |

**Practical implication:** an open port is not a finding. A *reachable service that should not be reachable, or that accepts anonymous access, or that runs a known-vulnerable version* is. Compare what you find with what should exist.

## Organize as you go

A map you can read beats a folder of output files.

| Host | Port / service | Version | Notes | Source | Next step |
|---|---|---|---|---|---|
| 10.10.20.50 | 445 SMB | Samba 4.x | Guest share `public` readable | `smbclient` | Check files for credentials |
| 10.10.20.50 | 8080 HTTP | Jenkins 2.x | Login page, no lockout seen | browser | Review version advisories |

Prioritize leads by this order of questions:

1. Is there **anonymous or default access**?
2. Is an **administrative interface** exposed?
3. Is a service **old enough to have known critical vulnerabilities** (check the CISA KEV catalog and vendor advisories)?
4. Did enumeration reveal **credentials, usernames or secrets** that can be tried elsewhere (within scope)?
5. Is the asset **forgotten**: a test server, an old subdomain, an unpatched appliance?

## What reconnaissance shows about you (the defender's view)

| Finding | Why it matters | Fix |
|---|---|---|
| Internal names in certificate transparency logs | Reveals structure and targets | Use an internal certificate authority for internal names; avoid sensitive names in public certificates |
| **Dangling DNS records** (a `CNAME` pointing to a deleted cloud resource) | **Subdomain takeover**: an attacker claims the resource and serves content from your domain | Inventory DNS; remove records when you decommission; monitor with scanners that check for takeover signatures |
| Exposed admin panels, databases, remote management | Direct attack surface | Put behind VPN or zero-trust access; allowlist; require MFA |
| Secrets in public repositories and packages | Direct credentials | Secret scanning, push protection, rotation; see [Secure development](../05-application-security/06-secure-development-and-supply-chain.md) |
| Software version banners | Helps targeting (not a vulnerability by itself) | Minimize, but do not rely on hiding |
| Document metadata | Names, software, internal paths | Strip metadata before publishing |
| Unmanaged cloud storage and forgotten test environments | Data exposure | Cloud posture management, asset inventory |
| Wildcard DNS and zone transfers enabled | Information and takeover risk | Restrict transfers to known secondaries |

| Defensive measure | How |
|---|---|
| **Run your own reconnaissance regularly** | Passive and active, from the internet's point of view, and diff against the previous run |
| **Monitor certificate issuance** for your domains | Certificate transparency monitors alert on unexpected certificates |
| **External attack surface management** | Tools and services that continuously discover and rank your exposed assets |
| **Alert on internal scanning** | Scans from inside are far more suspicious than internet noise |
| **Keep honeytokens** | Fake credentials and records that alert when touched |

## Practice

1. Passively map a domain **you own** (register a cheap one for the lab). List every subdomain, name server, mail provider and technology, then check each against what you intended to expose.
2. Query crt.sh for your domain and for a large organization's *public* name, and note what certificate logs reveal.
3. In your isolated lab, enumerate every service on Metasploitable 2 using the table above, and write an asset map with one next step per finding. The machine is documented in the [Metasploit documentation](https://docs.rapid7.com/metasploit/metasploitable-2/).
4. Run `ffuf` against a deliberately vulnerable web application in the lab, tune the filters, and find three endpoints that are not linked from the page.
5. Work through the Hack The Box Academy modules *Information Gathering - Web Edition* and *Network Enumeration with Nmap*.
6. Write a detection rule or query for "many 404 responses from one client in a short window" and test it against your own scan.

These support [Module 0.4](../../roadmap/phase-0-foundations/04-networking.md), [Module 2.1](../../roadmap/phase-2-guided-practice/01-ctf-foundations.md) and [Module 2.3](../../roadmap/phase-2-guided-practice/03-machines-and-ad.md) of the roadmap.

## What to do with this

- [ ] Explain the difference between passive and active reconnaissance, and give an example of each that is still subject to law.
- [ ] Build a personal enumeration checklist from the service table above, and refine it after each lab.
- [ ] Run a passive reconnaissance report on your own domain and fix one thing it shows.
- [ ] Describe subdomain takeover and how to prevent it.
- [ ] Record the commands, outputs and decisions of one complete enumeration in your notes.

## Key references

Bazzell (2023) · Lyon (2009) · MITRE ATT&CK · OWASP Web Security Testing Guide · RFC 6962 · SecLists. Full list in [References](../15-references.md).
