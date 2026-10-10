import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def update_tc(tc, text, bold=False, italic=False, font_size=8.5):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    p_elements = tc.findall('w:p', ns)
    if not p_elements:
        p = parse_xml(f'<w:p {nsdecls("w")}/>')
        tc.append(p)
    else:
        p = p_elements[0]
        for extra in p_elements[1:]:
            tc.remove(extra)
    
    # Remove existing runs
    for r in p.findall('w:r', ns):
        p.remove(r)
    
    b_tag = '<w:b/>' if bold else ''
    i_tag = '<w:i/>' if italic else ''
    sz_val = int(font_size * 2)
    run_xml = (
        f'<w:r {nsdecls("w")}>'
        f'<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>'
        f'<w:sz w:val="{sz_val}"/>{b_tag}{i_tag}</w:rPr>'
        f'<w:t>{text}</w:t>'
        f'</w:r>'
    )
    p.append(parse_xml(run_xml))

print("update_tc ready.")
