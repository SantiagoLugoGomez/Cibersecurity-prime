# Containers, Kubernetes and infrastructure as code

> [!TIP]
> **In short:** containers share the host kernel, so container isolation is weaker by default than virtual machine isolation, and the gap between "runs" and "runs safely" is a specific, learnable list of settings: who the process runs as, what capabilities it holds, whether it can reach the host. **Kubernetes** orchestrates many containers and adds its own identity and network layer (RBAC, network policies) on top, with the same "secure by configuration, not by default" character as the cloud IAM covered on the previous page. **Infrastructure as code** (Terraform and similar tools) means your infrastructure's security posture is now a text file: it can be reviewed, scanned and version-controlled before it is ever deployed, which is the single biggest advantage this stack offers over clicking through a console by hand.

## Containers: isolation, with caveats

A container is a set of Linux kernel features (namespaces for isolation, cgroups for resource limits) wrapped around a process, not a separate operating system. That single fact explains most of its security properties.

| Property | Consequence |
|---|---|
| **Shared kernel** | A kernel vulnerability can allow escape from the container to the host, something a hardware-virtualized VM boundary does not share |
| **Image layers** | A container image inherits every vulnerability in its base image and every layer added on top; an old, unscanned base image is a supply chain risk in the same sense covered in [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md) |
| **Root by default, unless configured otherwise** | Many container images run as root inside the container by default, which matters a great deal if the container can also reach the host in any way |
| **Ephemeral by design** | A compromised container may be destroyed and replaced automatically, which can hide an intrusion as easily as it limits persistence; logging and detection must happen centrally, not by inspecting the container afterward |

### Hardening a container

| Setting | Why |
|---|---|
| **Run as a non-root user** | If the process is compromised, it does not already hold root inside the container, which closes off several escape and host-interaction techniques that depend on it |
| **Drop unnecessary Linux capabilities**, starting from none and adding back only what is needed | A container with every default capability has far more ability to interact with the host than almost any application actually requires |
| **Read-only root file system** where possible | An attacker who gains code execution cannot persist by modifying the container's own files |
| **No privileged mode** | A privileged container can access host devices and effectively defeats the isolation the container was supposed to provide |
| **Never mount the container runtime's own socket into a container** | A container that can talk to the runtime that manages containers can usually create a new, unrestricted container, which is equivalent to controlling the host |
| **Scan images for known-vulnerable packages before deployment** | The same software composition analysis discipline from [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md), applied to the image instead of the application dependency list |
| **Use minimal base images** | Fewer installed packages means a smaller attack surface and fewer things to patch |

```dockerfile
FROM python:3.13-slim
RUN useradd --create-home appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
RUN pip install --no-cache-dir -r requirements.txt
USER appuser
CMD ["python", "app.py"]
```

A minimal base image, a dedicated non-root user, and ownership set correctly before switching to it: three small lines that close off a disproportionate share of common container misconfigurations.

## Kubernetes: the same two questions as everywhere else

Kubernetes orchestrates containers across many machines, and its security model asks the same two questions that have run through this entire knowledge base: **who is this (identity), and what may they do (authorization)?** It then adds the network question on top: **what may talk to what?**

### Pod Security Standards

Kubernetes defines three standard profiles for what a pod is allowed to do, enforced by an admission controller at the namespace level:

| Profile | Allows |
|---|---|
| **Privileged** | Everything, including host access; effectively unrestricted |
| **Baseline** | Blocks the known, most dangerous escalations (host namespaces, privileged containers, dangerous capabilities) while remaining broadly compatible with common workloads |
| **Restricted** | Enforces current pod hardening best practice (non-root, no privilege escalation, dropped capabilities, restricted volume types); the appropriate target for security-sensitive workloads |

A practical rollout path, rather than flipping straight to full enforcement: apply the standard in **audit** or **warn** mode first against existing workloads, review what would actually be blocked, fix those workloads, and only then move to **enforce**. Jumping directly to enforcement against a cluster full of existing, unreviewed workloads tends to break things in ways that produce pressure to disable the control entirely rather than fix the workloads.

### RBAC in Kubernetes

Kubernetes RBAC follows the same pattern as cloud IAM on the previous page: roles bind permissions to identities, and the official Kubernetes project guidance is explicit that **wildcard permissions and broad access to the `kube-system` namespace** are the patterns to eliminate first, because `kube-system` holds the cluster's own control-plane components. The same self-granting and role-passing caution from [Cloud IAM and attack paths](02-cloud-iam-and-attack-paths.md) applies here too: an identity that can create or modify RBAC rules, or create pods with a powerful service account attached, can escalate well beyond what its own stated role suggests.

| Risk | Why |
|---|---|
| **Default service account with excess permissions** | Every pod gets a service account automatically; if that default account can do more than the pod needs, every pod in the namespace inherits an unnecessarily wide blast radius |
| **Cluster-admin bound too broadly** | The most powerful built-in role; should be reserved for genuine cluster administration, never granted as a convenience |
| **No network policy** | By default, Kubernetes networking is flat: every pod can reach every other pod unless a network policy says otherwise, which is the cluster-level equivalent of the flat-network problem covered in [Network defense architecture](../03-networking/04-network-defense-architecture.md) |
| **Secrets stored without additional protection** | Kubernetes Secrets are only base64-encoded by default, not encrypted at rest unless the cluster is configured for it; treat this as a configuration requirement, not an assumption |

