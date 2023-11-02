import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QTabWidget

from ColorQt import CajaDeColor

class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ejemplo QTabWidget")

        tabs = QTabWidget()  # Aquí está la corrección
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)
        for color in ["red","green","blue","yellow"]:
            tabs.addTab(CajaDeColor(color),color)

        self.setCentralWidget(tabs)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PrimeraVentana()
    ventana.show()
    sys.exit(app.exec())
