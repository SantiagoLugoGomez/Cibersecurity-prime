# Tools

Two small, free, offline tools that support the rest of this repository. Neither depends on an internet connection or an account.

## toolkit.html

A single HTML file with no external dependencies: open it directly in any browser (double-click it, or `file://` the path) and every calculator runs locally in JavaScript. Nothing it does ever leaves your machine.

| Tool | What it does |
|---|---|
| Subnet / CIDR calculator | Network address, broadcast, usable range and host count for an IPv4 address and prefix |
| Unix permissions calculator | Converts octal mode to symbolic `rwx` form and back, including setuid/setgid/sticky bits |
| Password entropy and crack-time estimate | Bits of entropy and a rough time-to-crack at a chosen guess rate, per the math in [docs/04-cryptography-and-identity/04-passwords-and-mfa.md](../docs/04-cryptography-and-identity/04-passwords-and-mfa.md) |
| Encode / decode | Base64, URL and hex, plus the classic XOR single-byte/repeating-key cipher used throughout CTF crypto challenges |
| JWT decoder | Decodes a token's header and payload; never verifies a signature and never trusts the result (see [Authorization, sessions and federation](../docs/04-cryptography-and-identity/05-authorization-sessions-and-federation.md)) |
| Epoch / timestamp converter | Unix epoch to and from a human date, for reading raw logs |
| Hash identifier | Guesses an algorithm family from a hash's length and format (heuristic, not proof) |
| Port reference | Searchable table of the ports in [docs/cheatsheet.md](../docs/cheatsheet.md) |
| ATT&CK tactics reference | Searchable table of the 15 MITRE ATT&CK enterprise tactics |

Nothing here generates exploit payloads, shells or malicious code; every tool is for learning, analysis or quick lookup, consistent with [Legal limits and ethics](../docs/01-foundations/05-legal-and-ethics.md).

## tracker.xlsx

A spreadsheet version of [roadmap/progress.md](../roadmap/progress.md), for anyone who prefers a spreadsheet to a markdown checklist. Sheets:

| Sheet | Purpose |
|---|---|
| Weekly log | Tick R/P/D/E per week; a formula counts how many weeks you completed in full |
| Lab tracker | One row per machine, CTF challenge or lab exercise |
| Certifications | Planned and completed certifications (see [Certification strategy](../docs/11-learning-and-career/05-certification-strategy.md)) |
| Portfolio projects | The projects from [Phase 4 of the roadmap](../roadmap/phase-4-professional/README.md#portfolio-projects) |
| CTF and events | Competitions and meetups attended |
| Writeup log | Every writeup published, so portfolio growth is visible at a glance |

### Regenerating it

The file is generated from a script, not hand-built, so it stays in sync with the roadmap's week list:

```bash
pip install openpyxl
python3 tools/generate_tracker.py
```

The script writes formulas but does not evaluate them, so some spreadsheet viewers show a stale or blank result until they recalculate. After running the script, open the file once in LibreOffice Calc or Excel and save it, which caches the current formula results for every viewer:

```bash
soffice --headless --calc --convert-to xlsx:"Calc MS Excel 2007 XML" --outdir /tmp/tracker-out tools/tracker.xlsx
cp /tmp/tracker-out/tracker.xlsx tools/tracker.xlsx
```

Do this whenever you change `generate_tracker.py`, before committing.
