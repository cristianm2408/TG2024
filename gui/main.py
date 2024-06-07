from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QWidgetAction
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QDialog


from data.tarea import Tareadata
from model.tareas import Tarea






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
        self.v.fon.setText("")
        ImagEM = QPixmap("imagenes/TAREA.jpg")
        self.v.fon.setPixmap(ImagEM)


######## Tareas #######

    def registrarTarea(self):
        if self.v.usu.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar un usuario")
            mBox.exec()
            self.v.usu.setFocus()
        elif self.v.tipo.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar tipo de documento")
            mBox.exec()
            self.v.tipo.setFocus()
        elif len(self.v.ndo.text())<4:
            mBox = QMessageBox()
            mBox.setText("Debe ingresar número de documento válido")
            mBox.exec()
            self.v.ndo.setFocus()
        elif self.v.tarea.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar tipo de tarea")
            mBox.exec()
            self.v.tarea.setFocus()
        elif not self.v.nso.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("Debe ingresar número válido")
            mBox.exec()
            self.v.nso.setFocus()
        else:
            
            tarea =  Tarea(
                usuario = self.v.usu.currentText(),
                tipod = self.v.tipo.currentText(),
                numd = float(self.v.ndo.text()),
                tipot = self.v.tarea.currentText(),
                ticket = float(self.v.nso.text()),
                detalle = self.v.det.text(),
                realizada = self.v.rea.isChecked(),
                validacion = self.v.val.isChecked()

            )

            objData = Tareadata() 
            mBox = QMessageBox()
            if objData.regis(info=tarea):
                mBox.setText("Tarea registrada")
                self.limpiarcampos()
            else:
                mBox.setText("Tarea NO registrada")
            mBox.exec()   

    def limpiarcampos(self):
        self.v.usu.setCurrentIndex(0)
        self.v.tipo.setCurrentIndex(0)
        self.v.ndo.setText("")
        self.v.tarea.setCurrentIndex(0)
        self.v.nso.setText("")
        self.v.det.setText("")
        self.v.rea.setChecked(False)
        self.v.val.setChecked(False)





 

        
         
    
      
    
   
  
  

    
    
 
 