# Track deep dive: Cloud security (12 weeks)

For the student who chose cloud security. Cloud is where most new infrastructure lives, and security engineers who understand it deeply are in high demand. This curriculum builds from cloud fundamentals to attacking and defending a cloud environment, with a focus on AWS (the concepts transfer to Azure and GCP).

**Prerequisites:** Phase 2 complete; Phase 0 networking and Python solid.
**Main resources:** [AWS Skill Builder free tier](https://training.resources.awscloud.com/get-certified-security-specialty/free-digital-training-security), [hackingthe.cloud](https://hackingthe.cloud/), [flaws.cloud](http://flaws.cloud/) and [flaws2.cloud](http://flaws2.cloud/), [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat), [Wiz CTFs](https://www.wiz.io/ctf), [Prowler](https://github.com/prowler-cloud/prowler).
**Certification target:** AWS Certified Security - Specialty or CSA CCSK v5 (see [Phase 4](../phase-4-professional/README.md#stage-3-track-certification-one-in-your-primary-track)).

**Cost control:** use the AWS free account plan ($100 + up to $100 credits, 6 months) and set an [AWS Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) alert before deploying anything. Destroy resources when done. [Azure for Students](https://azure.microsoft.com/en-us/free/students/) gives $100 for 12 months with no card.

## Weeks 1-2: Cloud fundamentals and IAM

**Read/study:** AWS Skill Builder cloud-practitioner essentials and the IAM deep-dive; the shared responsibility model.
**Practice:** in your own AWS account, create users, roles, policies and groups; practice least-privilege policies; enable CloudTrail.
**Deep practice:** build a small multi-account-style setup (or a well-segmented single account) with IAM roles for different functions, and document the design and the least-privilege reasoning.
**English:** write the IAM design document.
**Deliverable:** a documented IAM setup with least-privilege policies.

## Weeks 3-4: Cloud attack techniques

**Read/study:** [hackingthe.cloud](https://hackingthe.cloud/) offensive techniques; how IAM misconfigurations, SSRF-to-metadata, and exposed storage lead to compromise.
**Practice:** [flaws.cloud](http://flaws.cloud/) and [flaws2.cloud](http://flaws2.cloud/) (hosted, free, no account); the [Wiz Big IAM Challenge](https://www.wiz.io/ctf).
**Deep practice:** [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) scenarios in your own account: deploy, attack, and document each path from entry to escalation. Destroy after each.
**English:** write a finding for each CloudGoat scenario.
**Deliverable:** writeups for at least three cloud attack scenarios.

## Weeks 5-6: Cloud detection and logging

**Read/study:** CloudTrail, CloudWatch, GuardDuty, and how cloud incidents are investigated from logs; the cloud sections of MITRE ATT&CK.
**Practice:** generate the attacks from weeks 3-4 in your account and find them in CloudTrail; write detections.
**Deep practice:** build a cloud detection set: for each attack technique you practiced, a detection with the CloudTrail event pattern and an ATT&CK mapping.
**English:** document each detection.
**Deliverable:** a cloud detection set mapped to ATT&CK.

## Weeks 7-8: Posture management and infrastructure as code

**Read/study:** cloud security posture management; [Prowler](https://github.com/prowler-cloud/prowler) and its framework mappings (CIS, NIST); infrastructure-as-code basics with [Terraform](https://developer.hashicorp.com/terraform/tutorials).
**Practice:** run Prowler against your account and triage the findings; write a small Terraform configuration and review it for misconfigurations.
**Deep practice:** take a deliberately insecure Terraform configuration (write one or use a known vulnerable example in your lab), find the misconfigurations, and fix them, documenting each.
**English:** write the posture assessment report.
**Deliverable:** a Prowler-based posture assessment and a fixed Terraform config.

## Weeks 9-10: Securing pipelines and workloads

**Read/study:** CI/CD security, secrets management, container and Kubernetes security basics; supply-chain risk (OWASP A03).
**Practice:** scan a container image for vulnerabilities; set up a basic secure pipeline check in your lab (a GitHub Actions workflow that runs a scanner).
**Deep practice:** build a small secure pipeline: a repo with IaC, a scanner that blocks insecure changes, and secret scanning; document the controls and what each prevents.
**English:** write the pipeline security design.
**Deliverable:** a working secure pipeline example in your repo.

## Weeks 11-12: Capstone tool and assessment

**Deep practice:** build a cloud misconfiguration checker in Python: it reads your own account via the AWS SDK (`boto3`) and reports on a handful of risky settings (public S3 buckets, overly permissive IAM policies, unencrypted volumes, disabled logging), each with a reference and a fix. Then run a full posture assessment of your account and write it up. The tool plus the assessment are your portfolio centerpiece.
**English:** full assessment report and a README for the tool.
**Deliverable:** a cloud misconfiguration checker and a cloud posture assessment report.

## You are ready for the certification when...

- [ ] You can design a least-privilege IAM setup and explain every grant.
- [ ] You can attack and then detect the common cloud misconfigurations.
- [ ] You can read and fix insecure infrastructure-as-code.
- [ ] You can automate a posture check against a real account.
- [ ] You have a cloud tool and a posture assessment in your portfolio.

**Free-only path:** flaws.cloud, the Wiz CTFs, hackingthe.cloud, Prowler and the AWS/Azure free tiers cover most of this; watch the credit limits and always set a budget alert.
