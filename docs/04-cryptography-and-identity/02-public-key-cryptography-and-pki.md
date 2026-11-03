# Public-key cryptography and PKI

> [!TIP]
> **In short:** public-key cryptography lets strangers establish secrets and verify identities without sharing a key beforehand. In practice it does three jobs: **key agreement** (Diffie-Hellman, X25519), **digital signatures** (Ed25519, ECDSA, RSA-PSS) and, rarely, **encrypting small secrets**. A **public-key infrastructure (PKI)** binds public keys to identities through **certificates** issued by **certificate authorities**, and the web's trust rests on that chain. Quantum computers will break today's RSA and elliptic curves, so migration to **post-quantum** algorithms has already started.

## Two keys, two jobs

A key pair has a **public key** (shared freely) and a **private key** (kept secret). What you can do depends on which operation you perform.

| Operation | Who uses which key | Guarantee |
|---|---|---|
| **Encryption** | Anyone encrypts with the recipient's *public* key; only the recipient decrypts with the *private* key | Confidentiality |
| **Digital signature** | The signer signs with the *private* key; anyone verifies with the *public* key | Integrity, authenticity and non-repudiation |
| **Key agreement** | Each side combines its own private key with the other's public key | A shared secret that no eavesdropper can compute |

A common misunderstanding: a signature is *not* "encrypting with the private key". The two are different operations with different security properties, and treating them as the same leads to design errors.

Asymmetric operations are slow and have size limits. Real systems use them to agree on or protect a symmetric key, then use fast symmetric encryption for the data. This is **hybrid encryption**, and TLS, SSH, Signal and disk encryption all work this way.

## The algorithms you will meet

| Family | Algorithms | Used for | Notes |
|---|---|---|---|
| **Finite-field Diffie-Hellman** | DH (Diffie and Hellman, 1976) | Key agreement | Needs large, well-chosen groups (2048 bits or more, RFC 7919). The 2015 *Logjam* attack exploited 512-bit export-grade groups still enabled on servers |
| **RSA** (Rivest, Shamir, Adleman, 1978) | RSA-OAEP, RSA-PSS | Encryption, signatures | Security rests on the difficulty of factoring `n = p × q`. Padding is critical; keys are large and slow |
| **Elliptic curve** | ECDH, ECDSA (NIST P-256, P-384), X25519, Ed25519 | Key agreement, signatures | Same security with much smaller keys; fast. X25519 and Ed25519 (RFC 7748, RFC 8032) are designed to be hard to misuse |
| **Post-quantum** | ML-KEM, ML-DSA, SLH-DSA | Key encapsulation, signatures | See the end of this page |

### RSA in practice

- Use **at least 2048-bit** keys; prefer **3072** for anything meant to last beyond 2030 (see the security-strength table in [Cryptography foundations](01-cryptography-foundations.md)).
- Use **OAEP** for encryption and **PSS** for signatures. The older PKCS#1 v1.5 encryption padding allowed Bleichenbacher's 1998 *padding oracle* attack, which reappeared in new forms for 20 years, most recently as ROBOT in 2017. **●●●**
- Generate keys with a good random source. Studies of internet-wide scans in 2012 found many keys sharing prime factors because of poor randomness at generation time, which made them trivially factorable (Heninger et al., 2012; Lenstra et al., 2012). **●●●**

### Elliptic curves in practice

- **ECDSA** signatures require a fresh, secret random number for every signature. Reusing it, or using a predictable one, reveals the private key. Sony's PlayStation 3 signing key was recovered this way in 2010 because the implementation used a constant. **●●●** **Ed25519** derives the nonce deterministically from the key and message and so avoids the problem.
- Implementations must validate that received public keys are on the curve; failing to do so enables *invalid curve* attacks.
- Prefer X25519 for key agreement and Ed25519 for signatures when you control both ends. Use P-256 where compatibility requires it.

## Digital signatures

To sign, the sender hashes the message and signs the digest with the private key. The verifier recomputes the hash and checks the signature with the public key.

A valid signature shows that the message has not changed since signing and that whoever holds the private key produced it. It says nothing about who that is unless the public key is **bound to an identity**, which is what certificates do. Typical uses are code signing, software update verification, signed commits and tags, document signing, signed container images (for example with Sigstore), and the authentication step inside TLS and SSH.

## Certificates and PKI

An **X.509 certificate** (RFC 5280) is a signed statement: "this public key belongs to this subject". The signer is a **certificate authority (CA)**.

| Field | Meaning |
|---|---|
| **Subject** | The entity the certificate identifies |
| **Issuer** | The CA that signed it |
| **Validity** | Not before / not after dates |
| **Public key** | The key being certified |
| **Subject Alternative Name (SAN)** | The DNS names or IP addresses the certificate covers. **Clients match names against the SAN**, not the old Common Name |
| **Key Usage / Extended Key Usage** | What the key may do: `serverAuth`, `clientAuth`, `codeSigning`, and so on |
| **Basic Constraints** | `CA:TRUE` for CAs; limits chain depth |
| **CRL / OCSP / AIA** | Where to check revocation and fetch the issuer |
| **SCTs** | Proof the certificate was logged in Certificate Transparency |

