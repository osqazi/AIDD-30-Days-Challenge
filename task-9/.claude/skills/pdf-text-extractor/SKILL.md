---
name: "pdf-text-extractor"
description: "Extract text from uploaded PDF files (searchable or scanned/image-based) using OCR when needed. Perfect for books, research papers, contracts, or any document."
version: "1.0.0"
---

# PDF Text Extractor Skill

## When to Use This Skill
- User uploads a PDF and asks to extract, read, or convert its text
- User says: “extract text from this PDF”, “OCR this document”, “what does this file say?”, “turn this PDF into text”
- The PDF is scanned, image-based, or contains mixed content

## How This Skill Works
1. Detect the uploaded PDF file
2. Run the companion Python tool (pdf_extractor_tool.py) via code_execution
3. Automatically fall back to high-quality OCR (Tesseract) for non-selectable pages
4. Return clean, full text with clear notes about which pages needed OCR

## Output Format
- **Source File**: Name of the processed PDF  
- **Total Pages**: Number of pages processed  
- **Extracted Text** (full continuous text)  
- **OCR Notes**: List of pages that required OCR + any warnings

## Example

**Input**: User uploads `novel_chapter_scanned.pdf` and says “Please extract all the text”

**Output**:
- **Source File**: novel_chapter_scanned.pdf  
- **Total Pages**: 18  
- **Extracted Text**:
    Chapter VII – The Hidden Door
    Elizabeth had never believed in ghosts until that rainy Tuesday...
    [continues with full novel text] 
- **OCR Notes**: OCR applied to pages 3–18 (scanned images). Text pages 1–2 extracted natively. 