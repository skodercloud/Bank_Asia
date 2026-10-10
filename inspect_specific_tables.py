import docx

doc = docx.Document('RFP_LMS Bank Asia_v0.3_backup.docx')

for t_idx in [6, 7, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24]:
    t = doc.tables[t_idx]
    print(f"\n=================== TABLE {t_idx} (rows={len(t.rows)}) ===================")
    for r_i, r in enumerate(t.rows):
        cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
        dedup = []
        for c in cells:
            if not dedup or dedup[-1] != c:
                dedup.append(c)
        print(f"R{r_i}: {dedup}")
