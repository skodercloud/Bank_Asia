import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def get_base_styles():
    styles = getSampleStyleSheet()
    
    custom_styles = {
        'HdrTitle': ParagraphStyle('HdrTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#0d47a1')),
        'HdrSub': ParagraphStyle('HdrSub', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10.5, textColor=colors.HexColor('#424242')),
        'DocTitle': ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#0d47a1'), alignment=1),
        'DocSubTitle': ParagraphStyle('DocSubTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=colors.HexColor('#1b5e20'), alignment=1),
        'SectionHdr': ParagraphStyle('SectionHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=colors.HexColor('#0d47a1')),
        'Body': ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#212121')),
        'BodyBold': ParagraphStyle('BodyBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=colors.HexColor('#212121')),
        'Bullet': ParagraphStyle('Bullet', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, leftIndent=12, textColor=colors.HexColor('#212121')),
        'TableHdr': ParagraphStyle('TableHdr', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10.5, textColor=colors.white, alignment=1),
        'TableCell': ParagraphStyle('TableCell', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10, textColor=colors.HexColor('#212121')),
        'TableCellBold': ParagraphStyle('TableCellBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#212121')),
        'TableCellRight': ParagraphStyle('TableCellRight', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10, textColor=colors.HexColor('#212121'), alignment=2),
        'TableCellRightBold': ParagraphStyle('TableCellRightBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#212121'), alignment=2),
    }
    return custom_styles

def create_header(styles):
    hdr_left = Paragraph('<b>SKODER TECHNOLOGIES</b><br/><font size="7" color="#555555">E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207<br/>BIN# 002855793-0401 | Trade# TRAD/DNCC/056205/2022</font>', styles['HdrTitle'])
    hdr_right = Paragraph('<font size="7" color="#555555">+88 01750 726094 | +88 01979 891996<br/>contact@skoder.co | abir.skoder@gmail.com<br/>www.skoder.co</font>', ParagraphStyle('HdrR', parent=styles['HdrSub'], alignment=2))
    hdr_table = Table([[hdr_left, hdr_right]], colWidths=[330, 180])
    hdr_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 1.2, colors.HexColor('#0d47a1')),
    ]))
    return hdr_table

def create_signature_block(styles, witness_needed=False):
    sig_img = Image('assets/abir_signature.jpg', width=80, height=45)
    seal_img = Image('assets/skoder_seal.jpg', width=52, height=52)
    sig_text = Paragraph('<b>K. M. ABIR MAHMUD</b><br/>Chief Executive Officer<br/><b>SKODER TECHNOLOGIES</b><br/>Cell: +88 01750 726094', styles['TableCell'])
    
    if not witness_needed:
        sig_table = Table([[sig_img, seal_img], [sig_text, '']], colWidths=[160, 350])
        sig_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        return sig_table
    else:
        w_text = Paragraph('<b>Witness 1:</b> Fahad Morshed, CIO, Skoder Technologies<br/><b>Witness 2:</b> Imran Bipu, Head of Business, Skoder Technologies', styles['TableCell'])
        sig_table = Table([[sig_img, seal_img, w_text], [sig_text, '', '']], colWidths=[130, 110, 270])
        sig_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        return sig_table

