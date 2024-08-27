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
        self.regt.setGeometry(QRect(120, 200, 181, 171))
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
        self.regt.setIconSize(QSize(230, 190))
        self.regtarea = QLabel(self.centralwidget)
        self.regtarea.setObjectName(u"regtarea")
        self.regtarea.setGeometry(QRect(90, 170, 241, 31))
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
        self.busu.setGeometry(QRect(740, 200, 181, 171))
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
        self.bas.setGeometry(QRect(430, 200, 181, 171))
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
        self.regtarea2 = QLabel(self.centralwidget)
        self.regtarea2.setObjectName(u"regtarea2")
        self.regtarea2.setGeometry(QRect(420, 190, 201, 191))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(11)
        self.regtarea2.setFont(font1)
        self.regtarea2.setLayoutDirection(Qt.LeftToRight)
        self.regtarea2.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea1 = QLabel(self.centralwidget)
        self.regtarea1.setObjectName(u"regtarea1")
        self.regtarea1.setGeometry(QRect(110, 190, 201, 191))
        self.regtarea1.setFont(font1)
        self.regtarea1.setLayoutDirection(Qt.LeftToRight)
        self.regtarea1.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea3 = QLabel(self.centralwidget)
        self.regtarea3.setObjectName(u"regtarea3")
        self.regtarea3.setGeometry(QRect(730, 190, 201, 191))
        self.regtarea3.setFont(font1)
        self.regtarea3.setLayoutDirection(Qt.LeftToRight)
        self.regtarea3.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea_2 = QLabel(self.centralwidget)
        self.regtarea_2.setObjectName(u"regtarea_2")
        self.regtarea_2.setGeometry(QRect(400, 170, 241, 31))
        self.regtarea_2.setFont(font)
        self.regtarea_2.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_2.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea_3 = QLabel(self.centralwidget)
        self.regtarea_3.setObjectName(u"regtarea_3")
        self.regtarea_3.setGeometry(QRect(700, 170, 271, 31))
        self.regtarea_3.setFont(font)
        self.regtarea_3.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_3.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea4 = QLabel(self.centralwidget)
        self.regtarea4.setObjectName(u"regtarea4")
        self.regtarea4.setGeometry(QRect(270, 440, 201, 191))
        self.regtarea4.setFont(font1)
        self.regtarea4.setLayoutDirection(Qt.LeftToRight)
        self.regtarea4.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.busf = QPushButton(self.centralwidget)
        self.busf.setObjectName(u"busf")
        self.busf.setGeometry(QRect(280, 450, 181, 171))
        self.busf.setCursor(QCursor(Qt.PointingHandCursor))
        self.busf.setAutoFillBackground(False)
        self.busf.setStyleSheet(u"\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/p/cale.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busf.setIcon(icon3)
        self.busf.setIconSize(QSize(172, 230))
        self.regtarea_4 = QLabel(self.centralwidget)
        self.regtarea_4.setObjectName(u"regtarea_4")
        self.regtarea_4.setGeometry(QRect(250, 420, 241, 31))
        self.regtarea_4.setFont(font)
        self.regtarea_4.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_4.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea5 = QLabel(self.centralwidget)
        self.regtarea5.setObjectName(u"regtarea5")
        self.regtarea5.setGeometry(QRect(590, 440, 201, 191))
        self.regtarea5.setFont(font1)
        self.regtarea5.setLayoutDirection(Qt.LeftToRight)
        self.regtarea5.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.busv = QPushButton(self.centralwidget)
        self.busv.setObjectName(u"busv")
        self.busv.setGeometry(QRect(600, 450, 181, 171))
        self.busv.setCursor(QCursor(Qt.PointingHandCursor))
        self.busv.setAutoFillBackground(False)
        self.busv.setStyleSheet(u"\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/p/vlan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busv.setIcon(icon4)
        self.busv.setIconSize(QSize(172, 230))
        self.regtarea_5 = QLabel(self.centralwidget)
        self.regtarea_5.setObjectName(u"regtarea_5")
        self.regtarea_5.setGeometry(QRect(570, 420, 241, 31))
        self.regtarea_5.setFont(font)
        self.regtarea_5.setLayoutDirection(Qt.LeftToRight)
        self.regtarea_5.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.regtarea_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.guiau = QPushButton(self.centralwidget)
        self.guiau.setObjectName(u"guiau")
        self.guiau.setGeometry(QRect(40, 620, 101, 111))
        self.guiau.setCursor(QCursor(Qt.PointingHandCursor))
        self.guiau.setAutoFillBackground(False)
        self.guiau.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none; \n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/p/in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.guiau.setIcon(icon5)
        self.guiau.setIconSize(QSize(88, 120))
        Main.setCentralWidget(self.centralwidget)
        self.fondo.raise_()
        self.emtelco.raise_()
        self.regtarea2.raise_()
        self.bas.raise_()
        self.regtarea1.raise_()
        self.regt.raise_()
        self.regtarea3.raise_()
        self.busu.raise_()
        self.regtarea_2.raise_()
        self.regtarea_3.raise_()
        self.regtarea.raise_()
        self.regtarea4.raise_()
        self.busf.raise_()
        self.regtarea_4.raise_()
        self.regtarea5.raise_()
        self.busv.raise_()
        self.regtarea_5.raise_()
        self.guiau.raise_()
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1002, 26))
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuinfo.menuAction())
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
        self.regtarea2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea1.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea3.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea_2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">TAREAS REGISTRADAS</span></p><p><br/></p></body></html>", None))
        self.regtarea_3.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR USUARIO Y FECHA</span></p></body></html>", None))
        self.regtarea4.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.busf.setText("")
        self.regtarea_4.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR POR FECHA</span></p></body></html>", None))
        self.regtarea5.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.busv.setText("")
        self.regtarea_5.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR POR VLAN</span></p><p><br/></p></body></html>", None))
        self.guiau.setText("")
        self.menuinfo.setTitle(QCoreApplication.translate("Main", u"Info", None))
    # retranslateUi

