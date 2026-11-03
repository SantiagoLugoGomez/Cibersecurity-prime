# Cryptography foundations

> [!TIP]
> **In short:** never invent cryptography and never assemble it from raw parts. Use a vetted high-level library, choose **authenticated encryption** (AES-GCM or ChaCha20-Poly1305), hash passwords with **Argon2id**, take randomness only from the operating system's **CSPRNG**, and protect the **keys**, because the algorithms are almost never what fails. Real-world breaks come from reused nonces, weak randomness, unauthenticated encryption, wrong comparison functions and hard-coded keys. Knowing the primitives lets you spot those mistakes.

## What cryptography gives you

| Goal | Primitive | Example |
|---|---|---|
| **Confidentiality** | Encryption | AES-GCM, ChaCha20-Poly1305 |
| **Integrity** | Hash, MAC, authenticated encryption | SHA-256, HMAC, AEAD |
| **Authenticity** | MAC (shared key) or digital signature (public key) | HMAC, Ed25519 |
| **Key agreement** | Diffie-Hellman | X25519, ECDH P-256 |
| **Non-repudiation** | Digital signature | Ed25519, ECDSA, RSA-PSS |
| **Unpredictability** | CSPRNG | `/dev/urandom`, `getrandom()`, Python `secrets` |

Two principles frame everything. **Kerckhoffs's principle**: a system must stay secure when everything except the key is public, so algorithms are published and keys are secret. And **security is in bits**: a cipher with a 128-bit security level costs roughly 2^128 operations to break by the best known attack; today that is out of reach for anyone. **●●●**

## Encoding, hashing and encryption are different things

This distinction is a classic interview question and a common error in reports.

| | Reversible? | Needs a key? | Purpose | Example |
|---|---|---|---|---|
| **Encoding** | Yes | No | Represent data in another format | Base64, hex, URL encoding |
| **Hashing** | No | No | Fixed-size fingerprint of data | SHA-256 |
| **Encryption** | Yes, with the key | Yes | Confidentiality | AES-GCM |
| **MAC / signature** | Verifies, not reversible | Yes | Integrity and authenticity | HMAC, Ed25519 |

"The password is Base64-encrypted" is wrong twice. Base64 is encoding; and passwords must be hashed with a slow password hash, not encrypted.

## Symmetric encryption

Symmetric ciphers use one key for both encryption and decryption. The two you will meet are **AES** (a block cipher with a 128-bit block and 128-, 192- or 256-bit keys, standardized in FIPS 197) and **ChaCha20** (a stream cipher, fast in software, used in TLS and WireGuard).

A block cipher only encrypts one block, so a **mode of operation** defines how to encrypt more. The mode matters as much as the cipher.

| Mode | Behavior | Verdict |
|---|---|---|
| **ECB** | Each block encrypted independently | **Never use.** Identical plaintext blocks produce identical ciphertext blocks, leaking structure (the "ECB penguin" image remains recognizable) |
| **CBC** | Each block XORed with the previous ciphertext; needs an unpredictable IV | Obsolete for new designs. Not authenticated, so it is malleable and, combined with error messages, exposes **padding oracle** attacks (Vaudenay, 2002) |
| **CTR** | Turns the block cipher into a stream cipher using a counter/nonce | Fine only with unique nonces and a separate MAC; **nonce reuse reveals the XOR of plaintexts** |
| **GCM** | CTR plus an authentication tag (AEAD) | **Recommended.** Use a unique 96-bit nonce per message per key; nonce reuse is catastrophic (it breaks authentication and confidentiality) |
| **ChaCha20-Poly1305** | Stream cipher plus Poly1305 MAC (AEAD, RFC 8439) | **Recommended.** Good where AES hardware is absent |
| **AES-GCM-SIV** | Nonce-misuse-resistant AEAD (RFC 8452) | Use when unique nonces cannot be guaranteed |

**AEAD** (authenticated encryption with associated data) encrypts the message *and* authenticates both it and any headers you want bound to it, in one operation (Rogaway, 2002). **●●●** An attacker who changes any bit makes decryption fail. This is the default you should reach for.

```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)    # store this in a secrets manager, not in code
aead = AESGCM(key)

nonce = os.urandom(12)                        # 96 bits, unique for each message under this key
ciphertext = aead.encrypt(nonce, b"transfer 100 COP", b"user=42")   # last arg: authenticated, not encrypted
plaintext = aead.decrypt(nonce, ciphertext, b"user=42")             # raises InvalidTag if tampered
```

Send the nonce along with the ciphertext (it is not secret). With random 96-bit nonces, NIST limits a single key to about 2^32 messages, after which you must rotate the key (NIST SP 800-38D). **●●●**

