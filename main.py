import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QWidgetAction
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QDate
from datetime import datetime
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon


import fitz 



from historial import Historialdata
from tarea import Tareadata
import tarea
from tareas import Tarea



class Mainwindow():


    def __init__(self):

        self.main = uic.loadUi("main.ui")

        self.main.setWindowIcon(QIcon('imagenes/em.png'))

        
        self.main.gest.setText("")
        ImagG = QPixmap("imagenes/ges.png")
        self.main.gest.setPixmap(ImagG)
         
        
        self.main.fondo.setText("")
        ImagFo = QPixmap("imagenes/fonda.png")
        self.main.fondo.setPixmap(ImagFo)
         
        self.main.emtelco.setText("")  
        ImagE = QPixmap("imagenes/Logop.png")
        self.main.emtelco.setPixmap(ImagE)

        ImagT = QPixmap("imagenes/regisfon.png")
        icono = QIcon(ImagT)
        self.main.regt.setIcon(icono)

        
        ImagB = QPixmap("imagenes/baset.png")
        icono = QIcon(ImagB)
        self.main.bas.setIcon(icono)

        
        ImagBU = QPixmap("imagenes/usuu.png")
        icono = QIcon(ImagBU)
        self.main.busu.setIcon(icono)

        
        ImagBUF = QPixmap("imagenes/cale.png")
        icono = QIcon(ImagBUF)
        self.main.busf.setIcon(icono)

           
        ImagBUV = QPixmap("imagenes/vlan.png")
        icono = QIcon(ImagBUV)
        self.main.busv.setIcon(icono)


        ImagBUG = QPixmap("imagenes/guia.png")
        icono = QIcon(ImagBUG)
        self.main.guiau.setIcon(icono)

        
        ImagE = QPixmap("imagenes/del.png")
        icono = QIcon(ImagE)
        self.main.eli.setIcon(icono)

     

     
     

     


     

     
        self.initGUI()
        self.main.show()

    def initGUI(self):
      

        self.main.regt.clicked.connect(self.abrirregistro)
        self.main.bas.clicked.connect(self.abrirbase)
        self.main.busu.clicked.connect(self.abrirhistorial)
        self.main.busf.clicked.connect(self.abrirhistorialf)
        self.main.busv.clicked.connect(self.abrirhistorialv)
        self.main.acerca.triggered.connect(self.abririnfo)
        self.main.manual.triggered.connect(self.abrirguia)
        self.main.guiau.clicked.connect(self.abrirguia)
        self.main.eli.clicked.connect(self.abrireli)
        self.baset = uic.loadUi("base.ui")
        self.registro = uic.loadUi("registrotarea.ui")
        self.historial = uic.loadUi("historial.ui")
        self.historialf = uic.loadUi("historialf.ui")
        self.historialv = uic.loadUi("historialc.ui")
        self.historiale = uic.loadUi("eliminar.ui")
        self.guia = uic.loadUi("guia.ui")
        self.guiau = uic.loadUi("guiau.ui")
        self.info = uic.loadUi("info.ui")
        self.historialdata = Historialdata(self.historiale) 
        self.historiale.eliminar.clicked.connect(self.historialdata.eliminar_tarea_por_ticket)


      


   
    

    
        

    def abrirregistro(self):
        self.registro.reg.clicked.connect(self.registrarTarea)
        self.registro.setWindowIcon(QIcon('imagenes/em.png'))

        self.registro.logo.setText("")
        ImagEM = QPixmap("imagenes/FOsp.png")
        self.registro.logo.setPixmap(ImagEM)

        self.registro.registro.setText("")
        ImagEM = QPixmap("imagenes/registro.png")
        self.registro.registro.setPixmap(ImagEM)

        self.registro.fon.setText("")
        ImagEM = QPixmap("imagenes/gra.png")
        self.registro.fon.setPixmap(ImagEM)
        
    
    
        self.registro.show()

    
    def abrirbase(self):
         
        
        self.baset.tablab.setColumnWidth(0,120) #usuario
        self.baset.tablab.setColumnWidth(1,150) #VLAN
        self.baset.tablab.setColumnWidth(2,110) #tipot
        self.baset.tablab.setColumnWidth(3,100)  #ticket
        self.baset.tablab.setColumnWidth(4,180) #equipos
        self.baset.tablab.setColumnWidth(5,200) #solicitud
        self.baset.tablab.setColumnWidth(6,190) #solucion
        self.baset.tablab.setColumnWidth(7,70) #realizad
        self.baset.tablab.setColumnWidth(8,150) #fecha

        self.baset.setWindowIcon(QIcon('imagenes/em.png'))
         
        his = Historialdata(self.historiale)
        data = his.basedatos("01/01/1970", "31/12/3099") 

        self.baset.log.setText("")
        ImagEM = QPixmap("imagenes/FOsp.png")
        self.baset.log.setPixmap(ImagEM)

        self.baset.registro.setText("")
        ImagEMT = QPixmap("imagenes/histo.png")
        self.baset.registro.setPixmap(ImagEMT)


        self.baset.fonhisb.setText("")
        ImagEM = QPixmap("imagenes/gra.png")
        self.baset.fonhisb.setPixmap(ImagEM)    
        
        fila=0
        self.baset.tablab.setRowCount(len(data))
        for item in data:
            self.baset.tablab.setItem(fila,0,QTableWidgetItem(str(item[0]))) #usuario
            self.baset.tablab.setItem(fila,1,QTableWidgetItem(str(item[1]))) #VLAN 
            self.baset.tablab.setItem(fila,2,QTableWidgetItem(str(item[2]))) #tipot
            self.baset.tablab.setItem(fila,3,QTableWidgetItem(str(item[3]))) #ticket
            self.baset.tablab.setItem(fila,4,QTableWidgetItem(str(item[4]))) #equipos
            self.baset.tablab.setItem(fila,5,QTableWidgetItem(str(item[5]))) #detalles
            self.baset.tablab.setItem(fila,6,QTableWidgetItem(str(item[6]))) #solucion
            self.baset.tablab.setItem(fila,8,QTableWidgetItem(str(item[9]))) #fecha
          
            if item[7] == 'True':
              self.baset.tablab.setItem(fila,7,QTableWidgetItem("si"))
            else:
              self.baset.tablab.setItem(fila,7,QTableWidgetItem("no"))
               
              
              

            fila=fila+1
    
    
        self.baset.show()    
        self.llenarhistorial()


    def abrirhistorial(self):

        self.historial.bus.clicked.connect(self.buscar)
        self.historial.setWindowIcon(QIcon('imagenes/em.png'))

        
        self.historial.registro2.setText("")
        ImagLO = QPixmap("imagenes/histo.png")
        self.historial.registro2.setPixmap(ImagLO)


        self.historial.log.setText("")
        ImagLO = QPixmap("imagenes/FOsp.png")
        self.historial.log.setPixmap(ImagLO)

        self.historial.fonhis.setText("")
        ImagFOON = QPixmap("imagenes/gra.png")
        self.historial.fonhis.setPixmap(ImagFOON)

       
        self.historial.tablat.setColumnWidth(0,120) #usuario
        self.historial.tablat.setColumnWidth(1,150) #VLAN
        self.historial.tablat.setColumnWidth(2,110) #tipot
        self.historial.tablat.setColumnWidth(3,100)  #ticket
        self.historial.tablat.setColumnWidth(4,200) #equipos
        self.historial.tablat.setColumnWidth(5,200) #solicitud
        self.historial.tablat.setColumnWidth(6,190) #solucion
        self.historial.tablat.setColumnWidth(7,70) #realizad
        self.historial.tablat.setColumnWidth(8,150) #fecha


        self.historial.show()
        self.llenarhistorial()


    def abrirhistorialf(self):

        self.historialf.hbus.clicked.connect(self.buscarf)
        self.historialf.setWindowIcon(QIcon('imagenes/em.png'))

        self.historialf.log.setText("")
        ImagLO = QPixmap("imagenes/FOsp.png")
        self.historialf.log.setPixmap(ImagLO)

        
        self.historialf.registro3.setText("")
        ImagLOF = QPixmap("imagenes/histo.png")
        self.historialf.registro3.setPixmap(ImagLOF)


        self.historialf.fonhis.setText("")
        ImagFOON = QPixmap("imagenes/gra.png")
        self.historialf.fonhis.setPixmap(ImagFOON)

      
        self.historialf.tablatf.setColumnWidth(0,120) #usuario
        self.historialf.tablatf.setColumnWidth(1,150) #VLAN
        self.historialf.tablatf.setColumnWidth(2,110) #tipot
        self.historialf.tablatf.setColumnWidth(3,100)  #ticket
        self.historialf.tablatf.setColumnWidth(4,200) #equipos
        self.historialf.tablatf.setColumnWidth(5,200) #solicitud
        self.historialf.tablatf.setColumnWidth(6,190) #solucion
        self.historialf.tablatf.setColumnWidth(7,70) #realizad
        self.historialf.tablatf.setColumnWidth(8,150) #fecha


      
        self.historialf.show()
        self.llenarhistorial()
    
    def abrirhistorialv(self):

        self.historialv.buscarv.clicked.connect(self.buscarv)
        self.historialv.setWindowIcon(QIcon('imagenes/em.png'))

        self.historialv.log.setText("")
        ImagLO = QPixmap("imagenes/FOsp.png")
        self.historialv.log.setPixmap(ImagLO)

        self.historialv.registro4.setText("")
        ImagLOF = QPixmap("imagenes/histo.png")
        self.historialv.registro4.setPixmap(ImagLOF)


        self.historialv.fonhis.setText("")
        ImagFOON = QPixmap("imagenes/gra.png")
        self.historialv.fonhis.setPixmap(ImagFOON)

       
        self.historialv.tablav.setColumnWidth(0,120) #usuario
        self.historialv.tablav.setColumnWidth(1,150) #VLAN
        self.historialv.tablav.setColumnWidth(2,110) #tipot
        self.historialv.tablav.setColumnWidth(3,100)  #ticket
        self.historialv.tablav.setColumnWidth(4,200) #equipos
        self.historialv.tablav.setColumnWidth(5,200) #solicitud
        self.historialv.tablav.setColumnWidth(6,190) #solucion
        self.historialv.tablav.setColumnWidth(7,70) #realizad
        self.historialv.tablav.setColumnWidth(8,150) #fecha
    

        self.historialv.show()
        self.llenarhistorial()

    def abrireli(self):
    # Mostrar la ventana de eliminación
        
        self.historiale.setWindowIcon(QIcon('imagenes/em.png'))
         
        
        

        self.historiale.log.setText("")
        ImagEM = QPixmap("imagenes/FOsp.png")
        self.historiale.log.setPixmap(ImagEM)

        self.historiale.fonhisb.setText("")
        ImagEM = QPixmap("imagenes/fonda.png")
        self.historiale.fonhisb.setPixmap(ImagEM)    
        self.historiale.show()
     

    def abririnfo(self):

        self.info.autor.setText("")
        ImagLO = QPixmap("imagenes/8083308.png")
        self.info.autor.setPixmap(ImagLO)
        self.info.setWindowIcon(QIcon('imagenes/em.png'))

        self.info.show()

    def abrirguia(self):
        
        self.guiau.setWindowIcon(QIcon('imagenes/em.png'))

        self.guiau.guia1.setText("")
        ImagEMG = QPixmap("imagenes/guia1.jpg")
        self.guiau.guia1.setPixmap(ImagEMG)

        self.guiau.guia2.setText("")
        ImagEMG = QPixmap("imagenes/guia2.jpg")
        self.guiau.guia2.setPixmap(ImagEMG)

        self.guiau.guia3.setText("")
        ImagEMG = QPixmap("imagenes/guia3.jpg")
        self.guiau.guia3.setPixmap(ImagEMG)
        
        self.guiau.guia4.setText("")
        ImagEMG = QPixmap("imagenes/guia4.jpg")
        self.guiau.guia4.setPixmap(ImagEMG)

        self.guiau.guia5.setText("")
        ImagEMG = QPixmap("imagenes/guia5.jpg")
        self.guiau.guia5.setPixmap(ImagEMG)

        self.guiau.guia6.setText("")
        ImagEMG = QPixmap("imagenes/guia6.jpg")
        self.guiau.guia6.setPixmap(ImagEMG)

        self.guiau.guia7.setText("")
        ImagEMG = QPixmap("imagenes/guia7.jpg")
        self.guiau.guia7.setPixmap(ImagEMG)


        
        self.guiau.manual.setText("")
        ImagLOG = QPixmap("imagenes/man.png")
        self.guiau.manual.setPixmap(ImagLOG)

        
        self.guiau.fonhis.setText("")
        ImagLOGF = QPixmap("imagenes/gra.png")
        self.guiau.fonhis.setPixmap(ImagLOGF)
       
       
      
       
      

      
        self.guiau.show()



   
