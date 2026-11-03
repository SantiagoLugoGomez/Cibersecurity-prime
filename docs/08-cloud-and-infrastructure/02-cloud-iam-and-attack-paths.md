# Cloud IAM and attack paths

> [!TIP]
> **In short:** in the cloud, permissions are the perimeter, and permissions are graphs, not simple lists. A role's danger is rarely visible from reading its own policy in isolation; it comes from what that role, combined with every other role and resource it can touch, adds up to. The recurring pattern behind real cloud privilege-escalation incidents is the same one behind the Active Directory attack paths covered earlier in this knowledge base: a permission that looks narrow turns out to be one step away from something much broader, because it lets its holder **grant themselves more**, **act as something more powerful**, or **modify the rules that would have stopped them**. Defending this means auditing the graph, not just the policy document.

## How cloud IAM decisions are made

| Concept | Meaning |
|---|---|
| **Principal** | Who is asking: a user, a role, a service, a federated identity |
| **Action** | What they are asking to do (an API call) |
| **Resource** | What they are asking to do it to |
| **Policy** | A document attaching allowed (and sometimes explicitly denied) actions to principals or resources |
| **Role** | An identity that can be assumed temporarily, usually by a workload or by another principal, rather than logged into directly |
| **Evaluation logic** | The provider's rule for combining multiple, possibly conflicting policies into one allow-or-deny decision |

The specific evaluation logic differs by provider (AWS evaluates explicit denies first, then looks for an explicit allow across every applicable policy; Azure RBAC and Google Cloud IAM have their own combination rules), but the conceptual risk is the same everywhere: **wide identity policies, attached broadly, are hard for a human to reason about by inspection**, which is exactly why the graph-based tools described below exist.

## The shape of cloud privilege escalation

Just as an Active Directory compromise is a path through relationships rather than a single exploit (see [Active Directory attacks](../06-offensive-security/05-active-directory-attacks.md)), a cloud identity compromise is usually a path through permissions: a foothold with limited rights, enumeration of what that identity can actually reach, and one of a short list of well-known **permission patterns** that lets a limited identity become a much more powerful one.

