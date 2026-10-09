import zipfile, os, shutil
import xml.etree.ElementTree as ET

def set_cell_text(tc, text):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    # Remove existing p elements
    p_elements = tc.findall('w:p', ns)
    if not p_elements:
        p = ET.SubElement(tc, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
    else:
        p = p_elements[0]
        for extra_p in p_elements[1:]:
            tc.remove(extra_p)
    
    # Remove runs
    for r in p.findall('w:r', ns):
        p.remove(r)
    
    # Create new run and text
    r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
    t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
    t.text = text

def update_rfp():
    temp_dir = 'temp_rfp_unpacked'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    with zipfile.ZipFile('RFP_LMS Bank Asia_v0.3.docx', 'r') as z:
        z.extractall(temp_dir)

    doc_xml_path = os.path.join(temp_dir, 'word', 'document.xml')
    with open(doc_xml_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    # Register namespaces
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
    
    # Table 20 (index 19) - Financial Proposal
    t20 = tables[19]
    t20_rows = t20.findall('w:tr', ns)
    
    # Row 2 (Data row)
    r2_cells = t20_rows[2].findall('w:tc', ns)
    set_cell_text(r2_cells[0], 'Litigation Management System (LMS)')
    set_cell_text(r2_cells[1], 'Skoder LMS Enterprise (Case Tracking, Recovery, Auction, WOA, CBS API Integration, Bangladesh Bank MIS Reporting) with 3-Year Warranty & Comprehensive Support')
    set_cell_text(r2_cells[2], 'v1.0 (Bank Enterprise Edition)')
    set_cell_text(r2_cells[3], '01 (Enterprise Bank-wide License)')
    set_cell_text(r2_cells[4], '1,500,000.00')
    set_cell_text(r2_cells[5], 'VAT 5% (75,000.00) + AIT 10% (150,000.00) = 15% (225,000.00)')
    set_cell_text(r2_cells[6], '1,725,000.00')
    set_cell_text(r2_cells[7], '402,500.00')
    set_cell_text(r2_cells[8], '402,500.00')
    set_cell_text(r2_cells[9], '402,500.00')
    set_cell_text(r2_cells[10], '2,932,500.00')

    # Row 3 (Summary row)
    r3_cells = t20_rows[3].findall('w:tc', ns)
    set_cell_text(r3_cells[0], 'Total Product Price (Incl. VAT & Tax)')
    set_cell_text(r3_cells[1], 'BDT 1,725,000.00 (In words: Taka Seventeen Lac Twenty-Five Thousand Only)')
    if len(r3_cells) > 2:
        set_cell_text(r3_cells[2], 'Total 3-Yr AMC (Years 4-6): BDT 1,207,500.00')
    if len(r3_cells) > 3:
        set_cell_text(r3_cells[3], 'Grand Total (Product + AMC): BDT 2,932,500.00 (In words: Taka Twenty-Nine Lac Thirty-Two Thousand Five Hundred Only)')

    # Table 21 (index 20) - Additional items
    t21 = tables[20]
    t21_rows = t21.findall('w:tr', ns)
    r1_cells = t21_rows[1].findall('w:tc', ns)
    set_cell_text(r1_cells[0], 'Functional & Technical Training (as per Clause 308 & 1673)')
    set_cell_text(r1_cells[1], 'BDT 5,000.00 per day (Excl. VAT/Tax) / BDT 5,750.00 per day (Incl. VAT 5% & AIT 10%)')

    r2_cells = t21_rows[2].findall('w:tc', ns)
    set_cell_text(r2_cells[0], 'Additional Custom Module / CBS Integration (Future Scope)')
    set_cell_text(r2_cells[1], 'BDT 150,000.00 per module (Inclusive of all Taxes)')

    # Table 24 (index 23) - Undertaking
    t24 = tables[23]
    t24_rows = t24.findall('w:tr', ns)
    r0_cells = t24_rows[0].findall('w:tc', ns)
    set_cell_text(r0_cells[0], 'We, Skoder Technologies, hereby Undertake to supply the item at the price quoted above. We confirm that the price will remain valid up to October 11, 2027.\n\nSignature: K. M. Abir Mahmud, Chief Executive Officer\nDate: October 11, 2026\nSEAL: Skoder Technologies')

    # Table 25 (index 24) - Pay Order Details
    t25 = tables[24]
    t25_rows = t25.findall('w:tr', ns)
    set_cell_text(t25_rows[0].findall('w:tc', ns)[1], 'SJIBL/MIR/PO/2026/04812, Date: 11/10/2026')
    set_cell_text(t25_rows[1].findall('w:tc', ns)[1], 'BDT 25,000/- (Taka Twenty-Five Thousand Only)')
    set_cell_text(t25_rows[2].findall('w:tc', ns)[1], 'Shahjalal Islami Bank PLC')
    set_cell_text(t25_rows[3].findall('w:tc', ns)[1], 'Mirpur Branch, Dhaka')

    # Bid Form text replacements in paragraphs
    paragraphs = tree.findall('.//w:p', ns)
    for p in paragraphs:
        txt = ''.join(p.itertext())
        if 'within . (.) days' in txt or 'within ……………….…… (………….) days' in txt:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'We undertake, if our bid is accepted, to Procurement, supply, implementation, Integration and support of a Litigation Management System (LMS), including software licenses and Annual Maintenance Contract (AMC) for Bank Asia PLC. within 112 (One Hundred Twelve) days after receiving and accepting the work order. We agree to abide by this tender document, which will remain valid up to October 11, 2027.'
        
        elif 'Dated this day of 2026' in txt or 'Dated this ………………………………………day of' in txt:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'Dated this 11th day of October 2026'

        elif 'Seal with Signature of the authorized official' in txt:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = 'K. M. ABIR MAHMUD, Chief Executive Officer, Skoder Technologies (Authorized Signatory & Seal)'

        elif '1.' in txt and 'Witness' not in txt and len(txt.strip()) < 10:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = '1. Fahad Morshed, Chief Intelligence Officer, Skoder Technologies, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207'

        elif '2.' in txt and 'Witness' not in txt and len(txt.strip()) < 10:
            for r in p.findall('w:r', ns):
                p.remove(r)
            r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
            t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            t.text = '2. Imran Bipu, Head of Business Operations, Skoder Technologies, E-14/X, ICT Tower (14th Floor), Agargaon, Dhaka-1207'

    # Save back
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
    print('Updated RFP_LMS Bank Asia_v0.3.docx successfully!')

if __name__ == '__main__':
    update_rfp()
