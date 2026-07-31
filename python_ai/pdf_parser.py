import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extract text from all pages of a PDF.
    """
    text = ""

    try:
        pdf = fitz.open(pdf_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()
        return text

    except Exception as e:
        return f"Error reading PDF: {e}"


# Test the parser
if __name__ == "__main__":
    pdf_path = "sample_data/sample_report.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)

    print("========== EXTRACTED TEXT ==========")
    print(extracted_text)