# DNS, HTTP and the web stack

> [!TIP]
> **In short:** loading a web page chains four protocols: **DNS** finds the server, **TCP** connects, **TLS** secures the channel and **HTTP** carries the request. Each step is a place where things can be spoofed, intercepted, misconfigured or abused. DNS is trust-based and heavily targeted (poisoning, hijacking, takeover, tunneling). HTTP is stateless text whose security behavior lives in **headers, cookies and origins**. Know the sequence cold; it is the most common interview question in the field and the map for every web attack.

## What happens when you load `https://example.com`

| Step | Protocol | What happens | Where it can go wrong |
|---|---|---|---|
| 1 | **URL parsing** | The browser splits scheme, host, port, path, query and fragment | Look-alike hostnames; parsers that disagree on where the host ends |
| 2 | **DNS** | The name is resolved to an IP address (cache, then recursive resolver) | Poisoned or forged answers; hijacked domain; malicious resolver |
| 3 | **TCP** | Three-way handshake to port 443 | SYN flood; route hijack; blocking |
| 4 | **TLS** | Server presents a certificate; keys are agreed; traffic is encrypted | Invalid or mis-issued certificate; downgrade; interception by a trusted device |
| 5 | **HTTP** | The browser sends the request with headers and cookies | Missing authorization; injection; unsafe headers |
| 6 | **Response and rendering** | Headers, body, scripts and sub-resources load | XSS, clickjacking, mixed content, malicious third-party scripts |

Hold on to this table; the rest of the page unpacks it.

## URLs

```
https://user:pass@www.example.com:8443/path/page?id=7&sort=asc#section
 |        |         |             |    |         |              |
 |        |         |             |    |         query          fragment (never sent to the server)
 |        |         |             |    path
 |        |         |             port
 |        |         host
 |        credentials (deprecated, risky)
 scheme
```

Two practical risks: **parser differentials** (two components that parse the same URL differently, which is the root of many SSRF and open-redirect bugs) and **homograph attacks** (internationalized domain names that use look-alike characters, such as Cyrillic "а" in place of Latin "a").

## DNS

### Resolution

```mermaid
flowchart LR
    app[Application] --> stub[Stub resolver on the OS]
    stub --> rec[Recursive resolver<br/>ISP or 1.1.1.1 / 8.8.8.8]
    rec --> root[Root servers]
    rec --> tld[TLD servers .com]
    rec --> auth[Authoritative server<br/>for example.com]
    auth --> rec
    rec --> stub
```

The recursive resolver does the work and **caches** each answer for the record's **TTL**. A short TTL means fast change; a long one means fast lookups and a long window during which a bad answer persists. Queries use UDP port 53 (TCP for large responses and zone transfers).

### Record types

| Type | Maps | Security notes |
|---|---|---|
| **A / AAAA** | Name to IPv4 / IPv6 address | The core of attacks that redirect users |
| **CNAME** | Name to another name | A CNAME pointing to a deprovisioned service enables **subdomain takeover** |
| **MX** | Mail servers for a domain | Reveals mail providers |
| **NS** | Authoritative name servers | Control of NS records is control of the domain |
| **TXT** | Free text | SPF, DKIM, DMARC, domain-ownership tokens |
| **SOA** | Zone parameters | Serial number, contact |
| **PTR** | IP address to name (reverse) | Used in logs and mail checks |
| **SRV** | Service location | Active Directory locates domain controllers with SRV records |
| **CAA** | Which CAs may issue certificates | Limits mis-issuance |

### Email authentication in DNS

Three TXT-based mechanisms let receivers judge whether a message really comes from a domain.

| Mechanism | Checks | Record |
|---|---|---|
| **SPF** (RFC 7208) | Is the sending IP authorized for this domain? | `v=spf1 include:_spf.provider.com -all` |
| **DKIM** (RFC 6376) | Does the message carry a valid cryptographic signature from the domain? | `selector._domainkey.example.com` |
| **DMARC** (RFC 7489) | Do SPF or DKIM align with the visible From address, and what should the receiver do on failure? | `_dmarc.example.com`: `v=DMARC1; p=reject; rua=mailto:...` |

A DMARC policy of `p=reject` (after monitoring with `p=none`) is what actually stops attackers from sending mail as your domain. **●●●**

### DNS attacks and defenses