| Pattern | The underlying design feature | Why it is dangerous when granted too broadly |
|---|---|---|
| **Self-granting permissions** | Identity systems allow an administrator to create or attach policies to principals, so that administration itself can be delegated | An identity that can modify its own or another principal's permissions can grant itself anything, regardless of what it started with |
| **"Pass a role" permissions** | Many cloud services need to be told which role to run as (a function, a deployment, a virtual machine) | An identity that can launch a resource **and** pass it a powerful role effectively inherits that role's power, even without being allowed to assume it directly |
| **Resource-based policy editing** | Some resources (storage, queues, secrets) carry their own policy stating who may access them | An identity that can edit a resource's own policy can grant itself, or anyone, access to that resource regardless of its own identity-based permissions |
| **Credential and key creation** | Identity systems let an administrator create new access keys or credentials for a principal | An identity that can create credentials for a more powerful principal can then authenticate as that principal |
| **Federation and trust configuration** | Cross-account and cross-cloud trust relationships let one identity provider vouch for principals in another account | Misconfigured trust conditions (an overly broad federation condition, a missing restriction on which external identities are trusted) can let an outside party assume a role they were never meant to reach |
| **Logging and detection tampering** | Administrative permissions typically include the ability to disable or redirect audit logging | An identity that reaches this pattern can make its own further actions invisible, which is why protecting logging configuration itself is treated as its own tier-0-equivalent concern in [Cloud security fundamentals](01-cloud-security-fundamentals.md#logging-and-visibility) |

**Practical implication:** none of these is a flaw in the platform. Each is a legitimate, necessary capability (administration has to be delegable; services have to be told which role to run as) that becomes a problem only when granted more broadly than the specific task requires. The fix, as with Active Directory, is almost always the same question asked rigorously: does this identity need this permission for its actual job, or was it granted for convenience?

## Enumeration: the graph maps itself, here too

An identity with even modest read permissions can typically enumerate a large part of an account's IAM structure: other roles, their attached policies, trust relationships, and resource policies. As with Active Directory, the practical question for both attackers and defenders is not "is there a vulnerability?" but "**what is the shortest path from this identity to something that matters?**"

Open-source graph-based tools exist specifically to answer that question for cloud IAM, the direct equivalent of the Active Directory graph tools covered earlier: they ingest an account's policies, roles and resources, and compute reachable permission paths rather than requiring a human to trace every policy by hand.

**Defender's use.** Run one of these tools against your own accounts on a schedule, the same discipline as the Active Directory graph audits. Treat every short, unintended path to broad administrative capability as a finding, prioritized the same way any other exposure is in [Vulnerability and exposure management](../07-defensive-security/07-vulnerability-and-exposure-management.md). Native cloud posture tools (introduced in [Cloud security fundamentals](01-cloud-security-fundamentals.md#cloud-security-posture-management)) increasingly surface some of these paths directly as findings, which is a reasonable starting point if you are new to this kind of audit.

## Designing IAM to resist this

| Practice | Effect |
|---|---|
| **Least privilege, scoped to specific resources**, not broad wildcard actions on broad wildcard resources | Shrinks what any single compromised identity can reach |
| **Separate who can use a permission from who can grant it** | Administration of IAM itself should be a narrow, audited role, not a side effect of a broader administrative grant |
| **Restrict "pass role" permissions to the specific roles a task actually needs**, never to all roles | Closes the most common escalation pattern in the table above |
| **Require conditions on federation and trust relationships** (specific external identities, specific source systems, short-lived sessions) | Narrows a trust relationship from "anyone who can obtain a token" to the specific, intended caller |
| **Protect logging configuration with its own narrow, highly audited permission set** | Keeps the detection layer intact even if another identity is compromised |
| **Regularly review unused permissions and stale credentials** | Permissions granted for a long-finished task are pure risk with no remaining benefit |
| **Use permission boundaries or equivalent guardrails** | A ceiling that even an administrator-granted identity cannot exceed, limiting the blast radius of a mistake or a compromise in the granting process itself |

## Detection

| Signal | Possible meaning |
|---|---|
| An identity creating or attaching a new, broad policy to itself or another principal | Self-granting escalation |
| A role-launch or deployment action immediately followed by actions far outside that identity's normal pattern | Role-passing escalation |
| A resource policy change granting access to an unfamiliar principal or account | Resource-based policy abuse |
| New access keys or credentials created for a sensitive principal, outside a normal provisioning workflow | Credential creation abuse |
| A change to federation trust conditions, or a sign-in from an unexpected external identity under an existing trust | Federation abuse |
| Audit logging disabled, redirected, or its retention shortened | An attempt to operate without being seen; treat this as one of the highest-priority alerts an account can produce |
| API calls from an identity at a volume or of a type far outside its historical baseline | A compromised credential or role being used for reconnaissance |

These pair with the cloud-specific logging guidance in [Cloud security fundamentals](01-cloud-security-fundamentals.md#logging-and-visibility) and the general detection discipline in [Detection engineering](../07-defensive-security/02-detection-engineering.md).

## Practice

1. In a free-tier cloud account, create two roles: one deliberately over-permissioned (able to attach policies to other principals) and one that only needs to read a single storage bucket. Use a graph-based IAM analysis tool to compute the path from the narrow role to full administrative control, and document the single permission change that would close it.
2. Create a role meant only to run one specific function, and a second, more powerful role. Configure the first role's "pass role" permission to be restricted to itself only, and confirm it cannot be used to launch a resource with the second, more powerful role attached.
3. Enable your account's audit logging, then test what a permission change to disable or redirect it actually looks like in the logs of a system that is still receiving them, and write the detection rule for it.
4. Review one of your own cloud accounts (or a deliberately built lab account) for every identity with a "pass role" or self-policy-attachment permission, and justify or remove each one.
5. Write a one-page comparison of the Active Directory and cloud IAM privilege-escalation patterns, noting what is structurally identical between them and what is genuinely different.

These support [Module 3](../../roadmap/phase-3-specialization/README.md) and the [cloud track](../../roadmap/phase-3-specialization/track-cloud.md) of the roadmap.

## What to do with this

- [ ] Explain why a cloud role's danger often cannot be judged from reading its own policy alone.
- [ ] Name the six permission patterns in the table above and the legitimate feature each one abuses.
- [ ] Run a graph-based IAM audit against a lab account and fix the shortest unintended path it finds.
- [ ] Explain why protecting logging configuration is treated as its own priority, separate from protecting data.
- [ ] Compare this page's patterns against [Active Directory attacks](../06-offensive-security/05-active-directory-attacks.md) and say what the two domains have in common structurally.

## Key references

AWS, Azure and Google Cloud IAM documentation · Cloud Security Alliance Security Guidance · NIST SP 800-210. Full list in [References](../15-references.md).
