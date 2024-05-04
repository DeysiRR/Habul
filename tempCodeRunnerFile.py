from PyQt5 import QtWidgets, QtCore, QtGui  # Importar QtGui para QIcon

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habul")
        self.resize(500, 200)
        
        # Establecer el icono de la ventana
        icon_path = "Imagenes/logo.ico"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        
        # Habilitar solo el botón de minimizar
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.show()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                reply = QtWidgets.QMessageBox.question(
                    self,
                    "Confirmación",
                    "¿Estás seguro de ocultar la ventana?",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No,
                )
                if reply == QtWidgets.QMessageBox.Yes:
                    self.hide()  # Ocultar la ventana
                else:
                    self.showNormal()  # Restaurar la ventana
        return super(MyWindow, self).changeEvent(event)  # Llamar al método base para no interferir

# Crear la aplicación y mostrar la ventana
app = QtWidgets.QApplication([])
window = MyWindow()
window.show()  # Mostrar la ventana
app.exec_()  # Ejecutar el bucle de eventos
