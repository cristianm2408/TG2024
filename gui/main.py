from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QWidgetAction
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QDialog





class Mainwindow():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.main.RegistrarT.triggered.connect(self.conectar)
        
        
        self.ventana = Ventana()
     

        self.main.fondo.setText("")
        ImagFo = QPixmap("imagenes/bluep.jpg")
        self.main.fondo.setPixmap(ImagFo)
         
        self.main.emtelco.setText("")  
        ImagE = QPixmap("imagenes/Logop.png")
        self.main.emtelco.setPixmap(ImagE)

        self.main.show()

      
    def conectar(self):
        self.ventana.exec()
       
    
    
class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.v = uic.loadUi("gui/registrotarea.ui",self)
        self.v.reg.clicked.connect(self.registrarTarea)
        self.v.logo.setText("")
        ImagEM = QPixmap("imagenes/FOsp.png")
        self.v.logo.setPixmap(ImagEM)

    def registrarTarea(self):
        if self.v.usu.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un usuario")
            mBox.exec()
        elif self.v.tipo.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar tipo de documento")
            mBox.exec()
        elif len(self.v.ndo.text())<4:
            mBox = QMessageBox()
            mBox.setText("Debe ingresar número de documento válido")
            mBox.exec()
        elif self.v.tarea.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar tipo de tarea")
            mBox.exec()
        elif not self.v.nso.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("Debe ingresar número válido")
            mBox.exec()
       
         
    
      
    
   
  
  

    
    
 
 