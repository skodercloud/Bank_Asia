import zipfile, os, html
import xml.etree.ElementTree as ET

def extract_tables_data():
    with zipfile.ZipFile('RFP_LMS Bank Asia_v0.3.docx') as z:
        xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    tables = tree.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl')
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    t11 = tables[10] # Tech spec
    t13 = tables[12] # Functional

    t11_rows = []
    for r in t11.findall('w:tr', ns):
        cells = [' '.join(c.itertext()).strip() for c in r.findall('w:tc', ns)]
        t11_rows.append(cells)

    t13_rows = []
    for r in t13.findall('w:tr', ns):
        cells = [' '.join(c.itertext()).strip() for c in r.findall('w:tc', ns)]
        t13_rows.append(cells)

    return t11_rows, t13_rows

def col_name(n):
    # n is 0-indexed
    s = ""
    while n >= 0:
        s = chr(n % 26 + 65) + s
        n = n // 26 - 1
    return s

def make_sheet_xml(rows):
    xml_parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
        '<sheetData>'
    ]
    for r_idx, row in enumerate(rows, start=1):
        xml_parts.append(f'<row r="{r_idx}">')
        for c_idx, cell in enumerate(row):
            col_letter = col_name(c_idx)
            cell_ref = f"{col_letter}{r_idx}"
            escaped_val = html.escape(str(cell))
            xml_parts.append(f'<c r="{cell_ref}" t="inlineStr"><is><t>{escaped_val}</t></is></c>')
        xml_parts.append('</row>')
    xml_parts.append('</sheetData></worksheet>')
    return ''.join(xml_parts)

def build_excel_file():
    t11_rows, t13_rows = extract_tables_data()

    sheet1_xml = make_sheet_xml(t11_rows)
    sheet2_xml = make_sheet_xml(t13_rows)

    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>'''

    pkg_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>'''

    workbook_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Technical_Specifications" sheetId="1" r:id="rId1"/>
    <sheet name="Functional_Requirements" sheetId="2" r:id="rId2"/>
  </sheets>
</workbook>'''

    wb_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
</Relationships>'''

    out_xlsx = 'Technical_and_Functional_Compliance_Matrix_Bank_Asia_LMS.xlsx'
    with zipfile.ZipFile(out_xlsx, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', content_types)
        z.writestr('_rels/.rels', pkg_rels)
        z.writestr('xl/workbook.xml', workbook_xml)
        z.writestr('xl/_rels/workbook.xml.rels', wb_rels)
        z.writestr('xl/worksheets/sheet1.xml', sheet1_xml)
        z.writestr('xl/worksheets/sheet2.xml', sheet2_xml)

    print(f"Generated Excel workbook: {out_xlsx}")

if __name__ == '__main__':
    build_excel_file()
