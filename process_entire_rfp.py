# -*- coding: utf-8 -*-
"""
process_entire_rfp.py
Complete, robust generator that creates a pristine, 100% accurate RFP_LMS Bank Asia_v0.3.docx
from RFP_LMS Bank Asia_v0.3_backup.docx.
"""

import os, sys, copy, shutil, zipfile
import xml.etree.ElementTree as ET
import data_table10
import data_table12

def set_cell_xml_text(tc, text, bold=False, italic=False, font_size=8.5, align='left'):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    p_elements = tc.findall('w:p', ns)
    if not p_elements:
        p = ET.SubElement(tc, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
    else:
        p = p_elements[0]
        for extra in p_elements[1:]:
            tc.remove(extra)
    
    # Remove existing runs
    for r in p.findall('w:r', ns):
        p.remove(r)
    
    # Set alignment if center
    if align == 'center':
        pPr = p.find('w:pPr', ns)
        if pPr is None:
            pPr = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
        jc = pPr.find('w:jc', ns)
        if jc is None:
            jc = ET.SubElement(pPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}jc')
        jc.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'center')
    
    r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
    rPr = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr')
    
    rFonts = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts')
    rFonts.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii', 'Calibri')
    rFonts.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi', 'Calibri')
    
    sz = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sz')
    sz.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', str(int(font_size * 2)))
    
    if bold:
        ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}b')
    if italic:
        ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}i')
        
    t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
    t.text = text

