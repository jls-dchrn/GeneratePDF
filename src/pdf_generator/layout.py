from reportlab.platypus import Paragraph, Spacer
import lorem

def generate_paragraph(style, word_count=100):
    words = lorem.text().split()[:word_count]
    return Paragraph(" ".join(words), style)

def add_paragraphs(count, style, spacing=10):
    elements = []
    for _ in range(count):
        elements.append(generate_paragraph(style))
        elements.append(Spacer(1, spacing))
    return elements
