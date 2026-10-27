# Module 1.3: Identity and access (weeks 6-7)

Authentication and authorization are where most real breaches start. This module covers how identity works on the web and in enterprises, and how it fails.

**Main resources:** [PortSwigger Web Security Academy](https://portswigger.net/web-security) (free), [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html), OWASP cheat sheets.

## Week 6: Authentication, passwords and MFA

**Goal:** understand how users prove who they are, and why each method fails.

**R. Read and study (75 min)**
- PortSwigger: the [Authentication](https://portswigger.net/web-security/authentication) topic overview.
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html): the authenticator and password sections.
- Notes: the three authentication factors; password attacks (guessing, spraying, stuffing, offline cracking); why the final 800-63B requires 15 characters for single-factor passwords, drops composition rules and forced rotation; TOTP vs push vs WebAuthn/passkeys and why passkeys are phishing-resistant.
- Flashcards: the three factors, password spraying vs stuffing vs brute force, what makes a passkey phishing-resistant, the 800-63B password rules.

**P. Guided practice (90 min)**
- PortSwigger: the Authentication apprentice labs (username enumeration, broken brute-force protection, flawed 2FA).
- Enable TOTP and a passkey on your own real accounts, and write what each protects against.

**D. Deep practice (3 h)**
- Build a tiny login demo in Python (Flask or standard library) that does it right: Argon2id password hashing, constant-time comparison, generic error messages, rate limiting, and a TOTP second factor. Then deliberately break each control and show the resulting attack (user enumeration via error messages, unlimited guessing, etc.). Document before and after.

**E. English (60 min)**
- Read the "password" requirements of 800-63B-4 and note the exact use of SHALL, SHOULD and MAY. Write a password policy for a fictional company in English using those words correctly.

**Check yourself**
1. What are the three authentication factors, with an example of each?
2. What is the difference between password spraying, stuffing and brute force?
3. Why does the current NIST guidance drop forced password rotation?
4. Why is a passkey resistant to phishing when a TOTP code is not?
5. Why must a login form return the same error for a bad username and a bad password?

**Deliverable:** the login demo showing each control working and broken, documented, plus your English password policy.

## Week 7: Authorization, sessions, OAuth and enterprise identity

**Goal:** understand what a user is allowed to do, how sessions are kept, and how federated login and enterprise identity work.

**R. Read and study (75 min)**
- PortSwigger: [Access control](https://portswigger.net/web-security/access-control) and [OAuth 2.0](https://portswigger.net/web-security/oauth) overviews.
- OWASP [Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) and [Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) cheat sheets.
- Notes: authentication vs authorization; session cookies and their attributes (`HttpOnly`, `Secure`, `SameSite`); RBAC vs ABAC; OAuth 2.0 roles and the authorization-code flow; OpenID Connect vs OAuth; the idea behind Kerberos and Active Directory authentication (tickets, not passwords on the wire).
- Flashcards: authn vs authz, the three cookie attributes, RBAC vs ABAC, OAuth vs OIDC, what a Kerberos ticket is.

**P. Guided practice (90 min)**
- PortSwigger: the Access Control apprentice labs (IDOR, role-based bypass) and one OAuth lab.
- Inspect a real login flow in your browser's dev tools: find the session cookie and its attributes; follow an OAuth "Sign in with..." redirect and identify the authorization code.

**D. Deep practice (3 h)**
- Extend your login demo with roles: a normal user and an admin. Implement an authorization check on every sensitive action, then introduce an insecure direct object reference (IDOR) by trusting a user-supplied ID, exploit it as one user against another, and fix it. Write up the root cause (this is OWASP A01).
- Read how Active Directory authenticates (Kerberos) at a high level; you will attack it in Phase 2 and 3.

**E. English (60 min)**
- Explain, out loud and recorded, the difference between authentication and authorization and between OAuth and OpenID Connect, in two minutes ([speaking-practice.md](../../english/speaking-practice.md)).

**Check yourself**
1. What is the difference between authentication and authorization?
2. What do `HttpOnly`, `Secure` and `SameSite` each protect against?
3. Walk through the OAuth 2.0 authorization-code flow at a high level.
4. What is OpenID Connect, and how does it relate to OAuth?
5. What is an IDOR, and which OWASP category does it fall under?

**Deliverable:** the role-based login demo with an IDOR exploited and fixed, documented with the root cause.

**Stretch:** read about SAML and the difference between session tokens and JWTs, including common JWT mistakes.
