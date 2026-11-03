# Detection: <short name> (<ATT&CK technique ID>)

See [Detection engineering](../docs/07-defensive-security/02-detection-engineering.md#writing-a-detection-from-an-attck-technique) for the method.

**Technique:** <name and link to the ATT&CK page>

**Hypothesis:** what would this technique look like in our own environment, specifically.

**Logic:** the exact query or correlation rule.

```
<query>
```

**Data required:** <log source, fields, whether it is enabled today>

**Expected false positives:** <known legitimate sources that would also trigger this, and how they are excluded>

**Response:** what an analyst does when this fires.

**Tested against:**

| Date | Test performed | Result |
|---|---|---|
| | Atomic Red Team test / manual reproduction | Fired as expected / did not fire / fired with noise |

**Owner:** <name>  ·  **Last reviewed:** <date>  ·  **Retired:** <date, reason, or leave blank>
