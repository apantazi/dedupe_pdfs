import PyPDF2

def remove_duplicates(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()

    seen_pages = set()
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        content = page.extract_text()
        if content not in seen_pages:
            seen_pages.add(content)
            writer.add_page(page)

    with open("output.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

remove_duplicates("Emails.pdf")
