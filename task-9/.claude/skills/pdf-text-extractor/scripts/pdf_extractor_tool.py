
### 2. pdf_extractor_tool.py
# pdf_extractor_tool.py
# Save this exact file in your tools folder — it works with the pdf-text-extractor skill

import pdfplumber
import pytesseract
from PIL import Image
import os
import sys

def extract_text_from_pdf(file_path):
    if not os.path.exists(file_path):
        return None, "Error: File not found."

    full_text = []
    ocr_pages = []
    native_pages = []
    total_pages = 0

    with pdfplumber.open(file_path) as pdf:
        total_pages = len(pdf.pages)
        
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            
            # Try native text extraction first
            if text and text.strip():
                full_text.append(text)
                native_pages.append(i)
            else:
                # Fall back to OCR
                try:
                    # Convert page to high-res image
                    img = page.to_image(resolution=300).original
                    ocr_text = pytesseract.image_to_string(img, lang='eng')
                    if ocr_text.strip():
                        full_text.append(ocr_text)
                    else:
                        full_text.append(f"[Page {i}: No text detected]")
                    ocr_pages.append(i)
                except Exception as e:
                    full_text.append(f"[Page {i}: OCR failed — {str(e)}]")
                    ocr_pages.append(i)

    result_text = "\n\n".join(full_text)
    
    notes = []
    if native_pages:
        notes.append(f"Native text extraction: pages {', '.join(map(str, native_pages))}")
    if ocr_pages:
        notes.append(f"OCR applied: pages {', '.join(map(str, ocr_pages))}")
    if not native_pages and not ocr_pages:
        notes.append("No text could be extracted from any page.")

    summary = f"Source File: {os.path.basename(file_path)}\nTotal Pages: {total_pages}\n"
    summary += "\nOCR Notes: " + (" | ".join(notes) if notes else "Unknown error")

    return result_text, summary


# —————— Run only when executed directly (for testing) ——————
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_extractor_tool.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    text, info = extract_text_from_pdf(pdf_path)
    print("\n" + "="*60)
    print(info)
    print("="*60 + "\n")
    print(text)