import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListView, \
    QPushButton, QGridLayout, QComboBox, QFrame


class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("examen")
        cajaV = QVBoxLayout()
        cajaH1 = QHBoxLayout()
        cajaH2 = QHBoxLayout()
        cajaV.addLayout(cajaH1)
        cajaV.addLayout(cajaH2)
        cajaH1.setAlignment(Qt.AlignmentFlag.AlignTop)
        caja3 = QHBoxLayout()

        cajaH1.addLayout(caja3)
        caja3.setAlignment(Qt.AlignmentFlag.AlignTop)
        lblIconCd=QLabel()
        lblIconCd.setPixmap(QPixmap("disco.png"))
        caja3.addWidget(lblIconCd)
        chkAnimation=QCheckBox("animation")
        caja3.addWidget(chkAnimation)
        lswLista=QListView()
        lswLista.setFixedSize(400,350)
        cajaH1.addWidget(lswLista)
        caja4=QVBoxLayout()
        cajaH1.addLayout(caja4)

        btnAñadir = QPushButton("añadir lista")
        caja4.addWidget(btnAñadir)
        btnSubir = QPushButton("Subir Lista")
        caja4.addWidget(btnSubir)
        btnBajar = QPushButton("bajar Lista")
        caja4.addWidget(btnBajar)

        grid = QGridLayout()
        btnSaltar = QPushButton("saltar")
        grid.addWidget(btnSaltar)  # Añade el botón a la posición (0, 0) del layout grid
        caja4.addLayout(grid)
        cmbSaltar = QComboBox()
        grid.addWidget(cmbSaltar, 0, 1)

        btnAbrir = QPushButton("abrir fichero")
        caja4.addWidget(btnAbrir)
        btnReproducir = QPushButton("reproducir fichero")
        caja4.addWidget(btnReproducir)
        btnGuardar = QPushButton("guradar como")
        caja4.addWidget(btnGuardar)
        btneLiminar = QPushButton("eliminar pista")
        caja4.addWidget(btneLiminar)

        grid2=QGridLayout()
        cajaH2.addLayout(grid2)
        lblSon=QLabel("son")
        lblRitmo = QLabel("Ritmo")
        lblVolumen = QLabel("Volumen")
        lblFormato = QLabel("Formato")
        lblSalida = QLabel("Salida")
        grid2.addWidget(lblSon,0,1,1,1)
        grid2.addWidget(lblRitmo, 1, 1, 1, 1)
        grid2.addWidget(lblVolumen,2, 1, 1, 1)
        grid2.addWidget(lblFormato, 3, 1, 1, 1)
        grid2.addWidget(lblSalida, 4, 1, 1, 1)


        caja5 = QHBoxLayout()
        frnOpReproductor = QFrame()
        frnOpReproductor.setLayout(caja5)
        frnOpReproductor.setWindowTitle("opcion")
        cajaH2.addWidget(frnOpReproductor)
        caja6=QVBoxLayout()
        caja7 = QVBoxLayout()
        caja5.addLayout(caja6)
        caja5.addLayout(caja7)

        ckhAsincrono=QCheckBox("asoncrono")
        ckhnombre = QCheckBox("nombre")
        ckhxml = QCheckBox("XML")


        caja6.addWidget(ckhAsincrono)
        caja6.addWidget(ckhnombre)
        caja6.addWidget(ckhxml)
        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)
        self.setFixedSize(800, 500)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    VentanaQt = PrimeraVentana()
    VentanaQt.show()
    sys.exit(aplicacion.exec())
