# Passwords and multi-factor authentication

> [!TIP]
> **In short:** passwords remain the most attacked part of authentication, mainly through **phishing, reuse and theft**, not through clever guessing. The current guidance (NIST SP 800-63B-4) favors **long** passwords or passphrases, screening against known-breached lists, **no composition rules and no forced rotation**, and **multi-factor authentication** everywhere. Prefer **phishing-resistant MFA** (passkeys, FIDO2 security keys) over SMS, one-time codes and push approvals, and protect the **recovery** path, because attackers go around the strongest front door.

## How accounts actually get compromised

| Route | Mechanism | Dominant defense |
|---|---|---|
| **Phishing** | A fake page or message captures credentials (and, with real-time proxies, the MFA code and session) | Phishing-resistant MFA, user reporting, email and web filtering |
| **Credential stuffing** | Lists of leaked email and password pairs from one site are tried on others | Unique passwords (a manager), MFA, breached-password screening, rate limits |
| **Password spraying** | One or a few common passwords tried across many accounts, staying below lockout thresholds | MFA, smart lockout, detection of failures across accounts from one source |
| **Brute force (online)** | Many guesses against one account | Throttling, lockout, MFA |
| **Offline cracking** | The attacker has the database of hashes and tries guesses at hardware speed | Slow, salted hashes (Argon2id) and long passwords |
| **Malware and infostealers** | Keyloggers and browser-credential or **session cookie** theft | Endpoint protection, device-bound sessions, short session lifetimes |
| **Social engineering and help desks** | Convincing support to reset a password or MFA | Strict identity verification procedures |
| **Recovery abuse** | Taking over the email account or phone that controls resets | Strong recovery factors, notifications |

Verizon's annual breach report has for years listed stolen credentials among the top initial access methods, alongside vulnerability exploitation (Verizon DBIR). **●●○** The implication is that password strength matters less than where a password is *used* and whether it can be *replayed*.

## Strength: length beats complexity

For a password chosen *randomly*, strength is the number of possibilities, measured in bits of **entropy**: `length × log2(alphabet size)`.

| Password type | Entropy |
|---|---|
| 8 random characters from 95 printable | about 53 bits |
| 12 random characters from 95 | about 79 bits |
| 16 random lowercase letters | about 75 bits |
| 5 random Diceware words (list of 7,776) | about 65 bits |
| **6 random Diceware words** | **about 78 bits** |
| 7 random Diceware words | about 91 bits |

Humans do not pick randomly. `Summer2026!` satisfies every classic composition rule and is cracked in seconds, because attackers try dictionary words, names, dates, keyboard patterns and the usual substitutions (`a` to `@`) first. A password's real strength is how many guesses a good cracker needs, not how many character classes it contains. Tools such as **zxcvbn** estimate this by modeling common patterns and are far more useful than "must contain a digit and a symbol" (Wheeler, 2016). **●●●**

How much entropy is enough depends on the attack:

- **Online** attacks are limited by rate limiting and lockouts, so even 30 to 40 bits can be acceptable if the system throttles well.
- **Offline** attacks are limited only by the attacker's hardware and your hash. A single modern GPU computes tens of billions of MD5 or NTLM hashes per second, but only thousands of bcrypt hashes per second at a typical cost. Against fast hashes, you want 70 bits or more; against Argon2id with sensible parameters, fewer bits hold up much longer. **◇**

## What current guidance says

NIST's *Digital Identity Guidelines*, SP 800-63B-4 (2025), reversed several decades of folk wisdom. **●●●**

| Requirement | Detail |
|---|---|
| **Minimum length** | **15 characters** when the password is the only factor; **8** when it is one factor within MFA |
| **Maximum length** | Verifiers should allow at least **64** characters |
| **Composition rules** | **Do not impose** them (no mandatory digits, symbols or mixed case) |
| **Periodic change** | **Do not require** it; change only on evidence of compromise |
| **Blocklist** | Screen new passwords against known-compromised, common and context-specific values |
| **Usability** | Allow paste and password managers; accept all printable characters, including spaces |
| **Security questions** | Do not use knowledge-based questions as a secret |

The research behind this is consistent: forced rotation makes people choose predictable variations (`Spring2026!` becomes `Summer2026!`), and composition rules produce the same few patterns. Length plus blocklists plus MFA does more with less friction. See also [Security principles](../01-foundations/02-security-principles.md), *psychological acceptability*.

