#from os import close
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QWidget
from archivosXML import analizarConfig, analizarSimulacion
from archivosXML import maquina, simulacion

# menú principal
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cargarWin = CargarWin()
        self.repWin = RepWin()
        self.ayudaWin = AyudaWin()
        uic.loadUi("GUI/mainWin.ui", self)

        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonSalir.clicked.connect(exit)
        self.botonCargar.clicked.connect(self.cargarWin.show)
        self.botonRep.clicked.connect(self.repWin.show)
        self.botonAyuda.clicked.connect(self.ayudaWin.show)
        self.botonActualizar.clicked.connect(self.actualizar)

    def actualizar(self):
        #actualizando el comboBox
        if maquina.lProductos != None:
            for p in maquina.lProductos.iterate():
                self.cBoxProducto.addItem(p.nombre)


# ventana para cargar los archivos xml
class CargarWin(QWidget):
    def __init__(self):
        super().__init__()
        self.cConfig = None
        self.cSimulacion = None
        uic.loadUi("GUI/cargaWin.ui", self)

        # labels
        self.label.setHidden(True)
        self.label_2.setHidden(True)

        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonAceptar.clicked.connect(self.close)
        self.botonConfigMaq.clicked.connect(self.browsefiles1)
        self.botonSimulacion.clicked.connect(self.browsefiles2)

    # función para cargar archivo
    def browsefiles1(self):
        # solo acepta archivos con extensión xml
        fname = QFileDialog.getOpenFileName(self, 'Abrir archivo', 'C:\\Users\\gerso\\Desktop\\PROGRAMACIÓN\\Python\\IPC2\\IPC2_Proyecto2_202000166\\PROYECTO2', 'Text files (*.xml)')
        if fname[0]: # si no está vacío el archivo lo lee.
            with open(fname[0], 'r') as f:
                analizarConfig(f)
                self.label.setHidden(False)
    
    def browsefiles2(self):
        # solo acepta archivos con extensión xml
        fname = QFileDialog.getOpenFileName(self, 'Abrir archivo', 'C:\\Users\\gerso\\Desktop\\PROGRAMACIÓN\\Python\\IPC2\\IPC2_Proyecto2_202000166\\PROYECTO2', 'Text files (*.xml)')
        if fname[0]: # si no está vacío el archivo lo lee.
            with open(fname[0], 'r') as f:
                analizarSimulacion(f)
                self.label_2.setHidden(False)


# ventana para crear los reportes
class RepWin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/repWin.ui", self)

        # labels
        self.label_2.setHidden(True)
        self.label_3.setHidden(True)

        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonAceptar.clicked.connect(self.close)


# ventana de ayuda
class AyudaWin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/ayudaWin.ui", self)
        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonAceptar.clicked.connect(self.close)


class ErrorDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/errorDialog.ui", self)
        # botones clickeados y por parámetro las funciones que desencadenan
        self.botonAceptar.clicked.connect(self.close)


# main del programa
app = QApplication(sys.argv)
gui = GUI()
gui.show()
sys.exit(app.exec_())