import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class CajaDeColor(Gtk.Box):
    def __init__(self, color):
        Gtk.Box.__init__(self)
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(color))

class PrimeraVentana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Aplicacion con cajas")

        caja1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caja2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caja3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        caja2.pack_start(CajaDeColor("red"), True, True, 0)
        caja2.pack_start(CajaDeColor("yellow"), True, True, 0)
        caja2.pack_start(CajaDeColor("purple"), True, True, 0)

        caja1.pack_start(caja2, True, True, 0)
        caja1.pack_start(CajaDeColor("green"), True, True, 0)

        caja3.pack_start(CajaDeColor("red"), True, True, 0)
        caja3.pack_start(CajaDeColor("purple"), True, True, 0)

        caja1.pack_start(caja3, True, True, 0)

        self.add(caja1)

if __name__ == "__main__":
    app = Gtk.Application()
    ventana = PrimeraVentana()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()
