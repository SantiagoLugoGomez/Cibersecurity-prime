# Security operations and the SIEM

> [!TIP]
> **In short:** a security operations center (SOC) is the function that turns the logging and detections from the previous two pages into a continuous, staffed function: someone is watching, someone triages what fires, someone investigates what matters, and someone makes sure the detections stay good. The **SIEM** is the platform most SOCs build this around: it centralizes logs, runs correlation and detection rules, and gives analysts a place to search and respond. None of the technology matters if **alert triage** is broken, which is why the most common SOC failure is not a missing tool but a queue of alerts nobody can keep up with.

## What a SOC does

| Function | In practice |
|---|---|
| **Monitoring** | Watching dashboards and queues for what the detections surface |
| **Triage** | Deciding, quickly, whether an alert is a false positive, needs more context, or is a real incident |
| **Investigation** | Following a triaged alert far enough to know what happened and what to do |
| **Escalation** | Handing confirmed incidents to [incident response](04-incident-response.md), with the context already gathered |
| **Threat hunting** | Proactively looking for what detections do not already catch (see [Threat intelligence and hunting](06-threat-intelligence-and-hunting.md)) |
| **Detection engineering** | Writing, testing and tuning the rules the SOC depends on (see [Detection engineering](02-detection-engineering.md)) |
| **Reporting and metrics** | Showing whether the function is working, to the team and to leadership |

A small organization may do all of this with one part-time person and a free SIEM; a large one may split it into tiers across a 24-hour rotation. The functions are the same either way.

## Tiered analyst work

| Tier | Typical scope | Produces |
|---|---|---|
| **Tier 1 (triage)** | Works the alert queue; closes clear false positives; escalates anything uncertain with the context gathered so far | A fast, consistent first pass |
| **Tier 2 (investigation)** | Takes escalated alerts; pivots across log sources; determines scope and root cause; declares an incident when warranted | A scoped, explained case |
| **Tier 3 (hunting and engineering)** | Hunts for what rules miss; writes and tunes detections; handles the hardest investigations | Better coverage over time |

This is a convenient way to organize work, not a rigid hierarchy: a one-person team does all three; a mature team routes work by complexity, not by job title. The dependency runs in one direction worth remembering: **alert quality has to be stable before you add automation or expand volume**, because automating a queue full of noise just produces noise faster.

## The SIEM's job

A SIEM does four things that, together, are what makes a SOC's job tractable instead of impossible:

1. **Centralizes** logs from the sources in [Logging and telemetry](01-logging-and-telemetry.md) into one searchable place.
2. **Normalizes** them into comparable fields, so one query can span sources that originally looked nothing alike.
3. **Correlates** across sources to express detections that no single log could support alone (see the cross-source example in [Detection engineering](02-detection-engineering.md)).
4. **Presents** the result as alerts, dashboards and a search interface analysts actually use.

| Option | Character | Notes |
|---|---|---|
| **Wazuh** | Free and open source (Apache 2.0), agent-based, built-in detection rules and compliance mappings | A reasonable starting point for a home lab or a small team with no budget |
| **Elastic Security** | A free tier with core SIEM and detection features; paid tiers add analytics | Strong search performance; check current licensing terms, which are not OSI open source for the bundled components |
| **Splunk Free** | 500 MB of daily ingestion, no clustering | Useful to learn Splunk's query language in a lab; the cap makes it impractical beyond that |
| **Commercial cloud-native SIEMs** | Vendor-hosted, scale without self-hosting infrastructure | Priced by ingestion volume; costs grow with log volume, which argues for deciding what to log deliberately (see [Logging and telemetry](01-logging-and-telemetry.md)) |

**Practical implication for a student lab:** Wazuh or a self-hosted Elastic stack cost nothing but your own compute and time, and both are common enough in real SOCs that the skills transfer directly.

## Alert triage

A triage workflow that scales from one person to a shift of ten:

1. **Read the alert's own context first**: what fired, on what host, for what account, at what time.
2. **Pivot to the raw event** behind the alert; never act on the alert summary alone.
3. **Ask what else happened around it**: same host, same account, nearby in time. Most SIEMs support this as a one-click pivot from an alert.
4. **Compare against the known-good baseline** you documented when the detection was built (see the false-positive notes in [Detection engineering](02-detection-engineering.md)).
5. **Decide**: close as benign (and note why, so the next analyst does not redo the work), escalate for deeper investigation, or declare an incident.
6. **Record the decision**, even a quick one. A triage history is what lets you measure the program and retrain a noisy detection.

