from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import lorem
import random

def generate_table(columns=3, rows=4, width=500):
    data = [["Header {}".format(i+1) for i in range(columns)]]
    for _ in range(rows):
        row = [" ".join(lorem.text().split()[:random.randint(2, 5)]) for _ in range(columns)]
        data.append(row)

    col_widths = [width / columns] * columns
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTSIZE", (0, 0), (-1, 0), 11),
        ("FONTSIZE", (0, 1), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return table
