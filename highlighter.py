#this is a tool to find all timestamps in a PDF & highlight them, making it easier to go through a timeline
import pdfplumber
import fitz  # PyMuPDF
import re

def highlight_dates(pdf_path, output_path):
    date_positions = []  # Store tuples of (page number, bbox)
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            for match in re.finditer(r'\d{2,4}[-/]\d{1,2}[-/]\d{1,4}', text):
                # Check if page.chars is available and structured as expected
                if not hasattr(page, 'chars') or not isinstance(page.chars, list):
                    continue

                char_bboxes = [char['bbox'] for char in page.chars if 'bbox' in char and match.start() <= char['x0'] < match.end()]
                if char_bboxes:
                    x0, y0 = min(bbox[0] for bbox in char_bboxes), min(bbox[1] for bbox in char_bboxes)
                    x1, y1 = max(bbox[2] for bbox in char_bboxes), max(bbox[3] for bbox in char_bboxes)
                    overall_bbox = (x0, y0, x1, y1)
                    date_positions.append((i, overall_bbox))

    # Highlight these dates in the PDF with PyMuPDF
    doc = fitz.open(pdf_path)
    for page_num, bbox in date_positions:
        page = doc.load_page(page_num)
        annot = page.add_highlight_annot(bbox)
        annot.update()

    # Save the modified PDF
    doc.save(output_path)

highlight_dates("bookmarked_pdf.pdf", "highlighted_dates.pdf")
