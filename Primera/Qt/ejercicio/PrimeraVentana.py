import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class PrimeraVentana(QMainWindow):#clase que hered las propiedades de QMainWindowss
    def __init__(self):#Lo primero que hacemos es llamar al inicializador(constructor) de la super clase
        super().__init__()

        self.setWindowTitle("Mi primera ventana con Qt")#LLamo a un método de la clase para poner el titulo de la ventana

        self.lblEtiqueta1 = QLabel("Hola, qué tal?")
        lblEtiqueta2 = QLabel()
        lblEtiqueta2.setPixmap(QPixmap("fotoluci2.jpg"))
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
        cajaVertical.addWidget(lblEtiqueta2)
        cajaVertical.addWidget(botonSaludo)

        container = QWidget()
        container.setLayout(cajaVertical)
        self.setCentralWidget(container)

        self.setFixedSize(400,400)
        self.show()

    def on_botonSaludo_clicked(self):#Tiene que llamarse igual que como lo declaraste en el clicked.connect.
        self.lblEtiqueta1.setText("Hola companheros!!!")


if __name__ =="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PrimeraVentana()#creamos instancia de nuestra primera ventana. Como en JAVA, llamamos a la clase.
    aplicacion.exec()
