#this is a tool to find all timestamps in a PDF & bookmark them, making it easier to go through a timeline
import PyPDF2
import datefinder

def add_bookmarks(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()

    # Copy all pages from reader to writer
    for page in reader.pages:
        writer.add_page(page)

    bookmarks = {}

    # Extract text and find dates on each page
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            matches = datefinder.find_dates(text, source=True)
            for match, _ in matches:
                # Format the date in a readable form
                date_str = match.strftime("%Y-%m-%d")
                if date_str not in bookmarks:
                    bookmarks[date_str] = []
                bookmarks[date_str].append(i)

    # Sort dates and add bookmarks
    for date in sorted(bookmarks.keys()):
        for page_num in bookmarks[date]:
            writer.add_outline_item(date, page_num)

    # Save the new PDF with bookmarks
    with open("bookmarked_pdf.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

add_bookmarks("output_reduced_no_empty_or_duplicate_pages.pdf")
