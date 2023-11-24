import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QPixmap

class TerceraVentana(QMainWindow):
    def __init__(self):#Lo primero que hacemos es llamar al inicializador(constructor) de la super clase
        super().__init__()

        self.setWindowTitle("Mi tercera ventana con Qt")

        #CReamos un widget central
        container = QWidget()

        # Creamos los botones
        boton1 = QPushButton("Boton 1")
        boton2 = QPushButton("Boton 2")
        boton3 = QPushButton("Boton 3")
        boton4 = QPushButton("Boton 4")
        boton5 = QPushButton("Boton 5")
        boton6 = QPushButton("Boton 6")

        # Creamos un layout vertical
        cajaVertical = QVBoxLayout()

        # Agregamos los botones al layout
        cajaVertical.addWidget(boton1)
        cajaVertical.addWidget(boton2)
        cajaVertical.addWidget(boton3)
        cajaVertical.addWidget(boton4)
        cajaVertical.addWidget(boton5)
        cajaVertical.addWidget(boton6)

        #Establecemos el layout en el widget central
        container.setLayout(cajaVertical)

        #Establecemos el widget central en la QMAinWindow
        self.setCentralWidget(container)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = TerceraVentana()  # creamos instancia de nuestra primera ventana. Como en JAVA, llamamos a la clase.
    ventana.show()
    aplicacion.exec()