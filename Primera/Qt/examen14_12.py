import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QDial, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget, QGridLayout)

import VentanaQt


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.nombre = 0
        self.setWindowTitle("Exame 14-12_2023")

        cajaV = QVBoxLayout()
        cajaH1 = QHBoxLayout()
        cajaH4 = QHBoxLayout()
        cajaH5 = QHBoxLayout()
        cajaH2 = QHBoxLayout()
        cajaH3 = QHBoxLayout()
        cajaV1= QVBoxLayout()
        cajaV2 = QVBoxLayout()
        cajah2 = QHBoxLayout()
        cajah3 = QHBoxLayout()
        cajaV.addLayout(cajaH4)
        cajaH1.addLayout(cajaH5)
        cajaV.addLayout(cajaH1)
        cajaV.addLayout(cajaH2)
        cajaV.addLayout(cajaH3)
        cajaH3.addLayout(cajah2)
        cajaH3.addLayout(cajah3)
        self.tedConsolaOperacions = QTextEdit()
        self.tedConsolaOperacions .setFixedSize(480, 200)
        self.lneOperacionResultado = QLineEdit()
        cajaH4.addWidget(self.tedConsolaOperacions)

        cajaH5.addWidget(self.lneOperacionResultado)



        self.cmbMoedaIncial = QComboBox()
        self.cmbMoedaCambio = QComboBox()
        lblCambio = QLabel("$0=€0")
        formatos = ["", "Dollar", "Euro", "libra Estalina", "Corona danesa"]
        self.cmbMoedaIncial.addItems(formatos)
        self.cmbMoedaCambio.addItems(formatos)

        self.cmbMoedaCambio.activated.connect(self.mostrar_formato_seleccionado)
        self.cmbMoedaIncial.activated.connect(self.mostrar_formato_seleccionado)
        cajaH2.addWidget(self.cmbMoedaIncial)
        cajaH2.addWidget(self.cmbMoedaCambio)
        cajaH2.addWidget(lblCambio)

        maya = QGridLayout()


        btnBorrar = QPushButton("Del")
        maya.addWidget((btnBorrar), 0, 0, 1, 1)
        btnAbreParentese = QPushButton("(")
        maya.addWidget((btnAbreParentese), 0, 1, 1, 1)
        btnPechaParentese = QPushButton(")")
        maya.addWidget((btnPechaParentese), 0, 2, 1, 1)
        btnModulo = QPushButton("Mod")
        maya.addWidget((btnModulo), 0, 3, 1, 1)
        btnLogaritmo = QPushButton("log")
        maya.addWidget((btnLogaritmo), 0, 4, 1, 1)


        btnSete = QPushButton("7")
        maya.addWidget((btnSete), 1, 0, 1, 1)
        btnOito = QPushButton("8")
        maya.addWidget((btnOito), 1, 1, 1, 1)
        btnNove = QPushButton("9")
        maya.addWidget((btnNove), 1, 2, 1, 1)
        btnDivision = QPushButton("/")
        maya.addWidget((btnDivision), 1, 3, 1, 1)
        btnRaiz = QPushButton("V")
        maya.addWidget((btnRaiz), 1, 4, 1, 1)

        btnCatro = QPushButton("4")
        maya.addWidget((btnCatro), 2, 0, 1, 1)
        btnCinco = QPushButton("5")
        maya.addWidget((btnCinco), 2, 1, 1, 1)
        btnSeis = QPushButton("6")
        maya.addWidget((btnSeis), 2, 2, 1, 1)
        btnMultiplicacion = QPushButton("*")
        maya.addWidget((btnMultiplicacion),2, 3, 1, 1)
        btnPotencia = QPushButton("xY")
        maya.addWidget((btnPotencia), 2, 4, 1, 1)


        btnUn = QPushButton("1")
        maya.addWidget((btnUn), 3, 0, 1, 1)
        btnUn.pressed.connect(self.on_numeros)
        btnDous = QPushButton("2")
        maya.addWidget((btnDous), 3,1, 1, 1)
        btnDous.pressed.connect(self.on_numeros)
        btnTres = QPushButton("3")
        maya.addWidget((btnTres), 3, 2, 1, 1)
        btnTres.pressed.connect(self.on_numeros)
        btnResta = QPushButton("-")
        maya.addWidget((btnResta), 3, 3, 1, 1)
        btnIgual = QPushButton("=")
        btnIgual.pressed.connect(self.on_calcular)
        maya.addWidget((btnIgual), 3, 4, 2, 1)

        btnCero = QPushButton("0")
        maya.addWidget((btnCero), 4, 0, 1, 1)
        btncoma = QPushButton(",")
        maya.addWidget((btncoma), 4, 1, 1, 1)
        btnporcentaje = QPushButton("%")
        maya.addWidget((btnporcentaje), 4, 2, 1, 1)
        btnSuma = QPushButton("+")
        maya.addWidget((btnSuma), 4, 3, 1, 1)
        btnSuma.pressed.connect(self.on_numeros)

        cajah2.addLayout(maya)

        maya2 = QGridLayout()
        btnCtrm = QPushButton("Ctrm")
        maya2.addWidget((btnCtrm),0, 0, 1, 1)
        btnDbd = QPushButton("Dbd")
        maya2.addWidget((btnDbd),0, 1, 1, 1)
        btnFv = QPushButton("Fv")
        maya2.addWidget((btnFv),0, 2, 1, 1)
        btnMBB = QPushButton("MBB")
        maya2.addWidget((btnMBB),1, 0, 1, 1)
        btnPmt = QPushButton("Pmt")
        maya2.addWidget((btnPmt),1, 1, 1, 1)
        btnPv = QPushButton("Pv")
        maya2.addWidget((btnPv),1, 2, 1, 1)
        btnTaxa = QPushButton("Taxa")
        maya2.addWidget((btnTaxa),2, 0, 1, 1)
        btnSln = QPushButton("Sln")
        maya2.addWidget((btnSln),2, 1, 1, 1)
        btnSyd = QPushButton("Syd")
        maya2.addWidget((btnSyd),2, 2, 1, 1)
        btnPeriodo = QPushButton("Período")
        maya2.addWidget((btnPeriodo), 3, 1, 1, 1)
        cmbEquis = QComboBox()
        maya2.addWidget((cmbEquis), 4, 0, 1, 3)
        cajah3.addLayout(maya2)




        contenedor = QWidget()
        contenedor.setLayout(cajaV)

        self.setCentralWidget(contenedor)
        self.setFixedSize(500, 450)

    def on_calcular(self):
        print("Has añadido un campo a la lista")
        aux = self.lneOperacionResultado.text().split("+")
        suma=0
        for numeros in aux:
            print(numeros)
            #resultado += int(numeros)
            resultado=suma+(numeros)
            print(resultado)



    def on_numeros(self):
        self.lneOperacionResultado.setText(self)
    
    def mostrar_formato_seleccionado(self, index,index2):
         formato_seleccionado = self.cmbMoedaIncial.itemText(index)
         formato_seleccionado1 = self.cmbMoedaCambio.itemText(index2)

         print(f"Usuario seleccionó el formato: {formato_seleccionado, formato_seleccionado1}")

if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()