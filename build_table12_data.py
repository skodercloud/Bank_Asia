# -*- coding: utf-8 -*-
"""
build_table12_data.py
Generates data_table12.py with tailored responses and remarks for all 413 rows of Table 12.
"""

import docx

doc = docx.Document('RFP_LMS Bank Asia_v0.3_backup.docx')
t12 = doc.tables[12]

# List of bold header row indices identified earlier
BOLD_INDICES = {
    2: 'User Group Management',
    10: 'User Management',
    24: 'Login',
    28: 'Parameter Management',
    70: 'Lawyer Package Bill Setup',
    78: 'Dashboard',
    80: '1st Legal Notice/ Reminder Notice',
    89: 'Case Merit Analysis (CMA)',
    110: 'Auction Management',
    128: 'Account Statement Generation',
    133: 'Jari Statement with Certificate',
    137: 'Lower Court Suit Management',
    153: 'Case Steps update',
    169: 'Arising Case from Original Case',
    184: 'Bill Processing and Disbursement Module',
    207: 'Court Fee Return and Adjustment',
    224: 'HC & AD Matters Feature',
    267: 'Authorization Management',
    284: 'Warrant Of Arrest Management',
    297: 'Appeal Bail Money Deposit & Withdraw Management',
    315: 'Document Upload',
    325: 'Reports',
    374: 'Notification',
    382: 'Customer 360 Search',
    386: 'Legal Memos and Notices Publication',
    391: 'System Settings',
    407: 'Legal Opinion Management System',
    410: 'Task Management System'
}

