# Incident response

> [!TIP]
> **In short:** an incident response plan is only useful if it was written and rehearsed **before** the incident. NIST's current guidance (SP 800-61 Revision 3, April 2025) stopped describing response as a straight line of phases and instead folds it into the same six functions as the NIST Cybersecurity Framework 2.0: **Govern, Identify, Protect, Detect, Respond, Recover**. The practical message is the same one experienced responders have always given: most of what makes an incident go well or badly was decided beforehand (who is in charge, what "contain" means for this system, who can authorize what), and most of what makes a postmortem valuable is whether the fixes it recommends actually get built.

## From phases to functions

The older, widely taught model (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned, often abbreviated PICERL) is still a fine mental checklist for a single incident's timeline, and the new guidance does not contradict it; it situates response inside the broader, continuous security program instead of treating it as a separate, one-off process.

| CSF 2.0 function | What it means for incident handling |
|---|---|
| **Govern** | Who owns the incident response program, what authority the response team has, what the organization's risk tolerance is, and how legal, communications and leadership are looped in |
| **Identify** | Knowing your assets, data flows and acceptable risk well enough to recognize when something is wrong and to scope an incident quickly |
| **Protect** | The controls in place before an incident, which determine how far an attacker can get and how much damage is possible |
| **Detect** | The logging, telemetry and detections from the earlier pages of this section, which determine whether and how fast you notice |
| **Respond** | The activities most people mean by "incident response": triage, containment, eradication, communication, coordination |
| **Recover** | Restoring normal operation, and feeding what was learned back into Govern, Identify and Protect |

**●●●** (NIST SP 800-61 Revision 3, which supersedes Revision 2 and is built as a CSF 2.0 community profile.) The old phases still describe real work; they now live mostly inside **Respond**, bracketed by preparation (Govern/Identify/Protect) on one side and recovery and feedback (Recover) on the other.

## Preparation: the plan you need before you need it

| Element | Content |
|---|---|
| **Incident response plan** | Roles, authority, escalation paths, communication templates, severity definitions |
| **Classification scheme** | What makes an incident Severity 1 versus 3, and who decides |
| **Contact list**, kept current | Technical responders, management, legal, communications, key vendors, and outside help if needed, reachable outside normal channels in case email or chat is compromised |
| **Playbooks per incident type** | Ransomware, business email compromise, data exposure, DDoS: each has a different first set of actions |
| **Tooling ready beforehand** | Forensic imaging tools, an out-of-band communication channel, pre-authorized access for the response team |
| **Legal and regulatory map** | Which laws and contracts require notification, to whom, and on what timeline (see below and [Colombian regulatory landscape](../10-governance-risk-and-compliance/05-colombian-regulatory-landscape.md)) |
| **Retainers and relationships** | A forensics or incident response firm, cyber insurance contacts, and law enforcement contacts established before they are needed |

A plan nobody has read is not a plan. **Tabletop exercises**, where the team talks through a realistic scenario step by step without touching production systems, are the cheapest way to find the gaps: the contact who no longer works there, the authority nobody actually has, the backup that turns out not to restore.

## Severity and the decision to declare

Most organizations use a simple tiered scale, something like:

| Severity | Example | Expectation |
|---|---|---|
| **Critical** | Active ransomware, confirmed large-scale data theft, compromise of identity infrastructure | Immediate, all-hands response; leadership notified immediately |
| **High** | A compromised server with lateral movement, a significant but contained exposure | Urgent response within the defined window |
| **Medium** | A contained, single-host compromise with no evidence of spread | Standard response during business hours, escalated if scope grows |
| **Low** | A policy violation or a failed attack with no impact | Logged and tracked, handled as routine work |

Declaring an incident formally (rather than treating it as "just another ticket") matters because it changes behavior: it may trigger legal review, change who has authority to take systems offline, and start the clock on notification obligations. When in doubt, declare and downgrade later; the cost of a false declaration is far lower than the cost of a late one.

## Response: triage, containment, eradication

This is the part [Security operations and the SIEM](03-security-operations-and-siem.md) feeds into directly: an escalated, triaged alert becomes an incident the moment someone with the authority to do so declares it.

| Step | Goal | Notes |
|---|---|---|
| **Scoping** | Understand what is actually affected, not just the first signal | Resist the urge to act before you have a working theory of scope; acting on a wrong theory can tip off an attacker or destroy evidence |
| **Containment** | Stop the bleeding without destroying evidence | Options range from network isolation of a single host to disabling an account to blocking an external address; choose the smallest action that stops the specific harm |
| **Evidence preservation** | Keep what you will need later | Volatile data (memory, active network connections) disappears first; see [Digital forensics](05-digital-forensics.md) |
| **Eradication** | Remove the attacker's access and foothold | Not just the malware file: also the account they created, the scheduled task they added, the backdoor credential, the trust relationship they abused |
| **Recovery** | Restore normal operation | From known-clean backups or rebuilt systems, never by "cleaning" a system you cannot fully trust again |
| **Validation** | Confirm the attacker is actually gone | Heightened monitoring after recovery; a quiet system is not the same as a clean one |

### Containment strategies, compared

