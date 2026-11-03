# Injection and cross-site scripting

> [!TIP]
> **In short:** injection happens when **data is interpreted as code**. The attacker supplies input that an interpreter (a SQL engine, a shell, a template engine, a browser's HTML parser) treats as instructions instead of values. The durable fix is structural, not a blocklist: **keep data and code separate** with parameterized queries, argument arrays instead of shell strings, auto-escaping templates and **context-aware output encoding**. Input validation, least privilege and CSP are second layers. Cross-site scripting (XSS) is injection into the browser; insecure deserialization is injection into the runtime itself.

> [!CAUTION]
> The techniques below are for your own lab applications and for platforms that authorize testing. Running injection attempts against systems you do not have permission to test is a crime under Ley 1273 de 2009 (see [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md)).

## The pattern

Every injection bug has the same three parts:

1. A **sink** that builds a command or document from strings (a query, a shell line, a template, HTML).
2. A **source** of untrusted input reaching it (a parameter, header, cookie, file, database field, another service).
3. **No separation** between the structure the developer wrote and the content the user supplied.

| Interpreter | Typical sink | Fix |
|---|---|---|
| SQL database | String-built queries | Parameterized queries |
| Operating-system shell | `os.system`, backticks, `shell=True` | Argument arrays, no shell |
| Template engine | Template built from user text | Pass data as variables; never compile user input as a template |
| HTML in the browser | `innerHTML`, unescaped template output | Output encoding, `textContent`, sanitization |
| XML parser | External entities enabled | Disable DTDs and entities |
| LDAP, XPath, NoSQL | String-built filters, operator objects from JSON | Parameterized APIs, type validation |
| Native deserializer | Object streams from untrusted sources | Data-only formats with schemas |

**●●●** (OWASP Top 10:2025, A05 and A08.)

## SQL injection

```python
query = f"SELECT id, name FROM users WHERE email = '{email}'"
rows = db.execute(query).fetchall()
```

If `email` is `x' OR '1'='1`, the query becomes `... WHERE email = 'x' OR '1'='1'` and matches every row. The classic effects, depending on the database and its privileges, are:

| Impact | How |
|---|---|
| **Authentication bypass** | Making the login condition always true |
| **Data theft** | Appending a second query (`UNION SELECT`) or extracting values through error messages |
| **Data modification or destruction** | Stacked queries or injectable `UPDATE` and `DELETE` statements |
| **Command execution** | Database features such as `xp_cmdshell` (SQL Server) or `COPY ... PROGRAM` (PostgreSQL) when the account is powerful |

### Variants

| Type | What the attacker sees | Technique |
|---|---|---|
| **In-band** (error-based, `UNION`) | Results or errors in the response | Combine the application's query with their own |
| **Blind, boolean** | A difference in the page for true and false | Ask yes/no questions one bit at a time |
| **Blind, time-based** | Only response delay | Make the database sleep when a condition is true |
| **Out-of-band** | Nothing in the response | Make the database contact a server the attacker controls |
| **Second-order** | The payload is stored first and executed later | Safe input at write time becomes dangerous when reused in a later query |

### The fix: parameters

```python
rows = db.execute("SELECT id, name FROM users WHERE email = ?", (email,)).fetchall()
```

The database receives the statement and the values **separately**, so the value can never change the statement's structure. Rules that go with it:

- **Parameterize everywhere.** Second-order injection comes from trusting data that "already came from our own database", so values read back from storage need the same treatment.
- **Identifiers cannot be parameters.** Table names, column names and `ORDER BY` terms need an **allowlist**:

```python
SORTABLE = {"name", "created_at", "price"}
column = request.args.get("sort", "name")
if column not in SORTABLE:
    column = "name"
rows = db.execute(f"SELECT * FROM products ORDER BY {column}").fetchall()
```

- **ORMs help but do not guarantee.** Raw-query escape hatches (`.raw()`, `text()`, `execute(f"...")`) reintroduce the bug.
- **Stored procedures** are safe only if they do not build dynamic SQL from their arguments.
- **Least privilege.** The application's database account should not own the schema, read other applications' tables, or have file and command features. Damage is limited by what the account can do.
- **Errors.** Never show database errors to users.
- **Escaping** by hand is a last resort and a recurring source of bypasses.

TalkTalk's 2015 breach through SQL injection on old web pages ended with a £400,000 fine from the UK Information Commissioner, a reminder that this "old" bug still produces regulatory and financial damage. **●●●**

### NoSQL injection

Document databases are not immune. A login endpoint that passes parsed JSON straight into a MongoDB query can be sent an *operator* instead of a string:

```json
{"username": "admin", "password": {"$ne": null}}
```

which means "password not equal to null": always true. Defenses: validate that fields are the expected **type** (a string, not an object), use schema validation, strip or reject keys starting with `$`, and never build queries from raw request bodies.

## OS command injection

```python
os.system(f"ping -c 1 {host}")
```

A `host` of `8.8.8.8; cat /etc/passwd` runs a second command, because the shell treats `;`, `|`, `&&`, `$()` and backticks as syntax.

```python
import ipaddress
import subprocess

def ping(host: str) -> str:
    ipaddress.ip_address(host)
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True, timeout=5)
    return result.stdout
```

Three protections work together: no shell (an argument **list** instead of a string), strict validation with the right parser (`ipaddress` raises for anything that is not an IP), and a timeout. Also guard against **argument injection**: a value beginning with `-` can be read as an option (for example `-oProxyCommand=...` in SSH). Validate the shape of the value, or place `--` before positional arguments where the command supports it. Prefer a library over calling an external program. **●●●**

## Server-side template injection

```python
@app.get("/hello")
def hello():
    name = request.args.get("name", "")
    return render_template_string("Hello " + name)
```

The user's text becomes part of the **template**, so `{{7*7}}` renders `49`, which proves expression evaluation; in engines such as Jinja2, template syntax can often be turned into code execution. The fix is to keep user data as a variable:

```python
return render_template_string("Hello {{ name }}", name=name)
```

## XML external entities

An XML parser that resolves **DTDs and external entities** can be told to read local files or request internal URLs when it parses attacker-supplied XML (also SOAP, SVG, Office documents). Disable DTD processing and external entities in the parser, or use a hardened library (`defusedxml` in Python). In Java, enable secure processing and disallow `doctype` declarations. This falls under A02 Security Misconfiguration in the Top 10. **●●●**

## Other injection forms

| Form | Where | Defense |
|---|---|---|
| **LDAP injection** | Filters built from user input | Escape per LDAP rules; parameterized filter APIs |
| **XPath injection** | XML queries | Parameterized XPath |
| **Header and CRLF injection** | User input placed into HTTP headers or redirects | Reject CR and LF; use framework header APIs |
| **Email header injection** | `To`, `Subject` fields built from input | Validate; use mail libraries that separate headers |
| **Log injection** | Newlines or control characters forge log entries | Encode or strip control characters; use structured logs |
| **CSV (formula) injection** | Exported cells that start with `=`, `+`, `-`, `@` | Prefix such cells with an apostrophe or tab; escape on export |
| **Expression language injection** | Java EL, SpEL, OGNL | Never evaluate user input; update frameworks |

## Cross-site scripting

**XSS** lets an attacker run JavaScript in a victim's browser **as your origin**. The script can read anything on the page, call your APIs with the victim's session, change what is displayed, capture keystrokes and send data out. It is injection into the HTML and JavaScript interpreters of the browser.

| Type | Where the payload lives | Example |
|---|---|---|
| **Reflected** | In the request (usually a URL) and echoed back in the same response | A search page that prints the query unencoded |
| **Stored** | Saved by the server and shown to other users | A comment or profile field rendered as HTML |
| **DOM-based** | Never reaches the server; client-side code moves untrusted data into a dangerous sink | `element.innerHTML = location.hash.slice(1)` |

### Sources and sinks in the DOM

| Sources (attacker-controllable) | Sinks (dangerous when fed untrusted data) |
|---|---|
| `location.hash`, `location.search`, `document.URL`, `document.referrer` | `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write` |
| `window.name`, `postMessage` data | `eval`, `new Function`, `setTimeout("string")` |
| Web storage, cookies, data from `fetch` | `element.setAttribute("on...", ...)`, `href`/`src` with `javascript:` URLs |
| | Library calls such as jQuery's `.html()` |

### The fix: encode for the context

The correct encoding depends on **where** the data lands.

| Context | Example | Encoding |
|---|---|---|
| **HTML body** | `<p>USER</p>` | HTML-entity encode `& < > " '` |
| **Quoted attribute** | `<input value="USER">` | HTML-attribute encode, and always quote attributes |
| **JavaScript string** | `var x = 'USER'` | Avoid; pass data in `data-` attributes or JSON and read with `textContent` |
| **URL** | `href="/s?q=USER"` | Percent-encode parameters; validate the scheme (`https:` or `http:`) of whole URLs |
| **CSS** | `style="color: USER"` | Do not put user input in CSS; if needed, strict allowlist |
| **Rich text** | User-supplied formatting | Sanitize with a vetted library (DOMPurify) with an allowlist of tags and attributes |

Modern frameworks encode output by default: React and Vue escape interpolated values, Angular sanitizes, Jinja2 auto-escapes HTML templates. The bugs appear where developers **opt out**: `dangerouslySetInnerHTML`, `v-html`, `|safe`, `innerHTML` and string-built HTML. Treat each of those as a code-review flag. **●●●**

### Layers behind the fix

| Layer | Role |
|---|---|
| **Content Security Policy** (nonces, no `unsafe-inline`) | Stops injected scripts from running; see [Browser security model](01-browser-security-model-and-headers.md) |
| **Trusted Types** | Blocks plain strings reaching DOM sinks |
| **`HttpOnly` cookies** | Prevents reading the session cookie, but the script can still act as the user |
| **Sanitizer** | For legitimate rich text; keep it updated, because browsers' parsers can *mutate* markup after sanitization (mXSS) |
| **Framework defaults** | Do not disable auto-escaping |
| **Validation** | Reject obviously wrong input (a phone number with tags); it is not the primary defense |

**Practical implication:** blocklists of `<script>` fail. Attackers use event handlers (`<img src=x onerror=...>`), SVG, `javascript:` URLs and encodings. Fix the output, not the input.

### Testing for XSS

1. Submit a unique harmless marker (`xss7391`) in each parameter and field.
2. Find every place it appears in the response and note the **context** (body, attribute, script, URL).
3. Try a context-appropriate break-out, for example `"><svg onload=alert(1)>` in an attribute, in **your own** lab application.
4. Look for DOM sinks in the JavaScript with the browser's developer tools and a static analyzer.
5. Check that CSP blocks what the encoding missed.

## Insecure deserialization

Many languages can serialize arbitrary object graphs. Deserializing data from an untrusted source lets the sender choose which classes are instantiated and which methods run during reconstruction. Attackers chain existing classes ("gadgets") to reach code execution. **●●●**

| Platform | Dangerous | Safer |
|---|---|---|
| Python | `pickle.loads`, `yaml.load` on untrusted data | JSON; `yaml.safe_load` |
| Java | `ObjectInputStream` | JSON with a typed schema; serialization filters |
| PHP | `unserialize` | JSON |
| .NET | `BinaryFormatter` (obsolete and removed from recent .NET) | `System.Text.Json` |
| Ruby | `Marshal.load`, unsafe YAML | JSON |

```python
import yaml
config = yaml.safe_load(text)
```

Use data-only formats (JSON, Protocol Buffers) with schema validation. If you must exchange serialized objects, **verify an HMAC or signature before deserializing** and restrict the allowed types. Do not accept pickles from the network, from user uploads or from caches that other tenants can write to. The same family of risk includes machine learning model files saved with pickle; prefer formats such as safetensors for weights you did not produce yourself.

## Defense in depth, in order

| Order | Control | Stops |
|---|---|---|
| 1 | **Structural separation**: parameters, argument lists, auto-escaping | The vulnerability itself |
| 2 | **Context-aware output encoding** | XSS and template misuse |
| 3 | **Allowlist input validation** (type, length, range, format) | Many payloads and logic errors |
| 4 | **Least privilege** for the database account, OS user and service role | Impact if a bug slips through |
| 5 | **CSP, Trusted Types, HttpOnly, SameSite** | Exploitation of XSS and CSRF |
| 6 | **WAF** | Known payloads; a compensating control, easy to bypass |
| 7 | **Logging and alerting** on errors and anomalies | Detection |
| 8 | **Automated tests**: SAST rules, DAST, unit tests with hostile input | Regression |

## Tools

| Purpose | Tools |
|---|---|
| Intercepting proxy | Burp Suite Community Edition, OWASP ZAP |
| SQL injection testing | `sqlmap` (learn the manual techniques first and run it only against your lab and authorized targets) |
| Static analysis | Semgrep, Bandit (Python), CodeQL |
| Safe libraries | `defusedxml`, DOMPurify, parameterized drivers of your language |
| Practice targets | PortSwigger Web Security Academy, OWASP Juice Shop, DVWA, Hacker101 |

## Practice

1. Create a small Flask application with a login and a product search that both use string-built SQL. Exploit each in your lab, then fix each with parameters and an allowlist for `ORDER BY`, and write a test with hostile input.
2. Write a command-execution endpoint that wraps `ping`, exploit it, and fix it with an argument list and `ipaddress` validation.
3. Build a comment page that is vulnerable to stored XSS. Add a strict CSP and show how it limits the damage even before you fix the encoding.
4. Complete the PortSwigger Web Security Academy topics for [SQL injection](https://portswigger.net/web-security/sql-injection), [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting), [OS command injection](https://portswigger.net/web-security/os-command-injection) and [server-side template injection](https://portswigger.net/web-security/server-side-template-injection).
5. Write a Semgrep rule that flags `os.system(` calls whose argument is an f-string.

These support [Module 1.4](../../roadmap/phase-1-security-fundamentals/04-web-security-owasp.md) and [Module 2.2](../../roadmap/phase-2-guided-practice/02-wargames-web-labs.md) of the roadmap.

## What to do with this

- [ ] Explain, in one sentence each, why parameters stop SQL injection and why a blocklist does not stop XSS.
- [ ] Review one of your projects for string-built queries, `shell=True`, `innerHTML`, `|safe` and `pickle.loads`.
- [ ] Fix every finding and add a test that fails if it returns.
- [ ] Solve five PortSwigger labs in this area and write one writeup using the [template](../../writeups/TEMPLATE.md).
- [ ] Add a Semgrep rule or CI check for the pattern you found.

## Key references

CWE-79 · CWE-89 · Halfond et al. (2006) · OWASP Cross Site Scripting Prevention Cheat Sheet · OWASP Deserialization Cheat Sheet · OWASP Injection Prevention Cheat Sheet · OWASP Query Parameterization Cheat Sheet · OWASP SQL Injection Prevention Cheat Sheet · PortSwigger Web Security Academy. Full list in [References](../15-references.md).
