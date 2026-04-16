import markdown
from weasyprint import HTML
from datetime import datetime

from ..core.config import OUTPUT_DIR


def export_to_pdf(report_text: str, filename: str = "Reporte_Pentest.pdf") -> str:
    html_content = markdown.markdown(report_text, extensions=["tables", "fenced_code"])

    css_style = """
    @page {
        size: A4;
        margin: 2cm;
        background-color: #ffffff;
        @bottom-right {
            content: "Página " counter(page) " de " counter(pages);
            font-size: 9pt;
        }
    }
    body {
        font-family: 'Helvetica', sans-serif;
        color: #2c3e50;
        line-height: 1.5;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        border-bottom: 2px solid #2c3e50;
        padding-bottom: 10px;
        margin-bottom: 50px;
    }
    h2 {
        color: #e74c3c;
        border-left: 5px solid #e74c3c;
        padding-left: 10px;
        margin-top: 30px;
    }
    h3 {
        color: #2980b9;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    th, td {
        border: 1px solid #bdc3c7;
        padding: 10px;
        text-align: left;
        font-size: 10pt;
    }
    th {
        background-color: #34495e;
        color: white;
    }
    pre, code {
        background-color: #f4f4f4;
        color: #c7254e;
        font-family: 'Courier New', monospace;
        padding: 5px;
        border-radius: 3px;
    }
    blockquote {
        border-left: 4px solid #7f8c8d;
        padding-left: 15px;
        color: #7f8c8d;
        font-style: italic;
    }
    """

    full_html = f"""
    <html>
    <head>
        <style>{css_style}</style>
    </head>
    <body>
        <div style="text-align: center;">
            <p style="color: #7f8c8d; font-size: 10pt;">INFORME TÉCNICO DE PENTESTING - PROYECTO RAG</p>
        </div>
        {html_content}
        <div style="margin-top: 50px; font-size: 8pt; color: #bdc3c7; text-align: center;">
            Generado automáticamente el {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        </div>
    </body>
    </html>
    """

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    full_path = OUTPUT_DIR / filename
    HTML(string=full_html).write_pdf(str(full_path))
    print(f"[+] Document generated: {full_path}")

    return str(full_path)