| Strategy | When to use | Trade-off |
|---|---|---|
| **Isolate the host** (network quarantine, keep it running) | You need to preserve live evidence (memory, active connections) | The attacker may notice and react |
| **Power off** | Destructive malware is actively running (wipers, ransomware mid-encryption) | Loses volatile memory evidence |
| **Disable the account** | Credential compromise without host compromise | Fast, low collateral damage, does not address a host-level foothold if one exists |
| **Block at the network/firewall** | A known command-and-control destination, while you still need the host running | Attacker may have other channels |
| **Do nothing visible yet** (monitor) | You need to understand the full scope of a sophisticated intrusion before acting | Risk of further damage; only appropriate with real justification and sign-off, often with outside expert help |

**A classic mistake:** killing an attacker's access the moment they are found, on the first compromised host you find, before you know whether they have a foothold elsewhere. If the eviction is partial, a sophisticated attacker simply uses the access you missed, now knowing you are looking. For anything beyond a simple, contained case, scope first, then act everywhere at once.

## Communication, inside and out

| Audience | What they need | Who speaks |
|---|---|---|
| **Responders** | Technical detail, in real time, on a channel assumed safe (not the primary email system if that may be compromised) | Incident commander coordinates |
| **Leadership** | Business impact, decisions needed from them, realistic timelines | Incident commander or a designated liaison |
| **Staff** | What to do differently right now (password reset, do not open X), without speculation | Communications, approved messaging |
| **Customers and the public** | Honest, timely, legally compliant disclosure | Communications and legal, together |
| **Regulators** | Legally required notifications, on the legally required timeline | Legal, with technical input |
| **Law enforcement** | When required or beneficial, coordinated through legal | Legal and leadership decide whether and when |

One person, the **incident commander**, should own the decision-making during an active incident, separate from the people doing hands-on technical work. Mixing the two roles is how both the response and the communication suffer.

## Legal and regulatory notification

Notification timelines are a matter of law and contract, not judgment, so they belong in the preparation phase, not improvised during an incident.

| Jurisdiction or standard | What it generally requires |
|---|---|
| **Colombia, Ley 1581 de 2012** and the Superintendencia de Industria y Comercio's guidance for the national database registry | Data controllers are expected to report security incidents affecting personal data to the SIC; a commonly cited window is within 15 business days of becoming aware, though you should confirm the current figure against the SIC's own current circular before relying on it, since this is an area that has been under legislative review. See [Colombian regulatory landscape](../10-governance-risk-and-compliance/05-colombian-regulatory-landscape.md) |
| **PCI DSS** | Card brand and acquirer notification requirements apply immediately on suspected compromise of card data, per your merchant agreement |
| **Sector regulators** (financial, health) | Often carry their own, shorter notification windows than general data-protection law |
| **Contracts** | B2B agreements frequently specify notification timelines to customers and partners, sometimes shorter than any statute |

**◇** Build the actual notification map, with current deadlines and the right regulator contacts, with legal counsel, and keep it current; this page tells you that the map needs to exist, not what every number in it is today.

## Working with outside help

Many organizations, especially smaller ones, do not have the depth to handle a serious incident alone. Knowing this in advance and having a retainer or at least a vetted contact for a forensics and incident response firm turns a frantic search under pressure into a phone call. The same applies to cyber insurance: know what it covers, what it requires you to do (sometimes including using a specific approved vendor), and what voids coverage, before an incident forces you to read the policy for the first time.

## After the incident: the postmortem

The point of a postmortem is to change what happens next time, not to assign blame. A useful postmortem:

| Section | Content |
|---|---|
| **Timeline** | What happened, in order, with timestamps, built from logs and the response team's own notes |
| **Root cause** | How the incident actually started, not just its visible symptoms |
| **What worked** | Keep doing it; say so explicitly, so it survives the next reorganization |
| **What did not work** | Named without blame, in terms of process and tooling gaps |
| **Action items**, each with an owner and a deadline | A postmortem with no owners produces no change |
| **New or improved detections** | Every real incident should leave the detection program measurably better; see [Detection engineering](02-detection-engineering.md) |

A blameless framing is not about avoiding accountability; it is about getting an accurate account of what happened. People who fear blame omit details, and omitted details are exactly the ones a postmortem needs.

## Practice

1. Write a one-page incident response plan for your own home lab or a small project: who is in charge (even if it is only you and a study partner), your severity scale, and your first five actions for a "ransomware on one machine" scenario and a "leaked credential" scenario.
2. Run a 30-minute tabletop exercise with a study partner using one of those scenarios. Narrate decisions out loud and write down every gap you find in your own plan.
3. In your lab, simulate a contained compromise (a reverse shell from an Atomic Red Team-style test is enough), practice the scoping and containment decision explicitly, and write a short postmortem using the template above.
4. Research your own jurisdiction's current data-breach notification requirement and write down the source you verified it against and the date you checked.
5. Draft a one-page communication template for staff and one for customers, written calmly and without speculation, for a hypothetical incident.

These support [Module 1.5](../../roadmap/phase-1-security-fundamentals/05-network-defense-monitoring.md) and the [defensive track](../../roadmap/phase-3-specialization/track-defensive.md) of the roadmap.

## What to do with this

- [ ] Write and keep current a one-page incident response plan for something you are personally responsible for.
- [ ] Run one tabletop exercise, even informally, and record what it revealed.
- [ ] Explain why scoping before eviction matters, with the trade-off it creates.
- [ ] Verify your own jurisdiction's breach notification timeline against a primary source.
- [ ] Write one practice postmortem from a lab exercise, with owners and deadlines on every action item.

## Key references

NIST CSF 2.0 · NIST SP 800-61 Revision 3 · SIC guidance on the national database registry (RNBD). Full list in [References](../15-references.md).
