# Red teaming and adversary emulation

> [!TIP]
> **In short:** a penetration test asks "what vulnerabilities exist?". **Adversary emulation** asks a narrower, more realistic question: "**if the specific threat actors who target organizations like ours came after us, using the techniques they are known to use, would we detect and stop them, and how far would they get first?**" The answer comes from running a scoped set of real-world techniques, mapped to a shared reference (MITRE ATT&CK), against production or production-like defenses, with the result measured in detections and response, not just in exploited vulnerabilities. **Purple teaming** removes the adversarial framing entirely: attackers and defenders work side by side, technique by technique, to make detections better on the spot.

## How this differs from a penetration test

| | Penetration test | Red team exercise | Purple team exercise |
|---|---|---|---|
| **Question** | What can be exploited? | Would a realistic adversary succeed, and would we notice? | How well does each specific detection work? |
| **Scope** | Defined systems | A goal (reach this data, this system) across the environment | Selected techniques |
| **Who knows** | Usually the defending team is informed | Often only a small "white cell" knows; defenders are tested for real | Everyone; it is collaborative by design |
| **Measure of success** | Vulnerabilities found and fixed | Objective reached or stopped; time to detect; time to respond | Detection coverage per technique, improved on the spot |
| **Output** | Vulnerability report | Narrative timeline plus detection and response gaps | Updated detection rules and a coverage record |

None of these replace the others. A mature program runs vulnerability management continuously, penetration tests on a schedule, purple team sessions frequently to tune detections, and red team exercises periodically to test the whole chain end to end.

## Threat-informed scoping

The exercise should emulate a **specific, documented adversary** relevant to the organization, not a generic hacker. The method:

1. **Choose a threat profile.** Pick a real intrusion set relevant to the organization's sector and region, from a source such as a threat intelligence provider, an ISAC, a national CERT, or MITRE ATT&CK's own group profiles. Financial services, government and critical infrastructure in Latin America have documented activity from both financially motivated and state-linked groups; pick what is relevant, not what is famous.
2. **Extract the technique list.** ATT&CK group pages list the tactics and techniques reported for that actor (initial access, execution, persistence, and so on through exfiltration and impact). This becomes the emulation plan.
3. **Define the objective**, not just the technique list: reach a specific data set, demonstrate the ability to disrupt a specific process, or prove a specific detection gap. A red team exercise without an objective tends to collect vulnerabilities instead of testing resilience.
4. **Set the rules of engagement** as in any engagement (see [Penetration testing methodology](01-penetration-testing-methodology.md)), with extra care around a white cell that can authorize a pause, limits on anything resembling real damage, and a clear "get out of jail" authorization letter naming the testers.
5. **Decide who is informed.** A fully blind test measures detection and response honestly but risks real disruption if nobody can vouch for the activity quickly; an informed test is safer to run often.

**MITRE ATT&CK Navigator** is the standard way to visualize a plan: highlight the techniques in scope, and later overlay which ones were detected, to produce a heat map the whole organization can read.

## Emulation at the technique level

Rather than running a single scripted intrusion, many teams validate detections **technique by technique**, which is faster to repeat and easier to attribute a result to a specific control.

| Approach | What it is | Tools |
|---|---|---|
| **Atomic tests** | A small, self-contained action that reproduces one ATT&CK technique (for example, a specific discovery command or a specific persistence mechanism), run and then checked against logs | Atomic Red Team (open source, maintained by Red Canary) |
| **Automated adversary emulation platforms** | Chain several atomic-style actions into a scripted operation across multiple hosts, with built-in reporting | MITRE Caldera |
| **Breach and attack simulation** | Commercial platforms that run a large library of techniques continuously and score detection coverage | Various vendors |
| **Manual operation** | A human operator adapts technique by technique based on what the environment allows, closest to a real intrusion | Skilled operators, typically on a longer engagement |

The output that matters from any of these is a **coverage map**: for each technique attempted, was it prevented, detected, or neither, and what would need to change for "neither" to become "detected"? A small, realistic result that improves ten detections is worth more than a dramatic domain-admin story with no follow-through.

## Purple teaming

Purple teaming removes the information gap on purpose. A typical session:

1. The red participant announces (or the group agrees on) a specific technique to run, with its ATT&CK ID.
2. They run it against the real environment, narrating what they are doing.
3. The blue participant watches their tools in real time: did an alert fire? What did the raw log look like? Was anything visible but not alerted on?
4. Together they write or tune the detection rule, immediately, and re-run the technique to confirm it now fires.
5. The pair moves to the next technique.

