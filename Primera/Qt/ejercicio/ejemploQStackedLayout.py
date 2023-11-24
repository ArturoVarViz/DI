import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, \
    QHBoxLayout, QPushButton

from cajaColor import CajaColor #cajaColor es la clase y CajaColor es el metodo


class GridConContenido(QGridLayout):#GRID ES MALLA EN LA VENTANA
    def __init__(self):
        super().__init__()

        self.addWidget(CajaColor("red"))
        self.addWidget(CajaColor("blue"), 0, 1, 1, 2)
        self.addWidget(CajaColor("green"), 1, 0, 2, 1)
        self.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        self.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        self.addWidget(CajaColor("yellow"), 2, 2, 1, 1)


class HBoxModificado (QHBoxLayout):#ESte el box MOdificado
    def __init__(self):
        super().__init__()

        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("purple"))
        self.addLayout(caja2)

        self.addWidget(CajaColor("green"))

        caja3.addWidget(CajaColor ("blue"))
        caja3.addWidget(CajaColor ("orange"))
        self.addLayout(caja3)

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QStacked Layout con Qt")


        cajaVertical = QVBoxLayout()
        cajaBotones = QHBoxLayout()
        cajaVertical.addLayout(cajaBotones)
        self.tarjetas = QStackedLayout()
        cajaVertical.addLayout(self.tarjetas)

        botonRojo = QPushButton("rojo")
        botonRojo.pressed.connect(self.on_btnRojo_pressed)
        cajaBotones.addWidget(botonRojo)

        botonAzul = QPushButton("azul")
        botonAzul.pressed.connect(self.on_btnAzul_pressed)
        cajaBotones.addWidget(botonAzul)

        # La malla es la red, como en ejemploGridLayout
        botonMalla = QPushButton("malla")
        botonMalla.pressed.connect(self.on_btnMalla_pressed)
        cajaBotones.addWidget(botonMalla)

        btnBModificado = QPushButton("Box modificado")
        btnBModificado.pressed.connect(self.on_btnModificado_pressed)
        cajaBotones.addWidget(btnBModificado)

        #cardLayout(son como tarjetas¿?). Importamos QStackedLayout.
        #Diferencia entre poner al final de QSTackedLAyout parentesis o no.
        self.tarjetas.addWidget(CajaColor("red"))
        self.tarjetas.addWidget(CajaColor("blue"))
        widgetGrid = QWidget()
        widgetGrid.setLayout(GridConContenido())
        self.tarjetas.addWidget(widgetGrid)
        widgetBox = QWidget()
        widgetBox.setLayout(HBoxModificado())
        self.tarjetas.addWidget(widgetBox)
        self.tarjetas.setCurrentIndex(1)

        control = QWidget()
        control.setLayout(cajaVertical)
        self.setCentralWidget(control)
        self.show()

    def on_btnRojo_pressed(self):
        self.tarjetas.setCurrentIndex(0)

    def on_btnAzul_pressed(self):
        self.tarjetas.setCurrentIndex(1)

    def on_btnMalla_pressed(self):
        self.tarjetas.setCurrentIndex(2)

    def on_btnModificado_pressed(self):
        self.tarjetas.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