## Hash functions

A cryptographic hash maps any input to a fixed-size output (a digest) and must resist three attacks.

| Property | Meaning |
|---|---|
| **Preimage resistance** | Given a digest, you cannot find an input that produces it |
| **Second-preimage resistance** | Given an input, you cannot find another with the same digest |
| **Collision resistance** | You cannot find any two inputs with the same digest |

The **birthday bound** halves the effective strength for collisions: an n-bit hash offers about n/2 bits of collision resistance, which is why digests are at least 256 bits.

| Hash | Output | Status |
|---|---|---|
| **MD5** | 128 bits | Broken for collisions since 2004. Do not use for security |
| **SHA-1** | 160 bits | Practical collision shown in 2017 ("SHAttered", Stevens et al.). NIST plans to retire it by 31 December 2030 |
| **SHA-256, SHA-384, SHA-512** (SHA-2) | 256 to 512 | Current standard (FIPS 180-4) |
| **SHA-3** (Keccak) | 224 to 512 | Different internal design (FIPS 202); a standby and the basis of SHAKE |
| **BLAKE2, BLAKE3** | Flexible | Fast, modern; not NIST-approved |

**Length extension**: SHA-256 and SHA-512 (and MD5, SHA-1) let an attacker who knows `H(secret || message)` compute `H(secret || message || extra)` without the secret. That is why you never build a MAC as a plain hash of key plus message; use HMAC, or SHA-3 / BLAKE2, which are not affected.

**Uses**: file integrity, content addressing (Git), digital signatures (hash then sign), certificate fingerprints, deduplication, commitments. For security-sensitive comparisons, prefer SHA-256 or SHA-3.

## Message authentication codes

A **MAC** proves a message came from someone holding the key and was not changed. **HMAC** (RFC 2104) builds one safely from a hash, for example HMAC-SHA-256. In Python:

```python
import hmac, hashlib
tag = hmac.new(key, message, hashlib.sha256).digest()
ok = hmac.compare_digest(tag, received_tag)    # constant-time comparison
```

Always compare tags with a **constant-time** function. Ordinary `==` stops at the first differing byte, and that timing difference can leak the correct tag one byte at a time. **●●●** When you can, use an AEAD instead of assembling "encrypt then MAC" yourself.

## Passwords and key derivation

Two different problems need two different tools.

### Passwords: use a slow, memory-hard hash

Passwords have low entropy, so an attacker with a stolen database tries billions of guesses. Hash functions like SHA-256 are designed to be fast, which helps the attacker. Password hashes are designed to be slow and, ideally, memory-hungry, which hurts GPUs and custom hardware. Each password gets a unique **salt** so identical passwords produce different hashes and precomputed tables are useless.

| Algorithm | Notes | OWASP minimum parameters |
|---|---|---|
| **Argon2id** (RFC 9106) | Winner of the Password Hashing Competition; first choice | 19 MiB memory, 2 iterations, parallelism 1 (or 46 MiB with 1 iteration) |
| **scrypt** (RFC 7914) | Memory-hard; good second choice | N=2^17, r=8, p=1 |
| **bcrypt** | Older, still acceptable; truncates input at 72 bytes | Cost factor 10 or more |
| **PBKDF2** (RFC 8018) | Not memory-hard; used when FIPS compliance is required | HMAC-SHA-256 with 600,000 iterations |

These values come from the OWASP Password Storage Cheat Sheet; they change as hardware improves, so check the current version. **●●○** Tune the cost so one hash takes a noticeable fraction of a second on your servers.

### High-entropy secrets: use a KDF, not a password hash

When you need to derive several keys from an already strong secret (for example the output of a key exchange), use **HKDF** (RFC 5869). It separates keys by purpose through its `info` parameter. Do not use HKDF to hash user passwords.

## Randomness

Cryptography needs unpredictable numbers: keys, nonces, salts, tokens. Use only the operating system's **cryptographically secure** generator.

| Language | Use | Never use |
|---|---|---|
| Python | `secrets`, `os.urandom` | `random` |
| JavaScript | `crypto.getRandomValues`, `crypto.randomBytes` | `Math.random()` |
| Java | `SecureRandom` | `java.util.Random` |
| C / Linux | `getrandom()`, `/dev/urandom` | `rand()` |
| Go | `crypto/rand` | `math/rand` |

Ordinary generators such as Python's Mersenne Twister are fast but predictable: from enough outputs you can reconstruct the internal state and predict the rest (a linear-algebra exercise; see [Your degree and security](../11-learning-and-career/04-your-degree-and-security.md)). Historical failures include the 2006 to 2008 Debian OpenSSL bug (CVE-2008-0166), which reduced the key space to about 32,000 possible keys, and the Dual_EC_DRBG generator, whose design allowed a suspected backdoor. **●●●**