### The chain of trust

```
Root CA (self-signed, in the operating system or browser trust store)
  └── Intermediate CA (signed by the root; issues leaf certificates)
        └── Leaf certificate for www.example.com (what the server presents)
```

The root's private key stays offline; intermediates do the day-to-day issuing so that a compromise does not require replacing the root. The server sends the leaf and intermediates; the client already has the root.

### What a client checks

A client that accepts a certificate must verify **all** of these:

1. The signature chain up to a root it trusts.
2. Every certificate is within its validity period.
3. The requested hostname matches the SAN.
4. The key usage and constraints permit this use.
5. The certificate has not been revoked (as far as the client can tell).
6. Where required, that it carries valid Certificate Transparency proofs.

A very common and serious bug is code that turns this checking off: `requests.get(url, verify=False)`, `InsecureSkipVerify: true`, or a trust-all `TrustManager`. It makes TLS useless against an active attacker. Grep for it. **●●●**

### Inspecting certificates

```bash
openssl s_client -connect example.com:443 -servername example.com -showcerts </dev/null
openssl x509 -in cert.pem -noout -text
openssl x509 -in cert.pem -noout -subject -issuer -dates -ext subjectAltName
```

### Types and uses

| Type | Meaning |
|---|---|
| **DV** (domain validated) | The CA checked control of the domain; automated; dominant on the web |
| **OV / EV** (organization / extended validation) | Additional vetting of the organization; browsers no longer show special EV indicators, so the value is limited |
| **Wildcard** (`*.example.com`) | Covers all subdomains at one level; convenient but one stolen key affects everything |
| **Client certificates** | Authenticate users or devices; the basis of **mutual TLS (mTLS)** between services |
| **Code-signing certificates** | Sign software and drivers |
| **Internal / private CA** | Used for internal services and devices (for example Active Directory Certificate Services, Smallstep, HashiCorp Vault) |

## Lifetimes, automation and revocation

### Certificates are getting short-lived

Public TLS certificates have been shortened repeatedly. Under the CA/Browser Forum ballot SC-081v3, the maximum validity falls from 398 days to **200 days** for certificates issued from 15 March 2026, to **100 days** from 15 March 2027 and to **47 days** from 15 March 2029. **●●○** Manual renewal becomes impractical, which is the point: short lifetimes limit the damage of key compromise and make revocation less critical. Automate with **ACME** (RFC 8555) using Let's Encrypt and clients such as certbot, or cert-manager on Kubernetes. An expired certificate is a common cause of outages, so monitor expiry as a service-level matter.

### Revocation is weak

When a key is compromised, the certificate should be revoked, but clients cannot reliably learn that.

| Mechanism | Idea | Problem |
|---|---|---|
| **CRL** (RFC 5280) | Download a signed list of revoked serial numbers | Large, slow, stale |
| **OCSP** (RFC 6960) | Ask the CA about one certificate | Privacy leak (the CA sees what you visit); availability dependency; most clients **soft-fail**, so an attacker who can block the check wins |
| **OCSP stapling** | The server attaches a recent signed OCSP response | Better, but optional |
| **Browser-pushed lists** (CRLite, CRLSets) | Browsers distribute compact revocation data | Not universal |

Let's Encrypt ended its OCSP service in August 2025 and relies on CRLs and short lifetimes. **●●●** The practical lesson: assume revocation will not save you, shorten lifetimes and protect the private keys.

### Certificate Transparency

**Certificate Transparency (CT)** requires CAs to record every issued certificate in public, append-only logs (RFC 6962; RFC 9162 for the second version). Browsers require proof of logging. This lets domain owners **detect certificates they did not request**. Monitor the logs for your domains with free services such as crt.sh or with your CA's monitoring. The same public logs help attackers and testers enumerate subdomains, so CT is both a defense and a source of reconnaissance data (see [Reconnaissance and enumeration](../06-offensive-security/02-reconnaissance-and-enumeration.md)). **●●●**

Add **CAA DNS records** that list which CAs may issue for your domain.

## When PKI fails

| Event | Lesson |
|---|---|
| **DigiNotar, 2011** | A Dutch CA was compromised and fraudulent certificates for many domains, including `*.google.com`, were issued and used against users in Iran. Browsers removed trust and the company collapsed: CA compromise is catastrophic and trust can be withdrawn |
| **Symantec CAs, 2017 to 2018** | After repeated mis-issuance, major browsers progressively distrusted the CAs' certificates: the ecosystem polices CAs |
| **Pinning (HPKP)** | Header-based public key pinning was meant to protect against rogue CAs, but a mistake could lock a site out for months, and it was removed from browsers. CT and CAA replaced it for most uses |

