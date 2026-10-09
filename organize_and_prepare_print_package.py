import os, shutil
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from skoder_pdf_builder import build_pdf_document, get_signature_block, FONT_NORMAL, FONT_BOLD

def create_pay_order_enclosure():
    story = []
    
    title_p = Paragraph(f"<font fontName='{FONT_BOLD}' size=13 color='#0d47a1'>ORIGINAL BID SECURITY (PAY ORDER) ENCLOSURE</font>", None)
    sub_p = Paragraph(f"<font fontName='{FONT_NORMAL}' size=8.5 color='#475569'>Procurement, Supply, Implementation, Integration, and Support of Litigation Management System (LMS)<br/>Tender Ref: RFP_LMS Bank Asia_v0.3 | Client: Bank Asia PLC</font>", None)
    
    story.append(title_p)
    story.append(sub_p)
    story.append(Spacer(1, 10))
    
    intro = Paragraph(f"<font fontName='{FONT_NORMAL}' size=8.5 color='#1e293b'>In strict compliance with RFP Section 6, Clause 214 and Section 10 (Earnest Money Schedule), <b>Skoder Technologies</b> hereby furnishes the original refundable Bid Security amounting to <b>BDT 25,000/-</b> in favor of <b>'Bank Asia PLC'</b>:</font>", None)
    story.append(intro)
    story.append(Spacer(1, 8))
    
    po_data = [
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Bid Security Type:</font>", None), Paragraph(f"<font fontName='{FONT_NORMAL}' size=8 color='#1e293b'>Payment Order (Pay Order)</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Pay Order No. & Date:</font>", None), Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0d47a1'>SJIBL/MIR/PO/2026/04812, Dated: 11 October, 2026</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Amount in Figures:</font>", None), Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>BDT 25,000/-</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Amount in Words:</font>", None), Paragraph(f"<font fontName='{FONT_NORMAL}' size=8 color='#1e293b'>Taka Twenty-Five Thousand Only</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Issuing Bank:</font>", None), Paragraph(f"<font fontName='{FONT_NORMAL}' size=8 color='#1e293b'>Shahjalal Islami Bank PLC</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Issuing Branch:</font>", None), Paragraph(f"<font fontName='{FONT_NORMAL}' size=8 color='#1e293b'>Mirpur Branch, Dhaka</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Beneficiary:</font>", None), Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Bank Asia PLC</font>", None)],
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=8 color='#0f172a'>Validity Tenure:</font>", None), Paragraph(f"<font fontName='{FONT_NORMAL}' size=8 color='#1e293b'>12 Months (Valid up to October 11, 2027)</font>", None)],
    ]
    
    t = Table(po_data, colWidths=[130, 357])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f8fafc')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    
    # Clip attachment area box
    clip_box = [
        [Paragraph(f"<font fontName='{FONT_BOLD}' size=9 color='#64748b'>[ AFFIX / STAPLE ORIGINAL PHYSICAL PAY ORDER LEAF HERE ]<br/><font size=7.5 color='#94a3b8'>(Shahjalal Islami Bank PLC • BDT 25,000/- • Pay Order No. SJIBL/MIR/PO/2026/04812)</font></font>", None)]
    ]
    clip_t = Table(clip_box, colWidths=[487], rowHeights=[140])
    clip_t.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(clip_t)
    story.append(Spacer(1, 10))
    
    story.append(get_signature_block())
    
    out_path = 'Original_Pay_Order_Enclosure_Sheet.pdf'
    build_pdf_document(out_path, story)
    print(f"Generated: {out_path}")

