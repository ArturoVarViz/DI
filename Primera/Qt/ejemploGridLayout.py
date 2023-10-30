import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QGridLayout,QLabel,QMainWindow, QWidget

from ColorQt import CajaDeColor

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ejemplo Grid Layout con Qt")

        maya=QGridLayout()
        maya.addWidget(CajaDeColor("red"))
        maya.addWidget(CajaDeColor("blue"),0,1,2,1)
        maya.addWidget(CajaDeColor("green"),1,0,1,2,)
        maya.addWidget(CajaDeColor("pink"),1,1,1,2)
        maya.addWidget(CajaDeColor("red"),2,1,1,1)
        maya.addWidget(CajaDeColor("red"), 2, 2, 1, 1)

        control =QWidget()
        control.setLayout(maya)
        self.setCentralWidget(control)
        self.show()

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        ventana= ventanaPrincipal()
        sys.exit(app.exec())
