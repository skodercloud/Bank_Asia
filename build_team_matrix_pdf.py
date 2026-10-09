import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as PlatypusImage, KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from skoder_pdf_builder import build_pdf_document, get_signature_block, FONT_NORMAL, FONT_BOLD, FONT_ITALIC

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=13,
    leading=17,
    textColor=colors.HexColor('#0d47a1'),
    alignment=TA_CENTER
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName=FONT_NORMAL,
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#475569'),
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=10,
    leading=13.5,
    textColor=colors.HexColor('#0d47a1'),
    spaceBefore=6,
    spaceAfter=3
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName=FONT_NORMAL,
    fontSize=8,
    leading=11.5,
    textColor=colors.HexColor('#1e293b')
)

th_style = ParagraphStyle(
    'TableHeader',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=7.5,
    leading=10,
    textColor=colors.white,
    alignment=TA_CENTER
)

td_style = ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontName=FONT_NORMAL,
    fontSize=7,
    leading=9.5,
    textColor=colors.HexColor('#1e293b')
)

td_bold = ParagraphStyle(
    'TableCellBold',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=7,
    leading=9.5,
    textColor=colors.HexColor('#0f172a')
)

def generate_team_doc():
    story = []
    story.append(Paragraph("PROPOSED PROJECT TEAM STRUCTURE & RESOURCE ALLOCATION MATRIX", title_style))
    story.append(Paragraph("Procurement, Supply, Implementation, Integration, and Support of Litigation Management System (LMS)<br/>Tender Ref: RFP_LMS Bank Asia_v0.3 | Client: Bank Asia PLC", subtitle_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Technical Team Structure & Project Governance Flow", heading_style))
    flow_text = """Skoder Technologies proposes a highly qualified, cross-functional engineering and domain delivery team dedicated to ensuring seamless execution within the required 16-week timeline, 3-year warranty, and subsequent AMC tenure:<br/>
<b>Project Governance & Executive Oversight:</b> K. M. Abir Mahmud (Project Director / Engagement Lead)<br/>
<b>Technical Architecture & Cloud Systems Leadership:</b> Ali Haider Fahad (Lead Architect & CTO) | Fahad Morshed (Chief Intelligence & Infrastructure Lead)<br/>
<b>Core Module Development & Technical Management:</b> Fahim Shahriar (Technical PM & Full-Stack Engineer) | Alamin (Frontend & Web Developer) | Alfee Bin Ferdous (UI/UX Designer)<br/>
<b>Quality Assurance, Enablement & Data Migration:</b> Ahmed Shafkat (QA Lead) | Bodrunnaher Toma (Training & Documentation Lead) | Md. Rafidul Islam (Operations & Migration Lead)"""
    story.append(Paragraph(flow_text, body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("2. Key Personnel Allocation Matrix & Role Responsibilities", heading_style))

    table_data = [
        [
            Paragraph("Team Member", th_style),
            Paragraph("Proposed Role", th_style),
            Paragraph("Qualifications & Background", th_style),
            Paragraph("Key Responsibilities on Bank Asia LMS", th_style),
            Paragraph("Involvement", th_style)
        ],
        [
            Paragraph("K. M. Abir Mahmud", td_bold),
            Paragraph("Project Director / Engagement Lead", td_style),
            Paragraph("Founder & CEO, Skoder; 10+ yrs enterprise software & financial systems leadership", td_style),
            Paragraph("Executive client liaison, contract governance, sprint sign-offs, and quality assurance.", td_style),
            Paragraph("Advisory / Executive", td_style)
        ],
        [
            Paragraph("Ali Haider Fahad", td_bold),
            Paragraph("Lead Solutions Architect & Backend Lead", td_style),
            Paragraph("CTO, Skoder; 8+ yrs in Laravel, PHP, RESTful microservices, MySQL/PostgreSQL", td_style),
            Paragraph("Core system architecture, CBS API Gateway integration, database design, and security protocols.", td_style),
            Paragraph("Full-time", td_style)
        ],
        [
            Paragraph("Fahad Morshed", td_bold),
            Paragraph("Chief Intelligence Officer & Infrastructure Lead", td_style),
            Paragraph("CIO, Skoder; 6+ yrs in cloud infrastructure, database security, AI/ML, and encryption", td_style),
            Paragraph("High-availability server deployment, database tuning, AES-256 data protection, and disaster recovery.", td_style),
            Paragraph("Full-time", td_style)
        ],
        [
            Paragraph("Fahim Shahriar", td_bold),
            Paragraph("Technical Project Manager & Senior Full-Stack Dev", td_style),
            Paragraph("Senior Software Engineer; 5+ yrs in enterprise systems and workflow automation", td_style),
            Paragraph("Core module engineering (Artha Rin, NI Act 138, Auction, WOA tracking), sprint execution, and UAT coordination.", td_style),
            Paragraph("Full-time", td_style)
        ],
        [
            Paragraph("Ahmed Shafkat", td_bold),
            Paragraph("QA & Systems Testing Lead", td_style),
            Paragraph("M.S. in Computer Science (Jahangirnagar University - CGPA 3.93/4.00); 4+ yrs QA experience", td_style),
            Paragraph("Comprehensive automated unit/integration testing, security vulnerability scanning, and load testing.", td_style),
            Paragraph("Full-time", td_style)
        ],
        [
            Paragraph("Bodrunnaher Toma", td_bold),
            Paragraph("Training & Enablement Lead", td_style),
            Paragraph("14+ yrs senior professional experience in training, communication & documentation", td_style),
            Paragraph("Authoring bilingual user manuals, SOPs, and conducting Legal & Branch user workshops.", td_style),
            Paragraph("Full-time (Rollout)", td_style)
        ],
        [
            Paragraph("Md. Rafidul Islam", td_bold),
            Paragraph("Operations & Migration Coordinator", td_style),
            Paragraph("4+ yrs in database operations, field deployment, and customer success", td_style),
            Paragraph("Legacy case data migration, CBS account reconciliation, and live system handoff.", td_style),
            Paragraph("Full-time", td_style)
        ],
        [
            Paragraph("Alfee Bin Ferdous / Alamin", td_bold),
            Paragraph("UI/UX & Frontend Engineers", td_style),
            Paragraph("4+ yrs in responsive web design, Vue/React, and user-centric interfaces", td_style),
            Paragraph("Modern, responsive litigation dashboard, hearing calendar UI, and legal notice generation UI.", td_style),
            Paragraph("Full-time", td_style)
        ],
    ]

    team_table = Table(table_data, colWidths=[75, 85, 125, 155, 50])
    team_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 2.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
    ]))
    story.append(team_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("3. Declaration of Resource Availability & Technical Commitment", heading_style))
    decl_text = "Skoder Technologies formally certifies that all key technical personnel listed above are currently in active service with our firm and are 100% committed and available to execute the assignment across the 16-week development lifecycle, 3-year warranty, and subsequent AMC support tenure as per Bank Asia PLC requirements."
    story.append(Paragraph(decl_text, body_style))
    story.append(Spacer(1, 8))

    story.append(get_signature_block())

    build_pdf_document("02_Project_Team_Structure_and_Matrix_Bank_Asia.pdf", story)

if __name__ == '__main__':
    generate_team_doc()
