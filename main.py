import sys
import sqlite3
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
        
        self.main.fondo.setText("")
        ImagFo = QPixmap("imagenes/bluep.jpg")
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

     


     

     
        self.initGUI()
        self.main.show()

    def initGUI(self):
        self.main.regt.clicked.connect(self.abrirregistro)
        self.main.bas.clicked.connect(self.abrirbase)
        self.main.busu.clicked.connect(self.abrirhistorial)
        self.main.buscarf.triggered.connect(self.abrirhistorialf)
        self.main.buscarv.triggered.connect(self.abrirhistorialv)
        self.main.acerca.triggered.connect(self.abririnfo)
        self.main.guia.triggered.connect(self.abrirguia)
        self.baset = uic.loadUi("base.ui")
        self.registro = uic.loadUi("registrotarea.ui")
        self.historial = uic.loadUi("historial.ui")
        self.historialf = uic.loadUi("historialf.ui")
        self.historialv = uic.loadUi("historialc.ui")
        self.guia = uic.loadUi("guia.ui")
        self.guiau = uic.loadUi("guiau.ui")
        self.info = uic.loadUi("info.ui")

      


   
    def mostrarg(self):
        self.guiau.show()

    
        

    def abrirregistro(self):
        self.registro.reg.clicked.connect(self.registrarTarea)
        self.registro.logo.setText("")
        ImagEM = QPixmap("imagenes/FOsp.png")
        self.registro.logo.setPixmap(ImagEM)

        self.registro.fon.setText("")
        ImagEM = QPixmap("imagenes/cla.png")
        self.registro.fon.setPixmap(ImagEM)
        
    
    
        self.registro.show()

    
    def abrirbase(self):
         
        
        self.baset.tablab.setColumnWidth(0,150) #usuario
        self.baset.tablab.setColumnWidth(1,150) #VLAN
        self.baset.tablab.setColumnWidth(2,110) #tipot
        self.baset.tablab.setColumnWidth(3,90)  #ticket
        self.baset.tablab.setColumnWidth(4,200) #equipos
        self.baset.tablab.setColumnWidth(5,120) #solicitud
        self.baset.tablab.setColumnWidth(6,260) #solucion
        self.baset.tablab.setColumnWidth(7,70) #realizad
        self.baset.tablab.setColumnWidth(8,150) #fecha

 
         
        his = Historialdata()
        data = his.basedatos("01/01/1970", "31/12/2099") 

        self.baset.log.setText("")
        ImagEM = QPixmap("imagenes/FOsp.png")
        self.baset.log.setPixmap(ImagEM)

        self.baset.fonhisb.setText("")
        ImagEM = QPixmap("imagenes/cla.png")
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

        self.historial.log.setText("")
        ImagLO = QPixmap("imagenes/FOsp.png")
        self.historial.log.setPixmap(ImagLO)

        self.historial.fonhis.setText("")
        ImagFOON = QPixmap("imagenes/cla.png")
        self.historial.fonhis.setPixmap(ImagFOON)

       
        self.historial.tablat.setColumnWidth(0,150) #usuario
        self.historial.tablat.setColumnWidth(1,150) #VLAN
        self.historial.tablat.setColumnWidth(2,110) #tipot
        self.historial.tablat.setColumnWidth(3,90)  #ticket
        self.historial.tablat.setColumnWidth(4,200) #equipos
        self.historial.tablat.setColumnWidth(5,120) #solicitud
        self.historial.tablat.setColumnWidth(6,260) #solucion
        self.historial.tablat.setColumnWidth(7,70) #realizad
        self.historial.tablat.setColumnWidth(8,150) #fecha


        self.historial.show()
        self.llenarhistorial()


    def abrirhistorialf(self):

        self.historialf.hbus.clicked.connect(self.buscarf)

        self.historialf.log.setText("")
        ImagLO = QPixmap("imagenes/FOsp.png")
        self.historialf.log.setPixmap(ImagLO)

        self.historialf.fonhis.setText("")
        ImagFOON = QPixmap("imagenes/TAREA.jpg")
        self.historialf.fonhis.setPixmap(ImagFOON)

      
        self.historialf.tablatf.setColumnWidth(0,150) #usuario
        self.historialf.tablatf.setColumnWidth(1,150) #VLAN
        self.historialf.tablatf.setColumnWidth(2,110) #tipot
        self.historialf.tablatf.setColumnWidth(3,90)  #ticket
        self.historialf.tablatf.setColumnWidth(4,200) #equipos
        self.historialf.tablatf.setColumnWidth(5,120) #solicitud
        self.historialf.tablatf.setColumnWidth(6,260) #solucion
        self.historialf.tablatf.setColumnWidth(7,70) #realizad
        self.historialf.tablatf.setColumnWidth(8,150) #fecha


      
        self.historialf.show()
        self.llenarhistorial()
    
    def abrirhistorialv(self):

        self.historialv.buscarv.clicked.connect(self.buscarv)

        self.historialv.log.setText("")
        ImagLO = QPixmap("imagenes/FOsp.png")
        self.historialv.log.setPixmap(ImagLO)

        self.historialv.fonhis.setText("")
        ImagFOON = QPixmap("imagenes/TAREA.jpg")
        self.historialv.fonhis.setPixmap(ImagFOON)

       
        self.historialv.tablav.setColumnWidth(0,150) #usuario
        self.historialv.tablav.setColumnWidth(1,150) #VLAN
        self.historialv.tablav.setColumnWidth(2,110) #tipot
        self.historialv.tablav.setColumnWidth(3,90)  #ticket
        self.historialv.tablav.setColumnWidth(4,200) #equipos
        self.historialv.tablav.setColumnWidth(5,120) #solicitud
        self.historialv.tablav.setColumnWidth(6,260) #solucion
        self.historialv.tablav.setColumnWidth(7,70) #realizad
        self.historialv.tablav.setColumnWidth(8,150) #fecha
    

        self.historialv.show()
        self.llenarhistorial()

    def abririnfo(self):

        self.info.autor.setText("")
        ImagLO = QPixmap("imagenes/8083308.png")
        self.info.autor.setPixmap(ImagLO)

        self.info.show()

    def abrirguia(self):
        self.guia.mostrar.clicked.connect(self.mostrarg)
        self.guia.foto.setText("")
        ImagLOG = QPixmap("imagenes/manual.png")
        self.guia.foto.setPixmap(ImagLOG) 
        self.guia.show()



   
