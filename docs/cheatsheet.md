# Cheat sheet

> [!TIP]
> A single dense reference page: the commands, tables and numbers you look up constantly, with no explanation. Read the linked doc page for the reasoning, the evidence and the warnings; come here only when you already know what you are doing and just need the exact syntax or number. Everything here assumes you are working in your own lab or an authorized engagement.

## Networking

**Private IPv4 ranges (RFC 1918):** `10.0.0.0/8` · `172.16.0.0/12` · `192.168.0.0/16`. Loopback: `127.0.0.0/8`. Link-local: `169.254.0.0/16`.

**CIDR quick table**

| /CIDR | Mask | Hosts |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /30 | 255.255.255.252 | 2 |

**Common ports:** 20/21 FTP · 22 SSH · 23 Telnet · 25 SMTP · 53 DNS · 67/68 DHCP · 80 HTTP · 88 Kerberos · 110 POP3 · 111 RPC · 123 NTP · 135 MSRPC · 137-139 NetBIOS · 143 IMAP · 161/162 SNMP · 389 LDAP · 443 HTTPS · 445 SMB · 464 Kerberos password change · 465/587 SMTPS/submission · 514 syslog · 636 LDAPS · 993 IMAPS · 995 POP3S · 1433 MSSQL · 1521 Oracle · 2049 NFS · 3268/3269 Global Catalog · 3306 MySQL · 3389 RDP · 5432 PostgreSQL · 5985/5986 WinRM · 6379 Redis · 8080/8443 HTTP(S) alt · 9200 Elasticsearch · 27017 MongoDB.

**HTTP status codes:** 200 OK · 201 Created · 301/302 Redirect · 304 Not Modified · 400 Bad Request · 401 Unauthorized · 403 Forbidden · 404 Not Found · 405 Method Not Allowed · 409 Conflict · 429 Too Many Requests · 500 Internal Server Error · 502 Bad Gateway · 503 Service Unavailable.

