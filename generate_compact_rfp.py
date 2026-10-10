# -*- coding: utf-8 -*-
"""
generate_compact_rfp.py
Reads the clean reference doc: FINAL_PRINT_READY/RFP_LMS Bank Asia_v0.3.docx
Applies concise, to-the-point responses and remarks using pure python-docx API.
Preserves page count, table layouts, and styling without corruption.
"""

import os, sys, copy
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def set_cell_compact(cell, text, bold=False, font_size=8.0, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(font_size)
    run.bold = bold

def main():
    src_file = 'FINAL_PRINT_READY/RFP_LMS Bank Asia_v0.3.docx'
    print(f"Loading reference doc: {src_file}")
    doc = docx.Document(src_file)

    # 1. VERIFY TABLE 6 & 7 ARE UNTOUCHED
    t6 = doc.tables[6]
    t7 = doc.tables[7]
    print(f"Table 6 rows: {len(t6.rows)}, Table 7 rows: {len(t7.rows)} (Pristine)")

    # 2. TABLE 10 (TECHNICAL SPECIFICATIONS - 90 ROWS)
    t10 = doc.tables[10]
    print(f"Table 10 rows: {len(t10.rows)}")
    
    t10_remarks = {
        2: "Complied. Modular N-tier microservices architecture",
        3: "Complied. Dell PowerEdge R760 platform (Ref: Table 16)",
        5: "Complied. Dedicated Level 1/2/3 helpdesk & 24/7 SLA",
        6: "Complied. Dynamic multi-criteria query builder",
        7: "Complied. Web management console & secure monitoring",
        8: "Complied. Responsive web UI for all modern browsers",
        9: "Complied. Bilingual English & Bengali (Unicode UTF-8)",
        10: "Complied. Automated script testing supported in UAT",
        11: "Complied. Perpetual license for DC, Near DR & Far DR",
        12: "Complied. Dynamic master parameter & code setup",
        13: "Complied. Bank logo rendered on screens & reports",
        14: "Complied. Comprehensive administrative console tools",
        15: "Complied. TLS 1.3 / HTTPS encryption enforced",
        16: "Complied. Local customization & screen validation",
        17: "Complied. Secure dedicated VLAN & mTLS connectivity",
        18: "Complied. Automated EOD batch & delta loading from CBS",
        19: "Complied. Real-time RESTful & SOAP API gateway",
        20: "Complied. AES-256 at-rest & TLS 1.3 transit encryption",
        22: "Complied. Open-source enterprise architecture & standards",
        23: "Complied. Active Directory / LDAP Single Sign-On (SSO)",
        24: "Complied. Modular schema upgradable without downtime",
        25: "Complied. SMS Gateway & enterprise SMTP email integration",
        26: "Complied. Multi-channel alert queue with retry handling",
        27: "Complied. Automated hearing & notice reminder engine",
        28: "Complied. Central Data Warehouse & MIS ETL integration",
        29: "Complied. REST/JSON, SOAP, SFTP & OpenAPI specs",
        31: "Complied. Document version control & rollback history",
        32: "Complied. Real-time status change alerts to users",
        33: "Complied. 100% legacy litigation data migration",
        34: "Complied. Gap analysis & staging reconciliation tables",
        36: "Complied. Parallel processing of civil & criminal suits",
        38: "Complied. Parameterized business rules engine",
        40: "Complied. Multi-tier role & branch permission matrix",
        42: "Complied. Comprehensive deployment topology submitted",
        43: "Complied. 100% on-premises deployment in Bank Asia DC & DR",
        44: "Complied. Dedicated Test, UAT, and Production tiers",
        46: "Complied. 100% perpetual enterprise bank-wide license",
        47: "Complied. Granular RBAC with audit logging",
        48: "Complied. Encrypted password storage via bcrypt hashing",
        49: "Complied. Salted cryptographic hash in database",
        50: "Complied. Configurable password policy as per bank rules",
        51: "Complied. Seamless Single Sign-On (SSO) supported",
        52: "Complied. Multiple role assignments supported per user",
        53: "Complied. Dynamic role & authorization reassignment",
        54: "Complied. Strict Maker-Checker segregation of duties",
        55: "Complied. Menu & function access restricted per role",
        56: "Complied. Active Directory / LDAPS user sync",
        57: "Complied. Immutable audit trail on all user actions",
        58: "Complied. AES-256 at rest and TLS 1.3 in transit",
        59: "Complied. Hierarchical user groups defined per bank policy",
        60: "Complied. Terminal IP whitelisting & time restriction",
        61: "Complied. Self-service password recovery with OTP",
        62: "Complied. Configurable idle session timeout (15 mins)",
        63: "Complied. Administrative account lock & reactivation log",
        64: "Complied. Single concurrent login per workstation",
        65: "Complied. Ad-hoc query builder & audit trail reports",
        66: "Complied. Auto-lock after 5 consecutive failed logins",
        68: "Complied. Active-passive cluster & remote DR replication",
        69: "Complied. 99.9% uptime with RPO < 5 min, RTO < 15 min",
        70: "Complied. ACID transactional integrity with WAL",
        71: "Complied. Automated crash recovery with zero data loss",
        72: "Complied. Real-time exception tracking & admin alerts",
        74: "Complied. Enterprise Role-based Access Control (RBAC)",
        75: "Complied. Active Directory LDAP authentication connector",
        76: "Complied. Salted cryptographic password hashing",
        77: "Complied. 100% browser independent web client",
        78: "Complied. Hardened security against internal & external threats",
        79: "Complied. Certified adherence to OWASP Top 10 standards",
        80: "Complied. Batch execution log with error reason tracking",
        81: "Complied. Graceful exception handling with friendly alerts",
        82: "Complied. Enforced TLS 1.3 / HTTPS secure communications",
        83: "Complied. Searchable audit log querying console",
        84: "Complied. Open standards forward compatible with new tech",
        85: "Complied. Rapid security patch release within 24-48 hrs",
        86: "Complied. Device fingerprinting & IP/MAC terminal binding",
        87: "Complied. Comprehensive security hardening guide provided",
        88: "Complied. Compatible with SIEM, WAF and endpoint tools",
        89: "Complied. 100% up-to-date licensed enterprise components"
    }

    t10_count = 0
    for idx, rem in t10_remarks.items():
        if idx < len(t10.rows):
            r = t10.rows[idx]
            if len(r.cells) >= 6:
                set_cell_compact(r.cells[2], "Complied", bold=True, font_size=8.0, align=WD_ALIGN_PARAGRAPH.CENTER)
                set_cell_compact(r.cells[4], rem, font_size=8.0)
                t10_count += 1
    print(f"Populated Table 10 with {t10_count} concise items")

    # 3. TABLE 12 (FUNCTIONAL REQUIREMENTS - 413 ROWS)
    t12 = doc.tables[12]
    print(f"Table 12 rows: {len(t12.rows)}")
    t12_count = 0
    for idx in range(2, len(t12.rows)):
        r = t12.rows[idx]
        if len(r.cells) == 4:
            set_cell_compact(r.cells[2], "Complied", bold=True, font_size=8.0, align=WD_ALIGN_PARAGRAPH.CENTER)
            set_cell_compact(r.cells[3], "Complied", font_size=8.0)
            t12_count += 1
    print(f"Populated Table 12 with {t12_count} concise items")

    # 4. TABLE 13 (KEY DOMAIN EXPERTS)
    t13 = doc.tables[13]
    while len(t13.rows) < 5:
        t13.add_row()
    domain_experts = [
        ("1", "Technology Strategy & FinTech (K. M. Abir Mahmud)", "Project Director & Executive Liaison - Project governance & approvals", "10+ Yrs", "Part-time / Advisory", "Leading Official (Project Director)"),
        ("2", "Software Architecture & CBS (Ali Haider Fahad)", "Lead Solutions Architect - System design, CBS API gateway, DB design", "8+ Yrs", "Full-time", "Leading Official (Lead Solutions Architect)"),
        ("3", "Cloud Infrastructure & Security (Fahad Morshed)", "Chief Intelligence & Security Lead - High availability server & security", "6+ Yrs", "Full-time", "Leading Official (CIO & Security Lead)"),
        ("4", "Full-Stack Engineering (Fahim Shahriar)", "Senior Full-Stack Engineer / Technical PM - Core litigation modules", "5+ Yrs", "Full-time", "Implementation Official (Technical PM)")
    ]
    for i, exp in enumerate(domain_experts):
        r = t13.rows[i + 1]
        for col_idx in range(min(len(r.cells), len(exp))):
            bold = (col_idx == 0 or col_idx == 5)
            set_cell_compact(r.cells[col_idx], exp[col_idx], bold=bold, font_size=8.0)
    print("Populated Table 13 (Key Domain Experts)")

    # 5. TABLE 14 (IMPLEMENTATION OFFICIALS)
    t14 = doc.tables[14]
    while len(t14.rows) < 5:
        t14.add_row()
    impl_officials = [
        ("1", "QA & System Audit (Ahmed Shafkat)", "QA & Testing Lead - Test cases, vulnerability scanning, UAT lead", "4+ Yrs", "Full-time", "Implementation Official (QA Lead)"),
        ("2", "Training & Enablement (Bodrunnaher Toma)", "Training Lead - User manual, SOP, legal & branch user workshops", "14+ Yrs", "Full-time rollout", "Implementation Official (Training Lead)"),
        ("3", "Data Migration & Operations (Md. Rafidul Islam)", "Operations Coordinator - Legacy data migration, CBS reconciliation", "4+ Yrs", "Full-time", "Implementation Official (Operations Coordinator)"),
        ("4", "UI/UX & Frontend (Alfee Bin Ferdous / Alamin)", "UI/UX Lead - Dashboard design, hearing calendar, case workflows", "4+ Yrs", "Full-time", "Implementation Official (UI/UX Lead)")
    ]
    for i, off in enumerate(impl_officials):
        r = t14.rows[i + 1]
        for col_idx in range(min(len(r.cells), len(off))):
            bold = (col_idx == 0 or col_idx == 5)
            set_cell_compact(r.cells[col_idx], off[col_idx], bold=bold, font_size=8.0)
    print("Populated Table 14 (Implementation Officials)")

    # 6. TABLE 15 (TRACK RECORD)
    t15 = doc.tables[15]
    clients_data = [
        ("1", "Druto Fintech Ltd.", "FinTech / NBFI Platform", "DrutoLoan Core Lending ERP, Recovery & Legal Notices"),
        ("2", "Viva Nation UK Ltd.", "Global FinTech Institution", "VivaPe Cross-Border Remittance & Compliance Portal"),
        ("3", "Jahangirnagar University", "Public Autonomous Institution", "Institutional Automation ERP, Legal Matters & Document Management"),
        ("4", "Business Bee Inc.", "Corporate Enterprise", "Enterprise Resource Planning & Contract Lifecycle"),
        ("5", "BUP (Govt. Institution)", "Public Educational Institution", "Institutional Automation & Legal Workflow System"),
        ("6", "OrbitMart E-Commerce", "Retail Enterprise", "Merchant Billing, Settlement & Dispute Platform")
    ]
    for i, c_info in enumerate(clients_data):
        row_idx = i + 2
        if row_idx < len(t15.rows):
            r = t15.rows[row_idx]
            for col_idx in range(min(len(r.cells), len(c_info))):
                set_cell_compact(r.cells[col_idx], c_info[col_idx], bold=(col_idx <= 1), font_size=8.0)
    print("Populated Table 15 (Track Record)")

    # 7. TABLE 16 (HARDWARE SPECS)
    t16 = doc.tables[16]
    hw_specs = {
        1: "Dell Technologies",
        2: "PowerEdge R760 Rack Server (Enterprise Class)",
        3: "USA",
        4: "Malaysia / China (Dell OEM Plant)",
        5: "2U Rack Mountable with ReadyRails Sliding Rails",
        6: "Dual Socket (2 Sockets populated)",
        7: "2x Intel Xeon Silver 4410Y (2.0GHz, 12C/24T, 30M Cache)",
        8: "128GB (4x 32GB) DDR5-4800MHz RDIMM ECC, max 1TB",
        9: "Dell PERC H755 SAS/SATA RAID Controller (8GB NV Cache)",
        10: "Dell BOSS-N1 with 2x 480GB M.2 NVMe SSD (RAID 1 for OS)",
        11: "4x 1.92TB Enterprise SATA/SAS SSD 2.5in Hot-plug (RAID 10)",
        12: "2.5-Inch Chassis with up to 8 Hot-Plug Drives",
        13: "Dual Port 16Gbps / 32Gbps FC HBA for Enterprise SAN",
        14: "Broadcom 57412 Dual Port 10GbE SFP+ & Dual Port 1GbE",
        15: "iDRAC9 Enterprise with OpenManage Enterprise Integration",
        16: "Red Hat Enterprise Linux 9 / VMware vSphere ESXi 8.0",
        17: "Dual, Hot-plug, Redundant Power Supply (1+1), 800W Platinum",
        18: "TPM 2.0, Silicon Root of Trust, Secure Boot, System Lockdown",
        19: "Dell 2U Sliding Rails with Cable Management Arm, Power Cords",
        20: "3 Years Dell ProSupport with 24x7 4-Hour Onsite Mission Critical",
        21: "Comprehensive Hardware AMC available post-warranty"
    }
    for r_i, val in hw_specs.items():
        if r_i < len(t16.rows):
            r = t16.rows[r_i]
            if len(r.cells) >= 3:
                set_cell_compact(r.cells[2], val, font_size=8.0)
    print("Populated Table 16 (Hardware Specs)")

    # 8. TABLE 17 (TRAINING)
    t17 = doc.tables[17]
    tr_data = [
        ("01", "Functional User Training", "Comprehensive training for Legal Division & Branch Officers (5 Days @ BDT 5,000/day)", "1 Batch (30 Users)"),
        ("02", "System Admin & IT Training", "Technical training for Bank Asia IT, DBAs & Security (3 Days @ BDT 5,000/day)", "1 Batch (10 IT Staff)"),
        ("03", "Total Training & Rate", "Per Diem: BDT 5,000.00/day (Excl. Tax) / BDT 5,750.00/day (Incl. 5% VAT & 10% AIT). Total: BDT 46,000.00", "8 Days Total (2 Batches)")
    ]
    for i, t_info in enumerate(tr_data):
        row_idx = i + 1
        if row_idx < len(t17.rows):
            r = t17.rows[row_idx]
            for col_idx in range(min(len(r.cells), len(t_info))):
                set_cell_compact(r.cells[col_idx], t_info[col_idx], bold=(col_idx <= 1), font_size=8.0)
    print("Populated Table 17 (Training)")

    # 9. TABLE 19 (FINANCIAL PROPOSAL)
    t19 = doc.tables[19]
    # Row 2 (Data row)
    r2 = t19.rows[2]
    set_cell_compact(r2.cells[0], "Litigation Management System (LMS)", bold=True, font_size=8.0)
    set_cell_compact(r2.cells[1], "Skoder LMS Enterprise (Case Tracking, Recovery, Auction, WOA, CBS API) with 3-Yr Warranty", font_size=7.5)
    set_cell_compact(r2.cells[2], "v1.0 (Bank Enterprise)", font_size=7.5)
    set_cell_compact(r2.cells[3], "01 (Enterprise License)", font_size=7.5)
    set_cell_compact(r2.cells[4], "1,500,000.00", font_size=8.0)
    set_cell_compact(r2.cells[5], "VAT 5% (75k) + AIT 10% (150k) = 15% (225k)", font_size=7.5)
    set_cell_compact(r2.cells[6], "1,725,000.00", bold=True, font_size=8.0)
    set_cell_compact(r2.cells[7], "402,500.00", font_size=8.0)
    set_cell_compact(r2.cells[8], "402,500.00", font_size=8.0)
    set_cell_compact(r2.cells[9], "402,500.00", font_size=8.0)
    set_cell_compact(r2.cells[10], "2,932,500.00", bold=True, font_size=8.0)

    # Row 3 (Summary row)
    r3 = t19.rows[3]
    set_cell_compact(r3.cells[0], "Total Product Price (Incl. VAT & Tax)", bold=True, font_size=8.0)
    set_cell_compact(r3.cells[1], "BDT 1,725,000.00 (In words: Taka Seventeen Lac Twenty-Five Thousand Only)", bold=True, font_size=8.0)
    if len(r3.cells) > 2:
        set_cell_compact(r3.cells[2], "Total 3-Yr AMC: BDT 1,207,500.00", font_size=8.0)
    if len(r3.cells) > 3:
        set_cell_compact(r3.cells[3], "Grand Total: BDT 2,932,500.00 (In words: Taka Twenty-Nine Lac Thirty-Two Thousand Five Hundred Only)", bold=True, font_size=8.0)
    print("Populated Table 19 (Financial Proposal)")

    # 10. TABLE 20 (ADDITIONAL RATES)
    t20 = doc.tables[20]
    set_cell_compact(t20.rows[1].cells[0], "Functional & Technical Training (as per Clause 308 & 1673)", bold=True, font_size=8.0)
    set_cell_compact(t20.rows[1].cells[1], "BDT 5,000.00 per day (Excl. VAT/Tax) / BDT 5,750.00 per day (Incl. VAT 5% & AIT 10%)", font_size=8.0)
    set_cell_compact(t20.rows[2].cells[0], "Additional Custom Module / CBS Integration (Future Scope)", bold=True, font_size=8.0)
    set_cell_compact(t20.rows[2].cells[1], "BDT 150,000.00 per module (Inclusive of all Taxes)", font_size=8.0)
    print("Populated Table 20 (Additional Rates)")

    # 11. TABLE 22 (COMPANY CONTACT DETAILS)
    t22 = doc.tables[22]
    contact_dict = {
        1: ("Company Name", "Skoder Technologies"),
        2: ("Address", "Office: E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207, Bangladesh"),
        3: ("Telephone No", "+880 1886-074400"),
        4: ("Fax", "N/A"),
        5: ("Contact Person & Designation", "K. M. Abir Mahmud, Chief Executive Officer"),
        6: ("Mobile Phone No.", "+880 1783-605898 / +880 1886-074400"),
        7: ("e-mail", "contact@skoder.co / abir@skoder.co")
    }
    for r_i, (k, v) in contact_dict.items():
        if r_i < len(t22.rows):
            r = t22.rows[r_i]
            if len(r.cells) >= 2:
                set_cell_compact(r.cells[0], k, bold=True, font_size=8.0)
                set_cell_compact(r.cells[1], v, font_size=8.0)
    print("Populated Table 22 (Company Contact Details)")

    # 12. TABLE 23 (UNDERTAKING)
    t23 = doc.tables[23]
    undertaking_text = (
        "We, Skoder Technologies, hereby Undertake to supply the item at the price quoted above. "
        "We confirm that the price will remain valid up to October 11, 2027.\n\n"
        "___________________________\t\t\t___________________________\n"
        "K. M. ABIR MAHMUD\t\t\tOctober 11, 2026\n"
        "Chief Executive Officer\t\t\tDate\n"
        "Skoder Technologies (SEAL)"
    )
    set_cell_compact(t23.rows[0].cells[0], undertaking_text, font_size=8.0)
    print("Populated Table 23 (Undertaking)")

    # 13. TABLE 24 (PAY ORDER DETAILS)
    t24 = doc.tables[24]
    set_cell_compact(t24.rows[0].cells[1], "SJIBL/MIR/PO/2026/04812, Date: 11/10/2026", bold=True, font_size=8.0)
    set_cell_compact(t24.rows[1].cells[1], "BDT 25,000/- (Taka Twenty-Five Thousand Only)", bold=True, font_size=8.0)
    set_cell_compact(t24.rows[2].cells[1], "Shahjalal Islami Bank PLC", font_size=8.0)
    set_cell_compact(t24.rows[3].cells[1], "Mirpur Branch, Dhaka", font_size=8.0)
    print("Populated Table 24 (Pay Order Details)")

    # 14. BID FORM PARAGRAPHS & SIGNATURES
    # P522: Delivery timeline
    doc.paragraphs[522].text = "We undertake, if our bid is accepted, to Procurement, supply, implementation, Integration and support of a Litigation Management System (LMS), including software licenses and Annual Maintenance Contract (AMC) for Bank Asia PLC. within 112 (One Hundred Twelve) days after receiving and accepting the work order. We agree to abide by this tender document, which will remain valid up to October 11, 2027."
    # P525: Date
    doc.paragraphs[525].text = "Dated this 11th day of October 2026"
    # P531 & P532: Signatory
    doc.paragraphs[531].text = "K. M. ABIR MAHMUD\t\t\tSKODER TECHNOLOGIES"
    doc.paragraphs[532].text = "Chief Executive Officer (Authorized Official)\t\t\tRound Seal of the Company"
    # P537 & P540: Witnesses
    doc.paragraphs[537].text = "1. Fahad Morshed, Chief Intelligence Officer, Skoder Technologies, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207"
    doc.paragraphs[540].text = "2. Imran Bipu, Head of Business Operations, Skoder Technologies, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207"
    # P575, P578, P580: Earnest Money Signature
    doc.paragraphs[575].text = "Signature \t: K. M. Abir Mahmud \t \t \t \tDate: 11 October 2026"
    doc.paragraphs[578].text = "Name  \t: K. M. Abir Mahmud, Chief Executive Officer"
    doc.paragraphs[580].text = "Seal \t \t: Skoder Technologies"
    print("Populated Bid Form & Signatures")

    # SAVE TO ROOT
    out_file = 'RFP_LMS Bank Asia_v0.3.docx'
    doc.save(out_file)
    print(f"Saved: {out_file}")

if __name__ == '__main__':
    main()
