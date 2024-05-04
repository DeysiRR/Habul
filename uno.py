from PyQt5 import QtWidgets, QtCore, QtGui

# Definir la clase para la ventana principal
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializar la clase base
        self.setWindowTitle("Habul")  # Establecer el título de la ventana
        self.resize(500, 200)  # Establecer el tamaño de la ventana
        
        # Establecer el icono de la ventana
        icon_path = "Imagenes/logo.ico"  # Ruta del icono
        self.setWindowIcon(QtGui.QIcon(icon_path))  # Configurar el icono
        
        # Crear el widget central
        central_widget = QtWidgets.QWidget(self)  # Widget central para el contenido
        self.setCentralWidget(central_widget)  # Configurar el widget central
        
        # Crear un layout para el contenido
        layout = QtWidgets.QVBoxLayout(central_widget)  # Layout vertical
        
        # Ajustar los márgenes y espaciado del layout
        layout.setContentsMargins(10, 10, 10, 10)  # Reducir el margen del layout
        layout.setSpacing(5)  # Ajustar el espaciado entre widgets
        
        # Crear un QLabel para el texto
        label = QtWidgets.QLabel("Traductor de Lengua de señas a texto")
        
        # Centramos el texto
        label.setAlignment(QtCore.Qt.AlignCenter)  # Centrar el texto
        
        # Añadir el QLabel al layout en la parte superior
        layout.addWidget(label, alignment=QtCore.Qt.AlignTop)  # Alineación en la parte superior
        
        # Crear un contenedor (QFrame) con borde negro
        frame = QtWidgets.QFrame()  # Crear el contenedor
        frame.setFrameShape(QtWidgets.QFrame.Box)  # Borde tipo caja
        frame.setLineWidth(1)  # Grosor del borde
        
        # Añadir el contenedor al layout
        layout.addWidget(frame, stretch=1)  # Añadir el frame con stretch para el espaciado

        # Mostrar la ventana
        self.show()  # Mostrar la ventana

# Crear la aplicación y mostrar la ventana
app = QtWidgets.QApplication([])  # Crear la aplicación
window = MyWindow()  # Crear la ventana
window.show()  # Mostrar la ventana
app.exec_()  # Ejecutar el bucle de eventos
