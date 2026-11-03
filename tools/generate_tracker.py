#!/usr/bin/env python3
"""Generate tools/tracker.xlsx from the roadmap structure.

Usage: python3 tools/generate_tracker.py
Requires: openpyxl (pip install openpyxl)
After running, open the file once in LibreOffice or Excel and save it,
so cached formula results are stored for viewers that do not recalculate.
"""
import datetime

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

HEADER_FILL = PatternFill("solid", fgColor="1F2937")
HEADER_FONT = Font(color="FFFFFF", bold=True)
TITLE_FONT = Font(bold=True, size=14)
SUBTEXT_FONT = Font(italic=True, color="555555")
WRAP = Alignment(wrap_text=True, vertical="top")

PHASE_WEEKS = [
    ("0. Foundations", "W1", "0.1 Study setup and Git"),
    ("0. Foundations", "W2", "0.2 Linux: navigation, files, shell"),
    ("0. Foundations", "W3", "0.2 Linux: redirection, permissions, users"),
    ("0. Foundations", "W4", "0.2 Linux: processes, services, SSH, text processing"),
    ("0. Foundations", "W5", "0.3 Bash scripting"),
    ("0. Foundations", "W6", "0.4 Networking: models, addressing, link layer"),
    ("0. Foundations", "W7", "0.4 Networking: IP, TCP, UDP, routing"),
    ("0. Foundations", "W8", "0.4 Networking: DNS, HTTP, TLS"),
    ("0. Foundations", "W9", "0.4 Networking: security basics and tooling"),
    ("0. Foundations", "W10", "0.5 Python: files, regex, CLI"),
    ("0. Foundations", "W11", "0.5 Python: networking and the web"),
    ("0. Foundations", "W12", "0.5 Python: crypto, subprocess, packaging"),
    ("0. Foundations", "W13", "0.6 Operating systems: processes and syscalls"),
    ("0. Foundations", "W14", "0.6 OS: memory and concurrency"),
    ("0. Foundations", "W15", "0.6 OS: filesystems and OS security"),
    ("0. Foundations", "W16", "0.7 Windows: internals and PowerShell"),
    ("0. Foundations", "W17", "0.7 Windows: logging and Sysmon"),
    ("0. Foundations", "W18", "0.7 Finish and validate the home lab"),
    ("1. Security fundamentals", "W1-2", "1.1 Principles and threat modeling"),
    ("1. Security fundamentals", "W3-5", "1.2 Applied cryptography"),
    ("1. Security fundamentals", "W6-7", "1.3 Identity and access"),
    ("1. Security fundamentals", "W8-11", "1.4 Web security and OWASP Top 10"),
    ("1. Security fundamentals", "W12-13", "1.5 Network security and monitoring"),
    ("1. Security fundamentals", "W14-16", "1.6 Frameworks and governance"),
    ("2. Guided practice", "W1-4", "2.1 CTF foundations"),
    ("2. Guided practice", "W5-10", "2.2 Wargames and web labs"),
    ("2. Guided practice", "W11-16", "2.3 Machines and Active Directory"),
    ("2. Guided practice", "W17-20", "2.4 Blue team labs"),
    ("3. Specialization", "Sampler", "Offensive sampler + artifact"),
    ("3. Specialization", "Sampler", "Defensive sampler + artifact"),
    ("3. Specialization", "Sampler", "Web security sampler + artifact"),
    ("3. Specialization", "Sampler", "Malware analysis sampler + artifact"),
    ("3. Specialization", "Sampler", "Cloud security sampler + artifact"),
    ("3. Specialization", "Sampler", "GRC sampler + artifact"),
    ("3. Specialization", "Deep dive W1-3", "Chosen track, weeks 1-3"),
    ("3. Specialization", "Deep dive W4-6", "Chosen track, weeks 4-6"),
    ("3. Specialization", "Deep dive W7-9", "Chosen track, weeks 7-9"),
    ("3. Specialization", "Deep dive W10-12", "Chosen track, weeks 10-12, capstone published"),
    ("4. Professional", "Ongoing", "Foundation certification (optional)"),
    ("4. Professional", "Ongoing", "First practical certification"),
    ("4. Professional", "Ongoing", "Track certification"),
    ("4. Professional", "Ongoing", "Portfolio project 1"),
    ("4. Professional", "Ongoing", "Portfolio project 2"),
    ("4. Professional", "Ongoing", "Portfolio project 3"),
    ("4. Professional", "Ongoing", "First bug bounty/disclosure report or top-third CTF"),
    ("4. Professional", "Ongoing", "Community contribution"),
]

LAB_COLUMNS = ["Date", "Platform", "Target / machine", "Type", "Difficulty",
               "Time spent (h)", "ATT&CK techniques", "Writeup link", "Status"]
LAB_STATUS = ["Not started", "In progress", "Stuck, needs a hint", "Solved", "Writeup published"]

CERT_COLUMNS = ["Certification", "Track", "Target date", "Cost (local currency)",
                "Study status", "Exam date", "Result", "Expiry date"]
CERT_STATUS = ["Not started", "Studying", "Scheduled", "Passed", "Failed, retaking", "Expired"]

PROJECT_COLUMNS = ["Project", "Track", "Start date", "Status", "Repository link", "What it demonstrates"]
PROJECT_STATUS = ["Idea", "In progress", "Published", "Needs an update"]

