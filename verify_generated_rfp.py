# -*- coding: utf-8 -*-
"""
verify_generated_rfp.py
Thorough verification of all tables and paragraphs in the generated RFP docx.
"""

import docx

doc = docx.Document('RFP_LMS Bank Asia_v0.3.docx')

print("=================== 1. VERIFY TABLE 6 (CRITERIA) ===================")
t6 = doc.tables[6]
for idx, r in enumerate(t6.rows):
    cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
    print(f"R{idx}: {cells}")

print("\n=================== 2. VERIFY TABLE 7 (SCORING MATRIX) ===================")
t7 = doc.tables[7]
for idx, r in enumerate(t7.rows):
    cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
    print(f"R{idx}: {cells}")

print("\n=================== 3. VERIFY TABLE 10 (TECHNICAL SPECS - FIRST & LAST 5 ROWS) ===================")
t10 = doc.tables[10]
for idx in [0, 1, 2, 3, 5, 87, 88, 89]:
    r = t10.rows[idx]
    cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
    # dedup
    dedup = []
    for c in cells:
        if not dedup or dedup[-1] != c:
            dedup.append(c)
    print(f"R{idx:02d}: {dedup}")

print("\n=================== 4. VERIFY TABLE 12 (FUNCTIONAL REQS - SAMPLE ROWS) ===================")
t12 = doc.tables[12]
for idx in [0, 1, 2, 3, 4, 10, 11, 80, 81, 110, 111, 407, 410, 411, 412]:
    r = t12.rows[idx]
    cells = [c.text.strip().replace('\n', ' ') for c in r.cells]
    dedup = []
    for c in cells:
        if not dedup or dedup[-1] != c:
            dedup.append(c)
    print(f"R{idx:03d}: {dedup}")

print("\n=================== 5. VERIFY TABLE 13 & 14 (TEAM) ===================")
t13 = doc.tables[13]
print(f"Table 13 rows: {len(t13.rows)}")
for idx in range(len(t13.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t13.rows[idx].cells]
    print(f"T13 R{idx}: {cells[:3]}")

t14 = doc.tables[14]
print(f"Table 14 rows: {len(t14.rows)}")
for idx in range(len(t14.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t14.rows[idx].cells]
    print(f"T14 R{idx}: {cells[:3]}")

print("\n=================== 6. VERIFY TABLE 15 (TRACK RECORD) ===================")
t15 = doc.tables[15]
for idx in range(len(t15.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t15.rows[idx].cells]
    print(f"T15 R{idx}: {cells}")

print("\n=================== 7. VERIFY TABLE 16 (HARDWARE) ===================")
t16 = doc.tables[16]
for idx in [0, 1, 2, 5, 7, 8, 11, 16, 20]:
    cells = [c.text.strip().replace('\n', ' ') for c in t16.rows[idx].cells]
    print(f"T16 R{idx}: {cells}")

print("\n=================== 8. VERIFY TABLE 17 (TRAINING) ===================")
t17 = doc.tables[17]
for idx in range(len(t17.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t17.rows[idx].cells]
    print(f"T17 R{idx}: {cells}")

print("\n=================== 9. VERIFY TABLE 19 & 20 (FINANCIALS) ===================")
t19 = doc.tables[19]
for idx in range(len(t19.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t19.rows[idx].cells]
    print(f"T19 R{idx}: {cells[:4]} ... {cells[-3:]}")

t20 = doc.tables[20]
for idx in range(len(t20.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t20.rows[idx].cells]
    print(f"T20 R{idx}: {cells}")

print("\n=================== 10. VERIFY TABLE 22, 23, 24 ===================")
t22 = doc.tables[22]
for idx in range(len(t22.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t22.rows[idx].cells]
    print(f"T22 R{idx}: {cells}")

t23 = doc.tables[23]
print(f"T23: {[c.text.strip().replace(chr(10), ' ') for c in t23.rows[0].cells]}")

t24 = doc.tables[24]
for idx in range(len(t24.rows)):
    cells = [c.text.strip().replace('\n', ' ') for c in t24.rows[idx].cells]
    print(f"T24 R{idx}: {cells}")

print("\n=================== 11. VERIFY BID FORM PARAGRAPHS ===================")
for i in range(518, 545):
    if i < len(doc.paragraphs):
        txt = doc.paragraphs[i].text.strip()
        if txt:
            print(f"P{i}: {txt}")

for i in range(570, len(doc.paragraphs)):
    txt = doc.paragraphs[i].text.strip()
    if txt:
        print(f"P{i}: {txt}")

print("\nAll verification checks complete!")
