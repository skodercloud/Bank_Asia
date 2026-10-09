import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as PlatypusImage, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

LOGO_PATH = os.path.join('ref_assets', 'Image23.png')

def get_cover_styles():
    styles = getSampleStyleSheet()
    return {
        'OrgHeader': ParagraphStyle('OrgHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=colors.HexColor('#00875a'), alignment=TA_LEFT),
        'OrgSub': ParagraphStyle('OrgSub', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor('#64748b'), alignment=TA_LEFT),
        'EnvBadge': ParagraphStyle('EnvBadge', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=colors.HexColor('#0d233a'), alignment=TA_CENTER),
        'DocType': ParagraphStyle('DocType', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=24, leading=29, textColor=colors.HexColor('#0d233a'), alignment=TA_LEFT),
        'DocSub': ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=15, textColor=colors.HexColor('#475569'), alignment=TA_LEFT),
        'ProjectTitle': ParagraphStyle('ProjectTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, leading=18, textColor=colors.HexColor('#0f172a'), alignment=TA_LEFT),
        'ProjectSub': ParagraphStyle('ProjectSub', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=colors.HexColor('#334155'), alignment=TA_LEFT),
        'MetaLabel': ParagraphStyle('MetaLabel', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=13, textColor=colors.HexColor('#0d233a')),
        'MetaVal': ParagraphStyle('MetaVal', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor('#1e293b')),
        'MetaValBold': ParagraphStyle('MetaValBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=colors.HexColor('#0f172a')),
        'Notice': ParagraphStyle('Notice', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=colors.HexColor('#c00000'), alignment=TA_CENTER),
        'FooterText': ParagraphStyle('FooterText', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor('#94a3b8'), alignment=TA_CENTER),
    }

def create_cover_page(filename, doc_type_title, doc_subtitle, env_badge_text, is_confidential=False, accent_color='#0d233a'):
    styles = get_cover_styles()
    
    # Target A4: 595.27 x 841.89 pt
    # Clean margins: 48 pt left/right, 45 pt top/bottom
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=48,
        rightMargin=48,
        topMargin=45,
        bottomMargin=45
    )
    
    story = []
    
    # 1. Top Bar: Logo & Company Name
    logo_img = PlatypusImage(LOGO_PATH, width=120, height=40) if os.path.exists(LOGO_PATH) else Paragraph("<b>SKODER</b>", styles['OrgHeader'])
    header_text = Paragraph("<b>SKODER TECHNOLOGIES</b><br/><font color='#64748b' size='7.5'>E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207<br/>BIN: 002855793-0401 | Trade: TRAD/DNCC/056205/2022</font>", styles['OrgSub'])
    
    top_tbl = Table([[logo_img, header_text]], colWidths=[150, 349])
    top_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(top_tbl)
    
    # Accent dividing line
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor(accent_color), spaceBefore=2, spaceAfter=22))
    
    # 2. Envelope / Dossier Badge
    badge_bg = '#f1f5f9'
    badge_border = '#cbd5e1'
    if is_confidential:
        badge_bg = '#fef2f2'
        badge_border = '#fca5a5'
        
    badge_tbl = Table([[Paragraph(f"<b>{env_badge_text}</b>", ParagraphStyle('Bdg', parent=styles['EnvBadge'], textColor=colors.HexColor('#b91c1c' if is_confidential else accent_color)))]], colWidths=[499])
    badge_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(badge_bg)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(badge_border)),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(badge_tbl)
    story.append(Spacer(1, 24))
    
    # 3. Main Document Title & Subtitle
    story.append(Paragraph(doc_type_title, styles['DocType']))
    story.append(Spacer(1, 6))
    story.append(Paragraph(doc_subtitle, styles['DocSub']))
    story.append(Spacer(1, 20))
    
    # 4. Project Details Box
    proj_box_data = [
        [Paragraph("<b>PROJECT:</b>", styles['MetaLabel']),
         Paragraph("<b>Procurement, Supply, Implementation, Integration, and Support of a Litigation Management System (LMS)</b><br/><font color='#64748b' size='8'>Including Software Licenses and Annual Maintenance Contract (AMC)</font>", styles['ProjectTitle'])],
        [Paragraph("<b>TENDER REF:</b>", styles['MetaLabel']),
         Paragraph("<b>RFP/BID Schedule for LMS — Version 1.0</b> (RFP_LMS Bank Asia_v0.3)", styles['MetaValBold'])],
        [Paragraph("<b>INVITATION BY:</b>", styles['MetaLabel']),
         Paragraph("<b>Bank Asia PLC</b> (ICT Division & Logistics and Support Services Division)", styles['MetaVal'])],
        [Paragraph("<b>SUBMISSION DATE:</b>", styles['MetaLabel']),
         Paragraph("<b>October 11, 2026 | Deadline: 02:30 PM (Opening: 03:00 PM)</b>", styles['MetaValBold'])],
    ]
    proj_tbl = Table(proj_box_data, colWidths=[110, 389])
    proj_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('LINEBELOW', (0,0), (-1,-2), 0.5, colors.HexColor('#edf2f7')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(proj_tbl)
    story.append(Spacer(1, 24))
    
    # 5. Dual Column: Submitted To vs Submitted By
    col_to = [
        Paragraph("<b>SUBMITTED TO:</b>", styles['MetaLabel']),
        Spacer(1, 4),
        Paragraph("<b>Logistics & Support Services Division (LSSD)</b><br/>Bank Asia PLC<br/>Corporate Office, Bank Asia Tower (1st Floor)<br/>32 & 34, Kazi Nazrul Islam Avenue, Karwan Bazar<br/>Dhaka-1215, Bangladesh<br/><b>Attention:</b> Head of ICT Division", styles['MetaVal']),
    ]
    
    col_by = [
        Paragraph("<b>SUBMITTED BY:</b>", styles['MetaLabel']),
        Spacer(1, 4),
        Paragraph("<b>SKODER TECHNOLOGIES</b><br/>E-14/X, ICT Tower (14th Floor)<br/>Agargaon, Dhaka-1207, Bangladesh<br/><b>Contact:</b> +88 01750 726094 | +88 01979 891996<br/><b>Email:</b> contact@skoder.co | abir.skoder@gmail.com<br/><b>Web:</b> www.skoder.co", styles['MetaVal']),
    ]
    
    meta_columns = Table([[col_to, col_by]], colWidths=[244, 255])
    meta_columns.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#f8fafc')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (0,0), 1, colors.HexColor('#e2e8f0')),
        ('BOX', (1,0), (1,0), 1, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_columns)
    story.append(Spacer(1, 22))
    
    # 6. Copy Status & Validity Box
    copy_box = [
        [Paragraph("<b>Copy Status:</b> [ &nbsp; ] ORIGINAL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ &nbsp; ] DUPLICATE COPY", styles['MetaValBold']),
         Paragraph("<b>Bid Validity:</b> 12 Months (Valid up to October 11, 2027)", ParagraphStyle('Rt', parent=styles['MetaVal'], alignment=TA_RIGHT))]
    ]
    copy_tbl = Table(copy_box, colWidths=[260, 239])
    copy_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEABOVE', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(copy_tbl)
    
    if is_confidential:
        story.append(Spacer(1, 14))
        story.append(Paragraph("<b>STRICTLY CONFIDENTIAL — TO BE OPENED ONLY BY THE PURCHASE / TENDER COMMITTEE</b>", styles['Notice']))
    
    # Footer notice
    story.append(Spacer(1, 20))
    story.append(Paragraph("Skoder Technologies • Proprietary & Confidential • Bank Asia LMS Tender Submission 2026", styles['FooterText']))
    
    doc.build(story)
    print(f"Generated cover page: {filename}")

if __name__ == '__main__':
    # 1. Master Tender Submission Cover Page
    create_cover_page(
        filename='00_Tender_Submission_Master_Cover_Page.pdf',
        doc_type_title='TENDER SUBMISSION DOSSIER',
        doc_subtitle='Comprehensive Technical & Financial Proposal Submission',
        env_badge_text='MASTER OUTER DOSSIER — CONTAINS SEALED ENVELOPE 1 & ENVELOPE 2',
        is_confidential=False,
        accent_color='#0d233a'
    )
    
    # 2. Technical Proposal Cover Page
    create_cover_page(
        filename='01_Technical_Proposal_Cover_Page.pdf',
        doc_type_title='TECHNICAL PROPOSAL',
        doc_subtitle='Volume 1: Technical & Functional Response, Implementation Plan, Team & Eligibility',
        env_badge_text='ENVELOPE 1 — TECHNICAL PROPOSAL (ORIGINAL / DUPLICATE)',
        is_confidential=False,
        accent_color='#00875a'
    )
    
    # 3. Financial Proposal Cover Page
    create_cover_page(
        filename='02_Financial_Proposal_Cover_Page.pdf',
        doc_type_title='FINANCIAL PROPOSAL',
        doc_subtitle='Volume 2: Commercial Quotation, AMC Schedules, Bid Security & Price Undertaking',
        env_badge_text='ENVELOPE 2 — FINANCIAL PROPOSAL (STRICTLY CONFIDENTIAL)',
        is_confidential=True,
        accent_color='#b91c1c'
    )