# -------------------------------------------------------------
# 1. Financial Proposal Document
# -------------------------------------------------------------
def build_financial_proposal():
    styles = get_base_styles()
    doc = SimpleDocTemplate('Financial_Proposal_Bank_Asia.pdf', pagesize=letter, rightMargin=40, leftMargin=40, topMargin=26, bottomMargin=24)
    story = [create_header(styles), Spacer(1, 6)]
    
    story.append(Paragraph('FINANCIAL PROPOSAL', styles['DocTitle']))
    story.append(Paragraph('Procurement, Supply, Implementation, Integration, and Support of Litigation Management System (LMS)<br/>Tender Ref: RFP_LMS Bank Asia_v0.3 | Client: Bank Asia PLC', styles['DocSubTitle']))
    story.append(Spacer(1, 6))
    
    # Financial Letter
    intro_txt = '<b>To: The Head of ICT Division, Bank Asia PLC</b> — We, <b>Skoder Technologies</b>, hereby submit our sealed Financial Proposal for the supply, implementation, integration, and comprehensive support of the <b>Litigation Management System (LMS)</b> for Bank Asia PLC in strict conformity with Section 9 & 10 of the RFP documents.'
    story.append(Paragraph(intro_txt, styles['Body']))
    story.append(Spacer(1, 5))
    
    # Table 20 Data
    story.append(Paragraph('1. Core LMS Commercial Schedule (As per RFP Table 20)', styles['SectionHdr']))
    story.append(Spacer(1, 3))
    
    headers_t20_r1 = [
        Paragraph('<b>Product Name</b>', styles['TableHdr']),
        Paragraph('<b>Proposed Product & BOQ Details</b>', styles['TableHdr']),
        Paragraph('<b>Model/Ver</b>', styles['TableHdr']),
        Paragraph('<b>Qty</b>', styles['TableHdr']),
        Paragraph('<b>Unit Price (BDT)</b>', styles['TableHdr']),
        Paragraph('<b>VAT 5% + AIT 10%</b>', styles['TableHdr']),
        Paragraph('<b>Total Price (BDT)</b>', styles['TableHdr']),
        Paragraph('<b>Yearly AMC after 3rd Year (BDT)</b>', styles['TableHdr']),
        '', '',
        Paragraph('<b>Grand Total (BDT)</b>', styles['TableHdr'])
    ]
    headers_t20_r2 = ['', '', '', '', '', '', '', Paragraph('<b>4th Yr</b>', styles['TableHdr']), Paragraph('<b>5th Yr</b>', styles['TableHdr']), Paragraph('<b>6th Yr</b>', styles['TableHdr']), '']
    
    row_data = [
        Paragraph('<b>Litigation Management System (LMS)</b>', styles['TableCellBold']),
        Paragraph('<b>Skoder LMS Enterprise Bank Edition</b><br/>• Pre-Litigation, Artha Rin, NI 138, Civil/Criminal<br/>• Auction, WOA Tracking, Panel Lawyer Mgmt<br/>• CBS Core Banking Integration & BB MIS Reports<br/><i>(Includes 3-Year Full Warranty & 24/7 Support)</i>', styles['TableCell']),
        Paragraph('v1.0 Bank Edition', styles['TableCell']),
        Paragraph('01 Bank-wide', styles['TableCell']),
        Paragraph('1,500,000.00', styles['TableCellRight']),
        Paragraph('VAT: 75,000<br/>AIT: 150,000<br/>(15% Total)', styles['TableCell']),
        Paragraph('<b>1,725,000.00</b>', styles['TableCellRightBold']),
        Paragraph('402,500.00', styles['TableCellRight']),
        Paragraph('402,500.00', styles['TableCellRight']),
        Paragraph('402,500.00', styles['TableCellRight']),
        Paragraph('<b>2,932,500.00</b>', styles['TableCellRightBold'])
    ]
    
    summary_row = [
        Paragraph('<b>Total Product Price (Initial 3 Yrs incl. VAT/Tax)</b>', styles['TableCellBold']),
        Paragraph('<b>BDT 1,725,000.00</b> <i>(Taka Seventeen Lac Twenty-Five Thousand Only)</i>', styles['TableCellBold']),
        '', '', '', '', '',
        Paragraph('<b>Total 3-Yr AMC (Y4–Y6)</b>', styles['TableCellBold']),
        '', '',
        Paragraph('<b>BDT 1,207,500.00</b>', styles['TableCellRightBold'])
    ]
    
    grand_row = [
        Paragraph('<b>GRAND TOTAL BID VALUE (Software + 6 Years Full Lifecycle including VAT & TAX)</b>', styles['TableCellBold']),
        '', '', '', '', '', '', '', '', '',
        Paragraph('<b>BDT 2,932,500.00</b>', styles['TableCellRightBold'])
    ]
    
    t20_table = Table([headers_t20_r1, headers_t20_r2, row_data, summary_row, grand_row], colWidths=[65, 135, 42, 32, 45, 45, 48, 35, 35, 35, 45])
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
    story.append(Spacer(1, 5))
    
    # Table 21 & Training
    story.append(Paragraph('2. Additional Scope & Training Rate Schedule (As per RFP Table 21 & Clause 308)', styles['SectionHdr']))
    story.append(Spacer(1, 3))
    
    t21_data = [
        [Paragraph('<b>Item Description</b>', styles['TableHdr']), Paragraph('<b>Rate / Commercial Terms (BDT)</b>', styles['TableHdr'])],
        [Paragraph('<b>Functional & Technical Training per Day</b><br/><i>(Comprehensive onsite sessions for Legal Dept & ICT Division, Clause 308)</i>', styles['TableCell']),
         Paragraph('<b>BDT 5,000.00 per day</b> (Excl. VAT/Tax) | <b>BDT 5,750.00 per day</b> (Incl. VAT 5% & AIT 10%)', styles['TableCell'])],
        [Paragraph('<b>Additional Custom Module / Future Integration Gateway</b> (Optional future workflows)', styles['TableCell']),
         Paragraph('BDT 150,000.00 per module (Inclusive of all applicable Taxes)', styles['TableCell'])],
        [Paragraph('<b>Optional Turnkey Server Infrastructure (Dell PowerEdge R760 2U HA Cluster)</b>', styles['TableCell']),
         Paragraph('BDT 4,970,000.00 (Optional Schedule detailed in Annexure; Bank may provide internally)', styles['TableCell'])],
    ]
    t21_table = Table(t21_data, colWidths=[330, 202])
    t21_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t21_table)
    story.append(Spacer(1, 5))
    
    # Pay Order Details & Undertaking Box
    story.append(Paragraph('3. Bid Security & Formal Price Undertaking', styles['SectionHdr']))
    story.append(Spacer(1, 3))
    
    po_data = [
        [Paragraph('<b>Pay Order No. & Date:</b>', styles['TableCellBold']), Paragraph('SJIBL/MIR/PO/2026/04812, Dated: 11 October, 2026', styles['TableCell'])],
        [Paragraph('<b>Amount:</b>', styles['TableCellBold']), Paragraph('BDT 25,000/- (Taka Twenty-Five Thousand Only)', styles['TableCell'])],
        [Paragraph('<b>Issuing Bank & Branch:</b>', styles['TableCellBold']), Paragraph('Shahjalal Islami Bank PLC, Mirpur Branch, Dhaka', styles['TableCell'])],
        [Paragraph('<b>Validity of Quotation:</b>', styles['TableCellBold']), Paragraph('12 (Twelve) Months from bid opening date (Valid up to October 11, 2027)', styles['TableCell'])],
    ]
    po_table = Table(po_data, colWidths=[150, 382])
    po_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdbdbd')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f5f5f5')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(po_table)
    story.append(Spacer(1, 4))
    
    undertaking_text = '<b>Undertaking:</b> We, <b>Skoder Technologies</b>, hereby undertake to supply, implement, integrate, and support the Litigation Management System at the prices quoted above in full conformity with Bank Asia\'s RFP specifications. All software prices include VAT (5%) and AIT (10%).'
    story.append(Paragraph(undertaking_text, styles['Body']))
    story.append(Spacer(1, 5))
    
    story.append(create_signature_block(styles, witness_needed=True))
    
    doc.build(story)
    print('Generated Financial_Proposal_Bank_Asia.pdf successfully!')

