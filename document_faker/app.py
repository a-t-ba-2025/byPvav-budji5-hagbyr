from docxtpl import DocxTemplate
import os
import random
import time
import html
from fakefile import generate_data
from pdf2image import convert_from_path
from PIL import Image
import comtypes.client
from fpdf import FPDF 
from tqdm import tqdm

base_dir = os.path.abspath('generated_documents')
pdf_text_dir = os.path.join(base_dir, 'pdf_text')
doc_dir = os.path.join(base_dir, 'doc')
png_dir = os.path.join(base_dir, 'png')

os.makedirs(base_dir, exist_ok=True)
os.makedirs(pdf_text_dir, exist_ok=True)
os.makedirs(doc_dir, exist_ok=True)
os.makedirs(png_dir, exist_ok=True)

blueprint_folder = os.path.abspath('blueprints')

# Masking special characters
def escape_xml_chars(data):
    if isinstance(data, dict):
        return {key: html.escape(str(value)) if isinstance(value, str) else value for key, value in data.items()}
    return data

# Generate PDF from DOCX
def export_docx_to_pdf_comtypes(docx_path, pdf_path):
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(docx_path)
        doc.SaveAs(pdf_path, FileFormat=17)  # 17 = wdFormatPDF
        doc.Close(False)
    except Exception as e:
        print(f"Error processing: {e}")
    finally:
        word.Quit()

# PDF -> PNG (300 DPI)
def convert_pdf_to_png(pdf_path, output_path):
    try:
        images = convert_from_path(pdf_path, dpi=300)
        images[0].save(output_path, 'PNG')
    except Exception as e:
        print(f"Error processing: {e}")

# Quantity of Documents to be generated
r = 3

start_time = time.time()

for i in tqdm(range(r), desc="Generate Documents", unit="File"):
    # random_vorlage = str(random.randint(1, 87)) + ".docx" # use random template
    # random_vorlage = str(42) + ".docx"   # use specific template
    used_blueprint = f"{i + 1}.docx"
    vorlage_datei = os.path.join(blueprint_folder, used_blueprint)
    doc = DocxTemplate(vorlage_datei)

    daten = generate_data()
    daten = escape_xml_chars(daten)

    try:
        doc.render(daten)
    except Exception as e:
        print(f"Error rendering template: {used_blueprint}: {e}")
        continue

    docx_filename = f"{i + 1}.docx"
    pdf_text_filename = f"pdf_text_{i + 1}.pdf"
    png_filename = f"png_{i + 1}.png"
    pdf_image_filename = f"pdf_image_{i + 1}.pdf"

    docx_path = os.path.join(doc_dir, docx_filename)
    pdf_text_path = os.path.join(pdf_text_dir, pdf_text_filename)
    png_path = os.path.join(png_dir, png_filename)

    # DOCX
    doc.save(docx_path)

    # generate PDF  (invisible)
    export_docx_to_pdf_comtypes(docx_path, pdf_text_path)

    # generate PNG
    convert_pdf_to_png(pdf_text_path, png_path)



end_time = time.time()
print(f"\nFertig: {r} documents generated in {end_time - start_time:.2f} seconds.")
