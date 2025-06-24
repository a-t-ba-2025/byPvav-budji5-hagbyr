# Document Faker 

This module creates fully populated `.docx`, `.pdf`, and `.png` documents from dynamic LaTeX-style Word templates (`.docx`). randomized data provided by the `Faker` library. It is designed to simulate realistic government- or business-like paperwork for testing document processing pipelines.

---

## Project Structure

```
document_faker/
├── app.py                        # Main generation script
├── fakefile.py                  # Generates random German-language data
├── requirements.txt             # Dependencies for Faker, DocxTPL, PDF, etc.
├── blueprints/                  # .docx templates with Jinja-style placeholders
│   ├── 1.docx, 2.docx, ...      # Sample templates
└── generated_documents/
    ├── doc/                     # Output .docx files
    ├── pdf_text/                # Exported PDF files (with selectable text)
    ├── png/                     # Rendered image previews of PDF files
```

---

## How to Use

1. **Install Dependencies**

Use a virtual environment and install all required packages:

```bash
pip install -r requirements.txt
```

---

2. **Place Templates**

Add your `.docx` templates with `{{ placeholder }}` fields into the `blueprints/` folder.

Placeholders will be filled using `faker`-generated data (see `fakefile.py`).

---

3. **Generate Documents**

Run the generation script:

```bash
python app.py
```

This will:
- Select `blueprints/1.docx`, `2.docx`, ... as template
- Render it using randomly generated fields (`{{ name1 }}`, `{{ email2 }}`, etc.)
- Save:
  - `.docx` to `generated_documents/doc/`
  - `.pdf` to `generated_documents/pdf_text/`
  - `.png` preview (from PDF) to `generated_documents/png/`

You can configure how many documents are created via the `r = ...` variable inside `app.py`.

---

## Template Syntax

Templates use Jinja-style placeholders, e.g.:

```docx
Sehr geehrte/r {{ name1 }},

Ihre Rechnung über {{ betrag2 }} € ist zum {{ datum1 }} fällig.
```

See `fakefile.py` for available placeholder keys (e.g. `name1`, `ort2`, `betrag4`, `email5`, ...). Each `X` ranges from 1 to 10.

---

Note:
- `comtypes` is used for DOCX → PDF export (requires Microsoft Word on Windows)
- `pdf2image` and `Pillow` are used to convert PDFs to PNG

---

## Notes

- Works on Windows with installed Microsoft Word (via `comtypes`)
- You may adapt `fakefile.py` to customize fields, categories, vocabularies etc.
- PDF output contains **real text**, PNGs are **image renders** (useful for OCR benchmarking)

---

## Example Output

Generated files will appear like:

```
generated_documents/
├── doc/
│   ├── 1.docx
│   ├── 2.docx
├── pdf_text/
│   ├── pdf_text_1.pdf
│   ├── pdf_text_2.pdf
├── png/
│   ├── png_1.png
│   ├── png_2.png
```

---

## Author
Part of Bachelor's thesis  
Anna M. T., June 2025
