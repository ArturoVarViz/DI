from reportlab.pdfgen import canvas

frase = ['esta es una frase', 'esta es una']

auxiliar = canvas.Canvas('ejemploTexto.pdf')
objetoTexto = auxiliar.beginText()
objetoTexto.setTextOrigin(100, 500)
objetoTexto.setFont('Courier', 16)
for linha in frase:
    objetoTexto.textLine(linha)

objetoTexto.setFillGray(0.5)

parrafo = '''cosasa que no se que escribir,
 como no se que escribir ,
no escribires lo que no se que escribo'''

objetoTexto.textLine(parrafo)
auxiliar.drawText(objetoTexto)
auxiliar.showPage()
auxiliar.save()
