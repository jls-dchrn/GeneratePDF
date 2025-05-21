from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

def get_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title", parent=base["Title"], fontSize=16, alignment=TA_CENTER, spaceAfter=10
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontSize=11, alignment=TA_JUSTIFY, spaceAfter=6
        ),
    }
