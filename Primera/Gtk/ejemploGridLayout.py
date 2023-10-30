import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("ejemplo grid layout")

        boton1 = Gtk.Button(label="boton 1")
        boton2 = Gtk.Button(label="boton 2")
        boton3 = Gtk.Button(label="boton 3")
        boton4 = Gtk.Button(label="boton 4")
        boton5 = Gtk.Button(label="boton 5")
        boton6 = Gtk.Button(label="boton 6")

        maia = Gtk.Grid()
        maia.add(boton1)
       
        maia.attach(boton2, 1, 0, 2, 1)
        maia.attach(boton3, 0, 1, 1, 2)

        # Corregir aquí: usar Gtk.PositionType.BOTTOM en lugar de Gtk.PositionType.DOWN
        maia.attach_next_to(boton4, boton3, Gtk.PositionType.RIGHT, 2,1)

        # Agregar botón 5 debajo del botón 4
        maia.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)

        # Agregar botón 6 al lado del botón 5
        maia.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

        self.add(maia)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


win = GridWindow()
Gtk.main()
