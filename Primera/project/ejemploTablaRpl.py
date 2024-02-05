from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table

hojaEstilo = getSampleStyleSheet()

elementoDoc = []

imagen = Image("mario.png")
datos = [['Empresas', 'candidato1', 'candidato2', 'Especialidad'],
         ['Ayco', 'Marcos', 'Ruben', 'desemvolvimiento web con php'],
         ['Iterat', 'borja', 'juan', 'Reconocimiento de imagen'],
         [['Optare', imagen], 'Lidier', 'Lucas', 'Aplicacion para Telco']]

estilo = [('TEXTCOLOR', (0, 0), (0, -1), colors.white),
          ('TEXTCOLOR', (1, 0), (-1, 0), colors.blue),
          ('TEXTCOLOR', (1, 1), (-1, -1), colors.blueviolet),
          ('BOX', (1, 1), (-1, -1), 1.25, colors.grey),
          ('INNERGRID', (1, 1), (-1, -1), 1.25, colors.lightgrey),
          ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]

tabla = Table(data=datos)
tabla.setStyle(estilo)

elementoDoc.append(tabla)
