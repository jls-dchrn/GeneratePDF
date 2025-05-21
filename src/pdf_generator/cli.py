import argparse
import time
from .builder import build_pdf

def main():
    parser = argparse.ArgumentParser(description="Generate structured PDFs with paragraphs and tables.")
    parser.add_argument("--pages", type=int, default=5, help="Number of pages")
    parser.add_argument("--paragraphs", type=int, default=3, help="Paragraphs per page")
    parser.add_argument("--tables", type=int, default=2, help="Tables per document")
    parser.add_argument("--output", type=str, default="generated.pdf", help="Output filename")
    parser.add_argument("--output-dir", type=str, default="pdf_files", help="Output directory")

    args = parser.parse_args()

    print(f"Generating '{args.output}' with {args.pages} pages, {args.paragraphs} paragraphs per page, and {args.tables} tables.")
    start = time.time()
    path, success, actual = build_pdf(
        filename=args.output,
        page_count=args.pages,
        paragraphs_per_page=args.paragraphs,
        tables_per_doc=args.tables,
        output_dir=args.output_dir,
    )
    duration = time.time() - start

    if success:
        print(f"✅ PDF generated: {path} ({actual} pages) in {duration:.2f}s")
    else:
        print(f"⚠️ Page mismatch: expected {args.pages}, got {actual}")
