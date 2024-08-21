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
    QMenuBar, QSizePolicy, QStatusBar, QWidget)
import imagen_rc
import imagen_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(2147, 1004)
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
        self.fondo.setGeometry(QRect(-110, -160, 2281, 1381))
        self.fondo.setPixmap(QPixmap(u":/p/bluep.jpg"))
        self.fondo.setScaledContents(True)
        self.emtelco = QLabel(self.centralwidget)
        self.emtelco.setObjectName(u"emtelco")
        self.emtelco.setGeometry(QRect(10, 20, 301, 101))
        self.emtelco.setPixmap(QPixmap(u":/p/Logop.png"))
        self.emtelco.setScaledContents(True)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2147, 26))
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
        self.menuArchivo.setTitle(QCoreApplication.translate("Main", u"Archivo", None))
        self.menuHistorial_de_Tareas.setTitle(QCoreApplication.translate("Main", u"Historial de Tareas", None))
        self.menuinfo.setTitle(QCoreApplication.translate("Main", u"Info", None))
    # retranslateUi

