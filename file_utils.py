import fitz  # PyMuPDF

def extract_text_from_pdfs(uploaded_files):
    """Extracts and concatenates text from multiple uploaded PDFs."""
    extracted_text = ""
    for uploaded_file in uploaded_files:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                extracted_text += page.get_text("text") + "\n\n"
    return extracted_text
