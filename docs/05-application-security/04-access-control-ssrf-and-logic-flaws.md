# Access control, SSRF and logic flaws

> [!TIP]
> **In short:** these are the flaws where every request looks valid and the application still does something it should not. Access control bugs let one user act on another's objects (covered in [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md)). This page covers the neighbouring families: **path traversal and file handling**, **server-side request forgery (SSRF)**, which turns your server into the attacker's browser inside your network, and **business logic flaws**, where the process itself can be abused. Scanners find few of them. You find them by understanding what the application is *supposed* to allow, then asking how to violate that with perfectly formed requests.

> [!CAUTION]
> Test only your own lab applications and authorized targets. Probing internal addresses through someone else's server is an attack on that organization's network.

## Path traversal and file access

A **path traversal** bug lets a user control which file the server reads or writes, usually through `../` sequences in a file name parameter.

```
GET /download?file=../../../../etc/passwd
```

| Variation | Why a naive filter misses it |
|---|---|
| `..%2f`, `%2e%2e/` | URL-encoded separators and dots |
| `..%252f` | Double encoding, decoded twice by two layers |
| `..\` | Backslash separators on Windows |
| Absolute paths (`/etc/passwd`, `C:\Windows\win.ini`) | The filter only looks for `..` |
| Archive entries named `../../x` | **Zip Slip**: extraction writes outside the target directory |
| Symbolic links inside uploaded archives | The path looks inside the directory but resolves outside |

The fix is **canonicalize, then compare**: resolve the final path and require that it is still inside the intended directory.

```python
from pathlib import Path

UPLOAD_ROOT = Path("/srv/app/uploads").resolve()

def read_upload(name: str) -> bytes:
    path = (UPLOAD_ROOT / name).resolve()
    if not path.is_relative_to(UPLOAD_ROOT):
        raise PermissionError("path outside the upload directory")
    return path.read_bytes()
```

Better still: do not accept paths at all. Store files under generated identifiers and map `id` to a stored path in the database. **Local and remote file inclusion** (a script `include`s a file chosen by a parameter, notably in PHP) is the same bug with code execution as the outcome; avoid dynamic includes and disable remote includes. Run the application with a user that can read only what it needs, ideally in a container with a read-only file system. **●●●**

## Unrestricted file upload

Uploads combine several risks: code execution (a script saved in a web-accessible, executable location), stored XSS (HTML or SVG served from your origin), denial of service (huge files, archive bombs), traversal in the file name, and exploits against the image or document parser.

| Control | Detail |
|---|---|
| **Allowlist** types | Accept only the extensions you need; verify the type by parsing the **content**, not the `Content-Type` header or the extension the client sent |
| **Rename** | Generate a random name; never trust the original |
| **Store safely** | Outside the web root, or in object storage with no execution; set no execute permissions |
| **Isolate serving** | Serve user content from a **separate domain** with `Content-Disposition: attachment` and `X-Content-Type-Options: nosniff`, so an uploaded HTML file cannot run in your origin |
| **Re-encode images** | Decoding and re-saving strips most payloads hidden in metadata or polyglot files |
| **Limit** | File size, count and rate; extract archives with size and entry-count limits |
| **Scan** | Malware scanning for files other users will download |
| **Authorize** | Check who may upload and who may download each file (this is access control) |

## Open redirect

An **open redirect** sends users to a URL taken from a parameter (`/login?next=https://evil.example`). On its own it is a phishing aid, because the link starts with your trusted domain. Chained with OAuth, it can leak authorization codes to the attacker, which is why loose redirect rules are on the list of OAuth failures.

```python
from urllib.parse import urlparse

def safe_next(target: str, default: str = "/") -> str:
    parts = urlparse(target)
    if parts.scheme or parts.netloc or not target.startswith("/") or target.startswith("//") or "\\" in target:
        return default
    return target
```

Accept only relative paths, or compare the full URL against an allowlist. Browsers treat `//host` and `/\host` as absolute, so those must be rejected too.

## Server-side request forgery

**SSRF** is a flaw in which an attacker makes the **server** send a request to a destination the attacker chooses. The server sits inside the network perimeter, has network access the attacker lacks, and often holds credentials, so the request reaches things that should never be exposed. In the OWASP Top 10:2025, SSRF is part of A01 Broken Access Control. **●●●**

### Where it hides

Any feature that makes the server fetch something based on user input:

