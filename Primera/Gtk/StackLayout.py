import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("ejemplo stack layout")


        cajaV=Gtk.Box(orientation=Gtk.Orientacion.VERTICAL,spacing=6)

        tarjeta=Gtk.Stack()
        tarjeta.set_transition_type(Gtk.StackTransitonType.SLIDE_LEFT_RIGHT)
        tarjeta.set_transition_duration(1000)

        chkPulsame=Gtk.CheckButton(label="pulsame")
        tarjeta.add_titled(chkPulsame,"Pulsame")

        lblEtiqueta=Gtk.Label()
        lblEtiqueta.set_markup("<big>Esta e una etiqueta elegante</big>")
        tarjeta.add_titled(lblEtiqueta,"etiqueta","Una etiqueta")


        botonTarjeta =Gtk.StackSwitcher()
        botonTarjeta.set_stack(tarjeta)
        cajaV.pack_Start(boto)