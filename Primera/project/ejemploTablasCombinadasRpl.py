from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, SimpleDocTemplate

hojaEstilo = getSampleStyleSheet()

elementos = []


datos=[['Arriba\nIzquierda', '','02','03','04'],
       ['','','12','13','14'],['20','21','22','Ariba\nDerecha',''],
       ['30','31','32','','']]

estilo = [('BOX', (0, 0), (-1, -1), 1.50, colors.grey),('TEXTCOLOR', (0, 0), (-1, -1), colors.grey),
          ('BACKGROUND', (0,0), (1, 1), colors.lavender),
          ('SPAN', (0, 0), (1, 1)),

          ('BACKGROUND', (-2, -2), (-1,-1), colors.lavenderblush),
          ('SPAN', (-2,-2), (-1,-1))]



tabla = Table(data=datos)
tabla.setStyle(estilo)

elementos.append(tabla)

# Crear un documento PDF y añadir la tabla
doc = SimpleDocTemplate("tabla_span.pdf", pagesize=A4)
doc.build(elementos)  # elementos es una lista que contiene tu tabla
