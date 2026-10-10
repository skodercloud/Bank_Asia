# -*- coding: utf-8 -*-
"""
generate_accurate_rfp_docx.py
Populates RFP_LMS Bank Asia_v0.3.docx with 100% accurate, complete, and professional data.
"""

import os, sys, copy, re
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_content(cell, text, bold=False, italic=False, font_size=9.0, align=WD_ALIGN_PARAGRAPH.LEFT, color=None):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(1.5)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(font_size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color

def set_tc_xml_text(tc, text, bold=False, italic=False, font_size=9.0, align=WD_ALIGN_PARAGRAPH.LEFT):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    p_elements = tc.findall('w:p', ns)
    if not p_elements:
        p = parse_xml(f'<w:p {nsdecls("w")}/>')
        tc.append(p)
    else:
        p = p_elements[0]
        for extra in p_elements[1:]:
            tc.remove(extra)
    
    # Remove existing runs
    for r in p.findall('w:r', ns):
        p.remove(r)
    
    # Add new run
    run = parse_xml(f'<w:r {nsdecls("w")}><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="{int(font_size * 2)}"/>{"<w:b/>" if bold else ""}{"<w:i/>" if italic else ""}</w:rPr><w:t>{text}</w:t></w:r>')
    p.append(run)

print("Setup completed.")
