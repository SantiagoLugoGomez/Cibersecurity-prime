# The browser security model and security headers

> [!TIP]
> **In short:** the browser is where your web application actually runs, and it runs code from many origins at once. Its protection rests on one rule, the **same-origin policy**, plus mechanisms that deliberately relax it (**CORS**) or tighten it (**CSP**, cookie attributes, framing and isolation headers). Most "web hardening" is switching these on correctly through a handful of **response headers**. None of them replaces fixing the underlying bug, but each one turns a bug that would be critical into one that is contained.

## Origins, sites and the same-origin policy

An **origin** is the triple *scheme + host + port*. Two URLs are same-origin only if all three match.

| URL compared with `https://app.example.com/` | Same origin? | Why |
|---|---|---|
| `https://app.example.com/other` | Yes | Same scheme, host and port |
| `http://app.example.com/` | No | Different scheme |
| `https://app.example.com:8443/` | No | Different port |
| `https://api.example.com/` | No | Different host |
| `https://example.com/` | No | Different host |

A **site** is broader: the *registrable domain* (the public suffix plus one label, such as `example.com` or `example.co.uk`) plus the scheme. `app.example.com` and `api.example.com` are *same-site* but *cross-origin*. The distinction matters because cookies and the `SameSite` attribute work at the site level, while the same-origin policy and CORS work at the origin level.

The **same-origin policy** (SOP) is the browser's core isolation rule: a page from one origin may not **read** data from another origin. It is a rule about *reading*, not about *sending*.

