import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as PlatypusImage, KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from skoder_pdf_builder import (
    build_pdf_document, get_signature_block, FONT_NORMAL, FONT_BOLD, FONT_ITALIC,
    SIGNATURE_PATH, SEAL_PATH
)

styles = getSampleStyleSheet()

# Reusable Typography
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
    fontSize=9.5,
    leading=13,
    textColor=colors.HexColor('#0d47a1'),
    spaceBefore=5,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName=FONT_NORMAL,
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#1e293b')
)

body_bold = ParagraphStyle(
    'BodyBoldCustom',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#1e293b')
)

bullet_style = ParagraphStyle(
    'BulletCustom',
    parent=styles['Normal'],
    fontName=FONT_NORMAL,
    fontSize=8.5,
    leading=12,
    leftIndent=12,
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
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor('#1e293b')
)

td_bold = ParagraphStyle(
    'TableCellBold',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor('#0f172a')
)

td_right = ParagraphStyle(
    'TableCellRight',
    parent=styles['Normal'],
    fontName=FONT_NORMAL,
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor('#1e293b'),
    alignment=TA_RIGHT
)

td_right_bold = ParagraphStyle(
    'TableCellRightBold',
    parent=styles['Normal'],
    fontName=FONT_BOLD,
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor('#0f172a'),
    alignment=TA_RIGHT
)

def get_witness_sig_block():
    sig_img = PlatypusImage(SIGNATURE_PATH, width=80, height=40) if os.path.exists(SIGNATURE_PATH) else Paragraph("[Signature]", None)
    seal_img = PlatypusImage(SEAL_PATH, width=54, height=54) if os.path.exists(SEAL_PATH) else Paragraph("[Seal]", None)
    label_p = Paragraph(f"<font fontName='{FONT_BOLD}' size=9.5 color='#000000'>K. M. ABIR MAHMUD</font><br/><font fontName='{FONT_NORMAL}' size=8.5 color='#333333'>Chief Executive Officer<br/><font fontName='{FONT_BOLD}' size=9 color='#00b050'>SKODER TECHNOLOGIES</font></font>", None)
    w_text = Paragraph(f"<font fontName='{FONT_NORMAL}' size=7.5 color='#333333'><b>Witness 1:</b> Fahad Morshed, CIO, Skoder Technologies<br/><b>Witness 2:</b> Imran Bipu, Head of Business, Skoder Technologies</font>", None)
    
    table_data = [
        [sig_img, seal_img, w_text],
        [label_p, "", ""]
    ]
    sig_table = Table(table_data, colWidths=[120, 70, 297])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('SPAN', (0,1), (1,1)),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    return sig_table

