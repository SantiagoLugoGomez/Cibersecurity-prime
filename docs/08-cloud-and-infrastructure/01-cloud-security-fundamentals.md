# Cloud security fundamentals

> [!TIP]
> **In short:** the cloud does not remove security work; it moves some of it to the provider and leaves the rest, often the part most responsible for real breaches, with you. The **shared responsibility model** draws that line, and it moves depending on what you buy (infrastructure, platform, or software as a service). The failures that actually happen in practice are overwhelmingly on the customer's side of the line: public storage that should have been private, identity permissions far wider than needed, and logging left off. Learn the model, learn each major provider's version of identity and storage, and treat "the cloud" as infrastructure you are still fully responsible for configuring correctly, not a service that configures itself.

## The shared responsibility model

| Service model | Provider secures | You secure |
|---|---|---|
| **IaaS** (virtual machines, networking) | Physical facilities, hardware, hypervisor, host network | Guest operating system, patching, network configuration, identity, data, application |
| **PaaS** (managed databases, managed Kubernetes, serverless platforms) | The above, plus the runtime and platform software | Configuration of the service, identity and access, data, application code |
| **SaaS** (email, CRM, collaboration suites) | Nearly everything about the running software | Configuration, identity, data classification, who has access to what |

The common phrase is "security **of** the cloud versus security **in** the cloud": the provider secures the infrastructure that runs the service; you secure how you configure and use it. **●●●** (AWS, Microsoft and Google all publish versions of this model, consistent on the substance.) Moving up the stack from IaaS to SaaS shifts more responsibility to the provider, but it never reaches zero: even in a fully managed SaaS product, who has access to what, and whether that access is being watched, is still yours.

**Practical implication:** nearly every well-documented cloud breach is a failure on the customer side of this line: a storage bucket left public, an identity role granted far more than it needed, logging that was never turned on, a credential embedded in code. The provider's infrastructure being compromised is comparatively rare. This is why the rest of this section focuses on configuration and identity rather than on attacking the cloud platform itself.

## The core services, across providers

| Concept | AWS | Azure | Google Cloud |
|---|---|---|---|
| **Identity and access** | IAM | Microsoft Entra ID (plus Azure RBAC) | Cloud IAM |
| **Virtual machines** | EC2 | Virtual Machines | Compute Engine |
| **Object storage** | S3 | Blob Storage | Cloud Storage |
| **Managed Kubernetes** | EKS | AKS | GKE |
| **Serverless functions** | Lambda | Azure Functions | Cloud Functions |
| **Audit logging** | CloudTrail | Activity Log / Microsoft Entra audit logs | Cloud Audit Logs |
| **Security posture service** | Security Hub | Microsoft Defender for Cloud | Security Command Center |
| **Secrets management** | Secrets Manager | Key Vault | Secret Manager |
| **Instance metadata service** | IMDS (v1/v2) | Azure IMDS | Metadata server |

Learning one provider deeply and recognizing the same concepts under different names in the others is a far more durable skill than memorizing any single provider's console.

## Identity is the real perimeter

In a traditional network, the firewall was the boundary. In the cloud, **identity and permissions** play that role: anyone with the right credentials and the right role can reach a resource from anywhere on the internet, by design. This is why [Cloud IAM and attack paths](02-cloud-iam-and-attack-paths.md) is the next and most important page in this section, and why every other control here assumes identity is already handled well.

| Principle | In practice |
|---|---|
| **Least privilege by default** | Start every role with nothing, add only what the task needs, and review regularly |
| **No standing use of the root or owner account** | Use it only for the handful of actions that require it, with MFA, and otherwise work through ordinary administrative roles |
| **Prefer temporary credentials to long-lived keys** | Workload identity and short-lived tokens (covered next) remove the risk of a leaked, permanent key |
| **Federate rather than duplicate identities** | Connect to your existing identity provider instead of creating a second, separately managed set of accounts |

## Workload identity instead of long-lived keys

