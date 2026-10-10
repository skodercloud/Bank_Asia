import zipfile, sys
import xml.etree.ElementTree as ET

with zipfile.ZipFile('RFP_LMS Bank Asia_v0.3_backup.docx') as z:
    xml_content = z.read('word/document.xml')

tree = ET.fromstring(xml_content)
tables = tree.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl')
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

t11 = tables[10]
with open('t11_rows.txt', 'w', encoding='utf-8') as f:
    for idx, r in enumerate(t11.findall('w:tr', ns)):
        cells = [' '.join(c.itertext()).strip() for c in r.findall('w:tc', ns)]
        c0 = cells[0] if len(cells) > 0 else ""
        c1 = cells[1] if len(cells) > 1 else ""
        c2 = cells[2] if len(cells) > 2 else ""
        c3 = cells[3] if len(cells) > 3 else ""
        f.write(f"Row {idx:02d} | len={len(cells)} | C0={c0} | C1={c1[:60]} | C2={c2} | C3={c3}\n")

print("Wrote t11_rows.txt")

t13 = tables[12]
with open('t13_rows.txt', 'w', encoding='utf-8') as f:
    for idx, r in enumerate(t13.findall('w:tr', ns)):
        cells = [' '.join(c.itertext()).strip() for c in r.findall('w:tc', ns)]
        c0 = cells[0] if len(cells) > 0 else ""
        c1 = cells[1] if len(cells) > 1 else ""
        c2 = cells[2] if len(cells) > 2 else ""
        c3 = cells[3] if len(cells) > 3 else ""
        f.write(f"Row {idx:03d} | len={len(cells)} | C0={c0} | C1={c1[:60]} | C2={c2} | C3={c3}\n")

print("Wrote t13_rows.txt")
