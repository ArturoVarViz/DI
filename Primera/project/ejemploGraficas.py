from reportlab.graphics.charts.legends import LineLegend
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

# Crear datos de temperaturas
temperaturas = [
               ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
               [15, 16, 20, 28, 30, 32, 35, 36, 34, 30, 20, 18],
               [-3, -4, -1, 18, 20, 22, 25, 26, 24, 20, 2, -2]
               ]

# Graficas de barras
dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
grafica = VerticalBarChart() # Crear un objeto de tipo VerticalBarChart
grafica.x = 50 # Posición en x de la gráfica
grafica.y = 50 # Posición en y de la gráfica
grafica.height = 125 # Altura de la gráfica
grafica.width = 300 # Ancho de la gráfica
grafica.data = temperaturas[1:] # Datos de la gráfica donde 1: es para omitir la primera fila de la tabla
grafica.strokeColor = colors.black # Color del borde de la gráfica
grafica.valueAxis.valueMin = -5 # Valor mínimo del eje vertical de la gráfica
grafica.valueAxis.valueMax = 40 # Valor máximo del eje vertical de la gráfica
grafica.valueAxis.valueStep = 5 # Paso del eje vertical de la gráfica
grafica.categoryAxis.labels.boxAnchor = 'ne' # Posición de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.dx = 8 # Distancia en x de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.dy = -10 # Distancia en y de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.angle = 30 # Ángulo de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.categoryNames = temperaturas[0] # Nombres de las categorías del eje horizontal de la gráfica
grafica.groupSpacing = 10 # Espacio entre grupos de barras de la gráfica
grafica.barSpacing = 2 # Espacio entre barras de la gráfica
dibujo.add(grafica) # Agregar la gráfica al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

elementosDoc.append(Spacer(1, 12)) # Agregar un espacio en blanco a la lista de elementos

# Graficas de líneas
dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
grafica1 = HorizontalLineChart() # Crear un objeto de tipo HorizontalLineChart
grafica1.x = 30 # Posición en x de la gráfica
grafica1.y = 50 # Posición en y de la gráfica
grafica1.height = 125 # Altura de la gráfica
grafica1.width = 350 # Ancho de la gráfica
grafica1.data = [temperaturas[1]] # Datos de la gráfica de la serie de las temperaturas máximas si quiero que refleje las dos series debo colocar esto: grafica1.data = temperaturas[1:]
grafica1.categoryAxis.categoryNames = temperaturas[0] # Nombres de las categorías del eje horizontal de la gráfica
grafica1.categoryAxis.labels.angle = 30 # Ángulo de las etiquetas del eje horizontal de la gráfica
grafica1.categoryAxis.labels.dx = 10 # Distancia en x de las etiquetas del eje horizontal de la gráfica
grafica1.categoryAxis.labels.dy = -10 # Distancia en y de las etiquetas del eje horizontal de la gráfica
grafica1.categoryAxis.labels.boxAnchor = 'n' # Posición de las etiquetas del eje horizontal de la gráfica
grafica1.valueAxis.valueMin = 0 # Valor mínimo del eje vertical de la gráfica
grafica1.valueAxis.valueMax = 40 # Valor máximo del eje vertical de la gráfica
grafica1.valueAxis.valueStep = 10 # Paso del eje vertical de la gráfica
grafica1.lines[0].strokeWidth = 2 # Grosor de la línea de la gráfica
grafica1.lines[0].symbol = makeMarker('FilledCircle') # Símbolo de la línea de la gráfica
grafica1.lines[1].strokeWidth = 1.5 # Grosor de la línea de la gráfica
dibujo.add(grafica1) # Agregar la gráfica al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

lenda=LineLegend()
lenda.fontSize=8
lenda.fontName='Helvetica'
lenda.alignment='right'
lenda.x=0
lenda.y=0
lenda.columnMaximum=2
series=['Maximo','Minimas']
lenda.colorNamePairs=[(grafica1.lines[0],grafica1.lines[i].strokeColor,series[i])for i in range(len(grafica1.lines))]


dibujo.add(lenda)
elementosDoc.append(dibujo)
documento = SimpleDocTemplate("ejemploGraficasRpl.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos