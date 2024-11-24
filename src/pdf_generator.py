from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_pdf(output_path, text):
    """
    Genera un archivo PDF con el texto digitalizado.
    """
    try:
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter

        x_margin = 50 
        y_position = height - 50 

        lines = text.split('\n')
        for line in lines:
            c.drawString(x_margin, y_position, line)
            y_position -= 15 

            if y_position < 50:
                c.showPage()
                y_position = height - 50

        c.save()
        print(f"PDF generado exitosamente en: {output_path}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")
