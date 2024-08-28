import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from usu import Usuariodata
from main import Mainwindow
from usuario import Usuario
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import uic

class Login():
    def __init__(self):
        self.login = uic.loadUi("inicio.ui")

        self.login.setWindowIcon(QIcon('imagenes/EMTEG.ico'))

       

        self.login.USUARIO.setText("")
        ImagU = QPixmap("imagenes/Up.png")
        self.login.USUARIO.setPixmap(ImagU)
         

        self.login.CLAVE.setText("")  
        ImagC = QPixmap("imagenes/CONp.png")
        self.initGUI()
        self.login.CLAVE.setPixmap(ImagC)

        
        self.login.LOGO.setText("")  
        ImagL = QPixmap("imagenes/Logo-footerp.png")
        self.login.LOGO.setPixmap(ImagL)
        
        self.login.FONDO.setText("")  
        ImagF = QPixmap("imagenes/fondp.png")
        self.login.FONDO.setPixmap(ImagF)

        self.login.MENSAJE.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.login.TEXTUSU.text()) < 2:
            self.login.MENSAJE.setText("Ingrese un usuario válido")
            self.login.TEXTUSU.setFocus()
        elif len(self.login.TEXTCLAVE.text()) < 3:
            self.login.MENSAJE.setText("Ingrese una contraseña válida")
            self.login.TEXTCLAVE.setFocus()
        else:
           self.login.MENSAJE.setText("")
           usu = Usuario(usuario=self.login.TEXTUSU.text(),clave=self.login.TEXTCLAVE.text())
           usudata = Usuariodata()
           res=usudata.login(usu)
           if res:
               self.main = Mainwindow()
               self.login.hide()
           else:
               self.login.MENSAJE.setText("Datos incorrectos")

    def initGUI(self):
        self.login.ACCEDER.clicked.connect(self.ingresar)
  
      