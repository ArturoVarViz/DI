from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = []
imagen = Image(400, 0, 300, 281, "mario.png")
dibujo = Drawing(A4[0], A4[1])
dibujo.add(imagen)

dibujo.translate(0, 700)
imagenes.append(dibujo)

dibujo = Drawing(A4[0], A4[1])
dibujo.add(imagen)
dibujo.rotate(45)
dibujo.scale(1.5, 0.5)
dibujo.translate(-90, 300)
imagenes.append(dibujo)

dibujo = Drawing(A4[0], A4[1])

for i in range(len(imagenes)):
    dibujo.add(imagenes[i])

renderPDF.drawToFile(dibujo, "imagen.pdf")
