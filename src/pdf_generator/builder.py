import random
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak, Paragraph
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader



from .tables import generate_table
from .layout import generate_paragraph_text
from .styles import get_styles, get_style_metrics

TABLE_ROW_HEIGHT = 25.0
LINE_PER_PARAGRAPH = 10

def distribute_items_across_pages(total_items, total_pages):
    """
    Distribute a number of items (e.g., tables) as evenly as possible across a fixed number of pages.
    """
    base = total_items // total_pages
    remainder = total_items % total_pages
    return [base + 1 if i < remainder else base for i in range(total_pages)]


def build_pdf(pages: int, total_tables: int, output_path: str):
    """
    Build a PDF document with the specified number of pages and tables.
    Paragraphs are generated dynamically to fill the space left by the tables on each page.
    """
    
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = get_styles()
    metrics = get_style_metrics(styles)
    elements = []

    # Page layout constants
    page_height = A4[1]
    page_width = A4[0]
    margin_top = margin_bottom = margin_right = margin_left =72  # 1 inch margins
    usable_height = page_height - margin_top - margin_bottom
    usable_width = page_width - margin_right - margin_left

    # Extracted metrics
    line_height = metrics["line_height"]
    paragraph_spacing = metrics["paragraph_spacing"]
    title_height = metrics["title_font_size"] + metrics["title_spacing"]
    avg_char_width = metrics["avg_char_width"]
    characters_per_line = int(usable_width / avg_char_width)

    # Distribute tables
    tables_per_page = distribute_items_across_pages(total_tables, pages)

    for page in range(pages):
 
        elements.append(Paragraph(f"Page {page + 1}", styles["title"]))


        num_tables = tables_per_page[page]
        table_size = [[random.randint(2, 4),random.randint(2, 5)] for _ in range(num_tables) ]
        estimated_table_height = sum(
            TABLE_ROW_HEIGHT*row + paragraph_spacing for _, row in table_size 
        )

        remaining_height = usable_height - title_height - estimated_table_height

        used_height = 0

        while remaining_height - used_height >= line_height * 2:
            base_lines = LINE_PER_PARAGRAPH
            para_height = base_lines * line_height + paragraph_spacing

            if used_height + para_height > remaining_height:
                lines_available = int((remaining_height - used_height) // line_height)
                if lines_available < 2:
                    break
                base_lines = lines_available
                para_height = base_lines * line_height + paragraph_spacing

            text = generate_paragraph_text(base_lines, characters_per_line)
            elements.append(Paragraph(text, styles["body"]))

            used_height += para_height

        for column,row in table_size:
            elements.append(Spacer(1, paragraph_spacing))
            elements.append(generate_table(columns=column, rows=row))

        if page < pages - 1:
            elements.append(PageBreak())

    doc.build(elements)
    # Page count check
    actual = len(PdfReader(output_path).pages)
    return output_path, actual == pages, actual