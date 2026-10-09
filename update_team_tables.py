import zipfile, os, shutil, copy
import xml.etree.ElementTree as ET

def set_cell_text(tc, text):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    p_elements = tc.findall('w:p', ns)
    if not p_elements:
        p = ET.SubElement(tc, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
    else:
        p = p_elements[0]
        for extra_p in p_elements[1:]:
            tc.remove(extra_p)
    
    for r in p.findall('w:r', ns):
        p.remove(r)
    
    r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
    t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
    t.text = text

def update_team_tables():
    temp_dir = 'temp_rfp_team'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    with zipfile.ZipFile('RFP_LMS Bank Asia_v0.3.docx', 'r') as z:
        z.extractall(temp_dir)

    doc_xml_path = os.path.join(temp_dir, 'word', 'document.xml')
    with open(doc_xml_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    ET.register_namespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
    tree = ET.fromstring(xml_content.encode('utf-8'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    tables = tree.findall('.//w:tbl', ns)

    # Table 14 (index 13): Key Domain Experts
    t14 = tables[13]
    t14_rows = t14.findall('w:tr', ns)
    while len(t14.findall('w:tr', ns)) < 5:
        new_r = copy.deepcopy(t14_rows[1])
        t14.append(new_r)
    
    t14_rows = t14.findall('w:tr', ns)
    
    # Row 1: K. M. Abir Mahmud
    r1 = t14_rows[1].findall('w:tc', ns)
    set_cell_text(r1[0], '1')
    set_cell_text(r1[1], 'Technology Strategy, Governance & FinTech (K. M. Abir Mahmud)')
    set_cell_text(r1[2], 'Project Director & Executive Liaison - Project governance, Bank Asia executive liaison, sprint milestone approvals')
    set_cell_text(r1[3], '10+ Years')
    set_cell_text(r1[4], 'Part-time / Advisory & Executive Oversight')
    set_cell_text(r1[5], 'Leading Official (Project Director)')

    # Row 2: Ali Haider Fahad
    r2 = t14_rows[2].findall('w:tc', ns)
    set_cell_text(r2[0], '2')
    set_cell_text(r2[1], 'Enterprise Software Architecture, Laravel & CBS API Integration (Ali Haider Fahad)')
    set_cell_text(r2[2], 'Lead Solutions Architect - System design, CBS API integration gateway, database architecture, and technical lead')
    set_cell_text(r2[3], '8+ Years')
    set_cell_text(r2[4], 'Full-time')
    set_cell_text(r2[5], 'Leading Official (Lead Solutions Architect)')

    # Row 3: Fahad Morshed
    r3 = t14_rows[3].findall('w:tc', ns)
    set_cell_text(r3[0], '3')
    set_cell_text(r3[1], 'Cloud Infrastructure, Database Systems & Security (Fahad Morshed)')
    set_cell_text(r3[2], 'Chief Intelligence & Security Lead - High availability server setup, PostgreSQL/Oracle configuration, AES-256 data security')
    set_cell_text(r3[3], '6+ Years')
    set_cell_text(r3[4], 'Full-time')
    set_cell_text(r3[5], 'Leading Official (CIO & Security Lead)')

    # Row 4: Fahim Shahriar
    r4 = t14_rows[4].findall('w:tc', ns)
    set_cell_text(r4[0], '4')
    set_cell_text(r4[1], 'Full-Stack Software Engineering & Workflow Automation (Fahim Shahriar)')
    set_cell_text(r4[2], 'Senior Full-Stack Engineer / Technical PM - Core litigation modules, Artha Rin, NI Act 138, Auction management')
    set_cell_text(r4[3], '5+ Years')
    set_cell_text(r4[4], 'Full-time')
    set_cell_text(r4[5], 'Implementation Official (Technical PM)')

    # Table 15 (index 14): Implementation & Rollout Officials
    t15 = tables[14]
    t15_rows = t15.findall('w:tr', ns)
    while len(t15.findall('w:tr', ns)) < 5:
        new_r = copy.deepcopy(t15_rows[1])
        t15.append(new_r)
        
    t15_rows = t15.findall('w:tr', ns)

    # Row 1: Ahmed Shafkat
    r1_15 = t15_rows[1].findall('w:tc', ns)
    set_cell_text(r1_15[0], '1')
    set_cell_text(r1_15[1], 'Quality Assurance, Automated Testing & System Audit (Ahmed Shafkat)')
    set_cell_text(r1_15[2], 'QA & Testing Lead - Test cases, security vulnerability scanning, performance load testing, and UAT coordination')
    set_cell_text(r1_15[3], '4+ Years')
    set_cell_text(r1_15[4], 'Full-time')
    set_cell_text(r1_15[5], 'Implementation Official (QA Lead)')

    # Row 2: Bodrunnaher Toma
    r2_15 = t15_rows[2].findall('w:tc', ns)
    set_cell_text(r2_15[0], '2')
    set_cell_text(r2_15[1], 'Training, Documentation & User Enablement (Bodrunnaher Toma)')
    set_cell_text(r2_15[2], 'Training & Enablement Lead - Authoring bilingual user manual & SOP, conducting Legal & Branch user workshops')
    set_cell_text(r2_15[3], '14+ Years')
    set_cell_text(r2_15[4], 'Full-time during rollout')
    set_cell_text(r2_15[5], 'Implementation Official (Training Lead)')

    # Row 3: Md. Rafidul Islam
    r3_15 = t15_rows[3].findall('w:tc', ns)
    set_cell_text(r3_15[0], '3')
    set_cell_text(r3_15[1], 'Data Migration, CBS Account Reconciliation & Operations (Md. Rafidul Islam)')
    set_cell_text(r3_15[2], 'Operations & Migration Coordinator - Legacy case data migration, CBS account reconciliation, UAT operations')
    set_cell_text(r3_15[3], '4+ Years')
    set_cell_text(r3_15[4], 'Full-time')
    set_cell_text(r3_15[5], 'Implementation Official (Operations Coordinator)')

    # Row 4: Alamin / Alfee Bin Ferdous
    r4_15 = t15_rows[4].findall('w:tc', ns)
    set_cell_text(r4_15[0], '4')
    set_cell_text(r4_15[1], 'UI/UX Design & Frontend Engineering (Alfee Bin Ferdous / Alamin)')
    set_cell_text(r4_15[2], 'UI/UX & Frontend Specialist - Intuitive dashboard design, responsive hearing calendar, case workflow interfaces')
    set_cell_text(r4_15[3], '4+ Years')
    set_cell_text(r4_15[4], 'Full-time')
    set_cell_text(r4_15[5], 'Implementation Official (UI/UX Lead)')

    # Save XML
    new_xml = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
    with open(doc_xml_path, 'wb') as f:
        f.write(new_xml)

    # Re-zip
    out_docx = 'RFP_LMS Bank Asia_v0.3.docx'
    with zipfile.ZipFile(out_docx, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, temp_dir)
                z_out.write(full_path, rel_path)

    shutil.rmtree(temp_dir)
    print('Updated Tables 14 & 15 in RFP_LMS Bank Asia_v0.3.docx successfully!')

if __name__ == '__main__':
    update_team_tables()
