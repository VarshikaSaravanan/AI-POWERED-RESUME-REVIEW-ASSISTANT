import pdfplumber



def extract_pdf_text(file_path):
    """
    Extracts text from a given PDF file.
    """
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"