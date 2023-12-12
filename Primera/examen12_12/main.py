import sys
from PyQt6.QtCore import QSize, Qt, QAbstractListModel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QListView)




class tareaModelo(QAbstractListModel):
    def __init__(self, tarea=None):
        super().__init__()
        self.tarea = tarea or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado, texto = self.tarea[indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado,_=self.tarea[indice.row()]

    def rowCount(self, indice):
        return len(self.tarea)

class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 12-12_2022")
        listaTareas = []
        self.modelo = tareaModelo(listaTareas)
        self.lstDireccionC = QListView()  # Cambiado a variable de instancia
        self.lstDireccionC.setModel(self.modelo)
        cajaV = QVBoxLayout()
        cajaH1= QVBoxLayout()
        cajah1=QHBoxLayout()
        cajah2 = QHBoxLayout()
        cajah3 = QHBoxLayout()
        cajaH2= QHBoxLayout()
        cajav1=  QVBoxLayout()
        cajav2 = QVBoxLayout()
        cajaH3=QHBoxLayout()
        cajaH4=QHBoxLayout()
        cajaH5 = QHBoxLayout()
        cajaH6 = QHBoxLayout()
        cajaV.addLayout(cajaH1)
        cajaV.addLayout(cajaH2)
        cajaV.addLayout(cajaH3)

        cajaH1.addLayout(cajah1)
        cajaH1.addLayout(cajah2)
        cajaH1.addLayout(cajah3)

        cajaH2.addLayout(cajav1)
        cajaH2.addLayout(cajav2)

        cajaV.addLayout(cajaH4)
        cajaV.addLayout(cajaH5)
        cajaV.addLayout(cajaH6)

        self. lblNome = QLabel("Nome")
        lblApelido = QLabel("Apelido")
        lblTratamento = QLabel("Tratamento")
        lblTelefono = QLabel("Telefono")
        self.txtNome = QLineEdit()
        self.txtApelido = QLineEdit()
        txtTratamento = QLineEdit()
        self.txtTelefono = QLineEdit()
        lblFormato = QLabel("Formato")
        self.cmbFormato = QComboBox()
        formatos = ["","color", "estructura", "tamaño"]
        self.cmbFormato.addItems(formatos)
        self.cmbFormato.activated.connect(self.mostrar_formato_seleccionado)

        cajah1.addWidget(self.lblNome)
        cajah1.addWidget(self.txtNome)
        cajah1.addWidget(lblApelido)
        cajah1.addWidget(self.txtApelido)

        cajah2.addWidget(lblTratamento)
        cajah2.addWidget(txtTratamento)
        cajah2.addWidget(lblTelefono)
        cajah2.addWidget(self.txtTelefono)

        cajah3.addWidget(lblFormato)
        cajah3.addWidget(self.cmbFormato)

        self. lstDireccionC = QListWidget()
        self.lstDireccionC.setFixedSize(350,200)
        cajav1.setAlignment(Qt.AlignmentFlag.AlignTop)

        cajav1.addWidget(self.lstDireccionC)
        lblFormato = QLabel("Formato de correo:")
        self.rbtHtml = QRadioButton("HTML")
        self.rbtTextoPlano = QRadioButton ("Texto Plano")
        self.rbtPersonalizado = QRadioButton ("Personalizado")

        cajav2.setAlignment(Qt.AlignmentFlag.AlignTop)
        cajav2.addWidget(lblFormato)
        cajav2.addWidget(self.rbtHtml)
        cajav2.addWidget(self.rbtTextoPlano)
        cajav2.addWidget(self.rbtPersonalizado)
        self.rbtHtml.toggled.connect(self.on_radioButton_toggled)
        self.rbtTextoPlano.toggled.connect(self.on_radioButton_toggled)
        self.rbtPersonalizado.toggled.connect(self.on_radioButton_toggled)

        lblDireccionC = QLabel("Dirección de correo")
        txtDireccionC = QLineEdit()

        cajaH4.setAlignment(Qt.AlignmentFlag.AlignTop)


        cajaH4.addWidget(lblDireccionC)
        cajaH4.addWidget(txtDireccionC)

        btnEngadir = QPushButton("Engadir")
        btnEngadir.pressed.connect(self.on_btnAnadir_pressed)
        btnEditar = QPushButton("Editar")
        btnEditar.pressed.connect(self.boton_editar_clicked)
        btnBorrar = QPushButton("Borrar")
        btnBorrar.pressed.connect(self.boton_borrar_clicked)
        btnPorDefecto = QPushButton("Por Defecto")
        cajaH5.setAlignment(Qt.AlignmentFlag.AlignLeft)
        cajaH5.addWidget(btnEngadir)
        cajaH5.addWidget(btnEditar)
        cajaH5.addWidget(btnBorrar)
        cajaH5.addWidget(btnPorDefecto)

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.pressed.connect(self.boton_Cancelar_clicked)

        cajaH6.addWidget(btnAceptar)
        cajaH6.addWidget(btnCancelar)
        cajaH6.setAlignment(Qt.AlignmentFlag.AlignRight)
        contenedor = QWidget()
        contenedor.setLayout(cajaV)


        self.setCentralWidget(contenedor)
        self.setFixedSize(500, 450)

    def on_btnAnadir_pressed(self):
        print("Has añadido un campo a la lista")
        nome = self.txtNome.text()  # Cambiado de self.miInputNome a self.txtNome
        apelidos = self.txtApelido.text()
        tlf = self.txtTelefono.text()
        self.lstDireccionC.addItem(f"{nome}, {apelidos}, {tlf}")
        self.txtNome.setText("")
        self.txtApelido.setText("")
        self.txtTelefono.setText("")

    def boton_Cancelar_clicked(self):

        FiestraPrincipal.close(self)

    def boton_editar_clicked(self):
        itemSeleccionado = self.lstDireccionC.currentItem()
        txtItem = itemSeleccionado.text()
        print(f"Has seleccionado editar la fila: {txtItem}")
        txtLista = (txtItem.split(","))
        self.txtNome.setText(txtLista[0])
        self.txtApelido.setText(txtLista[1])
        self.txtTelefono.setText(txtLista[2])

    def on_radioButton_toggled(self):
        # Comprobar cuál de los botones de opción está seleccionado
        if self.rbtHtml.isChecked():
            print("Has seleccionado HTML")
        elif self.rbtTextoPlano.isChecked():
            print("Has seleccionado Texto Plano")
        elif self.rbtPersonalizado.isChecked():
            print("Has seleccionado Personalizado")

    def mostrar_formato_seleccionado(self, index):
        formato_seleccionado = self.cmbFormato.itemText(index)

        print(f"Usuario seleccionó el formato: {formato_seleccionado}")

    def boton_borrar_clicked(self):
        indice = self.lstDireccionC.currentRow()


        if indice != -1:
            self.lstDireccionC.takeItem(indice)
            print("Borrado con exito")
        else:
            print("No hay ningún elemento seleccionado para borrar")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    VentanaQt = FiestraPrincipal()
    VentanaQt.show()
    sys.exit(aplicacion.exec())