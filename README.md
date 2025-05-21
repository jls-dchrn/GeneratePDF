# PDF Generator

A modular Python application to generate structured PDF files using `reportlab`. The output includes placeholder text, stylized sections, and optional tables.

## 📦 Features

- Modular codebase with separate components for layout, styles, and table generation.
- CLI interface for easy PDF creation with customizable parameters.
- Uses `lorem` for generating placeholder content.
- Output is cleanly structured with reusable blocks.

## 🗂️ Project Structure


```bash
├── README.md
├── pyproject.toml
├── pdf_files/ # Generated PDFs
└── src/
└── pdf_generator/
├── init.py
├── builder.py # Core logic to build the PDF
├── cli.py # Command-line interface
├── layout.py # PDF layout helpers
├── styles.py # Centralized style definitions
└── tables.py # Table generation logic
```


## 🚀 Installation

Make sure you have Python 3.8+ installed. Then, install the package locally:

```bash
pip install .
```
🛠️ Usage

Once installed, you can use the CLI to generate PDFs:

```bash
generate-pdf --pages 5 --paragraphs 3 --tables 2 --output pdf_files/example.pdf
```
CLI Options

| Argument       | Description                   | Default      |
| -------------- | ----------------------------- | ------------ |
| `--pages`      | Number of pages in the PDF    | `1`          |
| `--paragraphs` | Number of paragraphs per page | `2`          |
| `--tables`     | Number of tables per page     | `1`          |
| `--output`     | Output file path              | `output.pdf` |


🧪 Development

To run locally without installation:

```bash
python -m src.pdf_generator.cli --pages 2 --paragraphs 2 --output pdf_files/dev_test.pdf
```

📚 Dependencies

Managed in pyproject.toml:

    reportlab

    lorem

    PyPDF2

📝 License

MIT

---