import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QTabWidget

from cajaColor import CajaColor #cajaColor es la clase y CajaColor es el metodo

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTabWidget")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)#Para mover dentro de la caja blue, green, red.. En false no me dejaría

        for color in ["red", "green", "blue", "yellow"]:#enumerate es como una tupla pero añade numero a cada elemento
          tabs.addTab(CajaColor(color), color)

          self.setCentralWidget(tabs)
          self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
