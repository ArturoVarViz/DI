import sys
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit, QLabel, \
    QMessageBox, QGridLayout, QHBoxLayout, QComboBox


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 20-02-2024")
        self.setGeometry(100, 100, 1100, 800)

        # Inicializar la base de datos y la tabla
        self.init_database()
        self.init_table_model()

        # Crear la interfaz
        self.init_ui()
        self.load_nAlbaran_combobox()

    def init_database(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("modelosClasicos.dat")

        if not self.db.open():
            QMessageBox.critical(self, "Error", "No se pudo abrir la base de datos")
            sys.exit(1)

    def init_table_model(self):
        self.table_model = QSqlTableModel(db=self.db)
        self.table_model.setTable("detalleVentas")
        self.table_model.select()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Etiquetas y líneas de texto para los datos
        grid_layout = QGridLayout()

        # Número de albaran y data
        nAlbaran_label = QLabel("Número Albarán:")
        self.nAlbaran_combobox = QComboBox()  # Cambiando a un QComboBox
        data_label = QLabel("Data:")
        self.data_line_edit = QLineEdit()
        dataEntrega_label = QLabel("Data Entrega:")
        self.dataEntrega_line_edit = QLineEdit()
        nCliente_label = QLabel("Número Cliente:")
        self.nCliente_line_edit = QLineEdit()

        grid_layout.addWidget(nAlbaran_label, 0, 0)
        grid_layout.addWidget(self.nAlbaran_combobox, 0, 1)
        grid_layout.addWidget(data_label, 0, 2)
        grid_layout.addWidget(self.data_line_edit, 0, 3)
        grid_layout.addWidget(dataEntrega_label, 1, 0)
        grid_layout.addWidget(self.dataEntrega_line_edit, 1, 1, 1, 3)  # Ocupa 3 columnas
        grid_layout.addWidget(nCliente_label, 2, 0)
        grid_layout.addWidget(self.nCliente_line_edit, 2, 1, 1, 3)  # Ocupa 3 columnas

        layout.addLayout(grid_layout)

        # Deshabilitar líneas de texto inicialmente
        self.nAlbaran_combobox.setEnabled(True)
        self.data_line_edit.setEnabled(True)
        self.dataEntrega_line_edit.setEnabled(True)
        self.nCliente_line_edit.setEnabled(True)

        # Botones
        button_layout = QHBoxLayout()

        add_button = QPushButton("Agregar")
        add_button.clicked.connect(self.start_adding)  # Conectar botón Agregar
        button_layout.addWidget(add_button)

        delete_button = QPushButton("Borrar")
        delete_button.clicked.connect(self.delete_record)
        button_layout.addWidget(delete_button)

        edit_button = QPushButton("Editar")
        edit_button.clicked.connect(self.edit_data)
        edit_button.setEnabled(True)
        button_layout.addWidget(edit_button)

        # Tabla
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)

        accept_cancel_layout = QVBoxLayout(central_widget)
        accept_button = QPushButton("Aceptar")
        accept_button.clicked.connect(self.save_changes)
        accept_button.setEnabled(False)
        accept_cancel_layout.addWidget(accept_button)

        cancel_button = QPushButton("Cancelar")
        cancel_button.clicked.connect(self.cancel_changes)
        cancel_button.setEnabled(False)
        accept_cancel_layout.addWidget(cancel_button)

        # Agregar los botones Aceptar y Cancelar en un layout vertical
        button_layout.addLayout(accept_cancel_layout)

        # Agregar la tabla y los botones a un layout horizontal
        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.table_view)
        hbox_layout.addLayout(button_layout)

        # Agregar el layout horizontal al layout principal
        layout.addLayout(hbox_layout)

        # Establecer comportamiento de los botones
        self.add_button = add_button
        self.save_button = accept_button
        self.delete_button = delete_button
        self.cancel_button = cancel_button
        self.edit_button = edit_button

        layout.addWidget(self.table_view)
        layout.addLayout(button_layout)

        # Conectar la señal currentIndexChanged del QComboBox a la función update_fields
        self.nAlbaran_combobox.currentIndexChanged.connect(self.update_fields)

    def update_fields(self, index):
        # Obtener el número de albarán seleccionado
        selected_numero_albaran = self.nAlbaran_combobox.currentText()

        # Aplicar un filtro al modelo de la tabla para mostrar solo los registros con el número de albarán seleccionado
        self.table_model.setFilter(f"numeroAlbaran = '{selected_numero_albaran}'")
        self.table_model.select()

    def load_nAlbaran_combobox(self):
        try:
            # Limpiar el combo box
            self.nAlbaran_combobox.clear()

            # Obtener la lista de albaranes relacionados con los registros en la tabla detalleVentas
            query = QSqlQuery("SELECT DISTINCT numeroAlbaran FROM detalleVentas", self.db)

            # Agregar cada albarán al combo box
            while query.next():
                numero_albaran = query.value(0)
                self.nAlbaran_combobox.addItem(str(numero_albaran))
        except Exception as e:
            print(f"Excepción en load_nAlbaran_combobox: {e}")
            QMessageBox.critical(self, "Error", f"Excepción en load_nAlbaran_combobox: {e}")

    def start_adding(self):
        # Habilitar líneas de texto y deshabilitar botón Agregar

        self.dataEntrega_line_edit.setEnabled(True)
        self.nCliente_line_edit.setEnabled(True)
        self.add_button.setEnabled(False)
        self.save_button.setEnabled(True)
        self.delete_button.setEnabled(False)
        self.cancel_button.setEnabled(True)
        self.nAlbaran_combobox.setEnabled(True)  # Cambiar a habilitar el combo
        self.data_line_edit.setEnabled(True)


    def save_changes(self):
        nAlbaran = self.nAlbaran_combobox
        nome = self.data_line_edit.text()
        dataEntrega = self.dataEntrega_line_edit.text()
        nCliente = self.nCliente_line_edit.text()


        if not nAlbaran or not nome or not dataEntrega or not nCliente :
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios")
            return

        row = self.table_model.rowCount()
        self.table_model.insertRow(row)

        self.table_model.setData(self.table_model.index(row, 0), nAlbaran)
        self.table_model.setData(self.table_model.index(row, 1), nome)
        self.table_model.setData(self.table_model.index(row, 2), dataEntrega)
        self.table_model.setData(self.table_model.index(row, 3), nCliente)


        # Aplicar cambios a la base de datos
        self.table_model.submitAll()

        # Actualizar el modelo para reflejar los cambios en la tabla
        self.table_model.select()

        # Limpiar campos y deshabilitar botón Guardar
        self.nAlbaran_combo.clear()
        self.data_line_edit.clear()
        self.dataEntrega_line_edit.clear()
        self.nCliente_line_edit.clear()

        self.nAlbaran_combo.setEnabled(False)
        self.data_line_edit.setEnabled(False)
        self.dataEntrega_line_edit.setEnabled(False)
        self.nCliente_line_edit.setEnabled(False)

        self.add_button.setEnabled(True)
        self.save_button.setEnabled(False)
        self.delete_button.setEnabled(True)
        self.cancel_button.setEnabled(False)

        # Mostrar mensaje de éxito
        self.success_label.setText("<html><b style='color: green;'>LOS DATOS SE HAN GUARDADO CORRECTAMENTE</b></html>")

    def delete_record(self):
        selected_rows = self.centralWidget().findChild(QTableView).selectionModel().selectedRows()

        if selected_rows:
            reply = QMessageBox.question(self, "Confirmación", "¿Estás seguro que quieres borrar los datos?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                for index in selected_rows:
                    self.table_model.removeRow(index.row())

                # Actualizar el modelo para reflejar los cambios en la tabla
                self.table_model.select()

                # Limpiar campos y deshabilitar botón Guardar

                self.data_line_edit.clear()
                self.dataEntrega_line_edit.clear()
                self.nCliente_line_edit.clear()


                self.data_line_edit.setEnabled(False)
                self.dataEntrega_line_edit.setEnabled(False)
                self.nCliente_line_edit.setEnabled(False)

                self.add_button.setEnabled(True)
                self.save_button.setEnabled(False)
                self.delete_button.setEnabled(True)
                self.cancel_button.setEnabled(False)
               # self.success_label.setText("<html><b style='color: red;'>BORRADO EXITOSO</b></html>")
            else:
                # Si el usuario elige no borrar, mantener los campos y habilitar el botón Agregar
                self.add_button.setEnabled(True)
                self.save_button.setEnabled(False)
                self.delete_button.setEnabled(True)
                self.cancel_button.setEnabled(False)
        else:
            QMessageBox.warning(self, "Advertencia", "Selecciona al menos una fila para borrar.\nPulsa en el número de la fila.")


    def cancel_changes(self):
        reply = QMessageBox.question(self, "Confirmación", "¿Estás seguro que quieres borrar los datos introducidos?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            # Limpiar campos y deshabilitar botón Guardar
            #self.nAlbaran_combobox.clear()
            self.data_line_edit.clear()
            self.dataEntrega_line_edit.clear()
            self.nCliente_line_edit.clear()

            #self.nAlbaran_combobox.setEnabled(False)
            self.data_line_edit.setEnabled(False)
            self.dataEntrega_line_edit.setEnabled(False)
            self.nCliente_line_edit.setEnabled(False)
            self.add_button.setEnabled(True)
            self.save_button.setEnabled(False)
            self.delete_button.setEnabled(True)
            self.cancel_button.setEnabled(False)
            #self.success_label.clear()
        else:
            # Si el usuario elige no borrar, mantener los campos y habilitar el botón Agregar
            self.add_button.setEnabled(False)
            self.save_button.setEnabled(True)
            self.cancel_button.setEnabled(True)

    def edit_data(self):
        try:
            if self.edit_button.text() == "Editar":
                reply = QMessageBox.question(self, "Confirmación",
                                             "Estás entrando en el proceso de Edición de datos, ¿Quieres continuar?",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    selected_index = self.nAlbaran_combobox.currentIndex()  # Obtener el índice seleccionado del combo

                    # Obtener el valor seleccionado del combo
                    selected_option = self.nAlbaran_combobox.itemText(selected_index)

                    # Buscar la fila correspondiente a la opción seleccionada
                    for row in range(self.table_model.rowCount()):
                        if self.table_model.index(row, 0).data() == selected_option:
                            # Obtener los datos de la fila
                            nCliente = str(self.table_model.index(row, 2).data())
                            data = str(self.table_model.index(row, 0).data())
                            dEntrega = str(self.table_model.index(row, 1).data())

                            # Rellenar líneas de texto con los datos seleccionados
                            self.nAlbaran_combo.setText(nCliente)
                            self.data_line_edit.setText(data)
                            self.dataEntrega_line_edit.setText(dEntrega)

                            # Habilitar líneas de texto y deshabilitar/agregar/eliminar/botones según sea necesario
                            self.nAlbaran_combobox.setEnabled(True)
                            self.data_line_edit.setEnabled(True)
                            self.dataEntrega_line_edit.setEnabled(True)
                            self.nCliente_line_edit.setEnabled(True)

                            self.add_button.setEnabled(False)
                            self.save_button.setEnabled(False)
                            self.delete_button.setEnabled(False)
                            self.cancel_button.setEnabled(True)
                            self.edit_button.setText("Guardar Edición")

                            break  # Salir del bucle una vez que se haya encontrado la fila
                    else:
                        QMessageBox.warning(self, "Advertencia",
                                            "No se encontró el número de albarán seleccionado en la tabla.")
            elif self.edit_button.text() == "Guardar Edición":
                # Obtener el índice seleccionado del combo
                selected_index = self.nAlbaran_combobox.currentIndex()

                # Obtener el valor seleccionado del combo
                selected_option = self.nAlbaran_combobox.itemText(selected_index)

                # Buscar la fila correspondiente a la opción seleccionada
                for row in range(self.table_model.rowCount()):
                    if self.table_model.index(row, 0).data() == selected_option:
                        # Obtener los datos de la fila
                        # No es necesario obtener datos aquí porque ya estamos en la fila correcta

                        # Obtener los nuevos datos de los campos
                        data = self.data_line_edit.text()
                        dEntrega = self.dataEntrega_line_edit.text()
                        nCliente = self.nCliente_line_edit.text()

                        # Actualizar la tabla y la base de datos con los nuevos datos
                        self.table_model.setData(self.table_model.index(row, 0), data)
                        self.table_model.setData(self.table_model.index(row, 1), dEntrega)
                        self.table_model.setData(self.table_model.index(row, 2), nCliente)

                        self.table_model.submitAll()  # Guardar cambios en la base de datos

                        # Deshabilitar líneas de texto y habilitar/deshabilitar/agregar/eliminar botones según sea necesario
                        self.nAlbaran_combobox.clear()
                        self.data_line_edit.clear()
                        self.dataEntrega_line_edit.clear()
                        self.nCliente_line_edit.clear()

                        self.nAlbaran_combobox.setEnabled(False)
                        self.data_line_edit.setEnabled(False)
                        self.dataEntrega_line_edit.setEnabled(False)
                        self.nCliente_line_edit.setEnabled(False)

                        self.add_button.setEnabled(True)
                        self.save_button.setEnabled(False)
                        self.delete_button.setEnabled(True)
                        self.cancel_button.setEnabled(False)
                        self.edit_button.setEnabled(True)
                        self.success_label.setText("<html><b style='color: green;'>CAMBIO EXITOSO</b></html>")

                        # Refrescar la tabla para reflejar los cambios
                        self.table_model.select()

                        # Restablecer el nombre del botón y dejar de pintar en verde las líneas de texto
                        self.edit_button.setText("Editar")
                        self.nAlbaran_combobox.setStyleSheet("")
                        self.data_line_edit.setStyleSheet("")
                        self.dataEntrega_line_edit.setStyleSheet("")
                        self.nCliente_line_edit.setStyleSheet("")

                        break  # Salir del bucle una vez que se haya encontrado la fila
                else:
                    QMessageBox.warning(self, "Advertencia",
                                        "No se encontró el número de albarán seleccionado en la tabla.")
        except Exception as e:
            print(f"Excepción en edit_data: {e}")
            QMessageBox.critical(self, "Error", f"Excepción en edit_data: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())
