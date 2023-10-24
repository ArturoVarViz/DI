import sys
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QMainWindow

class CajaDeColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion con cajas")

        caja1 = QHBoxLayout()  # Cambiado a QVBoxLayout para disposición vertical
        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja2.addWidget(CajaDeColor("red"))
        caja2.addWidget(CajaDeColor("yellow"))
        caja2.addWidget(CajaDeColor("purple"))

        caja1.addLayout(caja2)
        caja1.addWidget(CajaDeColor("green"))

        caja3.addWidget(CajaDeColor("blue"))
        caja3.addWidget(CajaDeColor("orange"))

        caja1.addLayout(caja3)  # Añadido para agregar la tercera caja horizontalmente

        widgetP=QWidget()
        widgetP.setLayout(caja1)
        self.setCentralWidget(widgetP)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PrimeraVentana()
    ventana.show()
    sys.exit(app.exec())