def organize_folders():
    base_dir = 'FINAL_PRINT_READY'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
        
    m_dir = os.path.join(base_dir, '00_MASTER_ENVELOPE')
    t_dir = os.path.join(base_dir, 'ENVELOPE_1_TECHNICAL_PROPOSAL')
    f_dir = os.path.join(base_dir, 'ENVELOPE_2_FINANCIAL_PROPOSAL')
    e_dir = os.path.join(base_dir, 'POST_SUBMISSION_EMAIL')
    
    for d in [m_dir, t_dir, f_dir, e_dir]:
        os.makedirs(d, exist_ok=True)
        
    # Copy Master Envelope docs
    shutil.copy('00_Tender_Submission_Master_Cover_Page.pdf', os.path.join(m_dir, '00_Master_Outer_Dossier_Cover_Page.pdf'))
    
    # Copy Envelope 1 (Technical) docs in exact printing sequence
    tech_files = [
        ('01_Technical_Proposal_Cover_Page.pdf', '01_Technical_Proposal_Cover_Page.pdf'),
        ('BANK_ASIA_Cover_Letter.pdf', '02_Submission_Cover_Letter_Skoder_Pad.pdf'),
        ('Power_of_Attorney_Authorization_Letter.pdf', '03_Power_of_Attorney_Authorization_Letter.pdf'),
        ('OEM_Developer_Declaration_Skoder.pdf', '04_OEM_Developer_Declaration_Letter.pdf'),
        ('02_Project_Team_Structure_and_Matrix_Bank_Asia.pdf', '05_Project_Team_Structure_and_Matrix.pdf'),
        ('Implementation_Plan_BA.pdf', '06_Implementation_Plan_and_Gantt_Chart.pdf'),
        ('Draft_SLA_Bank_Asia_LMS.pdf', '07_Draft_Service_Level_Agreement_SLA.pdf'),
        ('Draft_NDA_Bank_Asia_LMS.pdf', '08_Draft_Non_Disclosure_Agreement_NDA.pdf'),
        ('RFP_LMS Bank Asia_v0.3.docx', '09_RFP_LMS_Technical_and_Functional_Response.docx'),
        ('Skoder Profile v4.0_20260802_112157_0000_compressed.pdf', '10_Skoder_Company_Profile_v4.0.pdf'),
        ('Skoder Client List.pdf', '11_Skoder_Client_List.pdf'),
        ('03_Compiled_Past_Experience_and_Certificates_Bank_Asia.pdf', '12_Compiled_Past_Experience_and_Certificates.pdf'),
        ('04_Compiled_Key_Personnel_CVs_Bank_Asia.pdf', '13_Compiled_Key_Personnel_CVs.pdf'),
    ]
    for src, dst in tech_files:
        if os.path.exists(src):
            shutil.copy(src, os.path.join(t_dir, dst))
            print(f"Copied to Tech Proposal: {dst}")

    # Copy Envelope 2 (Financial) docs in exact printing sequence
    fin_files = [
        ('02_Financial_Proposal_Cover_Page.pdf', '01_Financial_Proposal_Cover_Page.pdf'),
        ('Financial_Proposal_Bank_Asia.pdf', '02_Financial_Proposal_and_Undertaking.pdf'),
        ('Original_Pay_Order_Enclosure_Sheet.pdf', '03_Original_Pay_Order_Enclosure_Sheet.pdf'),
        ('Training_Proposal_and_Plan_Bank_Asia.pdf', '04_Training_Proposal_and_Methodology.pdf'),
        ('Hardware_Infrastructure_Quotation_Bank_Asia.pdf', '05_Hardware_Infrastructure_Quotation.pdf'),
        ('RFP_LMS Bank Asia_v0.3.docx', '06_RFP_LMS_Financial_Schedules_Section_9_and_10.docx'),
    ]
    for src, dst in fin_files:
        if os.path.exists(src):
            shutil.copy(src, os.path.join(f_dir, dst))
            print(f"Copied to Financial Proposal: {dst}")

    # Copy Post Submission Email file
    excel_file = 'Technical_and_Functional_Compliance_Matrix_Bank_Asia_LMS.xlsx'
    if os.path.exists(excel_file):
        shutil.copy(excel_file, os.path.join(e_dir, excel_file))
        print(f"Copied to Post Submission Email: {excel_file}")

    print("Finished organizing FINAL_PRINT_READY package successfully!")

if __name__ == '__main__':
    create_pay_order_enclosure()
    organize_folders()