| Attack | How it works | Defense |
|---|---|---|
| **Cache poisoning** | Inject a forged answer into a resolver's cache. Dan Kaminsky's 2008 discovery (CVE-2008-1447) showed it was practical against resolvers with predictable query IDs and ports | Randomize source port and query ID; DNSSEC |
| **Domain or registrar hijack** | Compromise the registrar account or change NS records | Registrar lock, MFA on the registrar account, monitoring for DNS changes |
| **Subdomain takeover** | A dangling CNAME points to a cloud service resource that no longer exists; the attacker claims it | Inventory DNS; delete records when decommissioning |
| **Zone transfer exposure** | A server answers `AXFR` requests from anyone and reveals every host | Restrict transfers to secondary servers |
| **DNS tunneling** | Hide data in query names and TXT answers to bypass firewalls (long, high-entropy subdomains) | DNS logging, length and entropy analytics, allow only approved resolvers |
| **Domain generation algorithms (DGA)** | Malware computes thousands of pseudo-random domains to find its controller | Detect NXDOMAIN bursts and algorithmic names; sinkholing |
| **Amplification** | Small spoofed queries cause large responses | Close open resolvers; response rate limiting |
| **DNS rebinding** | A malicious domain changes its answer to a private IP to reach internal services from a browser | Resolver filtering of private ranges; Host header checks |
| **Typosquatting and look-alikes** | Register names close to a real one | Defensive registration, takedowns, user training |

**DNSSEC** signs records so that a validating resolver can verify authenticity and integrity (RFC 4033 to 4035). It does not encrypt anything and does not protect the path between a client and its resolver. **DNS over TLS** (RFC 7858) and **DNS over HTTPS** (RFC 8484) encrypt that last hop, which protects privacy against local observers. They also move DNS out of the network's sight, so organizations should run their own resolvers and steer clients to them. **●●●**

**Practical implication:** DNS logs are one of the best security data sources, since almost everything starts with a lookup. Collect them.

## HTTP

### Anatomy of a request and response

```
GET /invoices/1042 HTTP/1.1
Host: shop.example.com
Cookie: session=7f3a...
Accept: application/json
User-Agent: Mozilla/5.0 ...

HTTP/1.1 200 OK
Content-Type: application/json
Set-Cookie: session=7f3a...; Secure; HttpOnly; SameSite=Lax
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'

{"id":1042,"total":59.90}
```

HTTP is **stateless**: each request stands alone. Anything that looks like a "session" is built on top with cookies or tokens, and every request must be authorized on its own (see [Security principles](../01-foundations/02-security-principles.md), *complete mediation*).

### Methods

| Method | Purpose | Notes |
|---|---|---|
| `GET` | Read a resource | Should not change state; parameters appear in URLs and logs |
| `POST` | Submit data, create | The usual state-changing method |
| `PUT`, `PATCH` | Replace / modify | Often forgotten in access-control checks |
| `DELETE` | Remove | Same |
| `HEAD` | Headers only | Handy for probing |
| `OPTIONS` | Ask what is allowed | Used by CORS preflight |

### Status codes

| Class | Examples |
|---|---|
| 2xx success | 200 OK, 201 Created, 204 No Content |
| 3xx redirect | 301 Moved Permanently, 302 Found, 304 Not Modified, 307 and 308 (method preserved) |
| 4xx client error | 400 Bad Request, **401 Unauthorized** (not authenticated), **403 Forbidden** (authenticated, not allowed), 404 Not Found, 405 Method Not Allowed, 429 Too Many Requests |
| 5xx server error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

Differences between 401, 403 and 404 can leak information (for example, confirming that a hidden page exists), so security-sensitive systems often return the same response in several cases.

### Security-relevant headers

| Header | Purpose |
|---|---|
| `Strict-Transport-Security` (HSTS) | Tells browsers to use HTTPS only for this host for a period; `preload` lists the host in browsers |
| `Content-Security-Policy` (CSP) | Restricts where scripts, styles, frames and other resources may load from; the strongest browser-side defense against XSS |
| `X-Content-Type-Options: nosniff` | Stops browsers guessing content types |
| `X-Frame-Options` / CSP `frame-ancestors` | Prevents your pages from being framed (clickjacking) |
| `Referrer-Policy` | Limits URLs leaked in the `Referer` header |
| `Permissions-Policy` | Disables powerful browser features (camera, geolocation) |
| `Cache-Control` | Controls caching; sensitive pages need `no-store` |
| `Access-Control-Allow-*` | CORS (below) |

The [`http_headers.py`](../../roadmap/phase-0-foundations/exercises/http_headers.py) exercise checks several of these.

### Versions

