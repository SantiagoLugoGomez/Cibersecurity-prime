# API security

> [!TIP]
> **In short:** the API is the application's real interface. Mobile apps, single-page apps, partners and microservices all talk to it directly, in machine-readable form, often with less review than the screens built on top. Attackers go straight to it, because anything a client can send, an attacker can send. The most common API failures are **authorization at the object, function and property level**, followed by weak authentication, **no limits on resource consumption**, and an **inventory** nobody controls. The fixes are consistent: check authorization on every request, validate every message against a schema, return explicit response models, limit everything, and know which APIs you run.

## Why APIs deserve their own treatment

| Property | Consequence |
|---|---|
| **No UI to hide things** | An admin function missing from the interface is still reachable by URL |
| **Clients are untrusted** | Hidden fields, client-side validation and "the app never sends that" are not controls |
| **Self-describing** | OpenAPI and GraphQL schemas hand attackers a map of every endpoint |
| **Built for automation** | Enumeration, scraping and abuse scale at machine speed |
| **Data-rich responses** | Developers return whole objects and let the client choose what to show |
| **Many versions and owners** | Old, undocumented or test endpoints stay online ("shadow" and "zombie" APIs) |

## The OWASP API Security Top 10 (2023)

| # | Risk | What goes wrong | Main defense |
|---|---|---|---|
| **API1** | **Broken Object Level Authorization** (BOLA) | Changing an object ID returns or alters another user's object | Ownership check on every object access |
| **API2** | **Broken Authentication** | Weak tokens, no throttling on login, credentials in URLs, unchecked JWTs | Proven identity provider, rate limits, strict token validation |
| **API3** | **Broken Object Property Level Authorization** | The API exposes fields it should not (data exposure) or accepts fields it should not (mass assignment) | Explicit request and response schemas |
| **API4** | **Unrestricted Resource Consumption** | No limits on requests, payload size, page size, expensive operations or paid third-party calls | Quotas, limits, timeouts, cost caps |
| **API5** | **Broken Function Level Authorization** | A normal user calls an administrative endpoint | Central policy per route and method; deny by default |
| **API6** | **Unrestricted Access to Sensitive Business Flows** | Automated abuse of legitimate flows (mass sign-up, ticket buying, scraping) | Flow-specific limits, bot defenses, abuse monitoring |
| **API7** | **Server-Side Request Forgery** | The API fetches attacker-chosen URLs | Allowlists and egress control; see [SSRF](04-access-control-ssrf-and-logic-flaws.md#server-side-request-forgery) |
| **API8** | **Security Misconfiguration** | Verbose errors, permissive CORS, debug endpoints, missing TLS, default credentials | Hardened configuration, automated review |
| **API9** | **Improper Inventory Management** | Old versions, undocumented endpoints and non-production hosts exposed | Inventory, versioning policy, retirement |
| **API10** | **Unsafe Consumption of APIs** | The application trusts responses from third-party APIs | Validate and bound all upstream data |

**●●●** (OWASP API Security Top 10, 2023 edition.)

The first, third and fifth entries are all authorization. They are covered with code and a testing method in [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md#how-authorization-fails).

## Authentication for APIs

| Mechanism | Identifies | Notes |
|---|---|---|
| **API key** | An application or client, not a person | Treat as a password: send in a header (never the URL), scope per client and per permission, rotate, revoke, store hashed |
| **OAuth 2.0 access token** | A user (and client) with scopes | Short-lived bearer or sender-constrained; validate issuer, audience, expiry, signature |
| **Mutual TLS** | A client certificate | Strong for business-to-business and service-to-service |
| **Signed requests** (for example HMAC or AWS Signature V4) | A key holder, per request | Ties each request to a timestamp and body; resists replay |
| **Session cookie** | A browser session | Subject to CSRF; see the session section of the identity chapter |

Throttle login, token, password-reset and one-time-code endpoints separately from the rest, and return generic errors. Details of token validation are in [Authorization, sessions and federation](../04-cryptography-and-identity/05-authorization-sessions-and-federation.md#tokens-and-jwt).

## Validate every message against a schema

Describe each endpoint in an **OpenAPI** document and enforce it at runtime. Reject anything the schema does not allow: unknown fields, wrong types, oversized strings, unexpected content types.

```yaml
components:
  schemas:
    ProfileUpdate:
      type: object
      additionalProperties: false
      required: [display_name]
      properties:
        display_name: { type: string, minLength: 1, maxLength: 60 }
        bio:          { type: string, maxLength: 500 }
```

`additionalProperties: false` is the single most effective guard against **mass assignment**: a request with `"role": "admin"` is rejected before it reaches your code. The same idea in application code:

```python
from pydantic import BaseModel, ConfigDict, Field

class ProfileUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display_name: str = Field(min_length=1, max_length=60)
    bio: str = Field(default="", max_length=500)
```

Validate **responses** too. Return explicit response models listing the fields that may leave the system; never serialize a database object directly, because the day someone adds a `password_hash` or `internal_notes` column, the API starts leaking it. **●●●**

| Concern | Practice |
|---|---|
| Content type | Reject bodies whose `Content-Type` does not match what the endpoint accepts |
| Sizes | Limit request body size, string length, array length, nesting depth |
| Pagination | Default and maximum page sizes; no "return everything" |
| Numbers | Range checks; reject negatives where meaningless |
| Identifiers | Validate format; use opaque IDs, but never rely on that for authorization |
| Errors | One consistent format (RFC 9457 "problem details"), generic messages, a correlation ID, no stack traces |

## Limit consumption

| Dimension | Why |
|---|---|
| **Requests per identity** (per API key, user, IP, endpoint) | Stops brute force, scraping and denial of service |
| **Payload and result sizes** | Stops memory exhaustion and bulk extraction |
| **Query cost** (GraphQL depth and complexity, expensive search) | A cheap request can trigger expensive work |
| **Time** | Timeouts on every upstream call and every query |
| **Money** | Cap actions that cost you money (SMS, email, AI model calls, third-party APIs) per identity and per day |
| **Concurrency** | Limit parallel requests per client to blunt races and floods |

Answer limit violations with `429 Too Many Requests` and a `Retry-After` header. Put limits at the gateway **and** in the application for sensitive flows, because attackers use many IP addresses. Rate-limit by *business meaning* too: "five password resets per account per hour" is more effective than a generic per-IP limit.

## Style-specific issues

### REST and JSON

- Check authorization for **every HTTP method** on a resource: protecting `GET /users/{id}` but forgetting `PUT` or `DELETE` is a classic.
- Test alternative routes to the same object (`/api/users/me` versus `/api/users/{id}`) and older versions (`/v1/` versus `/v2/`).
- Ignore method-override headers (`X-HTTP-Method-Override`) unless you need them.
- Do not put secrets or tokens in query strings: they end up in logs, browser history and `Referer` headers.

### GraphQL

| Issue | Detail | Defense |
|---|---|---|
| **Introspection** | The schema is queryable by default | Disable in production or restrict to authenticated developers |
| **Alias and batch abuse** | Hundreds of operations in one HTTP request bypass per-request rate limits and brute-force logins | Count operations, limit aliases and batch size, rate-limit per operation |
| **Deep or cyclic queries** | Nested relations multiply work | Depth and complexity limits, cost analysis, timeouts |
| **Authorization only at the entry point** | Nested fields reach data the root query would deny | Authorize in resolvers, per field and per object |
| **Verbose errors** | Suggestions and stack traces reveal the schema | Mask errors in production |
| **Mutations over `GET`** | CSRF through simple requests | Allow mutations only on `POST` with a non-form content type |
| **Arbitrary queries** | Clients can request any shape | Persisted (allowlisted) queries for first-party clients |

### WebSockets

Cookies are sent automatically with the WebSocket handshake, so a malicious page can open a socket to your server as the victim (**cross-site WebSocket hijacking**). Authenticate the connection, **check the `Origin` header** during the handshake, authorize every message (not only the connection), validate message formats, and rate-limit messages.

### gRPC and internal APIs

Use TLS (mutual TLS between services), enforce authorization in interceptors for each method, disable server reflection in production, set maximum message sizes and deadlines, and do not treat "internal" as "trusted": a single compromised service should not give access to all the others.

### Webhooks

*Receiving* webhooks: verify an HMAC signature over the body with a shared secret, include a timestamp and reject old ones to stop replay, and process idempotently. *Sending* webhooks: users supply the destination URL, so it is an SSRF risk; apply the egress controls in the SSRF section.

## Gateways and WAFs

An API gateway centralizes authentication, rate limiting, schema validation, routing and logging, and it is where a global policy is easiest to apply. It is **not a substitute for application-level authorization**: the gateway does not know that invoice 17 belongs to Alice. Use gateways for coarse controls and consistency, and keep object-level checks in the service.

## Inventory and lifecycle

| Practice | Why |
|---|---|
| Keep an **OpenAPI document per service** in source control and generate the catalog from it | One authoritative list of endpoints |
| Compare the catalog with **gateway and traffic logs** | Finds shadow APIs that nobody documented |
| A **versioning and retirement policy** (announce, `Deprecation` and `Sunset` headers, then remove) | Old versions often lack current protections |
| Separate **non-production** environments and keep production data out of them | Test hosts are exposed more often than people think |
| Require every API owner to register contact and data classification | Someone can be reached when it breaks |

**Practical implication:** API9 is a management problem more than a coding one. If you cannot list your endpoints, you cannot protect them.

## Consuming other people's APIs

Your service is a client of other services (payment providers, identity providers, partners, AI models). Treat their responses as **untrusted input**: validate against a schema, bound sizes and time, use TLS with certificate validation, do not follow redirects blindly, and do not pass their data to interpreters (SQL, shell, HTML) without the encoding you would apply to user input. A compromised or buggy upstream should degrade your feature, not your whole system. **●●○**

## Clients: mobile apps and single-page applications

Anything shipped to a client can be extracted: embedded API keys, "secret" endpoints, hard-coded credentials, signing keys. Keep real secrets on the server, give clients only short-lived tokens, and design as though the attacker has the app binary and can proxy its traffic. Certificate pinning and platform attestation raise the cost of abusing your API from a modified client, but they are not a security boundary against a determined attacker. **●●○**

## Testing and tooling

| Purpose | Tools |
|---|---|
| Explore and replay | Postman, Burp Suite, OWASP ZAP (import an OpenAPI document) |
| Schema-based automated testing | Schemathesis (generates test cases from OpenAPI), the ZAP API scan |
| GraphQL | The Burp extension InQL, introspection queries, GraphQL Voyager |
| Authorization testing | A role-by-endpoint matrix replayed with several accounts; the Burp extension Autorize |
| Secrets in clients | Decompile or inspect the app, search the bundle, run secret scanners |
| Practice targets | OWASP crAPI, VAmPI (vulnerable REST API), Damn Vulnerable GraphQL Application, OWASP Juice Shop, PortSwigger labs |

## Monitoring

| Signal | Possible meaning |
|---|---|
| Sequential or random ID enumeration from one client; bursts of `403` and `404` | BOLA probing |
| Many different accounts failing from one source | Credential stuffing or spraying |
| One API key moving large volumes or traversing all pages | Scraping or data exfiltration |
| Sudden growth in calls to a costly endpoint | Resource or cost abuse |
| Requests to undocumented endpoints or old versions | Shadow API use or reconnaissance |
| Tokens used from unexpected networks | Token theft |

Log identity, endpoint, method, status, size and latency for every request, without logging secrets or full personal data.

## Checklist

- [ ] Every endpoint and method has an authorization rule enforced on the server; the default is deny.
- [ ] Every object access is scoped to the caller.
- [ ] Request schemas reject unknown fields; response models whitelist outgoing fields.
- [ ] Limits exist for rate, size, page size, query cost, time and money.
- [ ] Login, reset and OTP endpoints are throttled separately.
- [ ] Errors are generic, structured and carry a correlation ID.
- [ ] A current OpenAPI document and an owner exist for every API; old versions are retired.
- [ ] Third-party responses are validated like user input.
- [ ] Logs support investigation and alerting without leaking secrets.

## Practice

1. Build a small API (FastAPI or Express) with users, orders and an admin route. Write the BOLA, BFLA and mass-assignment bugs on purpose, exploit each, then fix them with ownership checks, a policy layer and strict schemas.
2. Import your OpenAPI document into OWASP ZAP and run the API scan. Classify the findings and list what the scanner **cannot** know.
3. Run Schemathesis against your API and fix the crashes it finds.
4. Complete the PortSwigger Web Security Academy topics on [API testing](https://portswigger.net/web-security/api-testing) and [GraphQL API vulnerabilities](https://portswigger.net/web-security/graphql).
5. Deploy OWASP crAPI locally and solve at least five of its challenges, writing one up with the [template](../../writeups/TEMPLATE.md).

These support [Module 1.4](../../roadmap/phase-1-security-fundamentals/04-web-security-owasp.md) and the [web track](../../roadmap/phase-3-specialization/track-web.md) of the roadmap.

## What to do with this

- [ ] Name the ten API risks and give one example and one defense for each.
- [ ] Add `additionalProperties: false` (or `extra="forbid"`) to every request schema in one of your projects.
- [ ] Create a role-by-endpoint authorization test matrix and run it in CI.
- [ ] Write rate limits for the login, password reset and the most expensive endpoint of one of your APIs.
- [ ] List every API of a system you know, including the ones missing from the documentation.

## Key references

OWASP API Security Top 10 (2023) · OWASP GraphQL Cheat Sheet · OWASP REST Security Cheat Sheet · OpenAPI Specification · PortSwigger Web Security Academy · RFC 9457. Full list in [References](../15-references.md).

<!-- navigation -->
[← Access control, SSRF and logic flaws](04-access-control-ssrf-and-logic-flaws.md) · [Index](../00-start-here.md) · [Secure development and the software supply chain →](06-secure-development-and-supply-chain.md)