# -------------------------------------------------------------
# 2. OEM / Proprietary Solution Developer Declaration Letter
# -------------------------------------------------------------
def build_oem_declaration():
    styles = get_base_styles()
    doc = SimpleDocTemplate('OEM_Developer_Declaration_Skoder.pdf', pagesize=letter, rightMargin=50, leftMargin=50, topMargin=36, bottomMargin=36)
    story = [create_header(styles), Spacer(1, 12)]
    
    story.append(Paragraph('<b>Date:</b> October 11, 2026', styles['Body']))
    story.append(Spacer(1, 6))
    story.append(Paragraph('To<br/><b>The Head of ICT Division</b><br/>Bank Asia PLC<br/>Corporate Office, Bank Asia Tower (1st Floor)<br/>32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka-1215, Bangladesh', styles['Body']))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph('<b>Subject: OEM / Solution Developer & Intellectual Property Rights Declaration</b>', styles['DocSubTitle']))
    story.append(Paragraph('<b>Ref:</b> RFP for Litigation Management System (LMS) – Clause 211, 225 & 278', styles['Body']))
    story.append(Spacer(1, 10))
    
    p1 = 'Dear Sir/Madam,<br/><br/>We, <b>Skoder Technologies</b>, an established software engineering and innovation firm registered in Bangladesh, having our principal corporate office at E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207, do hereby formally certify and declare that:'
    story.append(Paragraph(p1, styles['Body']))
    story.append(Spacer(1, 8))
    
    c1 = '1. <b>100% Proprietary Solution:</b> Skoder Technologies is the Original Software Manufacturer (OSM) / Solution Developer and sole intellectual property owner of the proposed <b>Litigation Management System (LMS)</b>. The system has been 100% architected, developed, and maintained by our in-house engineering team.'
    c2 = '2. <b>No Third-Party OEM Dependency:</b> The core LMS application does not rely on third-party proprietary LMS platforms or foreign distributor licenses. Skoder Technologies holds complete, unencumbered rights to supply, install, configure, customize, integrate, and support the application.'
    c3 = '3. <b>6-Year Support & Product Availability Commitment:</b> In compliance with RFP Section 6, Clause 278, Skoder Technologies guarantees that the proposed solution, product roadmap, version enhancements, security patches, CBS integration interfaces, and full technical maintenance will be actively supported and available for a minimum of <b>06 (six) years</b> from the date of deployment.'
    c4 = '4. <b>24/7 Dedicated Technical Support:</b> Skoder Technologies maintains an active engineering and system support cell in Dhaka with 24/7/365 coverage for all warranty and AMC requirements.'
    c5 = '5. <b>Regulatory Compliance Guarantee:</b> Skoder Technologies commits to providing all regulatory reporting adaptations and compliance updates mandated by <b>Bangladesh Bank</b> without service disruption.'
    
    story.append(Paragraph(c1, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c2, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c3, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c4, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c5, styles['Bullet']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph('We confirm our absolute commitment to executing this project successfully in partnership with Bank Asia PLC.', styles['Body']))
    story.append(Spacer(1, 14))
    
    story.append(create_signature_block(styles))
    doc.build(story)
    print('Generated OEM_Developer_Declaration_Skoder.pdf successfully!')

# -------------------------------------------------------------
# 3. Draft Service Level Agreement (SLA)
# -------------------------------------------------------------
def build_draft_sla():
    styles = get_base_styles()
    doc = SimpleDocTemplate('Draft_SLA_Bank_Asia_LMS.pdf', pagesize=letter, rightMargin=50, leftMargin=50, topMargin=36, bottomMargin=36)
    story = [create_header(styles), Spacer(1, 10)]
    
    story.append(Paragraph('DRAFT SERVICE LEVEL AGREEMENT (SLA)', styles['DocTitle']))
    story.append(Paragraph('Litigation Management System (LMS) | Bank Asia PLC & Skoder Technologies', styles['DocSubTitle']))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph('1. Purpose & Scope of SLA', styles['SectionHdr']))
    p_sla = 'This Service Level Agreement (SLA) defines the service availability, response times, defect resolution windows, and support standards provided by <b>Skoder Technologies</b> (the "Service Provider") to <b>Bank Asia PLC</b> (the "Bank") for the Litigation Management System (LMS) during the 3-Year Warranty Period and subsequent Annual Maintenance Contract (AMC) tenure.'
    story.append(Paragraph(p_sla, styles['Body']))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('2. Support Availability & Coverage', styles['SectionHdr']))
    p_cov = '• <b>Help Desk Hours:</b> Standard operational support Sunday to Thursday, 10:00 AM to 06:00 PM (as per RFP Clause 276).<br/>• <b>Critical 24/7 Support:</b> 24/7/365 emergency phone and on-call response for Severity 1 (Critical) incidents (as per RFP Clause 293).<br/>• <b>Onsite Support:</b> Provision of technical subject matter experts onsite at Bank Asia Corporate Office during implementation and critical post-launch stabilization.'
    story.append(Paragraph(p_cov, styles['Body']))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('3. Incident Priority & Response Matrix', styles['SectionHdr']))
    sla_table_data = [
        [Paragraph('<b>Severity Level</b>', styles['TableHdr']), Paragraph('<b>Definition / Impact</b>', styles['TableHdr']), Paragraph('<b>Response Time</b>', styles['TableHdr']), Paragraph('<b>Resolution Time</b>', styles['TableHdr'])],
        [Paragraph('<b>Priority 1 (Critical)</b>', styles['TableCellBold']),
         Paragraph('System down; core legal workflows halted; CBS integration failure impacting all users.', styles['TableCell']),
         Paragraph('Within 30 Minutes', styles['TableCell']),
         Paragraph('Within 4 Hours', styles['TableCell'])],
        [Paragraph('<b>Priority 2 (High)</b>', styles['TableCellBold']),
         Paragraph('Major feature or module impaired (e.g. Artha Rin filing, legal notice generation) with no workaround.', styles['TableCell']),
         Paragraph('Within 1 Hour', styles['TableCell']),
         Paragraph('Within 8 Hours', styles['TableCell'])],
        [Paragraph('<b>Priority 3 (Medium)</b>', styles['TableCellBold']),
         Paragraph('Minor functionality issue, report generation discrepancy; workaround available.', styles['TableCell']),
         Paragraph('Within 2 Hours', styles['TableCell']),
         Paragraph('Within 24 Hours', styles['TableCell'])],
        [Paragraph('<b>Priority 4 (Low)</b>', styles['TableCellBold']),
         Paragraph('General inquiries, cosmetic UI issues, user rights changes, routine assistance.', styles['TableCell']),
         Paragraph('Within 4 Hours', styles['TableCell']),
         Paragraph('Within 48 Hours', styles['TableCell'])],
    ]
    sla_tbl = Table(sla_table_data, colWidths=[90, 230, 95, 95])
    sla_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(sla_tbl)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('4. System Availability & Maintenance Commitments', styles['SectionHdr']))
    p_up = '• <b>System Uptime:</b> 99.9% uptime guarantee excluding pre-scheduled off-peak maintenance.<br/>• <b>Software Updates:</b> Delivery of bug fixes, security enhancements, and Bangladesh Bank regulatory reporting changes at zero additional cost under warranty/AMC.<br/>• <b>Data Protection:</b> Strict adherence to Bank Asia security guidelines; zero data loss guarantee.'
    story.append(Paragraph(p_up, styles['Body']))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph('5. Support Escalation Matrix', styles['SectionHdr']))
    esc_data = [
        [Paragraph('<b>Escalation Tier</b>', styles['TableHdr']), Paragraph('<b>Contact Person & Designation</b>', styles['TableHdr']), Paragraph('<b>Direct Contact & Email</b>', styles['TableHdr'])],
        [Paragraph('Level 1: Helpdesk', styles['TableCellBold']), Paragraph('Support Cell Lead, Skoder Technologies', styles['TableCell']), Paragraph('+88 01979 891996 | support@skoder.co', styles['TableCell'])],
        [Paragraph('Level 2: Tech Lead', styles['TableCellBold']), Paragraph('Ali Haider Fahad, Chief Technology Officer', styles['TableCell']), Paragraph('+88 01750 726094 | fahad@skoder.co', styles['TableCell'])],
        [Paragraph('Level 3: Executive', styles['TableCellBold']), Paragraph('K. M. Abir Mahmud, Chief Executive Officer', styles['TableCell']), Paragraph('+88 01750 726094 | abir@skoder.co', styles['TableCell'])],
    ]
    esc_tbl = Table(esc_data, colWidths=[110, 210, 190])
    esc_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(esc_tbl)
    story.append(Spacer(1, 8))
    
    story.append(create_signature_block(styles))
    doc.build(story)
    print('Generated Draft_SLA_Bank_Asia_LMS.pdf successfully!')

