# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import imagen_rc
import imagen_rc

class Ui_Formlogin(object):
    def setupUi(self, Formlogin):
        if not Formlogin.objectName():
            Formlogin.setObjectName(u"Formlogin")
        Formlogin.resize(446, 526)
        Formlogin.setAutoFillBackground(False)
        Formlogin.setStyleSheet(u"")
        self.SESION = QLabel(Formlogin)
        self.SESION.setObjectName(u"SESION")
        self.SESION.setGeometry(QRect(100, 170, 271, 51))
        font = QFont()
        font.setPointSize(14)
        self.SESION.setFont(font)
        self.SESION.setAutoFillBackground(False)
        self.SESION.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.SESION.setAlignment(Qt.AlignCenter)
        self.USUARIO = QLabel(Formlogin)
        self.USUARIO.setObjectName(u"USUARIO")
        self.USUARIO.setGeometry(QRect(110, 230, 41, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.USUARIO.setFont(font1)
        self.USUARIO.setAutoFillBackground(False)
        self.USUARIO.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.USUARIO.setPixmap(QPixmap(u":/p/Up.png"))
        self.CLAVE = QLabel(Formlogin)
        self.CLAVE.setObjectName(u"CLAVE")
        self.CLAVE.setGeometry(QRect(110, 310, 41, 41))
        self.CLAVE.setFont(font1)
        self.CLAVE.setAutoFillBackground(False)
        self.CLAVE.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.CLAVE.setPixmap(QPixmap(u":/p/CONp.png"))
        self.TEXTUSU = QLineEdit(Formlogin)
        self.TEXTUSU.setObjectName(u"TEXTUSU")
        self.TEXTUSU.setGeometry(QRect(100, 230, 261, 61))
        self.TEXTUSU.setFont(font1)
        self.TEXTUSU.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px\n"
"")
        self.TEXTUSU.setAlignment(Qt.AlignCenter)
        self.TEXTCLAVE = QLineEdit(Formlogin)
        self.TEXTCLAVE.setObjectName(u"TEXTCLAVE")
        self.TEXTCLAVE.setGeometry(QRect(100, 300, 261, 61))
        self.TEXTCLAVE.setFont(font1)
        self.TEXTCLAVE.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px\n"
"")
        self.TEXTCLAVE.setEchoMode(QLineEdit.Password)
        self.TEXTCLAVE.setAlignment(Qt.AlignCenter)
        self.FONDO = QLabel(Formlogin)
        self.FONDO.setObjectName(u"FONDO")
        self.FONDO.setGeometry(QRect(-130, -220, 1051, 831))
        self.FONDO.setPixmap(QPixmap(u":/p/fondp.png"))
        self.FONDO.setScaledContents(True)
        self.LOGO = QLabel(Formlogin)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setGeometry(QRect(120, 60, 221, 81))
        self.LOGO.setPixmap(QPixmap(u"../imagenes/Logo-footerp.png"))
        self.LOGO.setScaledContents(True)
        self.ACCEDER = QPushButton(Formlogin)
        self.ACCEDER.setObjectName(u"ACCEDER")
        self.ACCEDER.setGeometry(QRect(180, 390, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.ACCEDER.setFont(font2)
        self.ACCEDER.setCursor(QCursor(Qt.PointingHandCursor))
        self.ACCEDER.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px\n"
"")
        self.MENSAJE = QLabel(Formlogin)
        self.MENSAJE.setObjectName(u"MENSAJE")
        self.MENSAJE.setGeometry(QRect(120, 450, 231, 41))
        font3 = QFont()
        font3.setPointSize(11)
        self.MENSAJE.setFont(font3)
        self.MENSAJE.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.MENSAJE.setAlignment(Qt.AlignCenter)
        self.FONDO.raise_()
        self.LOGO.raise_()
        self.TEXTUSU.raise_()
        self.TEXTCLAVE.raise_()
        self.ACCEDER.raise_()
        self.SESION.raise_()
        self.USUARIO.raise_()
        self.CLAVE.raise_()
        self.MENSAJE.raise_()

        self.retranslateUi(Formlogin)

        QMetaObject.connectSlotsByName(Formlogin)
    # setupUi

    def retranslateUi(self, Formlogin):
        Formlogin.setWindowTitle(QCoreApplication.translate("Formlogin", u"Inicio de sesi\u00f3n", None))
        self.SESION.setText(QCoreApplication.translate("Formlogin", u"Inicio de sesi\u00f3n", None))
        self.USUARIO.setText("")
        self.CLAVE.setText("")
        self.TEXTUSU.setPlaceholderText(QCoreApplication.translate("Formlogin", u"    Ingrese su usuario", None))
        self.TEXTCLAVE.setPlaceholderText(QCoreApplication.translate("Formlogin", u"         Ingrese su contrase\u00f1a", None))
        self.FONDO.setText("")
        self.LOGO.setText("")
        self.ACCEDER.setText(QCoreApplication.translate("Formlogin", u"INGRESAR", None))
        self.MENSAJE.setText(QCoreApplication.translate("Formlogin", u"mensaje", None))
    # retranslateUi

