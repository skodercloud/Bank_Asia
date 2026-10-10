# -*- coding: utf-8 -*-
"""
build_compact_rfp.py
Populates RFP_LMS Bank Asia_v0.3.docx cleanly using pure python-docx API.
Ensures concise, to-the-point responses and remarks so page count remains tight and clean.
"""

import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def set_cell(cell, text, bold=False, font_size=8.5, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(0.5)
    p.paragraph_format.space_after = Pt(0.5)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(font_size)
    run.bold = bold

print("Script template ready.")
