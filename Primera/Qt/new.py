
import sys

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtCore import Qt, QAbstractTableModel

class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla # Se almacena la tabla en un atributo de la clase

    # Métodos abstractos que deben implementarse
    def rowCount(self, indice): # Devuelve el número de filas de la tabla
        return len(self.tabla)
    def columnCount(self, indice): # Devuelve el número de columnas de la tabla
        return len(self.tabla[0])
    def data(self, indice, rol): # Devuelve el dato que se encuentra en el índice de la tabla
        if indice.isValid(): # Si el índice es válido
            if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole: # Si el rol es de edición o visualización de datos de la tabla
                valor = self.tabla[indice.row()][indice.column()] # Se obtiene el valor de la tabla
                return valor
            if rol == Qt.ItemDataRole.ForegroundRole:
                if self.tabla[indice.row()][3]==True:
                    return QColor('red')

            if rol == Qt.ItemDataRole.BackgroundRole:
                if self.tabla[indice.row()][2] == 'Home':
                    return QColor('blue')
                else :
                    if self.tabla[indice.row()][2] == 'Muller':
                        return QColor('pink')
    def setData(self, indice, valor, rol): # Establece el dato en el índice de la tabla
        if rol == Qt.ItemDataRole.EditRole: # Si el rol es de edición de datos de la tabla
            self.tabla[indice.row()][indice.column()] = valor # Se establece el valor en la tabla
            return True # Se devuelve True para indicar que se ha establecido el valor
        return False # Se devuelve False para indicar que no se ha establecido el valor
    def flags(self, indice): # Devuelve los flags de edición de la tabla
        if indice.row() == 0:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable # Se devuelven los flags de edición de la tabla

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QTableView con Qt")
        self.datos=[["Nome", "Dni", "Xenero", "Falecido"],
               ["Ana Pérez","12345678Y","Muller",True],
               ["Luis González","87654321K","Home",False],
               ["María Sánchez","87654891H","Outro",False],
               ["Jorge Ruíz","32754981U","Home",True],
               ]

        cajaV=QVBoxLayout()
        self.tvwTabla = QTableView()
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection) # Añadido aquí
        modelo = ModeloTabla(self.datos)
        self.tvwTabla.setModel(modelo)
        self.seleccion= self.tvwTabla.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_filaSeleccionada)
        cajaV.addWidget(self.tvwTabla)
        cajaH=QHBoxLayout()
        cajaV.addLayout(cajaH)
        self.txtNombre = QLineEdit("Nome")
        cajaH.addWidget(self.txtNombre)
        self.txtDni = QLineEdit("DNI")  # Cambiado a self.txtDni
        cajaH.addWidget(self.txtDni)
        self.cmbGenero = QComboBox()  # Cambiado a self.cmbGenero
        self.cmbGenero.addItems(('Home', 'Muller', 'Outros'))
        cajaH.addWidget(self.cmbGenero)
        self.chkFallecido = QCheckBox('Falecido')  # Cambiado a self.chkFallecido
        cajaH.addWidget(self.chkFallecido)

        componentePrincipal=QWidget()
        componentePrincipal.setLayout(cajaV)
        self.setCentralWidget(componentePrincipal)

        self.setFixedSize(400, 400)
        self.show()

    def on_filaSeleccionada(self):
        indices = self.tvwTabla.selectedIndexes()
        if indices:
            row = indices[0].row()
            if row < len(self.datos):
                print(self.datos[row])  # Imprime los valores de la fila seleccionada
                self.txtNombre.setText(self.datos[row][0])
                self.txtDni.setText(self.datos[row][1])
                self.cmbGenero.setCurrentText(self.datos[row][2])
                self.chkFallecido.setChecked(self.datos[row][3])
            else:
                print(f"Índice {row} fuera de rango")

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()