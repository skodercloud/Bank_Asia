import docx

doc = docx.Document('RFP_LMS Bank Asia_v0.3_backup.docx')
t12 = doc.tables[12]

with open('t12_all_rows.txt', 'w', encoding='utf-8') as f:
    for idx in range(len(t12.rows)):
        r = t12.rows[idx]
        c0 = r.cells[0].text.strip().replace('\n', ' ')
        c1 = r.cells[1].text.strip().replace('\n', ' ')
        c2 = r.cells[2].text.strip().replace('\n', ' ')
        c3 = r.cells[3].text.strip().replace('\n', ' ')
        f.write(f"R{idx:03d} | c0='{c0}' | c1='{c1}' | c2='{c2}' | c3='{c3}'\n")

print(f"Dumped {len(t12.rows)} rows to t12_all_rows.txt")