EVENT_COLUMNS = ["Date", "Event / CTF", "Team", "Result", "Notes"]
WRITEUP_COLUMNS = ["Date", "Target", "Platform", "Published?", "Link"]


def style_header(ws, row, columns):
    for col_index, title in enumerate(columns, start=1):
        cell = ws.cell(row=row, column=col_index, value=title)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = WRAP
    ws.freeze_panes = ws.cell(row=row + 1, column=1).coordinate


def set_widths(ws, widths):
    for col_index, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(col_index)].width = width


def add_dropdown(ws, column_letter, first_row, last_row, options):
    formula = '"' + ",".join(options) + '"'
    dv = DataValidation(type="list", formula1=formula, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{column_letter}{first_row}:{column_letter}{last_row}")


def build_weekly_log(wb):
    ws = wb.active
    ws.title = "Weekly log"
    ws["A1"] = "Weekly log"
    ws["A1"].font = TITLE_FONT
    ws["A2"] = "Tick R, P, D and E as you complete each session. See docs/11-learning-and-career/02-the-study-system.md."
    ws["A2"].font = SUBTEXT_FONT

    header_row = 4
    columns = ["Phase", "Week", "Module", "R", "P", "D", "E",
               "Check-yourself (x/5)", "Deliverable committed", "Notes"]
    style_header(ws, header_row, columns)
    set_widths(ws, [22, 10, 42, 6, 6, 6, 6, 14, 24, 40])

    start = header_row + 1
    for offset, (phase, week, module) in enumerate(PHASE_WEEKS):
        row = start + offset
        ws.cell(row=row, column=1, value=phase)
        ws.cell(row=row, column=2, value=week)
        ws.cell(row=row, column=3, value=module)
        for col in (4, 5, 6, 7):
            ws.cell(row=row, column=col, value=False)
        ws.cell(row=row, column=9, value=False)

    last = start + len(PHASE_WEEKS) - 1
    for col_letter in ("D", "E", "F", "G", "I"):
        add_dropdown(ws, col_letter, start, last, ["TRUE", "FALSE"])

    summary_row = last + 2
    ws.cell(row=summary_row, column=1, value="Weeks with all four sessions done:")
    ws.cell(row=summary_row, column=1).font = Font(bold=True)
    ws.cell(
        row=summary_row, column=3,
        value=f"=COUNTIFS(D{start}:D{last},TRUE,E{start}:E{last},TRUE,"
              f"F{start}:F{last},TRUE,G{start}:G{last},TRUE)&\" / {len(PHASE_WEEKS)}\"",
    )


def build_table_sheet(wb, name, title, note, columns, status_column_letter, status_options, rows=60):
    ws = wb.create_sheet(name)
    ws["A1"] = title
    ws["A1"].font = TITLE_FONT
    ws["A2"] = note
    ws["A2"].font = SUBTEXT_FONT

    header_row = 4
    style_header(ws, header_row, columns)
    set_widths(ws, [20] * len(columns))

    start = header_row + 1
    last = start + rows - 1
    if status_column_letter and status_options:
        add_dropdown(ws, status_column_letter, start, last, status_options)
    return ws


def main():
    wb = Workbook()
    build_weekly_log(wb)
    build_table_sheet(
        wb, "Lab tracker", "Lab and machine tracker",
        "One row per machine, CTF challenge or lab exercise. See writeups/TEMPLATE.md.",
        LAB_COLUMNS, "I", LAB_STATUS,
    )
    build_table_sheet(
        wb, "Certifications", "Certification tracker",
        "See docs/11-learning-and-career/05-certification-strategy.md and roadmap/phase-4-professional/README.md for the current price table.",
        CERT_COLUMNS, "E", CERT_STATUS, rows=20,
    )
    build_table_sheet(
        wb, "Portfolio projects", "Portfolio project tracker",
        "See docs/11-learning-and-career/06-portfolio-and-writing.md and roadmap/phase-4-professional/README.md#portfolio-projects.",
        PROJECT_COLUMNS, "D", PROJECT_STATUS, rows=20,
    )
    build_table_sheet(
        wb, "CTF and events", "CTF and event log",
        "See docs/11-learning-and-career/07-community.md.",
        EVENT_COLUMNS, None, None, rows=40,
    )
    build_table_sheet(
        wb, "Writeup log", "Writeup log",
        "Every writeup you publish, so your portfolio growth is visible at a glance.",
        WRITEUP_COLUMNS, "D", ["Yes", "No, private notes only"], rows=60,
    )

    info = wb.create_sheet("Read me", 0)
    info["A1"] = "Study and lab tracker"
    info["A1"].font = TITLE_FONT
    info["A3"] = "Generated by tools/generate_tracker.py."
    info["A4"] = f"Last generated: {datetime.date.today().isoformat()}"
    info["A6"] = "Sheets:"
    for i, text in enumerate([
        "Weekly log: tick R/P/D/E per week of the roadmap.",
        "Lab tracker: every machine, CTF challenge or lab exercise.",
        "Certifications: planned and completed certifications.",
        "Portfolio projects: the projects from Phase 4 of the roadmap.",
        "CTF and events: competitions and meetups attended.",
        "Writeup log: every writeup published, for visible portfolio growth.",
    ], start=7):
        info.cell(row=i, column=1, value="- " + text)
    set_widths(info, [90])

    wb.save("tools/tracker.xlsx")
    print("Wrote tools/tracker.xlsx")


if __name__ == "__main__":
    main()