# ---------------------------------------------------------------------------
# 1. BANK ASIA COVER LETTER
# ---------------------------------------------------------------------------
def build_cover_letter():
    story = []
    story.append(Paragraph("<b>Date:</b> October 11, 2026", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("To<br/><b>The Head of ICT Division</b><br/>Bank Asia PLC<br/>Corporate Office, Bank Asia Tower (1st Floor)<br/>32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka-1215, Bangladesh", body_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Subject: Bid Submission for Procurement, Supply, Implementation, Integration, and Support of Litigation Management System (LMS)</b>", ParagraphStyle('Subj', parent=body_bold, fontSize=9, textColor=colors.HexColor('#0d47a1'))))
    story.append(Paragraph("<b>Ref:</b> RFP/BID Schedule for Litigation Management System (LMS) – Version 1.0 (RFP_LMS Bank Asia_v0.3)", body_style))
    story.append(Spacer(1, 6))

    p1 = "Dear Sir/Madam,<br/><br/>Having examined the Request for Proposal (RFP) document for the <b>Litigation Management System (LMS)</b>, we, <b>Skoder Technologies</b>, hereby submit our proposal to supply, implement, integrate, and support the proposed solution in full compliance with your requirements."
    story.append(Paragraph(p1, body_style))
    story.append(Spacer(1, 5))

    p2 = "Our enterprise LMS is a 100% proprietary software platform developed by Skoder Technologies, purpose-engineered to provide 360-degree coverage for case tracking (Artha Rin Adalat, NI Act 138, Civil & Criminal suits), automated legal notice generation, auction management, Write-Off Account (WOA) tracking, panel lawyer/advocate management, automated hearing calendar alerts, seamless Core Banking System (CBS) integration, and regulatory reporting for Bangladesh Bank."
    story.append(Paragraph(p2, body_style))
    story.append(Spacer(1, 5))

    story.append(Paragraph("We confirm the following solemn commitments:", body_bold))
    story.append(Spacer(1, 3))

    b1 = "• <b>Bid Security:</b> Enclosed is <b>Pay Order No. SJIBL/MIR/PO/2026/04812</b> dated <b>October 11, 2026</b> for <b>BDT 25,000/-</b> (Taka Twenty-Five Thousand Only) issued by <b>Shahjalal Islami Bank PLC, Mirpur Branch, Dhaka</b> in favor of <b>Bank Asia PLC</b> (valid for 12 months)."
    b2 = "• <b>Offer Validity:</b> Our commercial quotation and terms remain valid for <b>12 (twelve) months</b> from the bid opening date (up to October 11, 2027)."
    b3 = "• <b>Compliance & Timeline:</b> We accept all terms, conditions, functional requirements, and technical specifications outlined in the RFP document and commit to delivering the complete project within <b>16 weeks (112 days)</b> upon contract award."
    b4 = "• <b>Warranty & AMC:</b> We provide <b>03 (three) years full warranty</b> followed by <b>03 (three) years Annual Maintenance Contract (AMC)</b> at guaranteed equal yearly rates with 24/7/365 support."
    story.append(Paragraph(b1, bullet_style))
    story.append(Paragraph(b2, bullet_style))
    story.append(Paragraph(b3, bullet_style))
    story.append(Paragraph(b4, bullet_style))
    story.append(Spacer(1, 5))

    p3 = "All required technical responses, financial schedules, eligibility documents, implementation methodology, draft SLA & NDA, and client references are attached in the prescribed formats."
    story.append(Paragraph(p3, body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Sincerely,", body_style))
    story.append(Spacer(1, 2))
    story.append(get_signature_block())

    build_pdf_document("BANK_ASIA_Cover_Letter.pdf", story)

# ---------------------------------------------------------------------------
# 2. FINANCIAL PROPOSAL DOCUMENT
# ---------------------------------------------------------------------------
def build_financial_proposal():
    story = []
    story.append(Paragraph("FINANCIAL PROPOSAL", title_style))
    story.append(Paragraph("Procurement, Supply, Implementation, Integration, and Support of Litigation Management System (LMS)<br/>Tender Ref: RFP_LMS Bank Asia_v0.3 | Client: Bank Asia PLC", subtitle_style))
    story.append(Spacer(1, 6))

    intro_txt = "<b>To: The Head of ICT Division, Bank Asia PLC</b> — We, <b>Skoder Technologies</b>, hereby submit our sealed Financial Proposal for the supply, implementation, integration, and comprehensive support of the <b>Litigation Management System (LMS)</b> for Bank Asia PLC in strict conformity with Section 9 & 10 of the RFP documents."
    story.append(Paragraph(intro_txt, body_style))
    story.append(Spacer(1, 5))

    story.append(Paragraph("1. Core LMS Commercial Schedule (As per RFP Table 20)", heading_style))
    story.append(Spacer(1, 3))

    headers_t20_r1 = [
        Paragraph("<b>Product Name</b>", th_style),
        Paragraph("<b>Proposed Product & BOQ Details</b>", th_style),
        Paragraph("<b>Model/Ver</b>", th_style),
        Paragraph("<b>Qty</b>", th_style),
        Paragraph("<b>Unit Price (BDT)</b>", th_style),
        Paragraph("<b>VAT 5% + AIT 10%</b>", th_style),
        Paragraph("<b>Total Price (BDT)</b>", th_style),
        Paragraph("<b>Yearly AMC after 3rd Year (BDT)</b>", th_style),
        "", "",
        Paragraph("<b>Grand Total (BDT)</b>", th_style)
    ]
    headers_t20_r2 = ["", "", "", "", "", "", "", Paragraph("<b>4th Yr</b>", th_style), Paragraph("<b>5th Yr</b>", th_style), Paragraph("<b>6th Yr</b>", th_style), ""]

    row_data = [
        Paragraph("<b>Litigation Management System (LMS)</b>", td_bold),
        Paragraph("<b>Skoder LMS Enterprise Bank Edition</b><br/>• Pre-Litigation, Artha Rin, NI 138, Civil/Criminal<br/>• Auction, WOA Tracking, Panel Lawyer Mgmt<br/>• CBS Core Banking Integration & BB MIS Reports<br/><i>(Includes 3-Year Full Warranty & 24/7 Support)</i>", td_style),
        Paragraph("v1.0 Bank Edition", td_style),
        Paragraph("01 Bank-wide", td_style),
        Paragraph("1,500,000.00", td_right),
        Paragraph("VAT: 75,000<br/>AIT: 150,000<br/>(15% Total)", td_style),
        Paragraph("<b>1,725,000.00</b>", td_right_bold),
        Paragraph("402,500.00", td_right),
        Paragraph("402,500.00", td_right),
        Paragraph("402,500.00", td_right),
        Paragraph("<b>2,932,500.00</b>", td_right_bold)
    ]

    summary_row = [
        Paragraph("<b>Total Product Price (Initial 3 Yrs incl. VAT/Tax)</b>", td_bold),
        Paragraph("<b>BDT 1,725,000.00</b> <i>(Taka Seventeen Lac Twenty-Five Thousand Only)</i>", td_bold),
        "", "", "", "", "",
        Paragraph("<b>Total 3-Yr AMC (Y4–Y6)</b>", td_bold),
        "", "",
        Paragraph("<b>BDT 1,207,500.00</b>", td_right_bold)
    ]

    grand_row = [
        Paragraph("<b>GRAND TOTAL BID VALUE (Software + 6 Years Full Lifecycle including VAT & TAX)</b>", td_bold),
        "", "", "", "", "", "", "", "", "",
        Paragraph("<b>BDT 2,932,500.00</b>", td_right_bold)
    ]

    t20_table = Table([headers_t20_r1, headers_t20_r2, row_data, summary_row, grand_row], colWidths=[65, 130, 42, 32, 45, 45, 48, 30, 30, 30, 40])
    t20_table.setStyle(TableStyle([
        ('SPAN', (7,0), (9,0)),
        ('SPAN', (0,0), (0,1)),
        ('SPAN', (1,0), (1,1)),
        ('SPAN', (2,0), (2,1)),
        ('SPAN', (3,0), (3,1)),
        ('SPAN', (4,0), (4,1)),
        ('SPAN', (5,0), (5,1)),
        ('SPAN', (6,0), (6,1)),
        ('SPAN', (10,0), (10,1)),
        ('SPAN', (1,3), (6,3)),
        ('SPAN', (7,3), (9,3)),
        ('SPAN', (0,4), (9,4)),
        ('BACKGROUND', (0,0), (-1,1), colors.HexColor('#0d47a1')),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor('#f5f5f5')),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor('#e8f5e9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t20_table)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. Additional Scope & Training Rate Schedule (As per RFP Table 21 & Clause 308)", heading_style))
    story.append(Spacer(1, 2))

    t21_data = [
        [Paragraph("<b>Item Description</b>", th_style), Paragraph("<b>Rate / Commercial Terms (BDT)</b>", th_style)],
        [Paragraph("<b>Functional & Technical Training per Day</b><br/><i>(Comprehensive onsite sessions for Legal Dept & ICT Division, Clause 308)</i>", td_style),
         Paragraph("<b>BDT 5,000.00 per day</b> (Excl. VAT/Tax) | <b>BDT 5,750.00 per day</b> (Incl. VAT 5% & AIT 10%)", td_style)],
        [Paragraph("<b>Additional Custom Module / Future Integration Gateway</b> (Optional future workflows)", td_style),
         Paragraph("BDT 150,000.00 per module (Inclusive of all applicable Taxes)", td_style)],
        [Paragraph("<b>Optional Turnkey Server Infrastructure (Dell PowerEdge R760 2U HA Cluster)</b>", td_style),
         Paragraph("BDT 4,970,000.00 (Optional Schedule detailed in Annexure; Bank may provide internally)", td_style)],
    ]
    t21_table = Table(t21_data, colWidths=[310, 177])
    t21_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t21_table)
    story.append(Spacer(1, 4))

    story.append(Paragraph("3. Bid Security & Formal Price Undertaking", heading_style))
    story.append(Spacer(1, 2))

    po_data = [
        [Paragraph("<b>Pay Order No. & Date:</b>", td_bold), Paragraph("SJIBL/MIR/PO/2026/04812, Dated: 11 October, 2026", td_style)],
        [Paragraph("<b>Amount:</b>", td_bold), Paragraph("BDT 25,000/- (Taka Twenty-Five Thousand Only)", td_style)],
        [Paragraph("<b>Issuing Bank & Branch:</b>", td_bold), Paragraph("Shahjalal Islami Bank PLC, Mirpur Branch, Dhaka", td_style)],
        [Paragraph("<b>Validity of Quotation:</b>", td_bold), Paragraph("12 (Twelve) Months from bid opening date (Valid up to October 11, 2027)", td_style)],
    ]
    po_table = Table(po_data, colWidths=[140, 347])
    po_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdbdbd')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f5f5f5')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(po_table)
    story.append(Spacer(1, 3))

    undertaking_text = "<b>Undertaking:</b> We, <b>Skoder Technologies</b>, hereby undertake to supply, implement, integrate, and support the Litigation Management System at the prices quoted above in full conformity with Bank Asia's RFP specifications. All software prices include VAT (5%) and AIT (10%)."
    story.append(Paragraph(undertaking_text, body_style))
    story.append(Spacer(1, 4))

    story.append(get_witness_sig_block())

    build_pdf_document("Financial_Proposal_Bank_Asia.pdf", story)

# ---------------------------------------------------------------------------
# 3. OEM / SOLUTION DEVELOPER DECLARATION
# ---------------------------------------------------------------------------
def build_oem_declaration():
    story = []
    story.append(Paragraph("<b>Date:</b> October 11, 2026", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("To<br/><b>The Head of ICT Division</b><br/>Bank Asia PLC<br/>Corporate Office, Bank Asia Tower (1st Floor)<br/>32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka-1215, Bangladesh", body_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Subject: OEM / Solution Developer & Intellectual Property Rights Declaration</b>", ParagraphStyle('Subj', parent=body_bold, fontSize=9.5, textColor=colors.HexColor('#0d47a1'))))
    story.append(Paragraph("<b>Ref:</b> RFP for Litigation Management System (LMS) – Clause 211, 225 & 278", body_style))
    story.append(Spacer(1, 6))

    p1 = "Dear Sir/Madam,<br/><br/>We, <b>Skoder Technologies</b>, an established software engineering and innovation firm registered in Bangladesh, having our principal corporate office at E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207, do hereby formally certify and declare that:"
    story.append(Paragraph(p1, body_style))
    story.append(Spacer(1, 5))

    c1 = "1. <b>100% Proprietary Solution:</b> Skoder Technologies is the Original Software Manufacturer (OSM) / Solution Developer and sole intellectual property owner of the proposed <b>Litigation Management System (LMS)</b>. The system has been 100% architected, developed, and maintained by our in-house engineering team."
    c2 = "2. <b>No Third-Party OEM Dependency:</b> The core LMS application does not rely on third-party proprietary LMS platforms or foreign distributor licenses. Skoder Technologies holds complete, unencumbered rights to supply, install, configure, customize, integrate, and support the application."
    c3 = "3. <b>6-Year Support & Product Availability Commitment:</b> In compliance with RFP Section 6, Clause 278, Skoder Technologies guarantees that the proposed solution, product roadmap, version enhancements, security patches, CBS integration interfaces, and full technical maintenance will be actively supported and available for a minimum of <b>06 (six) years</b> from the date of deployment."
    c4 = "4. <b>24/7 Dedicated Technical Support:</b> Skoder Technologies maintains an active engineering and system support cell in Dhaka with 24/7/365 coverage for all warranty and AMC requirements."
    c5 = "5. <b>Regulatory Compliance Guarantee:</b> Skoder Technologies commits to providing all regulatory reporting adaptations and compliance updates mandated by <b>Bangladesh Bank</b> without service disruption."

    story.append(Paragraph(c1, bullet_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph(c2, bullet_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph(c3, bullet_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph(c4, bullet_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph(c5, bullet_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("We confirm our absolute commitment to executing this project successfully in partnership with Bank Asia PLC.", body_style))
    story.append(Spacer(1, 8))
    story.append(get_signature_block())

    build_pdf_document("OEM_Developer_Declaration_Skoder.pdf", story)

# ---------------------------------------------------------------------------
# 4. POWER OF ATTORNEY / AUTHORIZATION LETTER
# ---------------------------------------------------------------------------
def build_power_of_attorney():
    story = []
    story.append(Paragraph("POWER OF ATTORNEY / AUTHORIZATION LETTER", title_style))
    story.append(Paragraph("In compliance with RFP Section 6, Clause 260 | Bank Asia PLC Tender", subtitle_style))
    story.append(Spacer(1, 8))

    p1 = "<b>TO WHOM IT MAY CONCERN</b><br/><br/>We, the management of <b>Skoder Technologies</b>, having our registered office at E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207, Bangladesh, do hereby nominate, constitute, and appoint:"
    story.append(Paragraph(p1, body_style))
    story.append(Spacer(1, 5))

    appointee_box = [
        [Paragraph("<b>Name:</b>", td_bold), Paragraph("<b>K. M. ABIR MAHMUD</b>", td_bold)],
        [Paragraph("<b>Designation:</b>", td_bold), Paragraph("Chief Executive Officer (CEO)", td_style)],
        [Paragraph("<b>NID No.:</b>", td_bold), Paragraph("8205149738", td_style)],
        [Paragraph("<b>Organization:</b>", td_bold), Paragraph("Skoder Technologies", td_style)],
        [Paragraph("<b>Contact No.:</b>", td_bold), Paragraph("+88 01750 726094 | abir.skoder@gmail.com", td_style)],
    ]
    app_tbl = Table(appointee_box, colWidths=[120, 367])
    app_tbl.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdbdbd')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f5f5f5')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(app_tbl)
    story.append(Spacer(1, 6))

    p2 = "as our true and lawful attorney and authorized representative to act on behalf of Skoder Technologies in connection with the tender for <b>\"Procurement, supply, implementation, Integration and support of a Litigation Management System (LMS)\"</b> for <b>Bank Asia PLC</b>.<br/><br/>The said attorney is fully authorized to:"
    story.append(Paragraph(p2, body_style))
    story.append(Spacer(1, 4))

    a1 = "1. Sign, seal, and submit the Technical and Financial Bids, schedules, undertaking letters, and tender responses."
    a2 = "2. Attend pre-bid meetings, commercial negotiations, and technical clarification sessions."
    a3 = "3. Furnish Bid Security (Earnest Money) and Performance Security on behalf of the company."
    a4 = "4. Sign and execute the formal Contract Agreement, Service Level Agreement (SLA), and Non-Disclosure Agreement (NDA) upon award of work."
    story.append(Paragraph(a1, bullet_style))
    story.append(Paragraph(a2, bullet_style))
    story.append(Paragraph(a3, bullet_style))
    story.append(Paragraph(a4, bullet_style))
    story.append(Spacer(1, 6))

    p3 = "All acts, deeds, and instruments done or executed by the said attorney shall be deemed as good, valid, and binding upon Skoder Technologies in all respects."
    story.append(Paragraph(p3, body_style))
    story.append(Spacer(1, 8))

    story.append(get_witness_sig_block())

    build_pdf_document("Power_of_Attorney_Authorization_Letter.pdf", story)

# ---------------------------------------------------------------------------
# 5. DRAFT SERVICE LEVEL AGREEMENT (SLA)
# ---------------------------------------------------------------------------
def build_draft_sla():
    story = []
    story.append(Paragraph("DRAFT SERVICE LEVEL AGREEMENT (SLA)", title_style))
    story.append(Paragraph("Litigation Management System (LMS) | Bank Asia PLC & Skoder Technologies", subtitle_style))
    story.append(Spacer(1, 6))

    p_sla = "This Service Level Agreement (SLA) defines the service availability, response times, defect resolution windows, and support standards provided by <b>Skoder Technologies</b> (the \"Service Provider\") to <b>Bank Asia PLC</b> (the \"Bank\") for the Litigation Management System (LMS) during the 3-Year Warranty Period and subsequent Annual Maintenance Contract (AMC) tenure."
    story.append(Paragraph(p_sla, body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. Incident Priority & Response Matrix (24/7/365 Coverage)", heading_style))
    sla_table_data = [
        [Paragraph("<b>Severity Level</b>", th_style), Paragraph("<b>Definition / Impact</b>", th_style), Paragraph("<b>Response Time</b>", th_style), Paragraph("<b>Resolution Time</b>", th_style)],
        [Paragraph("<b>Priority 1 (Critical)</b>", td_bold), Paragraph("System down; core legal workflows halted; CBS integration failure impacting all users.", td_style), Paragraph("Within 30 Minutes", td_style), Paragraph("Within 4 Hours", td_style)],
        [Paragraph("<b>Priority 2 (High)</b>", td_bold), Paragraph("Major feature impaired (e.g. Artha Rin filing, legal notice generation) with no workaround.", td_style), Paragraph("Within 1 Hour", td_style), Paragraph("Within 8 Hours", td_style)],
        [Paragraph("<b>Priority 3 (Medium)</b>", td_bold), Paragraph("Minor functionality issue, report generation discrepancy; workaround available.", td_style), Paragraph("Within 2 Hours", td_style), Paragraph("Within 24 Hours", td_style)],
        [Paragraph("<b>Priority 4 (Low)</b>", td_bold), Paragraph("General inquiries, cosmetic UI issues, user rights changes, routine assistance.", td_style), Paragraph("Within 4 Hours", td_style), Paragraph("Within 48 Hours", td_style)],
    ]
    sla_tbl = Table(sla_table_data, colWidths=[85, 222, 90, 90])
    sla_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(sla_tbl)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. Support Availability & Maintenance Commitments", heading_style))
    p_up = "• <b>Help Desk Hours:</b> Sunday to Thursday, 10:00 AM to 06:00 PM (Clause 276). <b>24/7 Hotline</b> for P1 emergencies.<br/>• <b>System Uptime:</b> 99.9% uptime guarantee excluding pre-scheduled off-peak maintenance.<br/>• <b>Software Updates:</b> Delivery of bug fixes, security enhancements, and Bangladesh Bank regulatory reporting changes at zero cost under warranty/AMC.<br/>• <b>Data Protection:</b> Strict adherence to Bank Asia security guidelines; zero data loss guarantee."
    story.append(Paragraph(p_up, body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("3. Support Escalation Matrix", heading_style))
    esc_data = [
        [Paragraph("<b>Escalation Tier</b>", th_style), Paragraph("<b>Contact Person & Designation</b>", th_style), Paragraph("<b>Direct Contact & Email</b>", th_style)],
        [Paragraph("Level 1: Helpdesk", td_bold), Paragraph("Support Cell Lead, Skoder Technologies", td_style), Paragraph("+88 01979 891996 | support@skoder.co", td_style)],
        [Paragraph("Level 2: Tech Lead", td_bold), Paragraph("Ali Haider Fahad, Chief Technology Officer", td_style), Paragraph("+88 01750 726094 | fahad@skoder.co", td_style)],
        [Paragraph("Level 3: Executive", td_bold), Paragraph("K. M. Abir Mahmud, Chief Executive Officer", td_style), Paragraph("+88 01750 726094 | abir@skoder.co", td_style)],
    ]
    esc_tbl = Table(esc_data, colWidths=[100, 207, 180])
    esc_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(esc_tbl)
    story.append(Spacer(1, 6))

    story.append(get_signature_block())

    build_pdf_document("Draft_SLA_Bank_Asia_LMS.pdf", story)

# ---------------------------------------------------------------------------
# 6. DRAFT NON-DISCLOSURE AGREEMENT (NDA)
# ---------------------------------------------------------------------------
def build_draft_nda():
    story = []
    story.append(Paragraph("DRAFT NON-DISCLOSURE AGREEMENT (NDA)", title_style))
    story.append(Paragraph("Confidentiality & Information Security Protection Agreement<br/>Between Bank Asia PLC and Skoder Technologies", subtitle_style))
    story.append(Spacer(1, 6))

    p_nda = "This Non-Disclosure Agreement (\"Agreement\") is entered into on October 11, 2026, by and between <b>Bank Asia PLC</b>, Corporate Office, Bank Asia Tower, 32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka-1215 (\"Disclosing Party\"), and <b>Skoder Technologies</b>, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207 (\"Receiving Party\")."
    story.append(Paragraph(p_nda, body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Key Terms & Obligations (As per RFP Section 6, Clause 287, 297–299):", heading_style))

    c1 = "1. <b>Scope of Confidential Information:</b> Any information disclosed by Bank Asia PLC, including customer accounts, credit facilities, recovery records, litigation files, CBS schemas, API architectures, network topology, and security policies."
    c2 = "2. <b>Non-Disclosure Obligations:</b> Skoder Technologies shall hold all Confidential Information in strictest confidence and shall not disclose or distribute such information to any third party without prior written consent from Bank Asia PLC. Access is restricted strictly to assigned personnel on a need-to-know basis."
    c3 = "3. <b>Mandatory 4-Hour Incident Protocol (Clause 297–299):</b> In the event of any data breach or suspected compromise, Skoder Technologies shall: (i) Notify Bank Asia in writing within <b>4 (four) hours</b>; (ii) Submit an incident report; (iii) Cooperate fully with investigation; (iv) Take immediate corrective actions at its own cost."
    c4 = "4. <b>Term of Confidentiality:</b> This obligation remains binding throughout the contract period and survives indefinitely following completion or termination of the project."
    c5 = "5. <b>Governing Law:</b> This agreement shall be governed in accordance with the prevailing laws of Bangladesh."

    story.append(Paragraph(c1, bullet_style))
    story.append(Spacer(1, 2.5))
    story.append(Paragraph(c2, bullet_style))
    story.append(Spacer(1, 2.5))
    story.append(Paragraph(c3, bullet_style))
    story.append(Spacer(1, 2.5))
    story.append(Paragraph(c4, bullet_style))
    story.append(Spacer(1, 2.5))
    story.append(Paragraph(c5, bullet_style))
    story.append(Spacer(1, 6))

    sig_bank = Paragraph("<b>For Bank Asia PLC:</b><br/><br/><br/>___________________________<br/>Authorized Signatory<br/>Bank Asia PLC", td_style)
    sig_skoder = Paragraph("<b>For Skoder Technologies:</b>", td_bold)

    sig_img = PlatypusImage(SIGNATURE_PATH, width=80, height=40) if os.path.exists(SIGNATURE_PATH) else Paragraph("[Signature]", None)
    seal_img = PlatypusImage(SEAL_PATH, width=54, height=54) if os.path.exists(SEAL_PATH) else Paragraph("[Seal]", None)
    sig_text = Paragraph(f"<font fontName='{FONT_BOLD}' size=9 color='#000000'>K. M. ABIR MAHMUD</font><br/><font fontName='{FONT_NORMAL}' size=8 color='#333333'>Chief Executive Officer<br/><font fontName='{FONT_BOLD}' size=8.5 color='#00b050'>SKODER TECHNOLOGIES</font></font>", None)

    skoder_box = Table([[sig_skoder], [sig_img, seal_img], [sig_text]], colWidths=[237])
    skoder_box.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))

    dual_sig = Table([[sig_bank, skoder_box]], colWidths=[240, 247])
    dual_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(dual_sig)

    build_pdf_document("Draft_NDA_Bank_Asia_LMS.pdf", story)

# ---------------------------------------------------------------------------
# 7. TRAINING PROPOSAL DOCUMENT
# ---------------------------------------------------------------------------
def build_training_proposal():
    story = []
    story.append(Paragraph("COMPREHENSIVE TRAINING PROPOSAL & ROLLOUT PLAN", title_style))
    story.append(Paragraph("Litigation Management System (LMS) | RFP Clause 308, 309 & 1673 | Bank Asia PLC", subtitle_style))
    story.append(Spacer(1, 6))

    p_tr = "In compliance with RFP Section 6, Clause 308–309 and Section 9, Clause 1673, Skoder Technologies provides this separate Training Proposal for the Litigation Management System (LMS). We provide both <b>Functional User Training</b> (for Legal Division, Law Officers, Recovery Officers) and <b>Technical System Administration Training</b> (for ICT Division, DBAs, and System Administrators)."
    story.append(Paragraph(p_tr, body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. Commercial Training Fee Structure (Quoted Separately)", heading_style))
    tr_fee_data = [
        [Paragraph("<b>Training Component</b>", th_style), Paragraph("<b>Rate per Day (BDT)</b>", th_style), Paragraph("<b>Proposed Duration</b>", th_style), Paragraph("<b>Total Commercial Fee (BDT)</b>", th_style)],
        [Paragraph("<b>Comprehensive LMS User & Admin Training</b><br/>• Track A: Functional Case & Recovery Workflows<br/>• Track B: ICT Admin, DB, Security & CBS Integration", td_style),
         Paragraph("<b>BDT 5,000.00 / day</b><br/><i>(Excl. VAT & Tax)</i>", td_bold),
         Paragraph("6 Training Days<br/>(1 Week Total)", td_style),
         Paragraph("<b>BDT 30,000.00</b> (Excl. Tax)<br/><b>BDT 34,500.00</b> (Incl. 5% VAT + 10% AIT)", td_bold)],
    ]
    tr_fee_tbl = Table(tr_fee_data, colWidths=[190, 107, 85, 105])
    tr_fee_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(tr_fee_tbl)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. Training Curriculum & Schedule Breakdown (Implementation Week 15–16)", heading_style))
    curric_data = [
        [Paragraph("<b>Day</b>", th_style), Paragraph("<b>Target Audience</b>", th_style), Paragraph("<b>Key Modules & Topics Covered</b>", th_style)],
        [Paragraph("Day 1", td_bold), Paragraph("Legal Officers & Branch Users", td_style), Paragraph("System Navigation, Role Dashboards, Case Initiation, Document Uploading, Artha Rin workflows.", td_style)],
        [Paragraph("Day 2", td_bold), Paragraph("Law Officers & Recovery Team", td_style), Paragraph("NI Act 138 suits, Legal Notice automated generation, Auction Management, Settlement logs.", td_style)],
        [Paragraph("Day 3", td_bold), Paragraph("Head Office & Senior Management", td_style), Paragraph("Write-Off Account (WOA) tracking, Panel lawyer allocation, Bangladesh Bank MIS reports, Analytics.", td_style)],
        [Paragraph("Day 4", td_bold), Paragraph("ICT System Administrators", td_style), Paragraph("User access control, Group permissions, Audit logs, Password policies, System configuration.", td_style)],
        [Paragraph("Day 5", td_bold), Paragraph("DBA & Infrastructure Engineers", td_style), Paragraph("Database backup/restore, Performance tuning, High Availability, Disaster Recovery failover.", td_style)],
        [Paragraph("Day 6", td_bold), Paragraph("Integration & Security Engineers", td_style), Paragraph("CBS API Gateway maintenance, Security parameter management, End-to-end troubleshooting & Q&A.", td_style)],
    ]
    curric_tbl = Table(curric_data, colWidths=[40, 140, 307])
    curric_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(curric_tbl)
    story.append(Spacer(1, 4))

    story.append(Paragraph("3. Designated Instructors & Training Methodology (Clause 309)", heading_style))
    p_inst = "• <b>Lead Technical Trainer:</b> Ali Haider Fahad (CTO, Skoder Technologies) – Enterprise Software Architect.<br/>• <b>Functional & Systems Trainer:</b> Fahad Morshed (CIO, Skoder Technologies) – Systems & AI Specialist.<br/>• <b>Deliverables:</b> Comprehensive User Manual, System Administrator SOP, Quick Reference Guides, and video recordings."
    story.append(Paragraph(p_inst, body_style))
    story.append(Spacer(1, 6))

    story.append(get_signature_block())

    build_pdf_document("Training_Proposal_and_Plan_Bank_Asia.pdf", story)

# ---------------------------------------------------------------------------
# 8. HARDWARE INFRASTRUCTURE PROPOSAL
# ---------------------------------------------------------------------------
def build_hardware_proposal():
    story = []
    story.append(Paragraph("TURNKEY SERVER INFRASTRUCTURE & PLATFORM QUOTATION", title_style))
    story.append(Paragraph("Litigation Management System (LMS) | RFP Section 7, Table 17 & 18 | Bank Asia PLC", subtitle_style))
    story.append(Spacer(1, 6))

    p_hw = "As requested in RFP Section 6 Clause 288, 304 and Section 7 Tables 17 & 18, Skoder Technologies provides this separate commercial quotation for the recommended High-Availability (HA) Server Infrastructure and Enterprise Systems Software based on competitive Bangladeshi market rates. <i>Note: This is an optional turnkey schedule; Bank Asia PLC may deploy on existing enterprise infrastructure if preferred.</i>"
    story.append(Paragraph(p_hw, body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. Server Hardware Specifications & Pricing (As per Table 17)", heading_style))
    hw_table_data = [
        [Paragraph("<b>Item & Specifications</b>", th_style), Paragraph("<b>Qty</b>", th_style), Paragraph("<b>Unit Price (BDT)</b>", th_style), Paragraph("<b>Total Price (BDT)</b>", th_style)],
        [Paragraph("<b>Dell PowerEdge R760 2U Rack Mount Server</b><br/>• Dual Intel Xeon Silver 4414T (20-Core / 40-Thread each)<br/>• 128 GB (4x 32GB) DDR5 4800MHz ECC RDIMM<br/>• PERC H755 SAS/SATA/NVMe RAID Controller (8GB Cache)<br/>• BOSS-N1 Card with 2x 480GB M.2 NVMe SSDs (RAID 1)<br/>• 4x 1.92TB SAS Enterprise 12Gbps 2.5in Hot-plug SSD<br/>• Quad-Port 10GbE SFP+ / 1GbE RJ45 OCP 3.0 NIC<br/>• Dual 800W Titanium Redundant Power Supply (1+1)<br/>• iDRAC9 Enterprise Remote Management<br/>• 3-Year Dell ProSupport & NBD Onsite Warranty", td_style),
         Paragraph("02 Units<br/><i>(Primary & DR)</i>", td_style),
         Paragraph("1,550,000.00", td_right),
         Paragraph("<b>3,100,000.00</b>", td_right_bold)],
    ]
    hw_tbl = Table(hw_table_data, colWidths=[260, 67, 80, 80])
    hw_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(hw_tbl)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. Enterprise System Software & Database Licenses (As per Table 18)", heading_style))
    sw_table_data = [
        [Paragraph("<b>Platform / Software Item</b>", th_style), Paragraph("<b>Description & Support Tenure</b>", th_style), Paragraph("<b>Qty</b>", th_style), Paragraph("<b>Total Price (BDT)</b>", th_style)],
        [Paragraph("<b>VMware vSphere 8 Enterprise Plus</b>", td_bold), Paragraph("Per CPU Socket License with 3-Year Production Support", td_style), Paragraph("02 Lic", td_style), Paragraph("840,000.00", td_right)],
        [Paragraph("<b>Red Hat Enterprise Linux (RHEL)</b>", td_bold), Paragraph("Server Standard Subscription (2 Sockets / 2 VMs, 3-Yr Support)", td_style), Paragraph("04 Sub", td_style), Paragraph("580,000.00", td_right)],
        [Paragraph("<b>PostgreSQL Enterprise Edition / Oracle 19c</b>", td_bold), Paragraph("Enterprise Database Engine with 3-Year Software Updates & Support", td_style), Paragraph("02 Lic", td_style), Paragraph("450,000.00", td_right)],
        [Paragraph("<b>Total Infrastructure & Platform Software Value (Optional)</b>", td_bold), Paragraph("All hardware and system software licenses with 3-Year Support", td_bold), "", Paragraph("<b>BDT 4,970,000.00</b>", td_right_bold)],
    ]
    sw_tbl = Table(sw_table_data, colWidths=[140, 197, 50, 100])
    sw_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#e8f5e9')),
        ('SPAN', (0,-1), (1,-1)),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(sw_tbl)
    story.append(Spacer(1, 6))

    story.append(get_signature_block())

    build_pdf_document("Hardware_Infrastructure_Quotation_Bank_Asia.pdf", story)

if __name__ == '__main__':
    build_cover_letter()
    build_financial_proposal()
    build_oem_declaration()
    build_power_of_attorney()
    build_draft_sla()
    build_draft_nda()
    build_training_proposal()
    build_hardware_proposal()
    print("All pad documents regenerated successfully!")