| Version | Notes |
|---|---|
| **HTTP/1.1** (RFC 9112) | Text, one request at a time per connection (with pipelining and keep-alive) |
| **HTTP/2** (RFC 9113) | Binary, multiplexed streams over one TCP connection; the 2023 "Rapid Reset" attack (CVE-2023-44487) abused stream cancellation to produce record-size denial of service |
| **HTTP/3** (RFC 9114) | Runs on QUIC (RFC 9000) over UDP; faster connection setup, TLS 1.3 built in |

The semantics (methods, headers, status codes) are the same across versions (RFC 9110).

## Cookies

A cookie is a small value the server asks the browser to store and return. They carry sessions, so protecting them protects accounts.

| Attribute | Effect |
|---|---|
| `Secure` | Sent only over HTTPS |
| `HttpOnly` | Not readable by JavaScript, which limits the damage of XSS |
| `SameSite=Strict / Lax / None` | Controls whether the cookie is sent on cross-site requests; `Lax` blocks most CSRF; browsers now treat cookies without the attribute as `Lax` by default |
| `Domain`, `Path` | Scope; broad domains share cookies with every subdomain |
| `Expires` / `Max-Age` | Lifetime |
| `__Host-` prefix | Forces `Secure`, no `Domain`, path `/`, so a sibling subdomain cannot overwrite it |

## The same-origin policy and CORS

An **origin** is scheme plus host plus port. The **same-origin policy** (SOP) is the browser's core isolation rule: a script from one origin cannot *read* responses from another. It does not stop a page from *sending* requests to other origins (an image, form post or fetch is still sent), which is exactly why **CSRF** exists and why `SameSite` cookies and anti-CSRF tokens are needed.

**Cross-Origin Resource Sharing (CORS)** lets a server deliberately relax the SOP for chosen origins with `Access-Control-Allow-Origin`. The classic mistakes:

- Reflecting any `Origin` value back, with `Access-Control-Allow-Credentials: true`, so any website can read authenticated responses.
- Allowing the `null` origin.
- Trusting a wildcard on subdomains that include user content.

The browser enforces SOP and CORS, not the server; a command-line tool ignores both.

## Intermediaries: proxies, CDNs and WAFs

Most traffic goes through one or more intermediaries: forward proxies, reverse proxies and load balancers, content delivery networks and web application firewalls. They bring security benefits (hiding origins, absorbing DDoS, filtering) and security problems.

| Issue | Description |
|---|---|
| **Client IP trust** | The app sees the proxy's address and relies on `X-Forwarded-For`, which a client can forge unless the proxy overwrites it |
| **Origin exposure** | If the origin server's IP is public, attackers can bypass the CDN or WAF entirely |
| **Request smuggling** | Front and back ends disagree on where a request ends (`Content-Length` versus `Transfer-Encoding` in HTTP/1.1, or unsafe HTTP/2 downgrades), letting an attacker prefix another user's request |
| **Cache poisoning and deception** | Making a shared cache store a malicious or private response and serve it to others |
| **Host header attacks** | Applications that trust `Host` to build links or route requests |

**Practical implication:** the security of a web application depends on the *whole chain*. When you test or review, map every hop and find out what each one trusts.

## Tools

| Task | Tool |
|---|---|
| Query DNS | `dig`, `nslookup`; `dig +trace` follows the delegation chain |
| See an HTTP exchange | `curl -v`, browser developer tools (Network tab) |
| Intercept and modify HTTP | Burp Suite or OWASP ZAP |
| Inspect TLS | `openssl s_client -connect host:443`, `testssl.sh` |
| Look at everything | Wireshark |

```bash
dig example.com A +short
dig example.com MX
dig +trace example.com
curl -sv https://example.com -o /dev/null
```

## What to do with this

- [ ] Run `dig +trace` for a domain and name each server in the chain.
- [ ] Look up the SPF, DKIM and DMARC records of three organizations and judge their policies.
- [ ] Capture one page load and mark the DNS query, TCP handshake, TLS handshake and HTTP request.
- [ ] Write the "what happens when I load a URL" page from memory, as in [Module 0.4, week 8](../../roadmap/phase-0-foundations/04-networking.md).
- [ ] Use browser developer tools to list the cookies and security headers of a site you use.

## Key references

Kaminsky (2008) · RFC 1035 · RFC 4033 · RFC 6265 · RFC 6797 · RFC 7208 · RFC 7489 · RFC 7858 · RFC 8484 · RFC 9000 · RFC 9110 · RFC 9112 · RFC 9113 · RFC 9114 · OWASP HTTP Headers Cheat Sheet. Full list in [References](../15-references.md).

<!-- navigation -->
[← TCP, UDP, ICMP and routing](02-tcp-udp-and-routing.md) · [Index](../00-start-here.md) · [Network defense architecture →](04-network-defense-architecture.md)
