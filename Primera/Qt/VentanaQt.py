import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mi primera ventana en qt")
        self.lblEt1=QLabel("hola")
        lblEt2=QLabel()
        lblEt2.setPixmap(QPixmap("paisaje.png"))
        btnSaludo=QPushButton("saludos")
        btnSaludo.clicked.connect(self.on_btnSaludo_cliked)

        cajaV=QVBoxLayout()
        cajaV.addWidget(self.lblEt1)
        cajaV.addWidget(lblEt2)
        cajaV.addWidget(btnSaludo)

        contenedor=QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)
        self.setFixedSize(400,300)
        self.show()

    def on_btnSaludo_cliked(self):
        self.lblEt1.setText("hola amigos")

if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    VentanaQt=main()
    aplicacion.exec()
