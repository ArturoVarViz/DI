import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk, Pango
import sqlite3 as dbapi


"""
axendaTel = (("Pepe", "Pérez", "986 444 555" ),
             ("Ana", "Yañéz", "985 333 777" ),
             ("Roque", "Diz", "987 222 889" ))
"""

class FiestraPrincipal (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title ("Exemplo listin telefonico con Treeview")
        self.set_default_size(250,100)
        self.set_border_width(10)

        modelo = Gtk.ListStore(str,str,str)

        try:
            bbdd = dbapi.connect ("bdListinTelefonico.dat")
            cursor =bbdd.cursor()
            cursor.execute ("select * from listaTelefonos")
            for usuarioListin in cursor:
                modelo.append(usuarioListin)
            cursor.close()
            bbdd.close()
        except dbapi.StandardError as e:
            print (e)
        except dbapi.DatabaseError as e:
            print (e)

        trvVista = Gtk.TreeView(model=modelo)
        obxetoSeleccion = trvVista.get_selection()
        obxetoSeleccion.connect("changed", self.on_obxectoSeleccion_changed)
        columnas = ("Nome", "Apelido", "Número de teléfono")
        for i, nomColumna in enumerate(columnas):
            celda = Gtk.CellRendererText()
            if i==0:
                celda.props.weight_set = True
                celda.props.weight = Pango.Weight.BOLD
            if i==2:
                celda.props.editable = True
                celda.connect ("edited",self.on_celdaTelefono_edited,modelo, i)
            col = Gtk.TreeViewColumn (nomColumna, celda, text =i)
            trvVista.append_column(col)


        caixa = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
        caixa.pack_start(trvVista, True, True,0)
        grid = Gtk.Grid()
        caixa.pack_start(grid, True, True, 0)

        lblNome = Gtk.Label(label="Nome")
        lblApelidos = Gtk.Label (label="Apelidos")
        lblTelefono = Gtk.Label (label ="Teléfono")
        self.txtNome = Gtk.Entry()
        self.txtApelidos = Gtk.Entry()
        self.txtTelefono = Gtk.Entry()
        btnEngadir = Gtk.Button(label="Engadir")
        btnBorrar = Gtk.Button(label = "Borrar")
        grid.add(lblNome)
        grid.attach_next_to(self.txtNome,lblNome,Gtk.PositionType.RIGHT, 1,1)
        grid.attach_next_to(lblApelidos,self.txtNome,Gtk.PositionType.RIGHT, 1,1)
        grid.attach_next_to(self.txtApelidos,lblApelidos,Gtk.PositionType.RIGHT, 1,1)
        grid.attach_next_to(lblTelefono, lblNome, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(self.txtTelefono, lblTelefono, Gtk.PositionType.RIGHT, 1,1)
        grid.attach_next_to(btnEngadir,self.txtTelefono, Gtk.PositionType.RIGHT, 2,1)
        grid.attach_next_to(btnBorrar, self.txtTelefono, Gtk.PositionType.BOTTOM, 2, 1)
        btnEngadir.connect("clicked", self.on_btnEngadir_clicked,modelo)
        btnBorrar.connect ("clicked", self.on_btnBorrar_clicked, obxetoSeleccion)


        self.add(caixa)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_obxectoSeleccion_changed(self,seleccion):
        (modelo, fila) = seleccion.get_selected()
        print (modelo [fila][0],modelo [fila][1], modelo [fila][2] )

    def on_btnBorrar_clicked (self, boton, seleccion):
        (modelo, fila) = seleccion.get_selected()
        print (modelo[fila][2])
        try:
            bbdd = dbapi.connect ("bdListinTelefonico.dat")
            cursor =bbdd.cursor()
            cursor.execute ("""delete from listaTelefonos 
                            where telefono = ?""", (modelo [fila][2],)
                            )
            bbdd.commit()
            cursor.close()
            bbdd.close()
        except dbapi.Error as e:
            print (e)
        except dbapi.DatabaseError as e:
            print (e)

        modelo.remove(fila)

    def on_btnEngadir_clicked (self, boton, modelo):

        if self.txtNome.get_text() != "" and self.txtApelidos.get_text() != "" and  self.txtTelefono.get_text() != "":
            elemento = [ self.txtNome.get_text(), self.txtApelidos.get_text(),self.txtTelefono.get_text()]

        modelo.append (elemento)
        self.txtNome.set_text("")
        self.txtApelidos.set_text("")
        self.txtTelefono.set_text("")
        try:
            bbdd = dbapi.connect ("bdListinTelefonico.dat")
            cursor =bbdd.cursor()
            cursor.execute ("""insert into listaTelefonos
                            values (?,?,?)""", elemento
                            )
            bbdd.commit()
            cursor.close()
            bbdd.close()
        except dbapi.Error as e:
            print (e)
        except dbapi.DatabaseError as e:
            print (e)

    def on_celdaTelefono_edited(self, celda, fila, texto, modelo, columna):

        try:
            bbdd = dbapi.connect ("bdListinTelefonico.dat")
            cursor =bbdd.cursor()
            cursor.execute ("""update listaTelefonos
                                    SET  telefono = ?
                                    WHERE telefono = ?""", (texto, modelo[fila][2])
                            )
            bbdd.commit()
            cursor.close()
            bbdd.close()
        except dbapi.Error as e:
            print (e)
        except dbapi.DatabaseError as e:
            print (e)

        modelo[fila][columna] = texto


if __name__=="__main__":
    FiestraPrincipal()
    Gtk.main()