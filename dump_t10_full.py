import docx

doc = docx.Document('RFP_LMS Bank Asia_v0.3_backup.docx')
t10 = doc.tables[10]
with open('t10_full_details.txt', 'w', encoding='utf-8') as f:
    for idx, r in enumerate(t10.rows):
        cells = [c.text.strip().replace('\r\n', ' ').replace('\n', ' ') for c in r.cells]
        # dedup
        dedup = []
        for c in cells:
            if not dedup or dedup[-1] != c:
                dedup.append(c)
        f.write(f"Index {idx:02d}: {dedup}\n")

print("Wrote t10_full_details.txt")