# -------------------------------------------------------------
# 4. Draft Non-Disclosure Agreement (NDA)
# -------------------------------------------------------------
def build_draft_nda():
    styles = get_base_styles()
    doc = SimpleDocTemplate('Draft_NDA_Bank_Asia_LMS.pdf', pagesize=letter, rightMargin=50, leftMargin=50, topMargin=36, bottomMargin=36)
    story = [create_header(styles), Spacer(1, 10)]
    
    story.append(Paragraph('DRAFT NON-DISCLOSURE AGREEMENT (NDA)', styles['DocTitle']))
    story.append(Paragraph('Confidentiality & Information Security Protection Agreement<br/>Between Bank Asia PLC and Skoder Technologies', styles['DocSubTitle']))
    story.append(Spacer(1, 8))
    
    p_nda = 'This Non-Disclosure Agreement ("Agreement") is made and entered into on this 11th day of October, 2026, by and between <b>Bank Asia PLC</b>, having its Corporate Office at Bank Asia Tower, 32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka-1215, Bangladesh ("Disclosing Party"), and <b>Skoder Technologies</b>, having its principal office at E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207 ("Receiving Party").'
    story.append(Paragraph(p_nda, styles['Body']))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('Key Terms & Obligations (As per RFP Section 6, Clause 287, 297–299):', styles['SectionHdr']))
    
    c1 = '1. <b>Definition of Confidential Information:</b> Any and all information disclosed by Bank Asia PLC to Skoder Technologies, including but not limited to customer details, credit facilities, recovery accounts, legal case records, CBS schemas, API architectures, network topology, and security policies.'
    c2 = '2. <b>Non-Disclosure Obligations:</b> Skoder Technologies agrees to hold all Confidential Information in strictest confidence and shall not disclose, reproduce, or distribute such information to any third party without prior written consent from Bank Asia PLC. Access shall be restricted strictly to employees assigned to this project on a need-to-know basis.'
    c3 = '3. <b>Data Breach Protocol (Clause 297–299):</b> In the event of any data breach or security compromise, Skoder Technologies shall: (i) Notify Bank Asia PLC in writing within <b>4 (four) hours</b> of detection; (ii) Submit an incident report; (iii) Fully cooperate in mitigation and investigation; (iv) Take immediate corrective actions at its own cost.'
    c4 = '4. <b>Term of Confidentiality:</b> This obligation remains binding throughout the contract period and survives indefinitely following completion or termination of the project.'
    c5 = '5. <b>Governing Law & Jurisdiction:</b> This agreement shall be governed and construed in accordance with the prevailing laws of Bangladesh.'
    
    story.append(Paragraph(c1, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c2, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c3, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c4, styles['Bullet']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(c5, styles['Bullet']))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph('In witness whereof, the authorized representatives have executed this Non-Disclosure Agreement.', styles['BodyBold']))
    story.append(Spacer(1, 8))
    
    sig_bank = Paragraph('<b>For Bank Asia PLC:</b><br/><br/><br/>___________________________<br/>Authorized Signatory<br/>Bank Asia PLC', styles['TableCell'])
    sig_skoder = Paragraph('<b>For Skoder Technologies:</b>', styles['TableCellBold'])
    
    sig_img = Image('assets/abir_signature.jpg', width=80, height=45)
    seal_img = Image('assets/skoder_seal.jpg', width=52, height=52)
    sig_text = Paragraph('<b>K. M. ABIR MAHMUD</b><br/>Chief Executive Officer<br/>Skoder Technologies', styles['TableCell'])
    
    skoder_box = Table([[sig_skoder], [sig_img, seal_img], [sig_text]], colWidths=[240])
    skoder_box.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    
    dual_sig = Table([[sig_bank, skoder_box]], colWidths=[250, 260])
    dual_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(dual_sig)
    
    doc.build(story)
    print('Generated Draft_NDA_Bank_Asia_LMS.pdf successfully!')

