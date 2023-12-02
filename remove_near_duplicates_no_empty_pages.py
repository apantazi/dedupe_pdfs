import PyPDF2
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')

def jaccard_similarity(str1, str2):
    a = set(word_tokenize(str1))
    b = set(word_tokenize(str2))
    c = a.intersection(b)
    
    if len(a) + len(b) - len(c) == 0:
        return 0.0

    return float(len(c)) / (len(a) + len(b) - len(c))

def remove_scattered_duplicates_and_empty_pages(pdf_path, similarity_threshold=0.95):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()

    seen_content = []
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        content = page.extract_text() or ""  # Ensure content is not None

        # Skip the page if it is empty
        if not content.strip():
            continue

        is_duplicate = False
        for seen in seen_content:
            if jaccard_similarity(content, seen) >= similarity_threshold:
                is_duplicate = True
                break

        # Add the page if it's not a duplicate
        if not is_duplicate:
            writer.add_page(page)
            seen_content.append(content)

    # Save the new PDF without duplicates and empty pages
    with open("output_reduced_no_empty_or_duplicate_pages.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

remove_scattered_duplicates_and_empty_pages("Emails.pdf")