## Key management

Keys are the secret. Handling them well is most of practical cryptography.

- **Generate** with the CSPRNG at the right length.
- **Store** in a secrets manager, HSM or cloud KMS, not in source code, images, environment files committed to Git or chat messages.
- **Separate** keys by purpose (encryption, signing, authentication) and by environment.
- **Use envelope encryption**: a data key encrypts the data; a master key in the KMS encrypts the data key. Rotating the master key does not require re-encrypting all data.
- **Rotate** on a schedule and after any suspected exposure; plan for it from the start.
- **Limit access** and log every use.
- **Destroy** keys when data must become unrecoverable.

### Key sizes and security levels

NIST SP 800-57 maps algorithms to security strength. **●●●**

| Security strength | Symmetric | Hash (collision) | RSA / DH modulus | Elliptic curve |
|---|---|---|---|---|
| 112 bits | (3DES, disallowed after 2023) | SHA-224 | 2048 bits | P-224 |
| **128 bits** | **AES-128** | SHA-256 | **3072 bits** | **P-256, Curve25519** |
| 192 bits | AES-192 | SHA-384 | 7680 bits | P-384 |
| 256 bits | **AES-256** | SHA-512 | 15360 bits | P-521 |

RSA keys grow much faster than elliptic curve keys for the same strength, which is a reason elliptic curves dominate new designs.

## Common mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| ECB mode | Pattern leakage | Use AEAD |
| Fixed or repeated IV or nonce | Plaintext leakage; forgery with GCM | Fresh random or counter nonce per message |
| Encrypting without authenticating | Tampering; padding oracles | AEAD, or encrypt-then-MAC |
| Home-made algorithms | Broken by experts in days | Use standard primitives |
| Hard-coded keys and secrets | Leak with the code | Secrets manager; rotate leaked keys |
| MD5 or SHA-256 for passwords | Fast cracking | Argon2id |
| Non-secure RNG for tokens | Predictable tokens | CSPRNG |
| `==` to compare MACs or tokens | Timing leak | Constant-time comparison |
| One key for several purposes | Cross-protocol attacks | Derive purpose-specific keys with HKDF |
| Reusing an ECDSA nonce | Private key recovery (this compromised Sony's PS3 code signing) | Use deterministic ECDSA or Ed25519 |
| Rolling your own protocol | Subtle flaws | Use TLS, Noise or an established library |

**Practical implication:** when reviewing code, grep for `ECB`, `MD5`, `SHA1`, `Math.random`, `random.`, `==` near secrets, hard-coded strings that look like keys, and `IV` or `nonce` defined as constants.

## What to use

| Need | Use |
|---|---|
| Encrypt data | AES-256-GCM or ChaCha20-Poly1305 via a high-level library |
| Hash data | SHA-256 or SHA-3 |
| Authenticate with a shared key | HMAC-SHA-256 |
| Store passwords | Argon2id |
| Derive keys from a strong secret | HKDF |
| Key exchange | X25519 |
| Sign | Ed25519 (or ECDSA P-256, RSA-PSS where compatibility requires) |
| Encrypt to a public key | Hybrid encryption (HPKE, RFC 9180) rather than raw RSA |
| Transport | TLS 1.3 |

Prefer libraries that make the safe choice the easy one: **libsodium** (NaCl), Google **Tink**, and Python's `cryptography` package with its high-level recipes. If you must pick one rule, it is this: **use a high-level API that does not ask you to choose a nonce, a mode or a padding.**

## What to do with this

- [ ] Encrypt and decrypt with AES-GCM in Python, then change one byte of the ciphertext and observe the failure.
- [ ] Demonstrate why ECB leaks patterns by encrypting a bitmap in ECB and in GCM.
- [ ] Hash a password with Argon2id and time it; then time SHA-256 for comparison.
- [ ] Solve the first CryptoHack categories (see [Module 1.2](../../roadmap/phase-1-security-fundamentals/02-applied-cryptography.md)).
- [ ] Review a small project's code for the mistakes in the table.

## Key references

FIPS 180-4 · FIPS 197 · FIPS 202 · NIST SP 800-38D · NIST SP 800-57 Part 1 Rev. 5 · OWASP Password Storage Cheat Sheet · RFC 2104 · RFC 5869 · RFC 7914 · RFC 8018 · RFC 8439 · RFC 8452 · RFC 9106 · RFC 9180 · Rogaway (2002) · Stevens et al. (2017) · Vaudenay (2002). Full list in [References](../15-references.md).
