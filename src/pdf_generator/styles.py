from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

def get_styles():
    base = getSampleStyleSheet()
    """
    [leading]: spacing between lines  
    [spaceAfter]: space after each paragraph
    """
    styles = {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontSize=16,
            leading=20,      
            alignment=TA_CENTER,
            spaceAfter=12      
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontSize=11,
            leading=14,         
            alignment=TA_JUSTIFY,
            spaceAfter=6         
        ),
    }
    return styles


def get_style_metrics(styles):
    """
    Returns computed metrics based on styles, so layout logic stays clean and centralized.
    """
    title_style = styles["title"]
    body_style = styles["body"]

    return {
        "font_size": body_style.fontSize,
        "line_height": body_style.leading,
        "paragraph_spacing": body_style.spaceAfter,
        "title_font_size": title_style.fontSize,
        "title_line_height": title_style.leading,
        "title_spacing": title_style.spaceAfter,
        "avg_char_width": 6,  # reasonable default for Helvetica-like fonts in 10-12pt
    }