| Feature | Example |
|---|---|
| Webhooks and callbacks | "Send events to this URL" |
| URL previews and link unfurling | Chat and social apps |
| Import and fetch by URL | Profile pictures, documents, feeds |
| Headless browsers and PDF generators | HTML-to-PDF services that load embedded URLs |
| XML, SVG and Office processing | Entities and embedded references fetched during parsing |
| Single sign-on and API integrations | Metadata and discovery URLs |
| "Test connection" and proxy features | Database, mail and API connectors |

### What the attacker reaches

| Target | Why it matters |
|---|---|
| **Cloud metadata service** (`169.254.169.254`, `metadata.google.internal`) | Returns the instance's temporary credentials, which can be used from anywhere until they expire |
| **`localhost` services** | Admin consoles and debug ports that trust the loopback interface |
| **Internal network** | Databases, caches (Redis), search clusters, Kubernetes and container APIs, internal web applications |
| **Other protocols** | `file://`, `gopher://`, `dict://` if the HTTP client library supports them |
| **Port scanning** | Response differences reveal which internal ports are open |

The best-known case is the 2019 Capital One breach: a server-side request flaw in a misconfigured web application firewall let an attacker retrieve temporary role credentials from the cloud metadata service and then read data from storage, affecting more than 100 million customers; the US bank regulator later imposed an $80 million penalty. **●●●**

Variants differ by what the attacker sees back. In **basic** SSRF the response comes back to the attacker. In **blind** SSRF it does not, and detection relies on timing, differences in errors, or an out-of-band server the attacker controls.

### Why simple filters fail

| Bypass | Idea |
|---|---|
| Alternative address forms | Decimal (`2130706433`), hexadecimal, octal, shortened or IPv6 forms of `127.0.0.1`; IPv4-mapped IPv6 |
| **DNS names that resolve internally** | A hostname the attacker controls that points to a private address |
| **DNS rebinding** | The name resolves to a public address during validation and to an internal one when the request is made |
| **Redirects** | An allowed external URL answers with a redirect to an internal one |
| **URL parser differences** | `http://allowed.example@evil.example/`, fragments, backslashes: validator and HTTP client disagree about the host |
| Unexpected schemes | `file:`, `gopher:` |

### Defenses, in layers

