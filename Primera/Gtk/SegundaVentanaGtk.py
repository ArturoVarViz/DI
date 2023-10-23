import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaGtk(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera ventana con Gtk")

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        lblEtiqueta = Gtk.Label(label="Introduce tu texto:")
        caja.pack_start(lblEtiqueta, False, False, 5)

        txtEntrada = Gtk.Entry()
        caja.pack_start(txtEntrada, False, False, 5)

        imagen = Gtk.Image()
        imagen.set_from_file("logo.png")
        caja.pack_start(imagen, True, True, 5)  # expand, fill, padding

        lblEtiqueta = Gtk.Label(label="Hola a todos")
        caja.pack_start(lblEtiqueta, False, False, 5)

        btnBoton = Gtk.Button(label="Púlsame")
        btnBoton.connect("clicked", self.on_btnBoton_clicked, lblEtiqueta)
        caja.pack_start(btnBoton, False, False, 5)

        txtEntrada.connect("activate", self.on_txtEntrada_activate, lblEtiqueta)

        self.add(caja)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btnBoton_clicked(self, boton, etiqueta):
        etiqueta.set_text("Hola alumnos de Gtk")

    def on_txtEntrada_activate(self, entrada, etiqueta):
        etiqueta.set_text(entrada.get_text())


if __name__ == "__main__":
    VentanaGtk()
    Gtk.main()
