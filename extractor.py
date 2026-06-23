import fitz
from docx import Document
from PIL import Image
import pytesseract
import os

# Change if your Tesseract path is different
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def read_pdf(path):
    try:
        doc = fitz.open(path)

        text = ""

        for page in doc[:3]:
            text += page.get_text()

        return text[:3000]

    except Exception as e:
        print(f"PDF Error: {e}")
        return ""

def read_docx(path):
    try:
        doc = Document(path)

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

        return text[:3000]

    except Exception as e:
        print(f"DOCX Error: {e}")
        return ""

def read_txt(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()[:3000]

    except Exception as e:
        print(f"TXT Error: {e}")
        return ""

def read_image(path):
    try:
        img = Image.open(path)

        text = pytesseract.image_to_string(img)

        return text[:2000]

    except Exception as e:
        print(f"OCR Error: {e}")
        return ""

def extract_content(filepath):

    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        return read_pdf(filepath)

    elif ext == ".docx":
        return read_docx(filepath)

    elif ext == ".txt":
        return read_txt(filepath)

    elif ext in [".jpg", ".jpeg", ".png"]:
        return read_image(filepath)

    return ""