#####REGISTRAR TAREA ###

    def registrarTarea(self):


        if len(self.registro.usu.text())<4:
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Debe ingresar usuario")
            self.registro.usu.setFocus()
    
        elif self.registro.rvlan.currentText() =="---Seleccione una opción":
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Debe seleccionar la VLAN")
            self.registro.rvlan.setFocus()

        elif self.registro.tarea.currentText() =="---Seleccione una opción":
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Debe seleccionar tipo de tarea")
            self.registro.tarea.setFocus()

        elif len(self.registro.nso.text())<4:
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Debe ingresar ticket válido")
            self.registro.nso.setFocus()

        elif len(self.registro.equi.toPlainText())<4:
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Ingrese el nombre de los equipos")
            self.registro.equi.setFocus()
        
        elif len(self.registro.det.toPlainText())<4:
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Ingrese descripción de solicitud")
            self.registro.equi.setFocus()

        elif len(self.registro.dets.toPlainText())<4:
            mbox = QMessageBox()
            mbox.information(self.registro, "Alerta", "Ingrese detalles de solucion")
            self.registro.equi.setFocus()
       
       
       
        else:
            
            tarea =  Tarea(
                
                usuario = self.registro.usu.text(),
                vlan = self.registro.rvlan.currentText(),
                tipot = self.registro.tarea.currentText(),
                ticket = float(self.registro.nso.text()),
                equipos = self.registro.equi.toPlainText(),
                detalle = self.registro.det.toPlainText(),
                detalles = self.registro.dets.toPlainText(),
                realizada = self.registro.rea.isChecked(),
                validacion = self.registro.val.isChecked(),

            )

            objData = Tareadata() 
            mBox = QMessageBox()
            if objData.regis(info=tarea):
                mBox.information(self.registro, "Registro", "¡Nueva tarea registrada!")
                  
                self.limpiarcampos()
            else:
                mBox.information(self.registro, "Error", "Tarea NO registrada")
             
              
           

    def limpiarcampos(self):
        self.registro.usu.setText("")
        self.registro.rvlan.setCurrentIndex(0)
        self.registro.tarea.setCurrentIndex(0)
        self.registro.nso.setText("")
        self.registro.equi.clear()
        self.registro.det.clear()
        self.registro.dets.clear()
        self.registro.rea.setChecked(False)
        self.registro.val.setChecked(False)
    

    




    def buscar(self):
        hisu = Historialdata(self.historiale)
        data =hisu.buscarfecha(self.historial.cusu.text(),self.historial.fdesde.text(),self.historial.fhasta.text())

        if not data:  
         QMessageBox.information(self.historial, "Sin resultados", "No hay tareas registradas con este usuario")
         return  
        fila=0
        self.historial.tablat.setRowCount(len(data))
        for item in data:
            self.historial.tablat.setItem(fila,0,QTableWidgetItem(str(item[0]))) #usuario
            self.historial.tablat.setItem(fila,1,QTableWidgetItem(str(item[1]))) #VLAN 
            self.historial.tablat.setItem(fila,2,QTableWidgetItem(str(item[2]))) #tipot
            self.historial.tablat.setItem(fila,3,QTableWidgetItem(str(item[3]))) #ticket
            self.historial.tablat.setItem(fila,4,QTableWidgetItem(str(item[4]))) #equipos
            self.historial.tablat.setItem(fila,5,QTableWidgetItem(str(item[5]))) #detalles
            self.historial.tablat.setItem(fila,6,QTableWidgetItem(str(item[6]))) #solucion
            self.historial.tablat.setItem(fila,8,QTableWidgetItem(str(item[9]))) #fecha
          
            if item[7] == 'True':
              self.historial.tablat.setItem(fila,7,QTableWidgetItem("si"))
            else:
              self.historial.tablat.setItem(fila,7,QTableWidgetItem("no"))
               
              
              

            fila=fila+1


    def buscarf(self):
        hisf = Historialdata(self.historiale)
        dataf =hisf.buscarfechaf(self.historialf.hdesdef.text(),self.historialf.hhastaf.text())
        if not dataf:  
         QMessageBox.information(self.historialf, "Sin resultados", "No hay tareas registradas en el rango de fechas")
         return  
        fila=0
        self.historialf.tablatf.setRowCount(len(dataf))
        for item in dataf:
            self.historialf.tablatf.setItem(fila,0,QTableWidgetItem(str(item[0])))
            self.historialf.tablatf.setItem(fila,1,QTableWidgetItem(str(item[1])))
            self.historialf.tablatf.setItem(fila,2,QTableWidgetItem(str(item[2])))
            self.historialf.tablatf.setItem(fila,3,QTableWidgetItem(str(item[3])))
            self.historialf.tablatf.setItem(fila,4,QTableWidgetItem(str(item[4])))
            self.historialf.tablatf.setItem(fila,5,QTableWidgetItem(str(item[5])))
            self.historialf.tablatf.setItem(fila,6,QTableWidgetItem(str(item[6])))
            self.historialf.tablatf.setItem(fila,8,QTableWidgetItem(str(item[9])))
            if item[7] == 'True':
              self.historialf.tablatf.setItem(fila,7,QTableWidgetItem("si"))
            else:
              self.historialf.tablatf.setItem(fila,7,QTableWidgetItem("no"))
               
              

            fila=fila+1

    def buscarv(self):
        hisv = Historialdata(self.historiale)
        datav =hisv.buscarfechav(self.historialv.nvlan.currentText(),"01/01/1970", "31/12/3099")
        if not datav:  
         QMessageBox.information(self.historialv, "Sin resultados", "No hay tareas registradas con esta VLAN")
         return  
        fila=0
        self.historialv.tablav.setRowCount(len(datav))
        for item in datav:
            self.historialv.tablav.setItem(fila,0,QTableWidgetItem(str(item[0])))
            self.historialv.tablav.setItem(fila,1,QTableWidgetItem(str(item[1])))
            self.historialv.tablav.setItem(fila,2,QTableWidgetItem(str(item[2])))
            self.historialv.tablav.setItem(fila,3,QTableWidgetItem(str(item[3])))
            self.historialv.tablav.setItem(fila,4,QTableWidgetItem(str(item[4])))
            self.historialv.tablav.setItem(fila,5,QTableWidgetItem(str(item[5])))
            self.historialv.tablav.setItem(fila,6,QTableWidgetItem(str(item[6])))
            self.historialv.tablav.setItem(fila,8,QTableWidgetItem(str(item[9])))
            if item[7] == 'True':
              self.historialv.tablav.setItem(fila,7,QTableWidgetItem("si"))
            else:
              self.historialv.tablav.setItem(fila,7,QTableWidgetItem("no"))
               
              

            fila=fila+1
        
     
    

    def  llenarhistorial(self):
        pass
   
      



        
         
    
      
    
   
  
  

    
    
 
 