# -------------------------------------------------------------
# 5. Training Proposal & Methodology Document
# -------------------------------------------------------------
def build_training_proposal():
    styles = get_base_styles()
    doc = SimpleDocTemplate('Training_Proposal_and_Plan_Bank_Asia.pdf', pagesize=letter, rightMargin=50, leftMargin=50, topMargin=36, bottomMargin=36)
    story = [create_header(styles), Spacer(1, 10)]
    
    story.append(Paragraph('COMPREHENSIVE TRAINING PROPOSAL & ROLLOUT PLAN', styles['DocTitle']))
    story.append(Paragraph('Litigation Management System (LMS) | RFP Clause 308, 309 & 1673 | Bank Asia PLC', styles['DocSubTitle']))
    story.append(Spacer(1, 8))
    
    p_tr = 'In compliance with RFP Section 6, Clause 308–309 and Section 9, Clause 1673, Skoder Technologies provides this separate Training Proposal for the Litigation Management System (LMS). We provide both <b>Functional User Training</b> (for Legal Division, Law Officers, Recovery Officers) and <b>Technical System Administration Training</b> (for ICT Division, DBAs, and System Administrators).'
    story.append(Paragraph(p_tr, styles['Body']))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('1. Commercial Training Fee Structure (Quoted Separately)', styles['SectionHdr']))
    tr_fee_data = [
        [Paragraph('<b>Training Component</b>', styles['TableHdr']), Paragraph('<b>Rate per Day (BDT)</b>', styles['TableHdr']), Paragraph('<b>Proposed Duration</b>', styles['TableHdr']), Paragraph('<b>Total Commercial Fee (BDT)</b>', styles['TableHdr'])],
        [Paragraph('<b>Comprehensive LMS User & Admin Training</b><br/>• Track A: Functional Case & Recovery Workflows<br/>• Track B: ICT Admin, DB, Security & CBS Integration', styles['TableCell']),
         Paragraph('<b>BDT 5,000.00 / day</b><br/><i>(Excl. VAT & Tax)</i>', styles['TableCellBold']),
         Paragraph('6 Training Days<br/>(1 Week Total)', styles['TableCell']),
         Paragraph('<b>BDT 30,000.00</b> (Excl. Tax)<br/><b>BDT 34,500.00</b> (Incl. 5% VAT + 10% AIT)', styles['TableCellBold'])],
    ]
    tr_fee_tbl = Table(tr_fee_data, colWidths=[200, 110, 90, 110])
    tr_fee_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(tr_fee_tbl)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph('2. Training Curriculum & Schedule Breakdown (Implementation Week 15–16)', styles['SectionHdr']))
    curric_data = [
        [Paragraph('<b>Day</b>', styles['TableHdr']), Paragraph('<b>Target Audience</b>', styles['TableHdr']), Paragraph('<b>Key Modules & Topics Covered</b>', styles['TableHdr'])],
        [Paragraph('Day 1', styles['TableCellBold']), Paragraph('Legal Officers & Branch Users', styles['TableCell']), Paragraph('System Navigation, Role Dashboards, Case Initiation, Document Uploading, Artha Rin workflows.', styles['TableCell'])],
        [Paragraph('Day 2', styles['TableCellBold']), Paragraph('Law Officers & Recovery Team', styles['TableCell']), Paragraph('NI Act 138 suits, Legal Notice automated generation, Auction Management, Settlement logs.', styles['TableCell'])],
        [Paragraph('Day 3', styles['TableCellBold']), Paragraph('Head Office & Senior Management', styles['TableCell']), Paragraph('Write-Off Account (WOA) tracking, Panel lawyer allocation, Bangladesh Bank MIS reports, Analytics.', styles['TableCell'])],
        [Paragraph('Day 4', styles['TableCellBold']), Paragraph('ICT System Administrators', styles['TableCell']), Paragraph('User access control, Group permissions, Audit logs, Password policies, System configuration.', styles['TableCell'])],
        [Paragraph('Day 5', styles['TableCellBold']), Paragraph('DBA & Infrastructure Engineers', styles['TableCell']), Paragraph('Database backup/restore, Performance tuning, High Availability, Disaster Recovery failover.', styles['TableCell'])],
        [Paragraph('Day 6', styles['TableCellBold']), Paragraph('Integration & Security Engineers', styles['TableCell']), Paragraph('CBS API Gateway maintenance, Security parameter management, End-to-end troubleshooting & Q&A.', styles['TableCell'])],
    ]
    curric_tbl = Table(curric_data, colWidths=[45, 145, 320])
    curric_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(curric_tbl)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph('3. Designated Instructors & Training Methodology (Clause 309)', styles['SectionHdr']))
    p_inst = '• <b>Lead Technical Trainer:</b> Ali Haider Fahad (CTO, Skoder Technologies) – Enterprise Software Architect with 8+ years experience in scalable systems.<br/>• <b>Functional & Systems Trainer:</b> Fahad Morshed (CIO, Skoder Technologies) – Systems & AI Specialist with extensive expertise in database and banking workflows.<br/>• <b>Deliverables:</b> Comprehensive User Manual, System Administrator SOP, Quick Reference Guides, and recorded video walkthroughs.'
    story.append(Paragraph(p_inst, styles['Body']))
    story.append(Spacer(1, 8))
    
    story.append(create_signature_block(styles))
    doc.build(story)
    print('Generated Training_Proposal_and_Plan_Bank_Asia.pdf successfully!')

