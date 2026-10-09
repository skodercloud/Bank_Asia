import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

pdf_path = 'BANK_ASIA_Cover_Letter.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=50,
    leftMargin=50,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

header_title = ParagraphStyle(
    'HeaderTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#0d47a1')
)

header_sub = ParagraphStyle(
    'HeaderSub',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=11,
    textColor=colors.HexColor('#424242')
)

body = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#212121')
)

bold_body = ParagraphStyle(
    'BoldBody',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#212121')
)

bullet = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12.5,
    leftIndent=12,
    textColor=colors.HexColor('#212121')
)

story = []

# Header Table
hdr_left = Paragraph('<b>SKODER TECHNOLOGIES</b><br/><font size="7.5" color="#555555">E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207<br/>BIN# 002855793-0401 | Trade# TRAD/DNCC/056205/2022</font>', header_title)
hdr_right = Paragraph('<font size="7.5" color="#555555">+88 01750 726094 | +88 01979 891996<br/>contact@skoder.co | abir.skoder@gmail.com<br/>www.skoder.co</font>', ParagraphStyle('HdrR', parent=header_sub, alignment=2))

hdr_table = Table([[hdr_left, hdr_right]], colWidths=[330, 182])
hdr_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LINEBELOW', (0,0), (-1,-1), 1.5, colors.HexColor('#0d47a1')),
]))
story.append(hdr_table)
story.append(Spacer(1, 10))

# Date & Recipient
story.append(Paragraph('<b>Date:</b> October 11, 2026', body))
story.append(Spacer(1, 5))
story.append(Paragraph('To<br/><b>The Head of ICT Division</b><br/>Bank Asia PLC<br/>Corporate Office, Bank Asia Tower (1st Floor)<br/>32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka-1215, Bangladesh', body))
story.append(Spacer(1, 7))

# Subject
story.append(Paragraph('<b>Subject: Bid Submission for Procurement, Supply, Implementation, Integration, and Support of Litigation Management System (LMS)</b>', ParagraphStyle('Subj', parent=bold_body, fontSize=9.5, textColor=colors.HexColor('#0d47a1'))))
story.append(Paragraph('<b>Ref:</b> RFP/BID Schedule for Litigation Management System (LMS) – Version 1.0 (RFP_LMS Bank Asia_v0.3)', body))
story.append(Spacer(1, 7))

# Body text
p1 = 'Dear Sir/Madam,<br/><br/>Having examined the Request for Proposal (RFP) document for the <b>Litigation Management System (LMS)</b>, we, <b>Skoder Technologies</b>, hereby submit our proposal to supply, implement, integrate, and support the proposed solution in full compliance with your requirements.'
story.append(Paragraph(p1, body))
story.append(Spacer(1, 6))

p2 = 'Our enterprise LMS is a 100% proprietary software platform developed by Skoder Technologies, purpose-engineered to provide 360-degree coverage for case tracking (Artha Rin Adalat, NI Act 138, Civil & Criminal suits), automated legal notice generation, auction management, Write-Off Account (WOA) tracking, panel lawyer/advocate management, automated hearing calendar alerts, Core Banking System (CBS) integration, and regulatory reporting for Bangladesh Bank.'
story.append(Paragraph(p2, body))
story.append(Spacer(1, 6))

story.append(Paragraph('We hereby confirm the following commitments:', bold_body))
story.append(Spacer(1, 3))

b1 = '• <b>Bid Security:</b> Enclosed is <b>Pay Order No. SJIBL/MIR/PO/2026/04812</b> dated <b>October 11, 2026</b> for <b>BDT 25,000/-</b> (Taka Twenty-Five Thousand Only) issued by <b>Shahjalal Islami Bank PLC, Mirpur Branch, Dhaka</b> in favor of <b>Bank Asia PLC</b> (valid for 12 months).'
b2 = '• <b>Offer Validity:</b> Our commercial quotation and terms remain valid for <b>12 (twelve) months</b> from the bid opening date (up to October 11, 2027).'
b3 = '• <b>Compliance & Timeline:</b> We accept all terms, conditions, functional requirements, and technical specifications outlined in the RFP document and commit to delivering the complete project within <b>16 weeks (112 days)</b> upon contract award.'
b4 = '• <b>Warranty & AMC:</b> We provide <b>03 (three) years full warranty</b> followed by <b>03 (three) years Annual Maintenance Contract (AMC)</b> at guaranteed equal yearly rates with 24/7/365 support.'
story.append(Paragraph(b1, bullet))
story.append(Paragraph(b2, bullet))
story.append(Paragraph(b3, bullet))
story.append(Paragraph(b4, bullet))
story.append(Spacer(1, 6))

p3 = 'All required technical responses, financial schedules, eligibility documents, implementation methodology, draft SLA & NDA, and client references are attached in the prescribed formats.'
story.append(Paragraph(p3, body))
story.append(Spacer(1, 10))

story.append(Paragraph('Sincerely,', body))
story.append(Spacer(1, 2))

# Signature & Seal block
sig_img = Image('assets/abir_signature.jpg', width=90, height=52)
seal_img = Image('assets/skoder_seal.jpg', width=60, height=60)

sig_text = Paragraph('<b>K. M. ABIR MAHMUD</b><br/>Chief Executive Officer<br/><b>SKODER TECHNOLOGIES</b><br/>Cell: +88 01750 726094', ParagraphStyle('SigText', parent=body, fontSize=8.5, leading=11))

sig_table = Table([[sig_img, seal_img], [sig_text, '']], colWidths=[180, 332])
sig_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story.append(sig_table)

doc.build(story)
print('Generated BANK_ASIA_Cover_Letter.pdf successfully')
