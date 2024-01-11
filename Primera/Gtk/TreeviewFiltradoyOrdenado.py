import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango
import sqlite3 as dbapi  # para imprimir los datos del SQLite


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo Treeview Filtrado y Ordenado")
        self.set_default_size(500, 300)  # Ajusta el tamaño según tus necesidades
        self.set_border_width(10)
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # Parte izquierda (TreeView)
        cajaIzquierda = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.filtradoGenero = "None"
        modelo = Gtk.ListStore(str, str, int, str, bool)
        modelo_filtrado = modelo.filter_new()
        modelo_filtrado.set_visible_func(self.filtro_usuarios_genero)

        # Conexión a la base de datos
        try:
            bbdd = dbapi.connect("baseDatos2.dat")
            cursor = bbdd.cursor()
            cursor.execute("SELECT * FROM usuarios")
            for fila in cursor:
                modelo.append(fila)
        except dbapi.Error as e:
            print(e)
        except dbapi.DatabaseError as e:
            print("Error al cargar la base de datos")
        finally:
            cursor.close()
            bbdd.close()

        tryDatosUsuarios = Gtk.TreeView(model=modelo_filtrado)
        seleccion = tryDatosUsuarios.get_selection()

        for i, tituloColumna in enumerate(["Dni", "Nome"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            tryDatosUsuarios.append_column(columna)

        celda = Gtk.CellRendererProgress()
        columna = Gtk.TreeViewColumn("Edade", celda, value=2)
        tryDatosUsuarios.append_column(columna)

        modeloCombo = Gtk.ListStore(str)
        modeloCombo.append(("Home",))
        modeloCombo.append(("Muller",))
        modeloCombo.append(("Outro",))
        celda = Gtk.CellRendererCombo()
        celda.set_property("editable", True)
        celda.props.model = modeloCombo
        celda.set_property("text-column", 0)
        celda.set_property("has-entry", False)
      #  celda.connect("edited", self.on_celdaGenero_edited, modelo_filtrado, 3)

        columna = Gtk.TreeViewColumn("Xenero", celda, text=3)
        tryDatosUsuarios.append_column(columna)

        cajaIzquierda.pack_start(tryDatosUsuarios, True, True, 2)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        cajaIzquierda.pack_start(cajaH, True, True, 0)

        rbtHombre = Gtk.RadioButton(label="Home")
        rbtMujer = Gtk.RadioButton.new_with_label_from_widget(rbtHombre, label="Muller")
        rbtOtro = Gtk.RadioButton.new_with_label_from_widget(rbtHombre, label="Outro")
        cajaH.pack_start(rbtHombre, True, True, 2)
        cajaH.pack_start(rbtMujer, True, True, 2)
        cajaH.pack_start(rbtOtro, True, True, 2)
        rbtHombre.connect("toggled", self.on_genero_toggled, "Home", modelo_filtrado)
        rbtMujer.connect("toggled", self.on_genero_toggled, "Muller", modelo_filtrado)
        rbtOtro.connect("toggled", self.on_genero_toggled, "Outro", modelo_filtrado)

        cajaDerecha = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        lblNombre = Gtk.Label(label="Nome:")
        entryNombre = Gtk.Entry()
        lblDNI = Gtk.Label(label="DNI:")
        entryDNI = Gtk.Entry()
        lblEdad = Gtk.Label(label="Edade:")
        entryEdad = Gtk.Entry()

        lblGenero = Gtk.Label(label="Xenero:")
        rbtHombre1 = Gtk.RadioButton(label="Home")
        rbtMujer1 = Gtk.RadioButton.new_with_label_from_widget(rbtHombre, label="Muller")
        rbtOtro1 = Gtk.RadioButton.new_with_label_from_widget(rbtHombre, label="Outro")

        cajaDerecha.pack_start(lblNombre, False, False, 0)
        cajaDerecha.pack_start(entryNombre, False, False, 0)
        cajaDerecha.pack_start(lblDNI, False, False, 0)
        cajaDerecha.pack_start(entryDNI, False, False, 0)
        cajaDerecha.pack_start(lblEdad, False, False, 0)
        cajaDerecha.pack_start(entryEdad, False, False, 0)
        cajaDerecha.pack_start(lblGenero, False, False, 0)
        cajaDerecha.pack_start(rbtHombre1, False, False, 0)
        cajaDerecha.pack_start(rbtMujer1, False, False, 0)
        cajaDerecha.pack_start(rbtOtro1, False, False, 0)

     

        # Botones
        btnEditar = Gtk.Button(label="Editar")
        btnEditar.connect("clicked", self.on_btn_editar_clicked)
        btnAnadir = Gtk.Button(label="Añadir")
        btnAnadir.connect("clicked", self.on_btn_anadir_clicked)
        btnAceptar = Gtk.Button(label="Aceptar")
        btnAceptar.connect("clicked", self.on_btn_aceptar_clicked)
        btnCancelar = Gtk.Button(label="Cancelar")
        btnCancelar.connect("clicked", self.on_btn_cancelar_clicked)
        btnAceptar.set_sensitive(False)
        btnCancelar.set_sensitive(False)
        # Caja para los botones con orientación horizontal
        cajaBotones = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        cajaBotones.pack_start(btnEditar, False, False, 0)
        cajaBotones.pack_start(btnAnadir, False, False, 0)
        cajaBotones.pack_start(btnAceptar, False, False, 0)
        cajaBotones.pack_start(btnCancelar, False, False, 0)

        # Añadir la caja de botones a la caja derecha
        cajaDerecha.pack_start(cajaBotones, False, False, 0)

        cajaPrincipal.pack_start(cajaIzquierda, True, True, 2)
        cajaPrincipal.pack_start(cajaDerecha, False, False, 2)

        self.add(cajaPrincipal)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_genero_toggled(self, botonSeleccionado, genero, modelo):
        if botonSeleccionado.get_active():
            self.filtradoGenero = genero
            modelo.refilter()

    def filtro_usuarios_genero(self, modelo, fila, datos):
        if self.filtradoGenero is None or self.filtradoGenero == "None":
            return True
        else:
            return modelo[fila][3] == self.filtradoGenero



    def on_btn_editar_clicked(self, widget):
        # Activar los botones Aceptar y Cancelar
        btnAceptar.set_sensitive(True)
        btnCancelar.set_sensitive(True)
        # Desactivar los botones Editar y Añadir
        btnEditar.set_sensitive(False)
        btnAnadir.set_sensitive(False)

    def on_btn_anadir_clicked(self, widget):
        # Activar los botones Aceptar y Cancelar
        btnAceptar.set_sensitive(True)
        btnCancelar.set_sensitive(True)
        # Desactivar los botones Editar y Añadir
        btnEditar.set_sensitive(False)
        btnAnadir.set_sensitive(False)

    def on_btn_aceptar_clicked(self, widget):
        # Desactivar los botones Aceptar y Cancelar
        btnAceptar.set_sensitive(False)
        btnCancelar.set_sensitive(False)
        # Activar los botones Editar y Añadir
        btnEditar.set_sensitive(True)
        btnAnadir.set_sensitive(True)

    def on_btn_cancelar_clicked(self, widget):
        # Desactivar los botones Aceptar y Cancelar
        btnAceptar.set_sensitive(False)
        btnCancelar.set_sensitive(False)
        # Activar los botones Editar y Añadir
        btnEditar.set_sensitive(True)
        btnAnadir.set_sensitive(True)


def on_celdaGenero_edited(self, celda, fila, texto, modelo, columna):
        try:
            bbdd = dbapi.connect("baseDatos2.dat")
            cursor = bbdd.cursor()
            cursor.execute("UPDATE usuarios SET xenero=? WHERE dni=?",
                           (texto, modelo[fila][0]))
            bbdd.commit()
        except dbapi.Error as e:
            print(e)
        except dbapi.DatabaseError as e:
            print("Error al cargar la base de datos")
        finally:
            cursor.close()
            bbdd.close()

        modelo[fila][columna] = texto
        modelo.refilter()




if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