#####REGISTRAR TAREA ###

    def registrarTarea(self):


    
        if self.registro.rvlan.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar la campaña")
            mBox.exec()
            self.registro.rvlan.setFocus()
        elif self.registro.tarea.currentText() =="---Seleccione una opción":
            mBox = QMessageBox()
            mBox.setText("Debe seleccionar tipo de tarea")
            mBox.exec()
            self.registro.tarea.setFocus()
        elif len(self.registro.nso.text())<4:
            mBox = QMessageBox()
            mBox.setText("Debe ingresar ticket válido")
            mBox.exec()
            self.registro.nso.setFocus()
       
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
                mBox.setText("Tarea registrada")
                mBox.exec()   
                self.limpiarcampos()
            else:
                mBox.setText("Tarea NO registrada")
                mBox.exec()   
              
           

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
        his = Historialdata()
        data =his.buscarfecha(self.historial.cusu.text(),self.historial.fdesde.text(),self.historial.fhasta.text())
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
        hisf = Historialdata()
        dataf =hisf.buscarfechaf(self.historialf.hdesdef.text(),self.historialf.hhastaf.text())
        fila=0
        self.historialf.tablatf.setRowCount(len(dataf))
        for item in dataf:
            self.historialf.tablatf.setItem(fila,0,QTableWidgetItem(str(item[0])))
            self.historialf.tablatf.setItem(fila,1,QTableWidgetItem(str(item[1])))
            self.historialf.tablatf.setItem(fila,2,QTableWidgetItem(str(item[4])))
            self.historialf.tablatf.setItem(fila,3,QTableWidgetItem(str(item[2])))
            self.historialf.tablatf.setItem(fila,4,QTableWidgetItem(str(item[5])))
            self.historialf.tablatf.setItem(fila,5,QTableWidgetItem(str(item[6])))
            self.historialf.tablatf.setItem(fila,6,QTableWidgetItem(str(item[7])))
            self.historialf.tablatf.setItem(fila,8,QTableWidgetItem(str(item[10])))
            if item[8] == 'True':
              self.historialf.tablatf.setItem(fila,7,QTableWidgetItem("si"))
            else:
              self.historialf.tablatf.setItem(fila,7,QTableWidgetItem("no"))
               
              

            fila=fila+1

    def buscarv(self):
        hisv = Historialdata()
        datav =hisv.buscarfechav(self.historialv.nvlan.currentText(),self.historialv.hdesdev.text(),self.historialv.hhastav.text())
        fila=0
        self.historialv.tablav.setRowCount(len(datav))
        for item in datav:
            self.historialv.tablav.setItem(fila,0,QTableWidgetItem(str(item[0])))
            self.historialv.tablav.setItem(fila,1,QTableWidgetItem(str(item[1])))
            self.historialv.tablav.setItem(fila,2,QTableWidgetItem(str(item[4])))
            self.historialv.tablav.setItem(fila,3,QTableWidgetItem(str(item[2])))
            self.historialv.tablav.setItem(fila,4,QTableWidgetItem(str(item[5])))
            self.historialv.tablav.setItem(fila,5,QTableWidgetItem(str(item[6])))
            self.historialv.tablav.setItem(fila,6,QTableWidgetItem(str(item[7])))
            self.historialv.tablav.setItem(fila,8,QTableWidgetItem(str(item[10])))
            if item[8] == 'True':
              self.historialv.tablav.setItem(fila,7,QTableWidgetItem("si"))
            else:
              self.historialv.tablav.setItem(fila,7,QTableWidgetItem("no"))
               
              

            fila=fila+1

        
    def  llenarhistorial(self):
        pass
   
      



        
         
    
      
    
   
  
  

    
    
 
 