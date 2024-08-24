# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import imagen_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1002, 910)
        Main.setStyleSheet(u"")
        self.RegistrarT = QAction(Main)
        self.RegistrarT.setObjectName(u"RegistrarT")
        self.acerca = QAction(Main)
        self.acerca.setObjectName(u"acerca")
        self.buscaruf = QAction(Main)
        self.buscaruf.setObjectName(u"buscaruf")
        self.buscarf = QAction(Main)
        self.buscarf.setObjectName(u"buscarf")
        self.guia = QAction(Main)
        self.guia.setObjectName(u"guia")
        self.buscarv = QAction(Main)
        self.buscarv.setObjectName(u"buscarv")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fondo = QLabel(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(-370, -220, 2281, 1381))
        self.fondo.setPixmap(QPixmap(u":/p/bluep.jpg"))
        self.fondo.setScaledContents(True)
        self.emtelco = QLabel(self.centralwidget)
        self.emtelco.setObjectName(u"emtelco")
        self.emtelco.setGeometry(QRect(10, 20, 301, 101))
        self.emtelco.setPixmap(QPixmap(u":/p/Logop.png"))
        self.emtelco.setScaledContents(True)
        self.regt = QPushButton(self.centralwidget)
        self.regt.setObjectName(u"regt")
        self.regt.setGeometry(QRect(110, 220, 201, 191))
        self.regt.setCursor(QCursor(Qt.PointingHandCursor))
        self.regt.setAutoFillBackground(False)
        self.regt.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c5dc4b;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/p/regisfon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.regt.setIcon(icon)
        self.regt.setIconSize(QSize(212, 170))
        self.regtarea = QLabel(self.centralwidget)
        self.regtarea.setObjectName(u"regtarea")
        self.regtarea.setGeometry(QRect(90, 160, 231, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        self.regtarea.setFont(font)
        self.regtarea.setLayoutDirection(Qt.LeftToRight)
        self.regtarea.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.busu = QPushButton(self.centralwidget)
        self.busu.setObjectName(u"busu")
        self.busu.setGeometry(QRect(730, 220, 201, 191))
        self.busu.setCursor(QCursor(Qt.PointingHandCursor))
        self.busu.setAutoFillBackground(False)
        self.busu.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c5dc4b;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/p/usuu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busu.setIcon(icon1)
        self.busu.setIconSize(QSize(210, 125))
        self.bas = QPushButton(self.centralwidget)
        self.bas.setObjectName(u"bas")
        self.bas.setGeometry(QRect(420, 220, 201, 191))
        self.bas.setCursor(QCursor(Qt.PointingHandCursor))
        self.bas.setAutoFillBackground(False)
        self.bas.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c5dc4b;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/p/baset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bas.setIcon(icon2)
        self.bas.setIconSize(QSize(197, 119))
        self.regtarea_4 = QLabel(self.centralwidget)
        self.regtarea_4.setObjectName(u"regtarea_4")
        self.regtarea_4.setGeometry(QRect(410, 210, 221, 211))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(11)
        self.regtarea_4.setFont(font1)
        self.regtarea_4.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_4.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea_6 = QLabel(self.centralwidget)
        self.regtarea_6.setObjectName(u"regtarea_6")
        self.regtarea_6.setGeometry(QRect(100, 210, 221, 211))
        self.regtarea_6.setFont(font1)
        self.regtarea_6.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_6.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea_7 = QLabel(self.centralwidget)
        self.regtarea_7.setObjectName(u"regtarea_7")
        self.regtarea_7.setGeometry(QRect(720, 210, 221, 211))
        self.regtarea_7.setFont(font1)
        self.regtarea_7.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_7.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea_2 = QLabel(self.centralwidget)
        self.regtarea_2.setObjectName(u"regtarea_2")
        self.regtarea_2.setGeometry(QRect(400, 160, 241, 31))
        self.regtarea_2.setFont(font)
        self.regtarea_2.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_2.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea_3 = QLabel(self.centralwidget)
        self.regtarea_3.setObjectName(u"regtarea_3")
        self.regtarea_3.setGeometry(QRect(700, 160, 281, 31))
        self.regtarea_3.setFont(font)
        self.regtarea_3.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_3.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        Main.setCentralWidget(self.centralwidget)
        self.fondo.raise_()
        self.emtelco.raise_()
        self.regtarea_4.raise_()
        self.bas.raise_()
        self.regtarea_6.raise_()
        self.regt.raise_()
        self.regtarea_7.raise_()
        self.busu.raise_()
        self.regtarea_2.raise_()
        self.regtarea_3.raise_()
        self.regtarea.raise_()
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1002, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuHistorial_de_Tareas = QMenu(self.menuArchivo)
        self.menuHistorial_de_Tareas.setObjectName(u"menuHistorial_de_Tareas")
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuinfo.menuAction())
        self.menuArchivo.addAction(self.RegistrarT)
        self.menuArchivo.addAction(self.menuHistorial_de_Tareas.menuAction())
        self.menuHistorial_de_Tareas.addAction(self.buscaruf)
        self.menuHistorial_de_Tareas.addAction(self.buscarf)
        self.menuHistorial_de_Tareas.addAction(self.buscarv)
        self.menuinfo.addAction(self.guia)
        self.menuinfo.addAction(self.acerca)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Redes Emtelco", None))
        self.RegistrarT.setText(QCoreApplication.translate("Main", u"Registrar Tarea", None))
#if QT_CONFIG(shortcut)
        self.RegistrarT.setShortcut(QCoreApplication.translate("Main", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.acerca.setText(QCoreApplication.translate("Main", u"Acerca de", None))
        self.buscaruf.setText(QCoreApplication.translate("Main", u"Buscar por usuario y fecha", None))
        self.buscarf.setText(QCoreApplication.translate("Main", u"Buscar por fecha", None))
        self.guia.setText(QCoreApplication.translate("Main", u"Gu\u00eda de usuario", None))
        self.buscarv.setText(QCoreApplication.translate("Main", u"Buscar por VLAN y fecha", None))
        self.fondo.setText("")
        self.emtelco.setText("")
        self.regt.setText("")
        self.regtarea.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">REGISTRAR TAREA</span></p></body></html>", None))
        self.busu.setText("")
        self.bas.setText("")
        self.regtarea_4.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea_6.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea_7.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea_2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">TAREAS REGISTRADAS</span></p><p><br/></p></body></html>", None))
        self.regtarea_3.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR USUARIO Y FECHA</span></p></body></html>", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("Main", u"Archivo", None))
        self.menuHistorial_de_Tareas.setTitle(QCoreApplication.translate("Main", u"Historial de Tareas", None))
        self.menuinfo.setTitle(QCoreApplication.translate("Main", u"Info", None))
    # retranslateUi

