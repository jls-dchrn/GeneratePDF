import os
from reportlab.platypus import SimpleDocTemplate, PageBreak
from reportlab.lib.pagesizes import letter
from .styles import get_styles
from .layout import add_paragraphs
from .tables import generate_table
from PyPDF2 import PdfReader

def build_pdf(filename, page_count=5, paragraphs_per_page=3, tables_per_doc=2, output_dir="pdf_files"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)
    margin = 54
    doc = SimpleDocTemplate(filepath, pagesize=letter,
                            rightMargin=margin, leftMargin=margin,
                            topMargin=margin, bottomMargin=margin)

    styles = get_styles()
    width = letter[0] - 2 * margin
    story = []

    tables_inserted = 0
    for page in range(page_count):
        story.extend(add_paragraphs(paragraphs_per_page, styles["body"]))

        if tables_inserted < tables_per_doc:
            story.append(generate_table(width=width))
            tables_inserted += 1

        if page < page_count - 1:
            story.append(PageBreak())

    doc.build(story)

    # Page count check
    actual = len(PdfReader(filepath).pages)
    return filepath, actual == page_count, actual