### Checking against breached passwords

The **Pwned Passwords** service lets an application check whether a password appears in known breaches without revealing it. The client computes the SHA-1 of the password, sends only the **first five hex characters**, receives the list of matching hash suffixes (several hundred) and looks for its own locally. This **k-anonymity** design means the service never sees the full hash. Use it at registration and password change; some systems also re-check stored passwords at login time while the plaintext is briefly available.

## Storing passwords (for developers)

Everything in [Cryptography foundations](01-cryptography-foundations.md#passwords-and-key-derivation) applies. In short:

- Hash with **Argon2id** (or scrypt, bcrypt, or PBKDF2 where FIPS is required), with a unique salt per password and parameters at or above current OWASP minimums.
- Optionally add a **pepper**: a secret key kept outside the database (in a KMS or HSM) and mixed in with HMAC. A stolen database alone then cannot be cracked.
- **Rehash on login** when parameters improve or the algorithm changes.
- Never store plaintext or reversibly encrypted passwords; never email them; never log them.
- Return the **same message and similar timing** for an unknown user and a wrong password, to avoid account enumeration.

Because the NT hash used in Windows is an unsalted MD4, it is cracked quickly and can be used directly without cracking in pass-the-hash attacks (see [Windows internals](../02-systems/02-windows-internals-for-security.md)).

## Password managers

A password manager generates and stores a unique random password for every site. It is the single most effective step an ordinary user can take against credential stuffing, and because it fills credentials only on the matching domain, it also resists many phishing pages. Choose a manager from a vendor with a good security record, protect it with a strong passphrase and MFA, and keep recovery material offline. A manager is a high-value target (the 2022 theft of encrypted vault backups from one vendor showed the cost of weak master passwords), but the alternative, reuse, is worse for nearly everyone. **●●○**

## Multi-factor authentication

MFA combines factors from different categories:

- **Something you know**: password, PIN.
- **Something you have**: phone, hardware key, smart card.
- **Something you are**: fingerprint, face (usually used locally to unlock a device or key, not sent to the server).

MFA works because a stolen password alone is no longer enough. A large Microsoft analysis of compromised accounts estimated that MFA reduced the risk of compromise by over 99% across the population studied (Meyer et al., 2023). **●●○** Treat that as a vendor study with a modeled estimate, not a controlled trial, but the direction is not in doubt.

### Not all MFA is equal

| Method | Phishable? | Notes |
|---|---|---|
| **SMS or voice code** | Yes | Also vulnerable to SIM swapping and SS7 weaknesses; better than nothing, avoid for admins |
| **Email code** | Yes | Only as strong as the mailbox |
| **TOTP app** (RFC 6238) | Yes | A real-time proxy site can relay the code; works offline; widely supported |
| **Push approval** | Yes | Vulnerable to *MFA fatigue* (repeated prompts until the user taps Approve); number matching reduces this |
| **Hardware OTP token** | Yes | Same phishing exposure as TOTP |
| **FIDO2 / WebAuthn security key** | **No** | The credential is bound to the website's origin; a fake site gets nothing |
| **Passkey** | **No** | A FIDO credential on a device or synced across a user's devices; unlocked by a local biometric or PIN |
| **Smart card / PIV** | No | PKI-based; common in government and enterprise |

**Phishing-resistant** means the authenticator cannot be tricked into answering a fake site and does not give the user a secret to type. The FIDO2 standards (W3C WebAuthn plus the FIDO Alliance's CTAP) achieve this with public-key cryptography: at registration, the device creates a key pair for that site; at login, it signs a challenge together with the site's origin. A look-alike domain has a different origin, so the signature is useless to the attacker. **●●●**

### How MFA is bypassed

| Attack | Description | Counter |
|---|---|---|
| **Adversary-in-the-middle phishing** | A reverse proxy (tools such as Evilginx) sits between victim and real site, relays the password and the MFA code, and steals the resulting session cookie | Phishing-resistant MFA; token binding where available; conditional access |
| **MFA fatigue (push bombing)** | Flood the user with prompts until one is accepted. Used in the 2022 Uber compromise | Number matching, limits, phishing-resistant MFA |
| **SIM swap** | Convince the mobile carrier to move a number to the attacker's SIM | Avoid SMS for high-value accounts |
| **Help desk social engineering** | Persuade support to reset MFA or password. Used in 2023 against a major casino operator by a group known as Scattered Spider | Verification procedures that cannot be satisfied by a phone call alone; approval workflows |
| **Session or token theft** | Malware steals cookies or tokens after login, bypassing MFA entirely | Endpoint security, short lifetimes, device-bound tokens, detection of impossible sessions |
| **Enrollment attacks** | Register the attacker's device as a factor on a new account | Verify enrollment; require existing strong factor |
| **Fallback abuse** | Downgrade from the strong method to SMS | Remove weak fallbacks for protected accounts |

**Practical implication:** MFA is necessary, not sufficient. For administrators, executives and anyone with access to money or sensitive data, require phishing-resistant MFA and remove the weaker methods.

## Passkeys

A passkey is a FIDO credential that replaces the password. The private key lives in a secure element or credential manager on the user's device; the site stores only the public key. Sign-in is a local unlock plus a signature. Benefits: nothing to remember, nothing to phish, nothing useful to steal from the server. Trade-offs: **synced passkeys** (through a platform account) are convenient but make the sync account critical; **device-bound** keys (hardware security keys) give the highest assurance and are what high-risk roles should use. Always provide at least two registered authenticators and a tested recovery plan.

## Recovery is the weakest link

Attackers choose the easiest path. If login needs a hardware key but reset needs only an email link, the email account is the real security boundary.

- Protect the recovery mailbox with the same strength of MFA as the account.
- Offer **recovery codes** or a second registered authenticator, stored offline.
- Use **delays and notifications** for sensitive changes (new device, new factor, email change).
- Avoid security questions; the answers are guessable or findable.
- Train and equip the **help desk** to verify identity properly and to refuse social pressure.

## Machine credentials are passwords too

API keys, database passwords, tokens and service-account secrets are the passwords of software, and they leak constantly through source code and logs. Keep them in a secrets manager, grant short-lived credentials where you can (workload identity, OIDC federation instead of long-lived keys), scan repositories for secrets, and rotate on any exposure. Compare the cloud entries in [Cloud IAM and attack paths](../08-cloud-and-infrastructure/02-cloud-iam-and-attack-paths.md).

## Detection

| Signal | Where |
|---|---|
| Many failed logins for one account | Application logs, Windows 4625, SSH logs, identity provider |
| One source failing across many accounts (spraying) | Same logs, aggregated by source address |
| Success after many failures | Highest-fidelity credential-attack alert |
| Login from a new country, device or impossible travel | Identity provider risk signals |
| Burst of MFA prompts | MFA logs; indicates fatigue attack or compromised password |
| New MFA method registered, recovery changed | Identity logs; often precedes takeover |
| Session used from a different IP than the one that authenticated | Token replay |

## A short checklist for developers

- Hash passwords with Argon2id; unique salt; tune the cost.
- Enforce length and a breached-password check; do not enforce composition or rotation.
- Rate-limit by account and by source; use progressive delays; support MFA.
- Offer passkeys.
- Use generic errors; avoid enumeration through timing and messages.
- Make recovery as strong as login; notify users of security changes.
- Log authentication events with enough context to investigate.
- Never roll your own authentication if a mature identity provider fits.

## What to do with this

- [ ] Enable a passkey or hardware security key on your most important accounts, and set up recovery codes.
- [ ] Move all your passwords into a password manager and replace the ten most important ones with generated passwords.
- [ ] Compute the entropy of five password policies and decide which would pass NIST SP 800-63B-4.
- [ ] Build the login demo from [Module 1.3, week 6](../../roadmap/phase-1-security-fundamentals/03-identity-and-access.md): hashing, throttling and TOTP.
- [ ] In your lab, crack hashes you created yourself with Hashcat or John the Ripper to see the speed difference between MD5 and bcrypt.

## Key references

Meyer et al. (2023) · NIST SP 800-63B-4 · OWASP Authentication Cheat Sheet · OWASP Password Storage Cheat Sheet · RFC 4226 · RFC 6238 · Verizon DBIR · W3C WebAuthn · Wheeler (2016). Full list in [References](../15-references.md).