1. **Avoid the feature** or replace free-form URLs with identifiers and predefined integrations.
2. **Allowlist** exact hosts, schemes and ports wherever the set of destinations is known.
3. When arbitrary external URLs are the product (webhooks), validate **after resolving the name**, using the address you will actually connect to, and refuse anything that is not a public address. Connect to the validated address to prevent rebinding, **do not follow redirects blindly** (or re-validate each hop), allow only `http` and `https`, and cap time and response size.
4. **Network controls**: run fetchers in a segment with no route to internal services, force outbound traffic through a dedicated egress proxy (for example Stripe's open-source Smokescreen), and block egress to metadata and private ranges.
5. **Cloud**: require **IMDSv2** on AWS (a session-oriented request with a token header, and a hop limit that stops containers from reaching the host's metadata by default), keep instance roles minimal, and disable the metadata service where unused. Other providers require special request headers, which also blocks simple SSRF.
6. **Authenticate internal services** (Redis, Elasticsearch, admin consoles) so network position alone is not trust.
7. **Detect**: alert on requests to metadata addresses from application hosts and on use of instance credentials from outside your cloud.

```python
import ipaddress
import socket
from urllib.parse import urlparse

def require_public_destination(url: str) -> None:
    parts = urlparse(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise ValueError("unsupported URL")
    for *_, sockaddr in socket.getaddrinfo(parts.hostname, parts.port or 443):
        if not ipaddress.ip_address(sockaddr[0]).is_global:
            raise ValueError("destination is not a public address")
```

This check is a **starting point only**: also connect to the address you validated, handle redirects yourself, and enforce egress controls, because name checks alone are defeated by rebinding.

## Business logic flaws

A **logic flaw** exists when the code does what it was written to do, but the *process* it implements can be abused. There is no malformed input. A user sends valid requests in an unexpected order, quantity or timing. Scanners cannot find them because they do not know what the business intends. In the Top 10 they belong mostly to A06 Insecure Design. **●●●**

| Pattern | Example | Defense |
|---|---|---|
| **Trusting client-side values** | Price, discount or role sent in a hidden field or JSON | Compute from server-side data; the client sends only IDs and quantities |
| **Numeric edge cases** | Negative quantity creates a credit; overflow; rounding errors | Range checks; integer cents or decimal types; reject negatives |
| **Skipping steps** | Calling the "confirm order" URL without paying; unverified email accepted | Server-side state machine that checks prerequisites at every step |
| **Promotion abuse** | Reusing single-use codes; stacking discounts; creating many accounts for trials | Atomic redemption, uniqueness constraints, per-identity limits |
| **Race conditions** | Parallel requests redeem a coupon or withdraw funds several times | Transactions, row locks or constraints; idempotency keys |
| **Account flows** | Different messages for known and unknown emails; reusable reset tokens | Generic responses; single-use, short-lived tokens; rate limits |
| **Volume abuse** | Scraping, inventory hoarding, SMS pumping that runs up messaging costs | Rate limits and cost caps per user, bot defenses, anomaly alerts |
| **Cross-service trust** | A microservice trusts a header set by an upstream gateway that clients can also set | Verify identity in every service; strip untrusted headers at the edge |

### Race conditions

```python
balance = account.balance
if balance >= amount:
    account.balance = balance - amount
```

Two requests running at the same time can both read the old balance and both pass the check. In 2023 James Kettle published the **single-packet attack**, which makes many requests arrive almost simultaneously and so makes these windows reliably exploitable over the internet (Kettle, 2023). **●●●** The fix is to let the database enforce the rule atomically:

```sql
UPDATE accounts SET balance = balance - :amount WHERE id = :id AND balance >= :amount;
```

and treat "0 rows updated" as a failed withdrawal. Use unique constraints for "once only" rules (one coupon per user), transactions with the right isolation, and idempotency keys for retried payments.

### Finding logic flaws

1. Draw the workflow as a state diagram, with every state a user can reach and every transition.
2. Write down the **invariants**: "a refund never exceeds the payment", "a coupon is used once per customer", "an order cannot ship unpaid".
3. For each invariant, ask how a valid user could break it: skip a step, repeat a step, reorder steps, send the request twice at once, change a number, use two accounts.
4. Test those ideas with an intercepting proxy or a script.
5. Add each confirmed invariant as an automated test.

This is the same discipline as [threat modeling](../01-foundations/03-threat-modeling.md): abuse cases next to use cases.

## A quick test plan

| Feature | Try |
|---|---|
| Any ID in a URL or body | Replace with another user's ID; remove it; use another type |
| Any file name parameter | `../`, absolute path, encoded forms |
| Any URL parameter the server fetches | Loopback, private ranges, metadata address, redirect to an internal host, an out-of-band server you control |
| File upload | Wrong extension with valid content and the reverse; HTML/SVG file; oversize; name with `../` |
| Redirect parameters | External URL, `//host`, `/\host` |
| Checkout, transfer, booking | Negative and huge numbers; replay; parallel requests; skip steps |
| Account recovery | Compare responses and timing for known and unknown accounts; reuse a token |

## Practice

1. Build a "fetch this URL" endpoint in your lab. Start a second service on `127.0.0.1:8081`, retrieve it through the endpoint, then fix the endpoint with the validation above and the network setting, and verify both layers.
2. Simulate a metadata service with a small local server and show what an SSRF read of it would expose. Then read the AWS IMDSv2 documentation and explain which of your mitigations match it.
3. Complete the PortSwigger Web Security Academy topics on [SSRF](https://portswigger.net/web-security/ssrf), [path traversal](https://portswigger.net/web-security/file-path-traversal), [file upload vulnerabilities](https://portswigger.net/web-security/file-upload), [business logic vulnerabilities](https://portswigger.net/web-security/logic-flaws) and [race conditions](https://portswigger.net/web-security/race-conditions).
4. Write a two-thread script that exploits the balance race against your own lab API, then fix it with the atomic update and show the test passing.

These support [Module 1.4](../../roadmap/phase-1-security-fundamentals/04-web-security-owasp.md) and [Module 2.2](../../roadmap/phase-2-guided-practice/02-wargames-web-labs.md) of the roadmap.

## What to do with this

- [ ] Explain why canonicalizing a path before comparing it beats filtering `..`.
- [ ] List every feature in one of your projects that makes the server fetch a URL, and apply the SSRF checklist.
- [ ] Write the invariants of a shop, a banking transfer and a ticket booking system.
- [ ] Reproduce the race condition and fix it at the database level.
- [ ] Write one writeup of a logic flaw using the [template](../../writeups/TEMPLATE.md).

## Key references

AWS IMDSv2 documentation · CWE-22 · CWE-434 · CWE-601 · CWE-918 · Kettle (2023) · OWASP File Upload Cheat Sheet · OWASP Server-Side Request Forgery Prevention Cheat Sheet · OWASP Web Security Testing Guide · PortSwigger Web Security Academy. Full list in [References](../15-references.md).

<!-- navigation -->
[← Injection and cross-site scripting](03-injection-and-xss.md) · [Index](../00-start-here.md) · [API security →](05-api-security.md)
