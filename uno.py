from PyQt5 import QtWidgets, QtCore

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habul")
        self.resize(500, 200)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilitar el botón de maximizar


app = QtWidgets.QApplication([])
window = MyWindow()
window.show()
app.exec_()
