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
        Main.resize(1002, 800)
        Main.setMinimumSize(QSize(1002, 800))
        Main.setMaximumSize(QSize(1002, 800))
        icon = QIcon()
        icon.addFile(u":/p/em.png", QSize(), QIcon.Normal, QIcon.Off)
        Main.setWindowIcon(icon)
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
        self.manual = QAction(Main)
        self.manual.setObjectName(u"manual")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.emtelco = QLabel(self.centralwidget)
        self.emtelco.setObjectName(u"emtelco")
        self.emtelco.setGeometry(QRect(420, 60, 191, 61))
        self.emtelco.setPixmap(QPixmap(u":/p/Logop.png"))
        self.emtelco.setScaledContents(True)
        self.regt = QPushButton(self.centralwidget)
        self.regt.setObjectName(u"regt")
        self.regt.setGeometry(QRect(130, 210, 161, 151))
        self.regt.setCursor(QCursor(Qt.PointingHandCursor))
        self.regt.setAutoFillBackground(False)
        self.regt.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c8cb2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/p/regisfon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.regt.setIcon(icon1)
        self.regt.setIconSize(QSize(230, 190))
        self.main1 = QLabel(self.centralwidget)
        self.main1.setObjectName(u"main1")
        self.main1.setGeometry(QRect(100, 180, 241, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        self.main1.setFont(font)
        self.main1.setLayoutDirection(Qt.LeftToRight)
        self.main1.setStyleSheet(u"\n"
"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.main1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.busu = QPushButton(self.centralwidget)
        self.busu.setObjectName(u"busu")
        self.busu.setGeometry(QRect(750, 210, 161, 151))
        self.busu.setCursor(QCursor(Qt.PointingHandCursor))
        self.busu.setAutoFillBackground(False)
        self.busu.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c8cb2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/p/usuu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busu.setIcon(icon2)
        self.busu.setIconSize(QSize(210, 125))
        self.bas = QPushButton(self.centralwidget)
        self.bas.setObjectName(u"bas")
        self.bas.setGeometry(QRect(440, 210, 161, 151))
        self.bas.setCursor(QCursor(Qt.PointingHandCursor))
        self.bas.setAutoFillBackground(False)
        self.bas.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c8cb2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/p/baset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bas.setIcon(icon3)
        self.bas.setIconSize(QSize(197, 119))
        self.regtarea2 = QLabel(self.centralwidget)
        self.regtarea2.setObjectName(u"regtarea2")
        self.regtarea2.setGeometry(QRect(430, 200, 181, 171))
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
        self.regtarea1.setGeometry(QRect(120, 200, 181, 171))
        self.regtarea1.setFont(font1)
        self.regtarea1.setLayoutDirection(Qt.LeftToRight)
        self.regtarea1.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea3 = QLabel(self.centralwidget)
        self.regtarea3.setObjectName(u"regtarea3")
        self.regtarea3.setGeometry(QRect(740, 200, 181, 171))
        self.regtarea3.setFont(font1)
        self.regtarea3.setLayoutDirection(Qt.LeftToRight)
        self.regtarea3.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.main2 = QLabel(self.centralwidget)
        self.main2.setObjectName(u"main2")
        self.main2.setGeometry(QRect(400, 180, 241, 31))
        self.main2.setFont(font)
        self.main2.setLayoutDirection(Qt.LeftToRight)
        self.main2.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.main2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.main3 = QLabel(self.centralwidget)
        self.main3.setObjectName(u"main3")
        self.main3.setGeometry(QRect(700, 180, 271, 31))
        self.main3.setFont(font)
        self.main3.setLayoutDirection(Qt.LeftToRight)
        self.main3.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.main3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea4 = QLabel(self.centralwidget)
        self.regtarea4.setObjectName(u"regtarea4")
        self.regtarea4.setGeometry(QRect(120, 450, 181, 171))
        self.regtarea4.setFont(font1)
        self.regtarea4.setLayoutDirection(Qt.LeftToRight)
        self.regtarea4.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.busf = QPushButton(self.centralwidget)
        self.busf.setObjectName(u"busf")
        self.busf.setGeometry(QRect(130, 460, 161, 151))
        self.busf.setCursor(QCursor(Qt.PointingHandCursor))
        self.busf.setAutoFillBackground(False)
        self.busf.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c8cb2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/p/cale.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busf.setIcon(icon4)
        self.busf.setIconSize(QSize(172, 230))
        self.main4 = QLabel(self.centralwidget)
        self.main4.setObjectName(u"main4")
        self.main4.setGeometry(QRect(90, 430, 241, 31))
        self.main4.setFont(font)
        self.main4.setLayoutDirection(Qt.LeftToRight)
        self.main4.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.main4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.regtarea5 = QLabel(self.centralwidget)
        self.regtarea5.setObjectName(u"regtarea5")
        self.regtarea5.setGeometry(QRect(430, 450, 181, 171))
        self.regtarea5.setFont(font1)
        self.regtarea5.setLayoutDirection(Qt.LeftToRight)
        self.regtarea5.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.busv = QPushButton(self.centralwidget)
        self.busv.setObjectName(u"busv")
        self.busv.setGeometry(QRect(440, 460, 161, 151))
        self.busv.setCursor(QCursor(Qt.PointingHandCursor))
        self.busv.setAutoFillBackground(False)
        self.busv.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c8cb2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/p/vlan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busv.setIcon(icon5)
        self.busv.setIconSize(QSize(172, 150))
        self.main5 = QLabel(self.centralwidget)
        self.main5.setObjectName(u"main5")
        self.main5.setGeometry(QRect(410, 430, 241, 31))
        self.main5.setFont(font)
        self.main5.setLayoutDirection(Qt.LeftToRight)
        self.main5.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.main5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.guiau = QPushButton(self.centralwidget)
        self.guiau.setObjectName(u"guiau")
        self.guiau.setGeometry(QRect(0, 0, 101, 111))
        self.guiau.setCursor(QCursor(Qt.PointingHandCursor))
        self.guiau.setAutoFillBackground(False)
        self.guiau.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none; \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/p/guia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.guiau.setIcon(icon6)
        self.guiau.setIconSize(QSize(60, 100))
        self.gest = QLabel(self.centralwidget)
        self.gest.setObjectName(u"gest")
        self.gest.setGeometry(QRect(240, 10, 541, 51))
        self.gest.setPixmap(QPixmap(u":/p/ges.png"))
        self.gest.setScaledContents(True)
        self.fondo = QLabel(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(-20, -200, 1101, 961))
        self.fondo.setAutoFillBackground(False)
        self.fondo.setStyleSheet(u"background-color: rgb(1, 27, 123);")
        self.fondo.setPixmap(QPixmap(u":/p/fonda.png"))
        self.eli = QPushButton(self.centralwidget)
        self.eli.setObjectName(u"eli")
        self.eli.setGeometry(QRect(750, 460, 161, 151))
        self.eli.setCursor(QCursor(Qt.PointingHandCursor))
        self.eli.setAutoFillBackground(False)
        self.eli.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #c8cb2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7ec361;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/p/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eli.setIcon(icon7)
        self.eli.setIconSize(QSize(150, 120))
        self.eli.setAutoRepeatDelay(250)
        self.eli.setAutoRepeatInterval(8)
        self.regtarea6 = QLabel(self.centralwidget)
        self.regtarea6.setObjectName(u"regtarea6")
        self.regtarea6.setGeometry(QRect(740, 450, 181, 171))
        self.regtarea6.setFont(font1)
        self.regtarea6.setLayoutDirection(Qt.LeftToRight)
        self.regtarea6.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"  border-radius: 20px;")
        self.regtarea6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.main6 = QLabel(self.centralwidget)
        self.main6.setObjectName(u"main6")
        self.main6.setGeometry(QRect(720, 430, 241, 31))
        self.main6.setFont(font)
        self.main6.setLayoutDirection(Qt.LeftToRight)
        self.main6.setStyleSheet(u"background-color: rgb(1, 27, 122);\n"
"\n"
"  border-radius: 10px;")
        self.main6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        Main.setCentralWidget(self.centralwidget)
        self.fondo.raise_()
        self.emtelco.raise_()
        self.regtarea2.raise_()
        self.bas.raise_()
        self.regtarea1.raise_()
        self.regt.raise_()
        self.regtarea3.raise_()
        self.busu.raise_()
        self.main2.raise_()
        self.main3.raise_()
        self.main1.raise_()
        self.regtarea4.raise_()
        self.busf.raise_()
        self.main4.raise_()
        self.regtarea5.raise_()
        self.busv.raise_()
        self.main5.raise_()
        self.guiau.raise_()
        self.gest.raise_()
        self.regtarea6.raise_()
        self.eli.raise_()
        self.main6.raise_()
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
        self.menuinfo.addAction(self.manual)
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
        self.manual.setText(QCoreApplication.translate("Main", u"Gu\u00eda de Usuario", None))
        self.emtelco.setText("")
        self.regt.setText("")
        self.main1.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">REGISTRAR TAREA</span></p></body></html>", None))
        self.busu.setText("")
        self.bas.setText("")
        self.regtarea2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea1.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.regtarea3.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.main2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">TAREAS REGISTRADAS</span></p><p><br/></p></body></html>", None))
        self.main3.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR USUARIO Y FECHA</span></p></body></html>", None))
        self.regtarea4.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.busf.setText("")
        self.main4.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR POR FECHA</span></p></body></html>", None))
        self.regtarea5.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.busv.setText("")
        self.main5.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">BUSCAR POR VLAN</span></p><p><br/></p></body></html>", None))
        self.guiau.setText("")
        self.gest.setText("")
        self.fondo.setText("")
        self.eli.setText("")
        self.regtarea6.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><br/></p></body></html>", None))
        self.main6.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" color:#ffffff;\">ELIMINAR TAREA</span></p></body></html>", None))
        self.menuinfo.setTitle(QCoreApplication.translate("Main", u"Archivo", None))
    # retranslateUi