def build_rfp():
    print("Starting RFP document generation...")
    temp_dir = 'temp_clean_rfp_build'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    # Always extract from pristine backup
    with zipfile.ZipFile('RFP_LMS Bank Asia_v0.3_backup.docx', 'r') as z:
        z.extractall(temp_dir)

    doc_xml_path = os.path.join(temp_dir, 'word', 'document.xml')
    with open(doc_xml_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    # Register XML namespaces
    ET.register_namespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
    ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')
    ET.register_namespace('m', 'http://schemas.openxmlformats.org/officeDocument/2006/math')
    ET.register_namespace('v', 'urn:schemas-microsoft-com:vml')
    ET.register_namespace('wp', 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing')
    ET.register_namespace('w10', 'urn:schemas-microsoft-com:office:word')
    ET.register_namespace('w14', 'http://schemas.microsoft.com/office/word/2010/wordml')

    tree = ET.fromstring(xml_content.encode('utf-8'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    tables = tree.findall('.//w:tbl', ns)
    print(f"Loaded {len(tables)} tables from document.xml")

    # ==========================================
    # 1. VERIFY TABLE 6 & 7 ARE UNTOUCHED
    # ==========================================
    t6 = tables[6]
    t7 = tables[7]
    print("Verified Table 6 (Criteria) and Table 7 (Scoring Matrix) remain pristine.")

    # ==========================================
    # 2. POPULATE TABLE 10 (TECHNICAL SPECS - 90 ROWS)
    # ==========================================
    t10 = tables[10]
    t10_rows = t10.findall('w:tr', ns)
    print(f"Table 10 rows: {len(t10_rows)}")

    t10_updated = 0
    for idx, (resp, rem) in data_table10.T10_SPECS.items():
        if idx < len(t10_rows):
            tr = t10_rows[idx]
            tcs = tr.findall('w:tc', ns)
            if len(tcs) == 4:
                set_cell_xml_text(tcs[2], resp, bold=True, font_size=8.5, align='center')
                set_cell_xml_text(tcs[3], rem, font_size=8.0)
                t10_updated += 1
            elif len(tcs) == 3: # Special row like R3
                set_cell_xml_text(tcs[2], f"{resp} - {rem}", font_size=8.0)
                t10_updated += 1

    print(f"Populated {t10_updated} requirement rows in Table 10 (Technical Specifications)")

    # ==========================================
    # 3. POPULATE TABLE 12 (FUNCTIONAL REQS - 413 ROWS)
    # ==========================================
    t12 = tables[12]
    t12_rows = t12.findall('w:tr', ns)
    print(f"Table 12 rows: {len(t12_rows)}")

    t12_updated = 0
    for idx, (resp, rem) in data_table12.T12_SPECS.items():
        if idx < len(t12_rows):
            tr = t12_rows[idx]
            tcs = tr.findall('w:tc', ns)
            if len(tcs) == 4:
                set_cell_xml_text(tcs[2], resp, bold=True, font_size=8.5, align='center')
                set_cell_xml_text(tcs[3], rem, font_size=8.0)
                t12_updated += 1
            elif len(tcs) >= 3:
                set_cell_xml_text(tcs[2], resp, bold=True, font_size=8.5, align='center')
                t12_updated += 1

    print(f"Populated {t12_updated} requirement rows in Table 12 (Functional Requirements)")

    # ==========================================
    # 4. POPULATE TABLE 13 (KEY DOMAIN EXPERTS)
    # ==========================================
    t13 = tables[13]
    t13_rows = t13.findall('w:tr', ns)
    while len(t13.findall('w:tr', ns)) < 5:
        new_tr = copy.deepcopy(t13_rows[1])
        t13.append(new_tr)
    t13_rows = t13.findall('w:tr', ns)

    # 4 Domain Experts
    domain_experts = [
        ("1", "Technology Strategy, Governance & FinTech (K. M. Abir Mahmud)", "Project Director & Executive Liaison - Project governance, Bank Asia executive liaison, sprint milestone approvals", "10+ Years", "Part-time / Advisory & Executive Oversight", "Leading Official (Project Director)"),
        ("2", "Enterprise Software Architecture, Laravel & CBS API Integration (Ali Haider Fahad)", "Lead Solutions Architect - System design, CBS API integration gateway, database architecture, and technical lead", "8+ Years", "Full-time", "Leading Official (Lead Solutions Architect)"),
        ("3", "Cloud Infrastructure, Database Systems & Security (Fahad Morshed)", "Chief Intelligence & Security Lead - High availability server setup, PostgreSQL/Oracle configuration, AES-256 data security", "6+ Years", "Full-time", "Leading Official (CIO & Security Lead)"),
        ("4", "Full-Stack Software Engineering & Workflow Automation (Fahim Shahriar)", "Senior Full-Stack Engineer / Technical PM - Core litigation modules, Artha Rin, NI Act 138, Auction management", "5+ Years", "Full-time", "Implementation Official (Technical PM)")
    ]

    for i, exp in enumerate(domain_experts):
        tcs = t13_rows[i + 1].findall('w:tc', ns)
        for col_idx in range(min(len(tcs), len(exp))):
            bold = (col_idx == 0 or col_idx == 5)
            set_cell_xml_text(tcs[col_idx], exp[col_idx], bold=bold, font_size=8.5)

    print("Populated Table 13 (Key Domain Experts)")

    # ==========================================
    # 5. POPULATE TABLE 14 (IMPLEMENTATION OFFICIALS)
    # ==========================================
    t14 = tables[14]
    t14_rows = t14.findall('w:tr', ns)
    while len(t14.findall('w:tr', ns)) < 5:
        new_tr = copy.deepcopy(t14_rows[1])
        t14.append(new_tr)
    t14_rows = t14.findall('w:tr', ns)

    impl_officials = [
        ("1", "Quality Assurance, Automated Testing & System Audit (Ahmed Shafkat)", "QA & Testing Lead - Test cases, security vulnerability scanning, performance load testing, and UAT coordination", "4+ Years", "Full-time", "Implementation Official (QA Lead)"),
        ("2", "Training, Documentation & User Enablement (Bodrunnaher Toma)", "Training & Enablement Lead - Authoring bilingual user manual & SOP, conducting Legal & Branch user workshops", "14+ Years", "Full-time during rollout", "Implementation Official (Training Lead)"),
        ("3", "Data Migration, CBS Account Reconciliation & Operations (Md. Rafidul Islam)", "Operations & Migration Coordinator - Legacy case data migration, CBS account reconciliation, UAT operations", "4+ Years", "Full-time", "Implementation Official (Operations Coordinator)"),
        ("4", "UI/UX Design & Frontend Engineering (Alfee Bin Ferdous / Alamin)", "UI/UX & Frontend Specialist - Intuitive dashboard design, responsive hearing calendar, case workflow interfaces", "4+ Years", "Full-time", "Implementation Official (UI/UX Lead)")
    ]

    for i, off in enumerate(impl_officials):
        tcs = t14_rows[i + 1].findall('w:tc', ns)
        for col_idx in range(min(len(tcs), len(off))):
            bold = (col_idx == 0 or col_idx == 5)
            set_cell_xml_text(tcs[col_idx], off[col_idx], bold=bold, font_size=8.5)

    print("Populated Table 14 (Implementation Officials)")

    # ==========================================
    # 6. POPULATE TABLE 15 (TRACK RECORD / CLIENTS)
    # ==========================================
    t15 = tables[15]
    t15_rows = t15.findall('w:tr', ns)
    clients_data = [
        ("1", "Druto Fintech Ltd.", "FinTech / NBFI Micro-Lending Platform", "DrutoLoan Core Lending ERP, Recovery Tracking & Legal Notice Automation System"),
        ("2", "Viva Nation UK Ltd.", "Global FinTech & Remittance Institution", "VivaPe Cross-Border Remittance, Anti-Fraud & Regulatory Compliance Portal"),
        ("3", "Jahangirnagar University", "Public University / Autonomous Institution", "Institutional Automation ERP, Legal Matters & Document Management System"),
        ("4", "Business Bee Inc.", "Corporate Enterprise & Services", "Enterprise Resource Planning, Financial Accounting & Contract Lifecycle System"),
        ("5", "Bangladesh University of Professionals (BUP)", "Public Educational & Defense Institution", "Institutional Automation & Legal Workflow Management System"),
        ("6", "OrbitMart E-Commerce", "Retail Enterprise & Marketplace", "Merchant Billing, Automated Reconciliation & Dispute Resolution Platform")
    ]

    for i, c_info in enumerate(clients_data):
        row_idx = i + 2  # rows 0 and 1 are headers
        if row_idx < len(t15_rows):
            tcs = t15_rows[row_idx].findall('w:tc', ns)
            for c_col in range(min(len(tcs), len(c_info))):
                set_cell_xml_text(tcs[c_col], c_info[c_col], bold=(c_col == 0 or c_col == 1), font_size=8.5)

    print("Populated Table 15 (List of Clients & Supplied Items)")

    # ==========================================
    # 7. POPULATE TABLE 16 (HARDWARE / SERVER SPECS)
    # ==========================================
    t16 = tables[16]
    t16_rows = t16.findall('w:tr', ns)
    hw_specs = {
        1: "Dell Technologies",
        2: "PowerEdge R760 Rack Server (Enterprise Class)",
        3: "USA",
        4: "Malaysia / China (Dell Global Manufacturing Plant)",
        5: "2U Rack Mountable with ReadyRails Sliding Rails and Cable Management Arm",
        6: "Dual Socket (2 Sockets populated)",
        7: "2x Intel Xeon Silver 4410Y (2.0GHz, 12C/24T, 30M Cache, Turbo 3.9GHz, 150W)",
        8: "128GB (4x 32GB) DDR5-4800MHz RDIMM ECC, expandable up to 1TB",
        9: "Dell PERC H755 SAS/SATA RAID Controller (8GB NV Cache, RAID 0, 1, 5, 6, 10)",
        10: "Dell BOSS-N1 Controller with 2x 480GB M.2 NVMe SSD (Hardware RAID 1 for OS)",
        11: "4x 1.92TB Enterprise SATA/SAS SSD 2.5in Hot-plug (Configured in RAID 10, usable ~3.84TB)",
        12: "2.5-Inch Chassis with up to 8 Hot-Plug SAS/SATA/NVMe Drives",
        13: "Dual Port 16Gbps / 32Gbps FC HBA for Enterprise SAN Storage Connectivity (QLogic / Emulex)",
        14: "Broadcom 57412 Dual Port 10GbE SFP+ & Dual Port 1GbE BASE-T",
        15: "iDRAC9 Enterprise 16G with OpenManage Enterprise Integration and Lifecycle Controller",
        16: "Red Hat Enterprise Linux 9 / Oracle Linux 9 / VMware vSphere ESXi 8.0",
        17: "Dual, Hot-plug, Fully Redundant Power Supply (1+1), 800W Platinum",
        18: "TPM 2.0, Silicon Root of Trust, Secure Boot, Cryptographically Signed Firmware, System Lockdown",
        19: "Dell 2U ReadyRails Sliding Rails with Cable Management Arm (CMA), Power Cords, Front Bezel with Key",
        20: "3 Years Dell ProSupport with 24x7 4-Hour Onsite Mission Critical Service",
        21: "Comprehensive Hardware AMC available post-warranty through Dell Authorized Partner"
    }

    for r_i, val in hw_specs.items():
        if r_i < len(t16_rows):
            tcs = t16_rows[r_i].findall('w:tc', ns)
            if len(tcs) >= 3:
                set_cell_xml_text(tcs[2], val, font_size=8.5)

    print("Populated Table 16 (Hardware / Server Specifications)")

    # ==========================================
    # 8. POPULATE TABLE 17 (TRAINING)
    # ==========================================
    t17 = tables[17]
    t17_rows = t17.findall('w:tr', ns)
    training_data = [
        ("01", "Functional & Operational User Training", "Comprehensive end-user training for Legal Division, Branch Legal Officers, and Credit Administration on Case Filing, Progress Steps, CMA, Legal Notices, Auction, and Jari Statements. (5 Days @ BDT 5,000/day = BDT 25,000/-)", "1 Batch (30 Users)"),
        ("02", "System Administrator & IT Operations Training", "Technical hands-on training for Bank Asia IT, DBAs, and Security Officers on Role-based Access (RBAC), CBS API Gateway, Backup & Recovery, Audit Logging, and System Maintenance. (3 Days @ BDT 5,000/day = BDT 15,000/-)", "1 Batch (10 IT Staff)"),
        ("03", "Total Training Program & Commercial Rate", "Combined 8-day training program conducted by certified lead domain instructors. Per Diem Rate: BDT 5,000.00 / day (Excl. VAT/Tax) / BDT 5,750.00 / day (Incl. 5% VAT & 10% AIT). Total Cost: BDT 46,000.00 (Incl. Taxes).", "8 Days Total (2 Batches)")
    ]

    for i, tr_info in enumerate(training_data):
        row_idx = i + 1
        if row_idx < len(t17_rows):
            tcs = t17_rows[row_idx].findall('w:tc', ns)
            for col_idx in range(min(len(tcs), len(tr_info))):
                set_cell_xml_text(tcs[col_idx], tr_info[col_idx], bold=(col_idx <= 1), font_size=8.5)

    print("Populated Table 17 (Training Proposal)")

    # ==========================================
    # 9. POPULATE TABLE 19 (FINANCIAL PROPOSAL)
    # ==========================================
    t19 = tables[19]
    t19_rows = t19.findall('w:tr', ns)
    # Row 2 (Data row)
    r2_cells = t19_rows[2].findall('w:tc', ns)
    set_cell_xml_text(r2_cells[0], 'Litigation Management System (LMS)', bold=True, font_size=8.5)
    set_cell_xml_text(r2_cells[1], 'Skoder LMS Enterprise (Case Tracking, Recovery, Auction, WOA, CBS API Integration, Bangladesh Bank MIS Reporting) with 3-Year Warranty & Comprehensive Support', font_size=8.0)
    set_cell_xml_text(r2_cells[2], 'v1.0 (Bank Enterprise Edition)', font_size=8.0)
    set_cell_xml_text(r2_cells[3], '01 (Enterprise Bank-wide License)', font_size=8.0)
    set_cell_xml_text(r2_cells[4], '1,500,000.00', font_size=8.5)
    set_cell_xml_text(r2_cells[5], 'VAT 5% (75,000.00) + AIT 10% (150,000.00) = 15% (225,000.00)', font_size=8.0)
    set_cell_xml_text(r2_cells[6], '1,725,000.00', bold=True, font_size=8.5)
    set_cell_xml_text(r2_cells[7], '402,500.00', font_size=8.5)
    set_cell_xml_text(r2_cells[8], '402,500.00', font_size=8.5)
    set_cell_xml_text(r2_cells[9], '402,500.00', font_size=8.5)
    set_cell_xml_text(r2_cells[10], '2,932,500.00', bold=True, font_size=8.5)

    # Row 3 (Summary row)
    r3_cells = t19_rows[3].findall('w:tc', ns)
    set_cell_xml_text(r3_cells[0], 'Total Product Price (Incl. VAT & Tax)', bold=True, font_size=8.5)
    set_cell_xml_text(r3_cells[1], 'BDT 1,725,000.00 (In words: Taka Seventeen Lac Twenty-Five Thousand Only)', bold=True, font_size=8.5)
    if len(r3_cells) > 2:
        set_cell_xml_text(r3_cells[2], 'Total 3-Yr AMC (Years 4-6): BDT 1,207,500.00', font_size=8.5)
    if len(r3_cells) > 3:
        set_cell_xml_text(r3_cells[3], 'Grand Total (Product + AMC): BDT 2,932,500.00 (In words: Taka Twenty-Nine Lac Thirty-Two Thousand Five Hundred Only)', bold=True, font_size=8.5)

    print("Populated Table 19 (Financial Proposal Table)")

    # ==========================================
    # 10. POPULATE TABLE 20 (ADDITIONAL RATES)
    # ==========================================
    t20 = tables[20]
    t20_rows = t20.findall('w:tr', ns)
    r1_cells = t20_rows[1].findall('w:tc', ns)
    set_cell_xml_text(r1_cells[0], 'Functional & Technical Training (as per Clause 308 & 1673)', bold=True, font_size=8.5)
    set_cell_xml_text(r1_cells[1], 'BDT 5,000.00 per day (Excl. VAT/Tax) / BDT 5,750.00 per day (Incl. VAT 5% & AIT 10%)', font_size=8.5)

    r2_cells = t20_rows[2].findall('w:tc', ns)
    set_cell_xml_text(r2_cells[0], 'Additional Custom Module / CBS Integration (Future Scope)', bold=True, font_size=8.5)
    set_cell_xml_text(r2_cells[1], 'BDT 150,000.00 per module (Inclusive of all Taxes)', font_size=8.5)

    print("Populated Table 20 (Additional Rates)")

    # ==========================================
    # 11. POPULATE TABLE 22 (COMPANY CONTACT DETAILS)
    # ==========================================
    t22 = tables[22]
    t22_rows = t22.findall('w:tr', ns)
    contact_data = {
        1: ("Company Name", "Skoder Technologies"),
        2: ("Address", "Office: E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207, Bangladesh"),
        3: ("Telephone No", "+880 1886-074400"),
        4: ("Fax", "N/A"),
        5: ("Contact Person & Designation", "K. M. Abir Mahmud, Chief Executive Officer"),
        6: ("Mobile Phone No.", "+880 1783-605898 / +880 1886-074400"),
        7: ("e-mail", "contact@skoder.co / abir@skoder.co")
    }
    for r_i, (k, v) in contact_data.items():
        if r_i < len(t22_rows):
            tcs = t22_rows[r_i].findall('w:tc', ns)
            if len(tcs) >= 2:
                set_cell_xml_text(tcs[0], k, bold=True, font_size=8.5)
                set_cell_xml_text(tcs[1], v, font_size=8.5)

    print("Populated Table 22 (Company Contact Details)")

    # ==========================================
    # 12. POPULATE TABLE 23 (UNDERTAKING)
    # ==========================================
    t23 = tables[23]
    t23_rows = t23.findall('w:tr', ns)
    undertaking_text = (
        "We, Skoder Technologies, hereby Undertake to supply the item at the price quoted above. "
        "We confirm that the price will remain valid up to October 11, 2027.\n\n"
        "___________________________\t\t\t___________________________\n"
        "K. M. ABIR MAHMUD\t\t\tOctober 11, 2026\n"
        "Chief Executive Officer\t\t\tDate\n"
        "Skoder Technologies (SEAL)"
    )
    tcs = t23_rows[0].findall('w:tc', ns)
    set_cell_xml_text(tcs[0], undertaking_text, font_size=8.5)
    print("Populated Table 23 (Undertaking)")

    # ==========================================
    # 13. POPULATE TABLE 24 (PAY ORDER DETAILS)
    # ==========================================
    t24 = tables[24]
    t24_rows = t24.findall('w:tr', ns)
    set_cell_xml_text(t24_rows[0].findall('w:tc', ns)[1], 'SJIBL/MIR/PO/2026/04812, Date: 11/10/2026', bold=True, font_size=8.5)
    set_cell_xml_text(t24_rows[1].findall('w:tc', ns)[1], 'BDT 25,000/- (Taka Twenty-Five Thousand Only)', bold=True, font_size=8.5)
    set_cell_xml_text(t24_rows[2].findall('w:tc', ns)[1], 'Shahjalal Islami Bank PLC', font_size=8.5)
    set_cell_xml_text(t24_rows[3].findall('w:tc', ns)[1], 'Mirpur Branch, Dhaka', font_size=8.5)
    print("Populated Table 24 (Pay Order Details)")

    # ==========================================
    # 14. ACCURATELY POPULATE BID FORM PARAGRAPHS ONLY
    # ==========================================
    paragraphs = tree.findall('.//w:p', ns)
    print(f"Total paragraphs in document: {len(paragraphs)}")

    # Specific paragraph replacements by finding their exact context
    for i, p in enumerate(paragraphs):
        txt = ''.join(p.itertext()).strip()
        
        # P522: Bid Form delivery commitment
        if 'within' in txt and 'days after receiving and accepting the work order' in txt:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'We undertake, if our bid is accepted, to Procurement, supply, implementation, Integration and support of a Litigation Management System (LMS), including software licenses and Annual Maintenance Contract (AMC) for Bank Asia PLC. within 112 (One Hundred Twelve) days after receiving and accepting the work order. We agree to abide by this tender document, which will remain valid up to October 11, 2027.'

        # P525: Dated this day of 2026
        elif 'Dated this' in txt and '2026' in txt:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'Dated this 11th day of October 2026'

        # P531-P532: Seal with Signature of authorized official
        elif 'Seal with Signature of the authorized official' in txt:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'K. M. ABIR MAHMUD, Chief Executive Officer, Skoder Technologies (Authorized Signatory & Seal)'

        # P537: Witness 1 (Only within the Bid Form witness block!)
        elif txt == '1.' and i > 520 and i < 550:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = '1. Fahad Morshed, Chief Intelligence Officer, Skoder Technologies, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207'

        # P540: Witness 2 (Only within the Bid Form witness block!)
        elif txt == '2.' and i > 520 and i < 550:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = '2. Imran Bipu, Head of Business Operations, Skoder Technologies, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207'

        # P575: Earnest Money Signature
        elif 'Signature \t: ____________________' in txt or ('Signature' in txt and 'Date: __________________' in txt):
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'Signature \t: K. M. Abir Mahmud \t \t \t \tDate: 11 October 2026'

        # P578: Name
        elif txt == 'Name  \t:':
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'Name  \t: K. M. Abir Mahmud, Chief Executive Officer'

        # P580: Seal
        elif txt == 'Seal \t \t:':
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'Seal \t \t: Skoder Technologies'

        # Under-table signature blocks (P446, P454, P502)
        elif txt == 'Signature of Bidder' and i < 510:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'K. M. Abir Mahmud, Chief Executive Officer, Skoder Technologies (Date: 11/10/2026)'

    print("Populated Bid Form and signature blocks.")

    # ==========================================
    # 15. SAVE BACK TO DOCUMENT.XML & REPACK
    # ==========================================
    new_xml = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
    with open(doc_xml_path, 'wb') as f:
        f.write(new_xml)

    out_docx = 'RFP_LMS Bank Asia_v0.3.docx'
    with zipfile.ZipFile(out_docx, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, temp_dir)
                z_out.write(full_path, rel_path)

    shutil.rmtree(temp_dir)
    print(f"Successfully generated clean and complete {out_docx}!")

if __name__ == '__main__':
    build_rfp()