### A minimal hardening checklist

- [ ] Pod Security Standards set to at least baseline, with a path toward restricted for sensitive workloads.
- [ ] Default service accounts stripped of unnecessary permissions; dedicated, narrowly scoped service accounts per workload that needs one.
- [ ] Network policies defining what each workload may actually talk to, rather than relying on the flat default.
- [ ] Secrets encrypted at rest at the cluster level, and not passed as plain environment variables where a mounted secret would do.
- [ ] RBAC audited for wildcard permissions and unnecessary access to `kube-system`.
- [ ] Images scanned before deployment, and only pulled from registries you trust (see [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md#defenses-for-what-you-consume)).

## Infrastructure as code

**Infrastructure as code** (Terraform, CloudFormation, Pulumi and similar tools) describes cloud and infrastructure resources in text files that are applied by a tool rather than clicked together by hand. This is a major security improvement over manual configuration, for a simple reason: a text file can be reviewed, scanned, versioned and rolled back the same way application code can, which a console click cannot.

| Practice | Why |
|---|---|
| **Scan every change before it is applied**, as a required check | Tools such as Checkov, tfsec (now developed as part of Trivy) and Terrascan check IaC definitions against known-bad patterns (public storage, overly permissive security groups, missing encryption) before anything is deployed, the same role SAST plays for application code in [Secure development and supply chain](../05-application-security/06-secure-development-and-supply-chain.md) |
| **Review the plan, not just the final state** | A plan output shows exactly what will change before it changes; reading it is cheap insurance against an unintended side effect |
| **Protect the state file** | The file tracking current infrastructure state often contains sensitive values (sometimes including secrets); treat it with the same care as a secrets store, never commit it to a public repository |
| **Detect drift** | Infrastructure changed by hand outside the code (an emergency fix, a console click under pressure) diverges from what the code describes; scheduled drift checks, or a cloud-native configuration monitoring service, catch this before it becomes the forgotten exception that causes an incident later |
| **Least privilege for the pipeline that applies changes** | The identity running your IaC tool is, by necessity, powerful; scope it as narrowly as the infrastructure it actually needs to manage, and apply the same workload-identity preference from [Cloud security fundamentals](01-cloud-security-fundamentals.md#workload-identity-instead-of-long-lived-keys) |

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "example-app-logs"
}

resource "aws_s3_bucket_public_access_block" "logs" {
  bucket                  = aws_s3_bucket.logs.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

Writing the public-access block as code alongside the bucket itself, rather than as a separate manual step performed (or forgotten) after creation, is what makes infrastructure as code a genuine security improvement rather than just a convenience: the safe configuration becomes part of the same reviewed, repeatable definition as the resource itself.

## How this section connects

The pattern across this entire section of the knowledge base repeats once more here: a powerful, necessary capability (container orchestration, declarative infrastructure) ships with permissive defaults, and the security work is almost entirely about **deliberately narrowing those defaults to what the specific task needs**, then checking continuously that the narrowing holds. That is the same sentence that closed both [Active Directory attacks](../06-offensive-security/05-active-directory-attacks.md) and [Cloud IAM and attack paths](02-cloud-iam-and-attack-paths.md), because it is the same underlying discipline wearing a different platform's vocabulary.

## Practice

1. Build the minimal Dockerfile pattern above for a small application you have already written, then try to break out of its restrictions (run as root, mount the Docker socket) in a lab and observe how each hardening setting specifically blocks that attempt.
2. Stand up a small Kubernetes cluster locally (kind or minikube), deploy a pod under the privileged, baseline and restricted Pod Security Standards in turn, and document exactly what each level blocks.
3. Write a Kubernetes network policy that allows a front-end pod to reach a back-end pod but blocks it from reaching a third, unrelated pod, and verify the block with a connectivity test.
4. Write a small Terraform configuration for a storage bucket, run Checkov or tfsec against it, fix every finding, and add the scan as a required check in a CI pipeline for that configuration.
5. Deliberately create infrastructure drift (change a security group by hand outside your Terraform code) and show how a plan run or a drift-detection tool surfaces it.

These support [Module 3](../../roadmap/phase-3-specialization/README.md) and the [cloud track](../../roadmap/phase-3-specialization/track-cloud.md) of the roadmap.

## What to do with this

- [ ] Explain why container isolation is weaker by default than virtual machine isolation, and what specifically closes that gap.
- [ ] Apply the minimal container hardening checklist to every image you build.
- [ ] Explain the three Pod Security Standard levels and which one your own workloads should target.
- [ ] Add an IaC security scanner as a required check to a real or lab pipeline.
- [ ] Explain, in your own words, why infrastructure as code is a security improvement and not just a convenience.

## Key references

Checkov, tfsec and Terrascan documentation · CIS Benchmarks for Docker and Kubernetes · Kubernetes documentation on Pod Security Standards and RBAC. Full list in [References](../15-references.md).
