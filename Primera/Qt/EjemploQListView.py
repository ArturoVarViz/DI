import sys
from PyQt6.QtGui import QColor, QPalette,QImage
from PyQt6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QMainWindow, QListView, QButtonGroup, \
    QPushButton, QLineEdit
from PyQt6.QtCore import Qt, QAbstractListModel

tick=QImage('check.png')

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
            if estado:
                return tick

    def rowCount(self, indice):
        return len(self.tarea)


class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion con cajas")
        listaTareas = [(False, "una tarea"), (False, "segunda Tarea")]
        self.modelo = tareaModelo(listaTareas)
        cajaV = QVBoxLayout()

        self.lstTarea = QListView()  # Cambiado a variable de instancia
        self.lstTarea.setModel(self.modelo)
        cajaV.addWidget(self.lstTarea)

        cajaH = QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnhecho = QPushButton("Hecho")
        btnhecho.pressed.connect(self.on_btnHecho_pressed)  # Agregado el evento al botón Hecho
        cajaH.addWidget(btnBorrar)
        cajaH.addWidget(btnhecho)

        cajaV.addLayout(cajaH)
        self.txtTarea = QLineEdit()
        cajaV.addWidget(self.txtTarea)

        btnAnadirTarea = QPushButton("añadir")
        btnAnadirTarea.pressed.connect(self.on_btnAnadirTarea_pressed)
        cajaV.addWidget(btnAnadirTarea)

        contenedor = QWidget()  # Aquí está la corrección
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)
        self.setFixedSize(400, 300)
        self.show()

    def on_btnAnadirTarea_pressed(self):
        texto = self.txtTarea.text().strip()
        if texto:
            self.modelo.tarea.append((False, texto))
            self.modelo.layoutChanged.emit()

    def on_btnHecho_pressed(self):  # Método modificado
        indice = self.lstTarea.currentIndex()
        if indice.isValid():
            fila = indice.row()
            estado, texto = self.modelo.tarea[fila]
            self.modelo.tarea[fila] = (not estado, texto)  # Cambia el estado a False si ya está marcado
            self.modelo.dataChanged.emit(indice, indice)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PrimeraVentana()
    ventana.show()
    sys.exit(app.exec())