**Practical implication:** the trust in a certificate is only as strong as the weakest CA your clients trust. Reduce that exposure with CAA, CT monitoring, short lifetimes and, for internal services, a private CA you control.

## Common mistakes

| Mistake | Fix |
|---|---|
| Disabling certificate verification "temporarily" | Never do it in production; install the internal CA in the trust store instead |
| Matching the Common Name instead of the SAN | Use the SAN |
| Reusing one private key across servers and renewals | Generate a fresh key per certificate; keep keys on the system that needs them |
| Private keys in Git, images, tickets or CDNs you do not control | Treat as compromised and rotate |
| Wildcards everywhere | Prefer specific names; limit key distribution |
| No expiry monitoring | Alert at least 30 days ahead, and automate renewal |
| Trusting a self-signed certificate by clicking through warnings | Pin it explicitly or use a proper private CA |

## Lab: build a tiny CA

Do this in your lab to make the chain concrete (OpenSSL 3).

```bash
# 1. A CA key and self-signed root certificate
openssl ecparam -name prime256v1 -genkey -noout -out ca.key
openssl req -x509 -new -key ca.key -sha256 -days 365 \
  -subj "/CN=Lab Root CA" -out ca.crt

# 2. A server key and certificate request with a SAN
openssl ecparam -name prime256v1 -genkey -noout -out server.key
openssl req -new -key server.key -subj "/CN=lab.local" \
  -addext "subjectAltName=DNS:lab.local" -out server.csr

# 3. The CA signs the request
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -days 90 -sha256 -copy_extensions copy -out server.crt

# 4. Verify the chain
openssl verify -CAfile ca.crt server.crt
```

Run a local HTTPS server with `server.crt` and `server.key`, connect with `curl --cacert ca.crt https://lab.local`, then remove the CA and watch validation fail.

## The post-quantum transition

A large, fault-tolerant quantum computer running **Shor's algorithm** would break RSA, finite-field DH and elliptic-curve cryptography. Such machines do not exist today, but two facts make the migration urgent: data with a long confidentiality life can be recorded now and decrypted later (*harvest now, decrypt later*), and replacing cryptography across an organization takes years. **Grover's algorithm** only halves the effective strength of symmetric ciphers and hashes, so AES-256 and SHA-256 remain adequate. **●●●**

NIST published the first three post-quantum standards in August 2024:

| Standard | Algorithm (original name) | Use |
|---|---|---|
| **FIPS 203** | ML-KEM (CRYSTALS-Kyber) | Key encapsulation (key exchange) |
| **FIPS 204** | ML-DSA (CRYSTALS-Dilithium) | Digital signatures |
| **FIPS 205** | SLH-DSA (SPHINCS+) | Hash-based signatures, a conservative alternative |

A further signature standard (FN-DSA, from Falcon) and a backup key-encapsulation algorithm (HQC, selected in March 2025) are in progress. **●●○**

Key exchange is moving first because of harvest-now-decrypt-later. A **hybrid** key exchange combines a classical algorithm with ML-KEM, so the connection stays secure if either one holds. **X25519MLKEM768** is already the preferred group in major browsers and widely deployed by CDNs, and a large share of browser traffic to them uses it. **●●○** Signatures and certificates will follow, which is harder because chains, hardware and long-lived devices are involved.

On timelines, NIST's transition report (NIST IR 8547, finalized in October 2026) sets the direction that quantum-vulnerable public-key algorithms are deprecated after 2030 and disallowed after 2035 for federal use. **●●○** The NSA's CNSA 2.0 guidance sets earlier dates for national security systems.

What to do now:

- **Inventory** where you use RSA, ECC and DH, including in libraries, devices, VPNs, certificates and code signing. Practise **crypto-agility**: be able to swap algorithms without redesign.
- **Prioritize** data that must stay confidential for 10 years or more.
- **Enable hybrid key exchange** where your TLS stack and clients support it.
- **Track vendor roadmaps** for HSMs, VPNs and certificate authorities.

## What to do with this

- [ ] Explain, without notes, why a signature is not encryption with the private key.
- [ ] Build the lab CA above and issue a certificate with a SAN.
- [ ] Use `openssl s_client` to dump the chain of three websites and identify the root of each.
- [ ] Find your domain's (or a public site's) certificates in crt.sh.
- [ ] Search a codebase for `verify=False` and `InsecureSkipVerify` patterns.
- [ ] Complete the RSA starter challenges on CryptoHack ([Module 1.2](../../roadmap/phase-1-security-fundamentals/02-applied-cryptography.md)).

## Key references

CA/Browser Forum SC-081v3 · Diffie and Hellman (1976) · FIPS 203 · FIPS 204 · FIPS 205 · Heninger et al. (2012) · Lenstra et al. (2012) · NIST IR 8547 · RFC 5280 · RFC 6960 · RFC 6962 · RFC 7748 · RFC 7919 · RFC 8032 · RFC 8555 · Rivest, Shamir and Adleman (1978). Full list in [References](../15-references.md).
