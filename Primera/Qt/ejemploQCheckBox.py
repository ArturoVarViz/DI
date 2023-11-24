 import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mi primera ventana en qt")



    def on_btnSaludo_cliked(self):
        self.lblEt1.setText("hola amigos")

if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    VentanaQt=main()
    aplicacion.show()
    aplicacion.exec()
