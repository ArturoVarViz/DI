from reportlab.pdfgen import canvas

auxiliar = canvas.Canvas('primero.pdf')


auxiliar.drawString(0,0,"Position origen(X,Y) = (0,0)")

auxiliar.drawString(50,100,"Position destino(X,Y) = (50,100)")
auxiliar.drawString(150,20,"Position destino(X,Y) = (150,20)")
auxiliar.drawString(590,850,"Position destino(X,Y) = (150,20)")
auxiliar.drawImage("mario.png", 20,200,30,30)


auxiliar.showPage()
auxiliar.save()