from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, SimpleDocTemplate

hojaEstilo = getSampleStyleSheet()

elementos = []

temperaturas = [['','enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
                ['maxima', 15, 16, 20, 25, 27, 30, 31, 32, 33, 34, 28, 23],
                ['minima', -3, -4, -1, 4, 6, 9, 12, 15, 16, 1, 2, -2]]

estilo = [('TEXTCOLOR', (1, 1), (1, -1), colors.grey),
          ('TEXTCOLOR', (1, 1), (1, -1), colors.grey),
          ('BOX', (1, 1), (-1, -1), 1.50, colors.grey),
          ('INNERGRID', (1, 1), (-1, -1), 0.5, colors.white)]

for i, fila in enumerate(temperaturas):
    for j, columna in enumerate(fila):
        if i > 0 and j > 0:  # Ignoramos la primera fila y la primera columna
            temp = temperaturas[i][j]
            if temp > 0:
                estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.black))
                if temp > 30:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.red))
                elif temp <= 30 and temp > 20:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange))
                elif temp <= 20 and temp > 10:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
                elif temp <= 10 and temp > 0:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.blue))
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))

tabla = Table(data=temperaturas)
tabla.setStyle(estilo)

elementos.append(tabla)

# Crear un documento PDF y añadir la tabla
doc = SimpleDocTemplate("tabla_temperaturas.pdf", pagesize=A4)
doc.build(elementos)  # elementos es una lista que contiene tu tabla
