import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,QLineEdit)
from PyQt6.QtCore import Qt

class SegundaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mi primera ventana en qt")
        self.txtSaludo=QLineEdit()

        self.lblEt1=QLabel("hola")
        font=self.lblEt1.font()
        font.setPointSize(30)
        self.lblEt1.setFont(font)
        self.lblEt1.setAlignment(Qt.AlignmentFlag.AlignHCenter| Qt.AlignmentFlag.AlignVCenter)

        btnSaludo=QPushButton("saludos")
        btnSaludo.clicked.connect(self.on_btnSaludos_cliked)

        cajaV=QVBoxLayout()

        cajaV.addWidget(self.lblEt1)
        cajaV.addWidget(self.txtSaludo)

        cajaV.addWidget(btnSaludo)

        contenedor=QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)
        self.setFixedSize(400,300)

        # Conectar la señal returnPressed del objeto txtSaludo a la función on_txtSaludo_returnPressed
        self.txtSaludo.returnPressed.connect(self.on_txtSaludo_returnPressed)
        #self.txtSaludo.editingFinished.connect(self.on_txtSaludo_editingFinished)

        self.show()

    def on_btnSaludos_cliked(self):
       saludo=self.txtSaludo.text()
       self.lblEt1.setText(saludo)

    def on_txtSaludo_returnPressed(self):
       saludo=self.txtSaludo.text()
       self.lblEt1.setText(saludo)

    def on_txtSaludo_editingFinished(self):
        saludo = self.txtSaludo.text()
        self.lblEt1.setText(saludo)


if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    VentanaQt=SegundaVentana()
    aplicacion.exec()