**tcpdump / Wireshark display filters:** see [Traffic analysis and scanning](03-networking/05-traffic-analysis-and-scanning.md#display-filters-you-will-use-constantly).

```bash
nmap -sn 10.10.20.0/24 -oA out/discovery           # host discovery
sudo nmap -p- --min-rate 1000 -T4 TARGET -oA out/all
sudo nmap -sV -sC -p 22,80,445 TARGET -oA out/detail
dig +short NS/MX/TXT/AXFR example.com @ns1.example.com
```

Full detail: [Models and addressing](03-networking/01-models-and-addressing.md) · [TCP, UDP and routing](03-networking/02-tcp-udp-and-routing.md) · [Traffic analysis and scanning](03-networking/05-traffic-analysis-and-scanning.md).

## Linux first commands

```bash
id; whoami; hostname; uname -a
sudo -l
find / -xdev -perm -4000 -type f 2>/dev/null        # SUID
getcap -r / 2>/dev/null                              # capabilities
cat /etc/crontab; ls -la /etc/cron.*
ss -tulpn
history; cat ~/.bash_history
```

See [Linux for security](02-systems/01-linux-for-security.md) · [Privilege escalation](06-offensive-security/04-privilege-escalation.md).

## Windows first commands

```powershell
whoami /all
Get-LocalGroupMember Administrators
schtasks /query /fo LIST /v
Get-CimInstance Win32_Service | Select Name,PathName,StartMode
wmic service get name,pathname,startmode
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
klist
```

Key event IDs: 4624 logon · 4625 failed logon · 4648 explicit creds · 4672 special privileges · 4688 process creation · 4698 scheduled task created · 4720 account created · 4732 added to local group · 4768/4769/4771 Kerberos TGT/service ticket/preauth failure · 4776 NTLM validation · 5136 directory object modified · 7045 service installed.

See [Windows internals for security](02-systems/02-windows-internals-for-security.md) · [Active Directory](02-systems/03-active-directory.md) · [Kerberos, NTLM and enterprise identity](04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md).

## Cryptography and TLS

```bash
openssl genpkey -algorithm ED25519 -out key.pem
openssl req -new -x509 -key key.pem -out cert.pem -days 365
openssl x509 -in cert.pem -noout -text
openssl s_client -connect host:443 -servername host
testssl.sh host:443
sha256sum file; echo -n "text" | sha256sum
```

| Algorithm | Use | Status |
|---|---|---|
| AES-256-GCM | Symmetric encryption | Current standard |
| ChaCha20-Poly1305 | Symmetric encryption | Current, good on low-power devices |
| Argon2id | Password hashing | Current recommendation |
| SHA-256 / SHA-3 | General hashing | Current |
| MD5, SHA-1 | Any security use | Broken, do not use |
| RSA 2048+ / ECDSA P-256 / Ed25519 | Signatures and key exchange | Current |
| ML-KEM (FIPS 203) | Post-quantum key exchange | Current standard |

Password entropy: `bits = length x log2(alphabet size)`. NIST SP 800-63B-4: 15 chars minimum single-factor, 8 with MFA, allow 64+, no composition rules, no forced rotation.

See [Cryptography foundations](04-cryptography-and-identity/01-cryptography-foundations.md) · [TLS in depth](04-cryptography-and-identity/03-tls-in-depth.md) · [Passwords and MFA](04-cryptography-and-identity/04-passwords-and-mfa.md).

## Web and API

**OWASP Top 10:2025:** A01 Broken Access Control (incl. SSRF) · A02 Security Misconfiguration · A03 Software Supply Chain Failures · A04 Cryptographic Failures · A05 Injection · A06 Insecure Design · A07 Authentication Failures · A08 Software/Data Integrity Failures · A09 Security Logging & Alerting Failures · A10 Mishandling of Exceptional Conditions.

**Security headers baseline:**

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Content-Security-Policy: default-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'
```

**Cookie baseline:** `Set-Cookie: __Host-session=...; Path=/; Secure; HttpOnly; SameSite=Lax`

See [The OWASP Top 10:2025](05-application-security/02-owasp-top-10-2025.md) · [Browser security model and headers](05-application-security/01-browser-security-model-and-headers.md) · [Injection and XSS](05-application-security/03-injection-and-xss.md) · [API security](05-application-security/05-api-security.md).

## Vulnerability scoring and prioritization

| Signal | Range | Meaning |
|---|---|---|
| CVSS v4.0 | 0.1-10.0 | Technical severity (0.1-3.9 low, 4.0-6.9 medium, 7.0-8.9 high, 9.0-10.0 critical) |
| EPSS | 0-1 (probability) | Likelihood of exploitation in the next 30 days |
| CISA KEV | listed / not listed | Confirmed real-world exploitation; fix first if exposed |

Priority order: exposed + in KEV → high EPSS + exposed → high CVSS on a valuable asset → everything else on a routine cycle. Full reasoning: [Vulnerabilities and exploitation](06-offensive-security/03-vulnerabilities-and-exploitation.md) · [Vulnerability and exposure management](07-defensive-security/07-vulnerability-and-exposure-management.md).

## MITRE ATT&CK tactics (v19)

Reconnaissance (TA0043) · Resource Development (TA0042) · Initial Access (TA0001) · Execution (TA0002) · Persistence (TA0003) · Privilege Escalation (TA0004) · Stealth (TA0005) · Defense Impairment (TA0112) · Credential Access (TA0006) · Discovery (TA0007) · Lateral Movement (TA0008) · Collection (TA0009) · Command and Control (TA0011) · Exfiltration (TA0010) · Impact (TA0040).

See [Adversaries and attack frameworks](01-foundations/04-adversaries-and-attack-frameworks.md).

## Incident first actions

1. Scope before you evict: confirm what else is touched before killing access anywhere.
2. Preserve volatile evidence first (memory, network state), then disk, per the order of volatility.
3. Declare severity and name an incident commander.
4. Contain with the smallest action that stops the specific harm.
5. Notify per your legal obligations' actual deadlines (verify current figures, do not assume).
6. Write the postmortem with named owners and deadlines on every action item.

See [Incident response](07-defensive-security/04-incident-response.md) · [Digital forensics](07-defensive-security/05-digital-forensics.md).

## Regular expressions, quick reference

| Pattern | Matches |
|---|---|
| `.` | Any character except newline |
| `*` / `+` / `?` | 0+ / 1+ / 0-1 of the preceding |
| `^` / `$` | Start / end of line |
| `[abc]` / `[^abc]` | Any of / none of |
| `(a\|b)` | Alternation |
| `\d` `\w` `\s` | Digit, word character, whitespace |
| `{n,m}` | Between n and m repetitions |

Catastrophic backtracking risk: nested quantifiers like `(a+)+` on adversarial input (ReDoS). See [Injection and XSS](05-application-security/03-injection-and-xss.md).

## Git, for your notes and portfolio

```bash
git init; git add -A; git commit -m "message"
git checkout -b branch-name
git log --oneline --graph
git diff; git stash; git stash pop
```

See [The study system](11-learning-and-career/02-the-study-system.md).

## File signatures (magic bytes)

| Hex | Type |
|---|---|
| `4D 5A` | Windows PE executable (`MZ`) |
| `7F 45 4C 46` | Linux ELF executable |
| `50 4B 03 04` | ZIP (also DOCX, XLSX, JAR, APK) |
| `25 50 44 46` | PDF |
| `89 50 4E 47` | PNG |
| `FF D8 FF` | JPEG |
| `D0 CF 11 E0` | Legacy Office (DOC, XLS) |

See [Static analysis](09-malware-and-reverse-engineering/03-static-analysis.md).

## Study system quick reference

| Mode | Weekly time | What runs |
|---|---|---|
| Green | ~7.5 h | R, P, D, E all run |
| Yellow | ~4 h | R + flashcards + one of P/D |
| Red | ~1.5-2 h | R + flashcards only |
| Pause | 0 h | Nothing, with a written resume plan |

See [Study load modes](11-learning-and-career/03-study-load-modes.md).

## What to do with this

- [ ] Print or pin this page somewhere visible during lab sessions.
- [ ] Add your own most-repeated command or lookup to a personal addendum once you notice yourself searching for it twice.
- [ ] Use this as the starting point for flashcards on anything you still cannot recall without looking it up.

## Key references

Every section's linked page carries its own Key references line. Full list in [References](15-references.md).