# -------------------------------------------------------------
# 6. Power of Attorney / Authorization Letter
# -------------------------------------------------------------
def build_power_of_attorney():
    styles = get_base_styles()
    doc = SimpleDocTemplate('Power_of_Attorney_Authorization_Letter.pdf', pagesize=letter, rightMargin=50, leftMargin=50, topMargin=36, bottomMargin=36)
    story = [create_header(styles), Spacer(1, 12)]
    
    story.append(Paragraph('POWER OF ATTORNEY / AUTHORIZATION LETTER', styles['DocTitle']))
    story.append(Paragraph('In compliance with RFP Section 6, Clause 260 | Bank Asia PLC Tender', styles['DocSubTitle']))
    story.append(Spacer(1, 12))
    
    p1 = '<b>TO WHOM IT MAY CONCERN</b><br/><br/>We, the management of <b>Skoder Technologies</b>, having our registered office at E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207, Bangladesh, do hereby nominate, constitute, and appoint:'
    story.append(Paragraph(p1, styles['Body']))
    story.append(Spacer(1, 8))
    
    appointee_box = [
        [Paragraph('<b>Name:</b>', styles['TableCellBold']), Paragraph('<b>K. M. ABIR MAHMUD</b>', styles['TableCellBold'])],
        [Paragraph('<b>Designation:</b>', styles['TableCellBold']), Paragraph('Chief Executive Officer (CEO)', styles['TableCell'])],
        [Paragraph('<b>NID No.:</b>', styles['TableCellBold']), Paragraph('8205149738', styles['TableCell'])],
        [Paragraph('<b>Organization:</b>', styles['TableCellBold']), Paragraph('Skoder Technologies', styles['TableCell'])],
        [Paragraph('<b>Contact No.:</b>', styles['TableCellBold']), Paragraph('+88 01750 726094 | abir.skoder@gmail.com', styles['TableCell'])],
    ]
    app_tbl = Table(appointee_box, colWidths=[120, 390])
    app_tbl.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdbdbd')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f5f5f5')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(app_tbl)
    story.append(Spacer(1, 10))
    
    p2 = 'as our true and lawful attorney and authorized representative to act on behalf of Skoder Technologies in connection with the tender for <b>"Procurement, supply, implementation, Integration and support of a Litigation Management System (LMS)"</b> for <b>Bank Asia PLC</b>.<br/><br/>The said attorney is authorized to:'
    story.append(Paragraph(p2, styles['Body']))
    story.append(Spacer(1, 6))
    
    a1 = '1. Sign, seal, and submit the Technical and Financial Bids, schedules, undertaking letters, and tender responses.'
    a2 = '2. Attend pre-bid meetings, commercial negotiations, and technical clarification sessions.'
    a3 = '3. Furnish Bid Security (Earnest Money) and Performance Security on behalf of the company.'
    a4 = '4. Sign and execute the formal Contract Agreement, Service Level Agreement (SLA), and Non-Disclosure Agreement (NDA) upon award of work.'
    story.append(Paragraph(a1, styles['Bullet']))
    story.append(Paragraph(a2, styles['Bullet']))
    story.append(Paragraph(a3, styles['Bullet']))
    story.append(Paragraph(a4, styles['Bullet']))
    story.append(Spacer(1, 8))
    
    p3 = 'All acts, deeds, and instruments done or executed by the said attorney shall be deemed as good, valid, and binding upon Skoder Technologies in all respects.'
    story.append(Paragraph(p3, styles['Body']))
    story.append(Spacer(1, 14))
    
    story.append(create_signature_block(styles, witness_needed=True))
    doc.build(story)
    print('Generated Power_of_Attorney_Authorization_Letter.pdf successfully!')

