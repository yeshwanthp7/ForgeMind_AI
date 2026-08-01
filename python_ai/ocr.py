import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path):

    try:
        print("\n===== OCR MODULE =====")
        print("Input Image:", image_path)

        # Read image
        image = cv2.imread(image_path)

        if image is None:
            return "Error: Image not found."

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Improve text visibility
        threshold = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        # OCR
        text = pytesseract.image_to_string(threshold)

        print("\nExtracted Text:")
        print(text)

        return text.strip()

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":

    image_path = "sample_data/sample_image.png"

    extracted_text = extract_text_from_image(image_path)

    print("\n===== FINAL OCR OUTPUT =====")
    print(extracted_text)