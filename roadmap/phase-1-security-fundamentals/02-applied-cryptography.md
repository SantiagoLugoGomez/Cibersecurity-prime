# Module 1.2: Applied cryptography (weeks 3-5)

Cryptography is where good intentions fail quietly. The goal of this module is not to design crypto but to choose the right primitive, use it correctly, and recognize the classic misuses.

**Main resources:** [CryptoHack](https://cryptohack.org/) (free), [Dan Boneh's Online Cryptography Course](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) (free lectures), [Serious Cryptography, 2nd ed.](https://nostarch.com/serious-cryptography-2nd-edition) (Aumasson, reference), OWASP crypto cheat sheets.

## Week 3: Encoding, hashing and symmetric encryption

**Goal:** separate encoding, hashing and encryption, and use symmetric encryption and password hashing correctly.

**R. Read and study (75 min)**
- Boneh: the introduction and the "Stream Ciphers" and "Block Ciphers" opening lectures.
- OWASP [Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) and [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) cheat sheets.
- Notes: encoding (Base64) vs hashing (SHA-256) vs encryption; symmetric vs asymmetric; AES modes and why ECB leaks patterns; authenticated encryption (AES-GCM, ChaCha20-Poly1305); why password hashing uses Argon2id/scrypt/bcrypt and not SHA-256; salt and pepper.
- Flashcards: ECB vs GCM, what a nonce/IV is, Argon2id vs SHA-256 for passwords, what a MAC provides, why `==` on secrets is unsafe.

**P. Guided practice (90 min)**
- CryptoHack: the "Introduction" and "General" categories, then the first "Symmetric Ciphers" challenges.
- Demonstrate the ECB penguin: encrypt a bitmap with AES-ECB and with AES-CBC/GCM and compare, or reproduce it with a provided image.

**D. Deep practice (3 h)**
- Write a small Python module using the `cryptography` package that: (1) encrypts and decrypts with AES-GCM including the nonce and tag correctly, (2) shows why reusing a nonce is catastrophic, (3) hashes a password with Argon2id and verifies it, and (4) demonstrates that ECB on repeated plaintext blocks produces repeated ciphertext blocks. Comment each with the "why".

**E. English (60 min)**
- Read the OWASP Password Storage Cheat Sheet aloud. Write a 150-word recommendation, in English, for how an app should store passwords in 2026, justifying the algorithm and parameters.

**Check yourself**
1. Why is Base64 not encryption?
2. Why must you never store passwords with plain SHA-256?
3. What does AES-GCM give you that AES-CBC alone does not?
4. What happens if you reuse a nonce with GCM?
5. Why compare MACs with a constant-time function?

**Deliverable:** the annotated crypto module and the ECB demonstration, committed to your notes repo.

## Week 4: Asymmetric crypto, signatures and certificates

**Goal:** understand public-key crypto, digital signatures, and the certificate trust model behind TLS.

**R. Read and study (75 min)**
- Boneh: public-key encryption and digital signatures lectures.
- Serious Cryptography: the RSA and elliptic-curve chapters (concept level).
- Notes: public/private key pairs; RSA vs elliptic curve; key exchange (Diffie-Hellman) vs encryption vs signing; what a digital signature proves; X.509 certificates, certificate authorities and chains of trust; why Ed25519 is preferred for new signatures.
- Flashcards: public vs private key uses, signing vs encrypting, what a CA does, what a certificate chain is, DH key exchange in one line.

**P. Guided practice (90 min)**
- CryptoHack: the "RSA" starter challenges (up to the first few).
- With OpenSSL, generate a key pair, create a self-signed certificate, inspect it (`openssl x509 -text`), and sign and verify a file.

**D. Deep practice (3 h)**
- Build a tiny end-to-end demo in Python: generate an Ed25519 key pair, sign a message, verify it, then tamper with the message and show verification fails. Then set up a local CA: create a root cert, issue a leaf cert for a lab hostname, and configure a local HTTPS server to use it; connect and show the chain validating (and failing when you remove the root).
- This makes TLS concrete and explains why browsers reject self-signed certs.

**E. English (60 min)**
- Read a real CA's Certification Practice Statement summary, or the Let's Encrypt docs intro. Note the vocabulary (issue, revoke, chain, root, intermediate). Explain a certificate chain out loud in two minutes.

**Check yourself**
1. If I encrypt with your public key, who can decrypt, and why?
2. If I sign with my private key, what does that prove and to whom?
3. What is the difference between key exchange, encryption and signing?
4. Why does a browser trust a website's certificate?
5. Why is a self-signed certificate rejected by default, and when is that acceptable?

**Deliverable:** the signature demo and the local CA with a validating (and failing) chain, documented.

## Week 5: TLS in depth, randomness and post-quantum

**Goal:** tie the primitives together in TLS 1.3, understand secure randomness, and know what post-quantum crypto changes.

**R. Read and study (75 min)**
- Re-read [The Illustrated TLS 1.3 Connection](https://tls13.xargs.org/) now that you know every primitive it uses.
- Read about NIST's post-quantum standards: [FIPS 203 (ML-KEM)](https://csrc.nist.gov/pubs/fips/203/final), and that FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) were finalized in August 2024.
- Notes: how TLS 1.3 combines key exchange, authentication and authenticated encryption; forward secrecy; why `secrets` not `random`; what quantum computers threaten (key exchange and signatures, not symmetric crypto as badly) and what ML-KEM replaces.
- Flashcards: TLS 1.3 handshake steps, forward secrecy, CSPRNG vs PRNG, what ML-KEM is for.

**P. Guided practice (90 min)**
- In Python, show why `random` is predictable (seed it, reproduce the sequence) and why `secrets` is not. Connect this to the degree's Linear Algebra course: the Mersenne Twister's state is recoverable because it is linear ([degree-connections.md](../../degree-connections.md)).
- Capture a TLS 1.3 handshake and label every message against the xargs.org walkthrough.

**D. Deep practice (3 h)**
- Write a clear note (portfolio-quality) titled "How TLS 1.3 keeps a connection private and authentic", walking through the handshake and naming which primitive provides confidentiality, integrity, authentication and forward secrecy at each step, with a capture as evidence. Add a short section on what changes under post-quantum crypto.

**E. English (60 min)**
- Read the abstract and introduction of [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final). Summarize, in 150 words of plain English, what problem ML-KEM solves and why it matters now.

**Check yourself**
1. Which parts of TLS 1.3 provide confidentiality, and which provide authentication?
2. What is forward secrecy, and why does it matter if a key leaks later?
3. Why is `random` unsafe for tokens but fine for a dice game?
4. What does a quantum computer threaten in today's crypto, and what is comparatively safe?
5. What does ML-KEM replace, and what does it not?

**Deliverable:** the TLS 1.3 explainer note with capture, and the `random` vs `secrets` demonstration.

**Stretch:** CryptoHack's "Diffie-Hellman" and "Elliptic Curves" categories; the lattice introduction once Linear Algebra covers bases.
