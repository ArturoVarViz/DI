import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        bd = QSqlDatabase.addDatabase("QSQLITE" )
        bd.setDatabaseName("baseDatos2.dat")
        bd.open()
        if not bd.open():
            print(bd.lastError().text())

        cajaV = QVBoxLayout()
        cajaH = QHBoxLayout()
        self.tabla = QTableView()
        self.model = QSqlTableModel(db=bd)
        self.tabla.setModel(self.model)


        self.model.setTable("usuarios")
        self.model.select()
        cajaV.addWidget(self.tabla)

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        cajaH.addWidget(btnAceptar)
        cajaH.addWidget(btnCancelar)
        btnAceptar.clicked.connect(self.on_btnAceptar_clicked)
        btnCancelar.clicked.connect(self.on_btnCancelar_clicked)

        cajaV.addLayout(cajaH)
        widget = QWidget()
        widget.setLayout(cajaV)
        self.setCentralWidget(widget)

        self.setMinimumSize(QSize(400, 400))
        self.show()

    def on_btnAceptar_clicked(self):
        print("Aceptar button clicked")

    def on_btnCancelar_clicked(self):
        print("Cancelar button clicked")

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