| Operation across origins | Allowed? |
|---|---|
| Read the response of a `fetch` or `XMLHttpRequest` | **No**, unless the other origin opts in with CORS |
| Read or modify another frame's DOM | **No** |
| Read another origin's cookies, `localStorage` or IndexedDB | **No** |
| **Send** a `GET` or form `POST` (navigation, `<form>`, `<img>`) | **Yes** (this is why CSRF exists) |
| **Embed** images, scripts, stylesheets, fonts, frames | **Yes**, with exceptions (scripts run with *your* origin's privileges) |

The last row is the root of third-party risk: a `<script src="https://cdn.other.com/lib.js">` tag executes with full access to your page. **●●●**

## CORS

**Cross-Origin Resource Sharing** is how a server *opts in* to letting other origins read its responses. It is not a security feature that protects the server; it is a relaxation of the SOP.

| Header | Direction | Meaning |
|---|---|---|
| `Origin` | Request (set by the browser) | The origin making the request |
| `Access-Control-Allow-Origin` | Response | Which origin may read the response (one origin or `*`) |
| `Access-Control-Allow-Credentials: true` | Response | Cookies and HTTP authentication may be included. Cannot be combined with `*` |
| `Access-Control-Allow-Methods` / `-Headers` | Response to a preflight | Which methods and headers are allowed |
| `Access-Control-Max-Age` | Response to a preflight | How long the browser may cache the preflight result |
| `Vary: Origin` | Response | Required when the answer depends on `Origin`, so caches do not mix responses |

Requests that could not have been made by a plain HTML form (custom headers, `PUT`, `DELETE`, JSON content type) trigger a **preflight**: the browser first sends an `OPTIONS` request and proceeds only if the server approves. "Simple" requests are sent immediately, and CORS only decides whether the page may *read* the answer.

### CORS misconfigurations

| Mistake | Consequence | Fix |
|---|---|---|
| **Reflecting any `Origin`** into `Access-Control-Allow-Origin` together with `Allow-Credentials: true` | Any website can read authenticated responses of a logged-in victim | Compare against an exact allowlist of origins |
| **Trusting the `null` origin** | Sandboxed frames and local files send `Origin: null`, so an attacker can obtain it | Never allow `null` |
| **Loose pattern matching** (`endsWith("example.com")`, unescaped dots in regular expressions) | `https://evilexample.com` or `https://example.com.attacker.net` pass | Parse the origin and compare the full string |
| **Trusting all subdomains** | One compromised or taken-over subdomain exposes the main application | Allow only the specific origins that need access |
| **`*` on endpoints with sensitive data** that rely on network position (internal tools) | A website can read internal responses through a victim's browser | Authenticate; do not rely on being "inside" |
| **Thinking CORS is access control** | Non-browser clients ignore CORS entirely; the request is still processed | Authorize on the server for every request |

**Practical implication:** if an endpoint changes state, CORS does not protect it, because the request is sent regardless; use authentication, CSRF defenses and validation. See [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md).

## Content Security Policy

**CSP** is a response header that tells the browser which sources of scripts, styles, frames and other resources are allowed. Its main job is to turn an XSS bug from "attacker runs arbitrary script" into "the browser refuses to run it" (see [Injection and XSS](03-injection-and-xss.md)).

| Directive | Controls |
|---|---|
| `default-src` | Fallback for the other fetch directives |
| `script-src` | Where scripts may come from or which inline scripts run |
| `style-src`, `img-src`, `font-src`, `media-src` | The corresponding resources |
| `connect-src` | Targets of `fetch`, XHR, WebSocket, `EventSource` |
| `frame-src`, `child-src` | What this page may embed |
| `frame-ancestors` | **Who may embed this page** (clickjacking defense; replaces `X-Frame-Options`) |
| `base-uri` | Allowed values of `<base>`, which can redirect relative URLs |
| `form-action` | Where forms may submit |
| `object-src` | Plugins; set to `'none'` |
| `upgrade-insecure-requests` | Upgrade `http:` subresources to `https:` |
| `report-to` / `report-uri` | Where violation reports go |

### Allowlists fail; use nonces

A policy such as `script-src 'self' https://cdn.example.com` looks safe but is often bypassable: any endpoint on an allowed host that reflects input, or any script gadget in a permitted library, can run attacker code. Google's analysis of thousands of real policies found most allowlist-based CSPs were bypassable (Weichselbaum et al., 2016). The recommended approach is a **strict CSP**: allow scripts by an unpredictable per-response **nonce** (or a hash), and let trusted scripts load their own dependencies with `'strict-dynamic'`. **●●●**

```
Content-Security-Policy: script-src 'nonce-R4nd0mPerResponse' 'strict-dynamic'; object-src 'none'; base-uri 'none'; frame-ancestors 'self'
```

Each response must carry a **new random nonce** that is also placed on the legitimate `<script nonce="...">` tags. A fixed or guessable nonce defeats the purpose.

| Pitfall | Why it weakens CSP |
|---|---|
| `'unsafe-inline'` in `script-src` | Allows injected inline scripts: the main thing CSP should stop |
| `'unsafe-eval'` | Allows `eval` and similar string-to-code sinks |
| Wildcards and whole CDNs (`*.googleapis.com`, `cdnjs.cloudflare.com`) | Hosts serve attacker-usable code or JSONP endpoints |
| Missing `base-uri` and `object-src` | Allow base-tag hijacking and plugin content |
| Policy only on some pages | Unprotected pages are the entry point |
| Never reading violation reports | You miss attacks and breakage |

Roll a policy out in **report-only** mode first (`Content-Security-Policy-Report-Only`), watch the reports, fix legitimate violations, then enforce. **Trusted Types** (`require-trusted-types-for 'script'`) goes further by blocking assignment of plain strings to dangerous DOM sinks such as `innerHTML`; it shipped first in Chromium-based browsers, so check current browser compatibility tables before relying on it. **●●○**

## The other security headers

| Header | Example value | What it does |
|---|---|---|
| **`Strict-Transport-Security`** (HSTS, RFC 6797) | `max-age=31536000; includeSubDomains` | Tells the browser to use HTTPS only for this host. Add `preload` only after you are sure every subdomain supports HTTPS, because removal from preload lists is slow |
| **`X-Content-Type-Options`** | `nosniff` | Stops the browser from guessing content types (prevents a text file from being run as script) |
| **`Referrer-Policy`** | `strict-origin-when-cross-origin` | Limits what URL information leaks to other sites |
| **`Permissions-Policy`** | `camera=(), microphone=(), geolocation=()` | Disables powerful features the page and its frames do not need |
| **`Cross-Origin-Opener-Policy`** (COOP) | `same-origin` | Isolates your window from cross-origin windows you open or that open you; blocks several cross-window leaks |
| **`Cross-Origin-Embedder-Policy`** (COEP) | `require-corp` | Requires embedded resources to opt in; with COOP, enables cross-origin isolation |
| **`Cross-Origin-Resource-Policy`** (CORP) | `same-origin` or `same-site` | Stops other origins from loading your resources (limits some side-channel leaks) |
| **`Cache-Control`** | `no-store` for sensitive responses | Prevents pages with personal data from being kept in shared or browser caches |
| **`Clear-Site-Data`** | `"cache", "cookies", "storage"` on logout | Asks the browser to wipe stored data |
| **`X-Frame-Options`** | `DENY` | Legacy clickjacking defense; prefer CSP `frame-ancestors` |
| **`X-XSS-Protection`** | `0` or omitted | The old browser XSS filter is gone; the header is obsolete and can introduce issues |
| `Server`, `X-Powered-By` | remove or minimize | Version banners help attackers fingerprint; low value, easy win |

A baseline for a typical application in nginx:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
add_header Content-Security-Policy "default-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'" always;
```

The CSP in this snippet blocks inline scripts, so adapt it to your application (nonces) rather than pasting it blindly.

Cookies, the other half of browser state, have their own attributes (`Secure`, `HttpOnly`, `SameSite`, the `__Host-` prefix); they are covered in [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md#cookie-attributes).

## Clickjacking

In **clickjacking**, an attacker's page loads yours in an invisible frame positioned under a decoy button, so the victim's click lands on your page while logged in. Defend with `frame-ancestors` (or `X-Frame-Options`) so the page cannot be embedded by untrusted origins, and require confirmation for sensitive actions. **●●●**

## Third-party scripts and Subresource Integrity

Everything you load by `<script src>` runs with your page's privileges. Tag managers, analytics, chat widgets and CDN libraries each add a supplier whose compromise becomes yours. Real cases:

| Case | What happened |
|---|---|
| **Magecart-style skimming** (British Airways, 2018, and many online shops) | Attackers modified a script on the payment page to copy card data to their own server |
| **polyfill.io, 2024** | After the domain changed hands, the service served malicious code to the sites that embedded it, reported on a very large number of sites |

Mitigations: load as few third-party scripts as possible, self-host libraries you control, add **Subresource Integrity** (`integrity="sha384-..."` with `crossorigin="anonymous"`) so the browser refuses a file that does not match the hash you reviewed, restrict them with CSP, and keep payment pages free of marketing scripts. SRI does not help for scripts that must change often, which is a reason to keep those out of sensitive pages. **●●○**

## Other browser-side details

| Topic | Guidance |
|---|---|
| **Web storage** (`localStorage`, `sessionStorage`, IndexedDB) | Readable by any script in the origin, so an XSS bug exposes everything stored there. Do not store session tokens or secrets there when an HttpOnly cookie will do |
| **`postMessage`** | Always check `event.origin` against an allowlist and specify the target origin when sending; never use `"*"` for sensitive data |
| **`window.open` and `target="_blank"`** | Modern browsers imply `rel="noopener"`, but add it explicitly for older clients; COOP handles the rest |
| **iframes** | Use the `sandbox` attribute for untrusted content, and `allow` to restrict features |
| **Open redirects and `javascript:` URLs** | Validate redirect targets against an allowlist; never put user input into `href` without scheme checks |
| **Service workers** | Run with persistent control over a scope; protect their script URLs and review third-party registrations |
| **Mixed content** | Never load `http:` resources on `https:` pages; use `upgrade-insecure-requests` as a safety net |
| **Fetch Metadata** (`Sec-Fetch-Site`, `Sec-Fetch-Mode`) | Request headers the browser sets; servers can reject unexpected cross-site requests ("resource isolation policy") |

## Practice

1. Open the developer tools on a site you run, read each response header, and list which of the headers above are missing.
2. Add the baseline to a small Flask or Express app. Then test your header set against [MDN HTTP Observatory](https://developer.mozilla.org/en-US/observatory) and [SecurityHeaders](https://securityheaders.com/). Run these only against sites you own.
3. Write a strict CSP for a page with one inline script. Deploy it in report-only mode, trigger violations, then enforce it and verify that an injected `<script>alert(1)</script>` is blocked.
4. Build two tiny pages on different ports. Make one call the other with `fetch`. Observe the SOP block, then add CORS headers and watch the preflight in the network tab. Finally write a deliberately broken reflecting-origin rule and exploit it from the second origin.
5. Check a CSP with Google's [CSP Evaluator](https://csp-evaluator.withgoogle.com/) and explain each finding.

These support [Module 1.4](../../roadmap/phase-1-security-fundamentals/04-web-security-owasp.md) of the roadmap.

## What to do with this

- [ ] Explain the difference between origin, site and domain, and why `SameSite` and CORS use different ones.
- [ ] Write the full header set for one of your own projects and keep it in the repository.
- [ ] Give one example where CORS would not have protected an endpoint and say why.
- [ ] Add CSP in report-only mode to a project and review the reports for a week.
- [ ] Add SRI hashes to every third-party script on one page, or remove the script.

## Key references

MDN Web Docs · OWASP Secure Headers Project · RFC 6265 · RFC 6454 · RFC 6797 · W3C Content Security Policy · WHATWG Fetch Standard · Weichselbaum et al. (2016) · Zalewski (2011). Full list in [References](../15-references.md).

<!-- navigation -->
[← Kerberos, NTLM and enterprise identity](../04-cryptography-and-identity/06-kerberos-ntlm-and-enterprise-identity.md) · [Index](../00-start-here.md) · [The OWASP Top 10:2025 →](02-owasp-top-10-2025.md)
