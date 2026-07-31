import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """
    Extract text from an image using OCR.
    """
    try:
        image = cv2.imread(image_path)

        if image is None:
            return "Error: Image not found."

        text = pytesseract.image_to_string(image)
        return text

    except Exception as e:
        return f"Error: {e}"


# Test
if __name__ == "__main__":
    image_path = "sample_data/sample_image.png"

    extracted_text = extract_text_from_image(image_path)

    print("===== EXTRACTED TEXT =====")
    print(extracted_text)