# -------------------------------------------------------------
# 7. Hardware & Turnkey Infrastructure Proposal
# -------------------------------------------------------------
def build_hardware_proposal():
    styles = get_base_styles()
    doc = SimpleDocTemplate('Hardware_Infrastructure_Quotation_Bank_Asia.pdf', pagesize=letter, rightMargin=50, leftMargin=50, topMargin=36, bottomMargin=36)
    story = [create_header(styles), Spacer(1, 10)]
    
    story.append(Paragraph('TURNKEY SERVER INFRASTRUCTURE & PLATFORM QUOTATION', styles['DocTitle']))
    story.append(Paragraph('Litigation Management System (LMS) | RFP Section 7, Table 17 & 18 | Bank Asia PLC', styles['DocSubTitle']))
    story.append(Spacer(1, 8))
    
    p_hw = 'As requested in RFP Section 6 Clause 288, 304 and Section 7 Tables 17 & 18, Skoder Technologies provides this separate commercial and technical quotation for the recommended High-Availability (HA) Server Infrastructure and Enterprise Systems Software based on competitive Bangladeshi market rates. <i>Note: This is an optional turnkey schedule; Bank Asia PLC may deploy on existing enterprise infrastructure if preferred.</i>'
    story.append(Paragraph(p_hw, styles['Body']))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('1. Server Hardware Specifications & Pricing (As per Table 17)', styles['SectionHdr']))
    hw_table_data = [
        [Paragraph('<b>Item & Specifications</b>', styles['TableHdr']), Paragraph('<b>Qty</b>', styles['TableHdr']), Paragraph('<b>Unit Price (BDT)</b>', styles['TableHdr']), Paragraph('<b>Total Price (BDT)</b>', styles['TableHdr'])],
        [Paragraph('<b>Dell PowerEdge R760 2U Rack Mount Server</b><br/>• Dual Intel Xeon Silver 4414T (20-Core / 40-Thread each)<br/>• 128 GB (4x 32GB) DDR5 4800MHz ECC RDIMM<br/>• PERC H755 SAS/SATA/NVMe RAID Controller (8GB Cache)<br/>• BOSS-N1 Card with 2x 480GB M.2 NVMe SSDs (RAID 1)<br/>• 4x 1.92TB SAS Enterprise 12Gbps 2.5in Hot-plug SSD<br/>• Quad-Port 10GbE SFP+ / 1GbE RJ45 OCP 3.0 NIC<br/>• Dual 800W Titanium Redundant Power Supply (1+1)<br/>• iDRAC9 Enterprise Remote Management<br/>• 3-Year Dell ProSupport & NBD Onsite Warranty', styles['TableCell']),
         Paragraph('02 Units<br/><i>(Primary & DR)</i>', styles['TableCell']),
         Paragraph('1,550,000.00', styles['TableCellRight']),
         Paragraph('<b>3,100,000.00</b>', styles['TableCellRightBold'])],
    ]
    hw_tbl = Table(hw_table_data, colWidths=[270, 70, 85, 85])
    hw_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(hw_tbl)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph('2. Enterprise System Software & Database Licenses (As per Table 18)', styles['SectionHdr']))
    sw_table_data = [
        [Paragraph('<b>Platform / Software Item</b>', styles['TableHdr']), Paragraph('<b>Description & Support Tenure</b>', styles['TableHdr']), Paragraph('<b>Qty</b>', styles['TableHdr']), Paragraph('<b>Total Price (BDT)</b>', styles['TableHdr'])],
        [Paragraph('<b>VMware vSphere 8 Enterprise Plus</b>', styles['TableCellBold']), Paragraph('Per CPU Socket License with 3-Year Production Support', styles['TableCell']), Paragraph('02 Lic', styles['TableCell']), Paragraph('840,000.00', styles['TableCellRight'])],
        [Paragraph('<b>Red Hat Enterprise Linux (RHEL)</b>', styles['TableCellBold']), Paragraph('Server Standard Subscription (2 Sockets / 2 VMs, 3-Yr Support)', styles['TableCell']), Paragraph('04 Sub', styles['TableCell']), Paragraph('580,000.00', styles['TableCellRight'])],
        [Paragraph('<b>PostgreSQL Enterprise Edition / Oracle 19c</b>', styles['TableCellBold']), Paragraph('Enterprise Database Engine with 3-Year Software Updates & DBA Support', styles['TableCell']), Paragraph('02 Lic', styles['TableCell']), Paragraph('450,000.00', styles['TableCellRight'])],
        [Paragraph('<b>Total Infrastructure & Platform Software Value (Optional)</b>', styles['TableCellBold']), Paragraph('All hardware and system software licenses with 3-Year Support', styles['TableCellBold']), '', Paragraph('<b>BDT 4,970,000.00</b>', styles['TableCellRightBold'])],
    ]
    sw_tbl = Table(sw_table_data, colWidths=[150, 200, 50, 110])
    sw_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#e8f5e9')),
        ('SPAN', (0,-1), (1,-1)),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9e9e9e')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(sw_tbl)
    story.append(Spacer(1, 8))
    
    story.append(create_signature_block(styles))
    doc.build(story)
    print('Generated Hardware_Infrastructure_Quotation_Bank_Asia.pdf successfully!')

if __name__ == '__main__':
    build_financial_proposal()
    build_oem_declaration()
    build_draft_sla()
    build_draft_nda()
    build_training_proposal()
    build_power_of_attorney()
    build_hardware_proposal()
