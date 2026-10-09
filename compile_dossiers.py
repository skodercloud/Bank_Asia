import os
from pypdf import PdfWriter, PdfReader

def compile_experience_dossier():
    writer = PdfWriter()
    
    cert_dir = 'certificates'
    files_order = [
        os.path.join(cert_dir, '3.1 Drutoloan Skoder Work completion certificate.pdf'),
        os.path.join(cert_dir, '3.2 VivaPe System Development Completion Certificate.pdf'),
        os.path.join(cert_dir, '3.3 JU noa comptroller office notification of Award skoder.pdf'),
        os.path.join(cert_dir, '3.4 BuseineeBee Skoder Work completion certificate-updated.pdf'),
        os.path.join(cert_dir, '3.5 OrbitMart-Skoder-Software-Development-Work-Order-updated.pdf'),
        os.path.join(cert_dir, '06_Project_ProbashiBazar_Ecommerce_Completion_Certificate.pdf'),
        os.path.join(cert_dir, 'sjib bank solvency 2026-09-06.pdf'),
        os.path.join(cert_dir, 'nbr_tin_certificate_327560545079 (1).pdf'),
        'BIN Certification Skoder.pdf',
        'Trade License Skoder renew 2026-2027 (1).pdf',
        'acknowledgement_abir_2024-2025.pdf',
    ]
    
    for f in files_order:
        if os.path.exists(f):
            try:
                reader = PdfReader(f)
                for page in reader.pages:
                    writer.add_page(page)
                print(f"Added {f} ({len(reader.pages)} pages)")
            except Exception as e:
                print(f"Error adding {f}: {e}")
        else:
            print(f"Warning: {f} not found")
            
    out_file = '03_Compiled_Past_Experience_and_Certificates_Bank_Asia.pdf'
    with open(out_file, 'wb') as f_out:
        writer.write(f_out)
    print(f"Compiled: {out_file}")

def compile_cvs_dossier():
    writer = PdfWriter()
    
    cv_dir = 'cv'
    cvs_order = [
        'K. M. ABIR MAHMUD.pdf',
        'Ali Haider Fahad.pdf',
        'Fahad Morshed.pdf',
        'Fahim Shahriar.pdf',
        'Shafkat.pdf',
        'BODRUNNAHER TOMA.pdf',
        'Md. Rafidul Islam.pdf',
        'Alamin.pdf',
        'Alfee Bin Ferdous.pdf'
    ]
    
    for cv in cvs_order:
        full_p = os.path.join(cv_dir, cv)
        if os.path.exists(full_p):
            try:
                reader = PdfReader(full_p)
                for page in reader.pages:
                    writer.add_page(page)
                print(f"Added CV: {cv} ({len(reader.pages)} pages)")
            except Exception as e:
                print(f"Error adding CV {cv}: {e}")
        else:
            print(f"Warning: CV {cv} not found")
            
    out_file = '04_Compiled_Key_Personnel_CVs_Bank_Asia.pdf'
    with open(out_file, 'wb') as f_out:
        writer.write(f_out)
    print(f"Compiled: {out_file}")

if __name__ == '__main__':
    compile_experience_dossier()
    compile_cvs_dossier()