This is the fastest way to close detection gaps, because the feedback loop is minutes, not a report delivered weeks later. It also builds the single skill that separates a strong defender from an average one: reading what an attacker's action actually looks like in your own telemetry, not in a vendor's description of it. See [Detection engineering](../07-defensive-security/02-detection-engineering.md) for how the resulting rules get written and tested.

## Command and control, conceptually

Red team tooling includes a **command and control (C2) framework**: infrastructure that lets an operator control implants on compromised hosts. Understanding what a C2 framework provides, and what it looks like on the wire and on the endpoint, is squarely a defensive skill:

| Property | Why defenders care |
|---|---|
| **Beaconing** | Implants check in on an interval, which produces regular, low-volume outbound connections, often disguised to look like ordinary web traffic. Network analytics that look for regularity and for traffic shaped unlike normal browsing are a standard detection approach (see [Traffic analysis and scanning](../03-networking/05-traffic-analysis-and-scanning.md)) |
| **Profiles that mimic legitimate services** | Operators configure traffic to resemble common cloud or CDN traffic to blend in, which is why allowlisting known-good destinations and inspecting TLS metadata both matter |
| **Staged payloads** | An initial small implant fetches a larger one; endpoint detection of unusual child-process and network behavior around newly run programs catches this stage regardless of the specific framework used |
| **Living-off-the-land execution** | Red team operators, like real intruders, prefer built-in administrative tools over custom malware wherever possible, which is why [privilege escalation](04-privilege-escalation.md)'s LOLBAS reference matters to detection, not only to offense |

Open-source frameworks exist for authorized testing and research (Sliver and Mythic are widely used examples); commercial platforms exist as well. This document deliberately does not walk through configuring one: that belongs in a supervised course or certification lab where the exercise is paired with the matching detection lab, not in a static reference.

## Running this safely and usefully

| Practice | Why |
|---|---|
| **A named white cell** who can authorize, pause and de-conflict the exercise | So a real incident response is never wasted chasing an authorized test, and so the test can be stopped instantly if something unexpected happens |
| **An authorization letter and written scope**, as for any engagement | Legal protection; see [Penetration testing methodology](01-penetration-testing-methodology.md) |
| **Explicit limits on impact** (no real data exfiltration, no production disruption, no actual destructive actions) | Objectives can be demonstrated with markers and logs instead of real damage |
| **A record of every action with timestamps** | Lets the exercise be matched against logs afterward, which is where the learning happens |
| **A debrief that includes the defenders**, not only a report to management | The people who will fix detections need the detail, not just the summary |
| **Tracking the same gap across exercises** | A finding that reappears a year later means the fix did not hold; track remediation like any other finding |

## Measuring the program, not just the exercise

| Metric | What it tells you |
|---|---|
| **ATT&CK technique coverage** | What fraction of a relevant technique set has a working detection, tracked over time |
| **Mean time to detect / respond**, per exercise | Whether the defensive side is improving |
| **Findings that recur across exercises** | Whether fixes are holding |
| **Detections that fired but were not actioned** | A people-and-process gap, not a tooling gap |

## Practice

1. Pick one ATT&CK group profile relevant to a sector you are interested in, and list the ten techniques it reports most prominently. For each, write one sentence on how you would detect it with the logging you already learned in earlier modules.
2. In your own lab, run a handful of Atomic Red Team tests (choose ones with clearly reversible, non-destructive actions) and check, for each, whether your lab's logging would have surfaced it. Write the detection rule for any that would not have.
3. Run a short purple-team session with a study partner: one of you runs an agreed, safe technique in the lab while the other watches logs live and writes the detection, then swap roles.
4. Build an ATT&CK Navigator layer for a fictional organization's threat profile and explain, for each highlighted technique, which of your existing lab detections would catch it.

These map to [Module 2.4](../../roadmap/phase-2-guided-practice/04-blue-team-labs.md) and the [offensive](../../roadmap/phase-3-specialization/track-offensive.md) and [defensive](../../roadmap/phase-3-specialization/track-defensive.md) tracks of the roadmap.

## What to do with this

- [ ] Explain, in your own words, the difference between a penetration test, a red team exercise and a purple team session, and when each is the right tool.
- [ ] Build an ATT&CK Navigator layer for one threat profile and keep it in your notes.
- [ ] Run three Atomic Red Team tests in your lab and write the matching detection for each.
- [ ] Describe what a white cell is for and why a red team exercise needs one.
- [ ] Keep a running list, across every lab exercise you do, of findings that recur, and treat a repeat as a fix that did not hold.

## Key references

Atomic Red Team documentation · MITRE ATT&CK · MITRE ATT&CK Navigator · MITRE Caldera documentation · Red Canary resources. Full list in [References](../15-references.md).
