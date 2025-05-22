import click
from .builder import build_pdf
import time

@click.command()
@click.option(
    "--pages",
    default=3,
    type=int,
    help="Number of pages in the PDF document."
)
@click.option(
    "--tables",
    default=5,
    type=int,
    help="Total number of tables to include across all pages."
)
@click.option(
    "--output",
    default="output.pdf",
    type=click.Path(),
    help="Path to the output PDF file."
)
def generate_pdf(pages, tables, output):
    """Generate a PDF document with a given number of pages and tables."""
    print(f"Generating PDF with {pages} pages and {tables} tables...")
    start = time.time()
    path, success, actual = build_pdf(pages, tables, output)
    duration = time.time() - start

    if success:
        print(f"✅ PDF generated: {path} ({actual} pages) in {duration:.2f}s")
    else:
        print(f"⚠️ Page mismatch: expected {pages}, got {actual}")
