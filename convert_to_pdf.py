"""
Convert PRESENTATION.md to PDF
Requires: pip install markdown2 pdfkit (and wkhtmltopdf installed)
"""

try:
    import markdown2
    import pdfkit

    # Read the markdown file
    with open('PRESENTATION.md', 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Convert markdown to HTML
    html = markdown2.markdown(markdown_text, extras=['tables', 'fenced-code-blocks'])

    # Add CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                page-break-before: always;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 5px;
                margin-top: 30px;
            }}
            h3 {{
                color: #7f8c8d;
                margin-top: 20px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            pre {{
                background-color: #2c3e50;
                color: #ecf0f1;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }}
            pre code {{
                background-color: transparent;
                color: #ecf0f1;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 20px;
                margin: 20px 0;
                color: #7f8c8d;
            }}
            hr {{
                border: none;
                border-top: 2px solid #3498db;
                margin: 30px 0;
            }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """

    # Configure PDF options
    options = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': 'UTF-8',
        'no-outline': None,
        'enable-local-file-access': None
    }

    # Convert to PDF
    pdfkit.from_string(styled_html, 'PRESENTATION.pdf', options=options)

    print("✓ PDF created successfully: PRESENTATION.pdf")

except ImportError as e:
    print("Error: Required libraries not installed")
    print("\nTo convert to PDF, you need to:")
    print("1. Install wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
    print("2. Install Python packages: pip install markdown2 pdfkit")
    print("\nOR use one of these alternative methods:")
    print("- Open PRESENTATION.md in VSCode and use 'Markdown PDF' extension")
    print("- Upload to https://www.markdowntopdf.com/")
    print("- Use online converter: https://cloudconvert.com/md-to-pdf")
    print("- Open in browser and print to PDF")

except Exception as e:
    print(f"Error creating PDF: {e}")
    print("\nAlternative: Open PRESENTATION.md in a markdown viewer and print to PDF")
