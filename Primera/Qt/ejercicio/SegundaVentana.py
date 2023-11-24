import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap

class SegundaVentana(QMainWindow):#clase que hereda las propiedades de QMainWindowss

    def __init__(self):#Lo primero que hacemos es llamar al inicializador(constructor) de la super clase
        super().__init__()

        self.setWindowTitle("Mi segunda ventana con Qt")#LLamo a un método de la clase para poner el titulo de la ventana

        self.txtSaludo = QLineEdit()#Es un objeto que sirve para...¿?
        #self.txtSaludo.editingFinished.connect(self.on_botonSaludo_clicked)#Para que cuando pulsemos enter se cambie solo el texto sin ncesidad de darle click con el ratón
        self.txtSaludo.returnPressed.connect(self.on_botonSaludo_clicked)#Otra forma de hacer lo mismo que el de arriba

        self.lblEtiqueta1 = QLabel("Hola, qué tal?")
        fuente = self.lblEtiqueta1.font()#del control podemos obtener la fuente
        fuente.setPointSize(30)
        self.lblEtiqueta1.setFont(fuente)
        self.lblEtiqueta1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)#Para alinear la etiqueta a la derecha

        botonSaludo = QPushButton("Saludo")
        botonSaludo.clicked.connect(self.on_botonSaludo_clicked)#Un control podria reaccionar a varios eventos.
        # Aqui decimos que tratamos evento clicked, yc cuando hagas click sobr eel boton, el metodo de referencia
        # va a ser on_botonSaludo_clicked
        #botonSaludo.clicked.connect = control.señal.connect.
        #Con esto hemos "activado/creado" que en el boton se pueda hacer click.
        #Ahora le asociaremos una accion, la cual será saludar. Así, cuando se clickee sobre el botón, saldrá un saludo.


        #Aquí añado las etiquetas, los botones... al layout
        cajaVertical = QVBoxLayout()#QVerticalBoxLayout -- En Horizontal: QHboxLayout
        cajaVertical.addWidget(self.lblEtiqueta1)
        cajaVertical.addWidget(self.txtSaludo)
        cajaVertical.addWidget(botonSaludo)

        container = QWidget()
        container.setLayout(cajaVertical)
        self.setCentralWidget(container)

        self.setFixedSize(400,400)
        self.show()

    def on_botonSaludo_clicked(self):#Tiene que llamarse igual que como lo declaraste en el clicked.connect.
        saludo = self.txtSaludo.text()
        self.lblEtiqueta1.setText(saludo)


if __name__ =="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = SegundaVentana()#creamos instancia de nuestra primera ventana. Como en JAVA, llamamos a la clase.
    aplicacion.exec()