| Common mistake | Why it hurts |
|---|---|
| Closing alerts without recording a reason | The same question gets re-investigated from zero every time it fires |
| Treating every alert as equally urgent | Analysts burn out and stop reading carefully |
| Never feeding triage outcomes back to detection engineering | Noisy rules stay noisy forever |
| Measuring only alert volume | Volume says nothing about whether real incidents are caught |

## Runbooks

A **runbook** (or playbook) is a written, repeatable procedure for a specific alert type: what to check, in what order, and when to escalate. Runbooks are what let a Tier 1 analyst handle a case correctly on their first week, and what keep an experienced analyst from skipping a step at 3 a.m.

```markdown
## Runbook: impossible travel sign-in alert

1. Confirm the two sign-in locations and the time between them in the identity provider's log.
2. Check whether the account uses a VPN or corporate proxy that could explain the apparent location (known exit nodes list).
3. Check for other risk signals on the same account in the same window (new device, new MFA method, failed attempts).
4. If unexplained: suspend the session, require a password reset and MFA re-registration, notify the user through a channel other than email, and escalate to incident response.
5. If explained: close with the reason recorded.
```

Build runbooks for your highest-volume and highest-risk alert types first, and update them whenever a triage decision surprises someone experienced.

## Metrics that mean something

| Metric | What it tells you | Caution |
|---|---|---|
| **Mean time to detect (MTTD)** | How fast a real incident is noticed after it starts | Hard to measure precisely without knowing the true start time; use known exercises to calibrate |
| **Mean time to respond / acknowledge (MTTR / MTTA)** | How fast the team acts once alerted | Watch for gaming by closing alerts fast without real investigation |
| **False positive rate per rule** | Which detections need tuning | Pair with false negative awareness; a rule that never fires is not necessarily a good rule |
| **Alerts per analyst per shift** | Workload and burnout risk | A rising number with flat headcount is an early warning, not a success metric |
| **ATT&CK technique coverage** | Breadth of what the SOC can actually detect | Coverage of what, exactly: a heatmap without validated rules behind it overstates readiness |

Pairing ATT&CK-based coverage reporting with a governance framework such as NIST CSF 2.0 gives both a technical and a management view of the same program; see [Frameworks and standards](../10-governance-risk-and-compliance/02-frameworks-and-standards.md).

## Automation, carefully

**SOAR** (security orchestration, automation and response) tools automate repeatable steps of triage and response: enriching an alert with threat intelligence lookups, disabling an account, isolating a host. Automation is valuable once the underlying decision logic is trustworthy, and actively harmful before that: automating a bad decision just makes the bad decision happen faster and at greater scale. Start by automating the enrichment steps that save analyst time without taking irreversible action, and only automate containment actions for well-understood, well-tested cases.

## Shift handoff and continuity

For any SOC running more than a single person, the handoff between shifts is where context is most often lost. A short, written handoff covering open investigations, anything unusual in baseline traffic, and any detection that is currently noisy keeps the next shift from starting cold.

## Practice

1. Deploy Wazuh (or an equivalent free stack) in your lab, enroll at least two hosts, and confirm end to end that an action on one host produces a searchable alert within a reasonable delay.
2. Write a runbook for one alert type in your lab, following the example above, and have a study partner follow it without your help to see where it is unclear.
3. Generate ten alerts in your lab (a mix of benign and the Atomic Red Team tests from earlier modules) and triage all of them, recording your decision and reasoning for each.
4. Track your own MTTD and MTTA across a week of lab exercises and write down what slowed you down.
5. Pick one noisy detection from your earlier work in [Detection engineering](02-detection-engineering.md) and use a week of triage notes to decide how to tune it.

These support [Module 1.5](../../roadmap/phase-1-security-fundamentals/05-network-defense-monitoring.md) and the [defensive track](../../roadmap/phase-3-specialization/track-defensive.md) of the roadmap.

## What to do with this

- [ ] Explain the three analyst tiers and why the dependency between them runs in one direction.
- [ ] Build and run a working SIEM in your lab end to end.
- [ ] Write two runbooks for alert types you expect to see often.
- [ ] Track one week of your own triage decisions and summarize what you would automate first, and why.
- [ ] Explain why automating triage before alert quality is stable makes things worse, not better.

## Key references

Elastic Security documentation · MITRE ATT&CK · NIST CSF 2.0 · Splunk documentation · Wazuh documentation. Full list in [References](../15-references.md).

<!-- navigation -->
[← Detection engineering](02-detection-engineering.md) · [Index](../00-start-here.md) · [Incident response →](04-incident-response.md)