A recurring, serious mistake is embedding a long-lived access key (in code, in a configuration file, in a CI pipeline) so a program can call cloud APIs. Every such key is a secret that can leak exactly the way any other secret leaks (see [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md#secrets-management)), except that a leaked cloud key can often reach far more than a leaked application password.

| Approach | How it works | Why it is safer |
|---|---|---|
| **Instance or attached-identity roles** | A virtual machine, container or function is assigned a role, and the platform's SDK fetches short-lived credentials for it automatically | No key to leak, because there is no long-lived secret in the first place |
| **OIDC federation for CI/CD** | A pipeline exchanges a short-lived, provider-verified identity token for temporary cloud credentials, scoped to that specific job | Removes the long-lived cloud key from CI secrets entirely |
| **Cross-account and cross-cloud roles** | A trusted identity in one account or provider assumes a role in another, for a limited time | Access is time-bound and auditable, instead of a standing credential |

Treat any long-lived access key still in use as a finding to remediate, not a normal state, and prioritize replacing them with one of the mechanisms above.

## The instance metadata service, and why it needs a current version

Every major provider exposes a **metadata service**, reachable only from inside a running instance, that the instance uses to fetch its own configuration and, critically, its temporary credentials. This is convenient and, if reachable by an attacker through a web application running on that instance, extremely dangerous: it was the exact mechanism abused in the 2019 Capital One breach, covered in detail in [Access control, SSRF and logic flaws](../05-application-security/04-access-control-ssrf-and-logic-flaws.md#server-side-request-forgery).

AWS's newer metadata protocol version, **IMDSv2**, requires a session token obtained through a specific request method that most simple server-side request forgery techniques cannot replicate, and AWS made it the account-level default for newly launched instances starting in 2024. Existing instances and AMIs are not automatically upgraded, so an inventory check for instances still permitting the older, token-less version is a concrete, high-value action in any AWS environment. **●●●** Azure and Google Cloud provide their own metadata services with their own hardening guidance; the general principle, confirm the instance's software cannot be tricked into fetching and leaking its own metadata-derived credentials, applies regardless of provider.

## Storage: the most common real-world failure

Publicly exposed object storage is, by a wide margin, the most frequently reported category of cloud data exposure, precisely because the default used to be permissive on some platforms and because "make it public" is a single setting that is easy to apply by mistake to an entire bucket rather than the one file that needed it. **●●○**

| Control | Why |
|---|---|
| **Default to private**, and treat "public" as an explicit, reviewed exception | The overwhelming majority of exposed-storage incidents are an accidental public setting, not a sophisticated attack |
| **Block public access at the account level**, not just the bucket level | A single setting that prevents the mistake from being possible in the first place, across every bucket in the account |
| **Use signed, time-limited URLs** for the rare case where an outsider genuinely needs one specific object | Gives access to exactly one object for a limited time, instead of the whole container |
| **Enable access logging** on storage containing anything sensitive | Without it, you cannot tell whether an exposure was ever actually accessed by anyone else |
| **Scan continuously for public exposure**, not just at setup time | Settings drift, and a bucket made public "temporarily" for a one-off task is a common way exposures persist for years |

## Logging and visibility

Cloud control-plane logs (who called which API, from where, successfully or not) are the cloud equivalent of a Windows Security log, and they are the first thing an investigation needs. Unlike on-premises logging, many providers do not enable comprehensive audit logging by default in every service, which means **a disabled or never-enabled log is itself one of the most common cloud misconfigurations**, and often the one that turns a contained incident into an unanswerable one. Treat enabling and protecting these logs as a day-one task, cross-referenced with the general discipline in [Logging and telemetry](../07-defensive-security/01-logging-and-telemetry.md).

## Cloud security posture management

Manually reviewing every setting across a modern cloud account, which can easily have thousands of resources and settings, does not scale. **Cloud security posture management (CSPM)** tools continuously check configuration against known-good baselines (public storage, missing logging, overly permissive network rules, excessive permissions) and are the practical way most organizations keep up. Each major provider offers a native version (Security Hub, Defender for Cloud, Security Command Center), and third-party and open-source tools exist as well. Treat the findings the same way as any vulnerability feed: prioritized, not read in raw order, using the method in [Vulnerability and exposure management](../07-defensive-security/07-vulnerability-and-exposure-management.md).

## A starting checklist

- [ ] MFA enforced on every account, with no standing use of the root or owner account for daily work.
- [ ] No long-lived access keys where a workload identity or federated credential could be used instead.
- [ ] Public access blocked by default at the account level for object storage, with exceptions reviewed and logged.
- [ ] Audit and access logging enabled, shipped off the platform, and protected, for every account and service in use.
- [ ] A posture management tool (native or third-party) running continuously, with findings triaged, not ignored.
- [ ] An inventory of what is actually deployed, matching the discipline in [Vulnerability and exposure management](../07-defensive-security/07-vulnerability-and-exposure-management.md#asset-inventory).

## Practice

1. Create a free-tier account with one major provider. Enable MFA on the root or owner account, create an ordinary administrative user for daily use, and never use the root credentials again except for the handful of actions that require them.
2. Create a storage bucket, deliberately make one object public with a signed URL instead of making the whole bucket public, and verify in the console that the bucket itself remains private.
3. Enable the provider's audit logging service, perform a few actions, and find the resulting log entries, noting exactly what each one captures.
4. Launch a small virtual machine, attach an instance role with a narrow, specific permission (not administrator), and write a short script running on the instance that fetches its own temporary credentials from the metadata service and uses them for exactly that one permission.
5. Enable the provider's native posture management tool on your free-tier account and work through its top findings using the prioritization method from [Vulnerability and exposure management](../07-defensive-security/07-vulnerability-and-exposure-management.md).

These support [Module 3](../../roadmap/phase-3-specialization/README.md) and the [cloud track](../../roadmap/phase-3-specialization/track-cloud.md) of the roadmap.

## What to do with this

- [ ] Explain the shared responsibility model and say, for one service you use, exactly where the line falls.
- [ ] Explain why most real cloud breaches are configuration failures rather than platform compromises.
- [ ] Replace one long-lived credential in a personal project with a workload identity or federated equivalent.
- [ ] Audit your own cloud accounts for public storage and missing logging, and fix what you find.
- [ ] Explain, from the Capital One case, exactly how the metadata service became the path to the data.

## Key references

AWS, Microsoft and Google shared responsibility documentation · AWS IMDSv2 documentation · Cloud Security Alliance Security Guidance · NIST SP 800-144 and SP 800-145. Full list in [References](../15-references.md).
