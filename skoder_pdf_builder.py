import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Image as PlatypusImage
)

# Register Calibri fonts from Windows Fonts directory
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
try:
    pdfmetrics.registerFont(TTFont('Calibri', os.path.join(FONTS_DIR, 'calibri.ttf')))
    pdfmetrics.registerFont(TTFont('Calibri-Bold', os.path.join(FONTS_DIR, 'calibrib.ttf')))
    pdfmetrics.registerFont(TTFont('Calibri-Italic', os.path.join(FONTS_DIR, 'calibrii.ttf')))
    pdfmetrics.registerFont(TTFont('Calibri-BoldItalic', os.path.join(FONTS_DIR, 'calibriz.ttf')))
    FONT_NORMAL = 'Calibri'
    FONT_BOLD = 'Calibri-Bold'
    FONT_ITALIC = 'Calibri-Italic'
except Exception as e:
    print(f"Warning: could not register Calibri ({e}), falling back to Helvetica")
    FONT_NORMAL = 'Helvetica'
    FONT_BOLD = 'Helvetica-Bold'
    FONT_ITALIC = 'Helvetica-Oblique'

REF_ASSETS_DIR = 'ref_assets'
LOGO_PATH = os.path.join(REF_ASSETS_DIR, 'Image23.png')
PHONE_ICON = os.path.join(REF_ASSETS_DIR, 'Image27.png')
WEB_ICON = os.path.join(REF_ASSETS_DIR, 'Image29.png')
EMAIL_ICON = os.path.join(REF_ASSETS_DIR, 'Image25.png')
SEAL_PATH = os.path.join('extracted_assets', 'Image23.jpg')
SIGNATURE_PATH = os.path.join('extracted_assets', 'Image24.jpg')

class SkoderPadCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_skoder_pad(self._pageNumber, num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_skoder_pad(self, page_num, total_pages):
        width, height = A4

        # -------------------------------------------------------------
        # HEADER (Exact coordinates from reference/skoder pad.pdf)
        # -------------------------------------------------------------
        # Logo on left: x=49.6, y=780.97, w=131.55, h=44.65
        if os.path.exists(LOGO_PATH):
            self.drawImage(LOGO_PATH, 49.6, 780.97, width=131.55, height=44.65, preserveAspectRatio=True, mask='auto')

        # Company Name: Calibri-Bold 14.04 pt, Color: rgb(0, 0.69, 0.314) #00b050
        self.setFont(FONT_BOLD, 14.04)
        self.setFillColor(colors.HexColor('#00b050'))
        self.drawRightString(580.92, 816.0, 'SKODER TECHNOLOGIES')

        # Address: Calibri 12.0 pt, Color: rgb(0.753, 0, 0) #c00000
        self.setFont(FONT_NORMAL, 12.0)
        self.setFillColor(colors.HexColor('#c00000'))
        self.drawRightString(580.92, 799.56, 'ICT Tower: E-14/X, Agargaon, Dhaka 1207')

        # BIN & Trade: Calibri-Bold 9.96 pt, Color: rgb(0, 0.439, 0.753) #0070c0
        self.setFont(FONT_BOLD, 9.96)
        self.setFillColor(colors.HexColor('#0070c0'))
        self.drawRightString(580.92, 785.64, 'BIN# 002855793-0401  Trade# DNCC-056205/2022')

        # -------------------------------------------------------------
        # FOOTER (Exact coordinates from reference/skoder pad.pdf)
        # -------------------------------------------------------------
        # Page Number: Calibri 8.04 pt, Black, x=54.96, y=63.72
        self.setFont(FONT_NORMAL, 8.04)
        self.setFillColor(colors.black)
        self.drawString(54.96, 63.72, f'Page | {page_num}')

        # Phone Icon & Text: Icon x=72.0, y=25.826, w=18.4, h=18.4
        if os.path.exists(PHONE_ICON):
            self.drawImage(PHONE_ICON, 72.0, 25.826, width=18.4, height=18.4, preserveAspectRatio=True, mask='auto')
        self.setFont(FONT_BOLD, 11.04)
        self.setFillColor(colors.HexColor('#2c8469')) # rgb(0.173, 0.518, 0.412)
        self.drawString(94.0, 31.2, '+88 01750 726094')

        # Web Icon & Text: Icon x=262.5, y=27.476, w=14.45, h=14.45
        if os.path.exists(WEB_ICON):
            self.drawImage(WEB_ICON, 262.5, 27.476, width=14.45, height=14.45, preserveAspectRatio=True, mask='auto')
        self.setFont(FONT_BOLD, 11.04)
        self.setFillColor(colors.HexColor('#2c8469'))
        self.drawString(283.01, 32.52, 'www')
        self.setFillColor(colors.HexColor('#c00000'))
        self.drawString(307.15, 32.52, '.skoder.')
        self.setFillColor(colors.HexColor('#2f5496')) # rgb(0.184, 0.329, 0.588)
        self.drawString(342.79, 32.52, 'co')

        # Email Icon & Text: Icon x=447.2, y=28.576, w=13.5, h=13.6
        if os.path.exists(EMAIL_ICON):
            self.drawImage(EMAIL_ICON, 447.2, 28.576, width=13.5, height=13.6, preserveAspectRatio=True, mask='auto')
        self.setFont(FONT_BOLD, 11.04)
        self.setFillColor(colors.HexColor('#2f5496'))
        self.drawString(466.42, 31.92, 'contact@skoder.co')

def get_signature_block():
    sig_img = PlatypusImage(SIGNATURE_PATH, width=95, height=48) if os.path.exists(SIGNATURE_PATH) else Paragraph("[Signature]", None)
    seal_img = PlatypusImage(SEAL_PATH, width=65, height=65) if os.path.exists(SEAL_PATH) else Paragraph("[Seal]", None)
    
    label_p = Paragraph(f"<font fontName='{FONT_BOLD}' size=11 color='#000000'>K. M. ABIR MAHMUD</font><br/><font fontName='{FONT_NORMAL}' size=9.5 color='#333333'>Chief Executive Officer<br/><font fontName='{FONT_BOLD}' size=10 color='#00b050'>SKODER TECHNOLOGIES</font></font>", None)

    table_data = [
        [sig_img, seal_img],
        [label_p, ""]
    ]
    sig_table = Table(table_data, colWidths=[120, 80])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('SPAN', (0,1), (1,1)),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    return sig_table

def build_pdf_document(filename, story):
    # Printable area:
    # Top margin: 80 pt (leaves space below header text at y=785)
    # Bottom margin: 76 pt (leaves space above footer text at y=64)
    # Left margin: 54 pt, Right margin: 54 pt
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=80,
        bottomMargin=76
    )
    doc.build(story, canvasmaker=SkoderPadCanvas)
    print(f"Generated: {filename}")
