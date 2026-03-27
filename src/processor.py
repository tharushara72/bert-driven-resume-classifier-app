import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return clean_text(text)

def clean_text(text):
    # Basic NLP cleaning for BERT (Keep structure, remove noise)
    text = " ".join(text.split())  # Remove extra whitespaces
    return text