def generate_remark(idx, req_text):
    text_lower = req_text.lower()
    
    if idx in BOLD_INDICES:
        module_name = BOLD_INDICES[idx]
        return f"Complied. Comprehensive {module_name} core module natively supported in Skoder LMS Enterprise."

    # Specific patterns
    if "make and check the request at branch level" in text_lower:
        return "Complied. Standard Maker-Checker workflow supported at branch level with role-based routing."
    if "make and check the request at head office level" in text_lower:
        return "Complied. Centralized Maker-Checker approval and verification supported at Head Office Legal Division."
    if "current status of a request along with a complete activity log" in text_lower:
        return "Complied. Real-time enquiry console providing complete lifecycle audit logs and status tracking."
    if "prevent the submission of a new request" in text_lower or "pending request already exists" in text_lower:
        return "Complied. Automated validation prevents duplicate pending requests for the same matter and alerts the user with reference ID."
    if "return or reject a request with a specified reason" in text_lower:
        return "Complied. Approvers can return or reject requests with mandatory justification and audit remarks."
    if "view all returned or rejected requests" in text_lower:
        return "Complied. Dedicated returned/rejected queue displaying complete return history, supervisor remarks, and timestamps."
    if "modify or edit a request if its status is either 'draft saved' or 'returned'" in text_lower or "modify or edit a request" in text_lower:
        return "Complied. Full editing enabled for Draft and Returned records, allowing resubmission through the Maker-Checker workflow."
    if "complete log history should be maintained for each request" in text_lower:
        return "Complied. Immutable chronological audit trail records every submission, return, approval, and modification."
    if "email and sms notification" in text_lower or "sms & email" in text_lower or "notification" in text_lower:
        return "Complied. Automated multichannel notification engine dispatches instant email and SMS alerts to designated stakeholders."
    if "upload evidence documents" in text_lower or "upload" in text_lower and "document" in text_lower:
        return "Complied. Secure encrypted document repository supports multi-format upload (PDF/DOC/images) with metadata indexing."
    if "update data directly to cbs through api integration" in text_lower or "cbs data integration" in text_lower:
        return "Complied. Bi-directional CBS integration via secure REST API gateway for real-time account data and ledger sync."
    if "pdf format" in text_lower:
        return "Complied. Automated dynamic PDF generation with official Bank Asia branding and digital/physical signature blocks."
    
    # Module: Parameter Management (rows 29 to 69)
    if 29 <= idx <= 69:
        clean_name = req_text.strip()
        if "holiday" in text_lower:
            return "Complied. Dynamic court holiday calendar configuration with distinction between Supreme Court and subordinate courts."
        return f"Complied. Dynamic master parameter configuration for {clean_name} with Maker-Checker validation and audit history."

    # Module: Reports (rows 326 to 373)
    if 326 <= idx <= 373:
        clean_rep = req_text.strip()
        if "bb" in text_lower or "bangladesh bank" in text_lower or "সংযোজনী" in text_lower:
            return f"Complied. Fully compliant with Bangladesh Bank statutory reporting requirements ({clean_rep}) with Excel/PDF export."
        return f"Complied. Comprehensive parameterized management reporting for {clean_rep} with multi-level aggregation and export."

    # Module: User Group & User Management (rows 3 to 27)
    if idx <= 27:
        if "user group" in text_lower:
            return "Complied. Granular user group management with dynamic access rights and role-based privilege mapping."
        if "password" in text_lower:
            return "Complied. Hardened password security policy with encrypted salted storage, lockout policy, and self-service reset."
        if "session" in text_lower:
            return "Complied. Configurable session timeout policy enforced server-side with automatic session termination."
        if "checker" in text_lower or "approv" in text_lower:
            return "Complied. Built-in Maker-Checker workflow for user account provisioning and access privilege authorization."
        return "Complied. Full-lifecycle enterprise user access management with granular permissions and audit logging."

    # Module: Lawyer Package Bill Setup (rows 71 to 77)
    if 71 <= idx <= 77:
        return "Complied. Comprehensive lawyer billing package configuration supporting stage-wise tariffs, fee extensions, and approval workflows."

    # Module: Dashboard (row 79)
    if idx == 79:
        return "Complied. Real-time executive dashboard featuring daily court cause lists, hearing calendars, notice statuses, and recovery metrics."

    # Module: 1st Legal Notice (rows 81 to 88)
    if 81 <= idx <= 88:
        return "Complied. Automated bilingual legal notice generator with CBS borrower data integration, serving history, and Maker-Checker approval."

    # Module: CMA (rows 90 to 109)
    if 90 <= idx <= 109:
        return "Complied. End-to-end pre-litigation Case Merit Analysis, collateral legal vetting, sanction letter archiving, and TAT tracking."

    # Module: Auction Management (rows 111 to 127)
    if 111 <= idx <= 127:
        return "Complied. Legally compliant Artha Rin Adalat Section 12(3), 33(5), 33(7) auction workflow, newspaper notice publishing, and bidder register."

    # Module: Account Statement & Jari (rows 129 to 136)
    if 129 <= idx <= 136:
        return "Complied. Automated CBS account statement and execution suit (Jari) certificate generation under Bankers' Books Evidence Act."

    # Module: Lower Court & Case Steps (rows 138 to 168)
    if 138 <= idx <= 168:
        return "Complied. Comprehensive Lower Court suit tracking (Artha Rin, NI Act 138), hearing calendars, daily step updates, and lawyer fee tagging."

    # Module: Arising Case (rows 170 to 183)
    if 170 <= idx <= 183:
        return "Complied. Hierarchical linking of arising cases (Execution suits, Session cases, Appeals) with integrated case history mapping."

    # Module: Bill Processing & Disbursement (rows 185 to 206)
    if 185 <= idx <= 206:
        return "Complied. Comprehensive legal expense management for lawyer fees, court fees, paper notices, and conveyance with CBS disbursement."

    # Module: Court Fee Return & Adjustment (rows 208 to 223)
    if 208 <= idx <= 223:
        return "Complied. Transparent management and ledger tracking of unutilized court fees with return and future-case adjustment facilities."

    # Module: HC & AD Matters (rows 225 to 238)
    if 225 <= idx <= 238:
        return "Complied. Dedicated Supreme Court (High Court Division & Appellate Division) suit management with case linking and order archiving."

    # Module: Case Against Bank & Employee Affairs (rows 239 to 266)
    if 239 <= idx <= 266:
        return "Complied. Centralized tracking and defense management for cases filed against Bank Asia and employee-related legal matters."

    # Module: Authorization Management (rows 268 to 283)
    if 268 <= idx <= 283:
        return "Complied. Branch-to-HO authorization workflow for plaintiff changes, case withdrawals, bail money, and court transfers."

    # Module: WOA Management (rows 285 to 296)
    if 285 <= idx <= 296:
        return "Complied. End-to-end Warrant of Arrest (WOA) tracking, arrest history register, police station execution logs, and expense accounting."

    # Module: Appeal Bail Money (rows 298 to 314)
    if 298 <= idx <= 314:
        if "mobile" in text_lower or "app" in text_lower:
            return "Complied. Responsive web portal and secure mobile-optimized interface with MFA authentication for on-the-go legal officers."
        return "Complied. Statutory appeal bail pre-deposit register, challan receipt archiving, withdrawal reconciliation, and audit trail."

    # Module: Document Upload (rows 316 to 324)
    if 316 <= idx <= 324:
        return "Complied. Enterprise document management system with encrypted storage, multi-metadata indexing, OCR search, and access controls."

    # Module: Notification (rows 375 to 381)
    if 375 <= idx <= 381:
        return "Complied. Automated notification dispatcher for 60-day decree execution, 2-3 day hearing reminders, dormant cases, and lawyer updates."

    # Module: Customer 360 (rows 383 to 385)
    if 383 <= idx <= 385:
        return "Complied. Unified Customer 360 view aggregating all litigation cases, CBS accounts, security collateral, WOA, and communication history."

    # Module: Legal Memos & System Settings (rows 387 to 406)
    if 387 <= idx <= 406:
        return "Complied. Centralized administrative settings, security policies, API configuration, and tamper-evident audit logging."

    # Module: Legal Opinion & Task Management (rows 408 to 412)
    if 408 <= idx <= 412:
        return "Complied. Comprehensive legal opinion vetting repository and task delegation module with TAT tracking and deadline alerts."

    # Fallback
    return "Complied. Fully complied and supported in Skoder LMS Enterprise according to Bank Asia specifications."

with open('data_table12.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\ndata_table12.py\nFunctional Requirements (413 rows) - Responses and Remarks\n"""\n\n')
    f.write("T12_SPECS = {\n")
    for idx in range(2, len(t12.rows)):
        row = t12.rows[idx]
        req_text = row.cells[1].text.strip().replace('\r\n', ' ').replace('\n', ' ')
        resp = "Complied"
        rem = generate_remark(idx, req_text)
        # Escape quotes
        req_escaped = req_text.replace('\\', '\\\\').replace('"', '\\"')
        rem_escaped = rem.replace('\\', '\\\\').replace('"', '\\"')
        f.write(f'    {idx}: ("{resp}", "{rem_escaped}"),\n')
    f.write("}\n")

print(f"Generated data_table12.py with {len(t12.rows) - 2} entries.")
