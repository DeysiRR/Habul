from PyQt5 import QtWidgets, QtCore, QtGui

# Definir la clase para la ventana principal
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Habul") 
        self.resize(500, 200)  
        
        icon_path = "Imagenes/logo.ico"  
        self.setWindowIcon(QtGui.QIcon(icon_path))  
        
        # Crear el widget central
        central_widget = QtWidgets.QWidget(self)  
        self.setCentralWidget(central_widget) 
        
        # Crear un layout para el contenido
        layout = QtWidgets.QVBoxLayout(central_widget)  
        
        # Ajustar los márgenes y espaciado del layout
        layout.setContentsMargins(20, 10, 20, 30)  
        layout.setSpacing(10)  # Ajustar el espaciado entre widgets
        
        label = QtWidgets.QLabel("Traductor de Lengua de señas a texto")
        
        label.setAlignment(QtCore.Qt.AlignCenter)  
        
        layout.addWidget(label, alignment=QtCore.Qt.AlignTop)  
        
        # Crear un contenedor (QFrame) con borde negro
        frame = QtWidgets.QFrame()  
        frame.setFrameShape(QtWidgets.QFrame.Box)  
        frame.setLineWidth(1)  
        
        layout.addWidget(frame, stretch=1)  

        # Mostrar la ventana
        self.show()  

# Crear la aplicación y mostrar la ventana
app = QtWidgets.QApplication([]) 
window = MyWindow()  
window.show()  # Mostrar la ventana
app.exec_()  # Ejecutar el bucle de eventos
