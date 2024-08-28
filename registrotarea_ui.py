# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrotarea.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)
import imagen_rc

class Ui_Registro(object):
    def setupUi(self, Registro):
        if not Registro.objectName():
            Registro.setObjectName(u"Registro")
        Registro.resize(869, 778)
        font = QFont()
        font.setPointSize(1)
        Registro.setFont(font)
        icon = QIcon()
        icon.addFile(u":/p/em.png", QSize(), QIcon.Normal, QIcon.Off)
        Registro.setWindowIcon(icon)
        Registro.setStyleSheet(u"")
        self.logo = QLabel(Registro)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 131, 131))
        self.logo.setPixmap(QPixmap(u":/p/FOsp.png"))
        self.logo.setScaledContents(True)
        self.registro = QLabel(Registro)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(240, 20, 431, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(23)
        font1.setBold(True)
        self.registro.setFont(font1)
        self.registro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tusu = QLabel(Registro)
        self.tusu.setObjectName(u"tusu")
        self.tusu.setGeometry(QRect(30, 140, 181, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.tusu.setFont(font2)
        self.tusu.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tusu.setAlignment(Qt.AlignCenter)
        self.nso = QLineEdit(Registro)
        self.nso.setObjectName(u"nso")
        self.nso.setGeometry(QRect(370, 300, 241, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.nso.setFont(font3)
        self.nso.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.nso.setReadOnly(False)
        self.tarea = QComboBox(Registro)
        self.tarea.addItem("")
        self.tarea.addItem("")
        self.tarea.addItem("")
        self.tarea.addItem("")
        self.tarea.addItem("")
        self.tarea.addItem("")
        self.tarea.addItem("")
        self.tarea.setObjectName(u"tarea")
        self.tarea.setGeometry(QRect(30, 300, 261, 31))
        font4 = QFont()
        font4.setPointSize(10)
        self.tarea.setFont(font4)
        self.tarea.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.ttarea = QLabel(Registro)
        self.ttarea.setObjectName(u"ttarea")
        self.ttarea.setGeometry(QRect(70, 250, 151, 31))
        self.ttarea.setFont(font2)
        self.ttarea.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ns = QLabel(Registro)
        self.ns.setObjectName(u"ns")
        self.ns.setGeometry(QRect(370, 250, 221, 31))
        self.ns.setFont(font2)
        self.ns.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dt = QLabel(Registro)
        self.dt.setObjectName(u"dt")
        self.dt.setGeometry(QRect(60, 360, 321, 41))
        self.dt.setFont(font2)
        self.dt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.reg = QPushButton(Registro)
        self.reg.setObjectName(u"reg")
        self.reg.setGeometry(QRect(670, 700, 151, 61))
        self.reg.setFont(font2)
        self.reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg.setStyleSheet(u"background-color: rgb(197, 220, 75);\n"
"border-radius:8px")
        self.tvlan = QLabel(Registro)
        self.tvlan.setObjectName(u"tvlan")
        self.tvlan.setGeometry(QRect(370, 140, 221, 21))
        self.tvlan.setFont(font2)
        self.tvlan.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rea = QCheckBox(Registro)
        self.rea.setObjectName(u"rea")
        self.rea.setGeometry(QRect(180, 700, 191, 61))
        self.rea.setFont(font2)
        self.rea.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.val = QCheckBox(Registro)
        self.val.setObjectName(u"val")
        self.val.setGeometry(QRect(400, 700, 241, 61))
        self.val.setFont(font2)
        self.val.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rvlan = QComboBox(Registro)
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.addItem("")
        self.rvlan.setObjectName(u"rvlan")
        self.rvlan.setGeometry(QRect(370, 190, 241, 31))
        self.rvlan.setFont(font4)
        self.rvlan.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.usu = QLineEdit(Registro)
        self.usu.setObjectName(u"usu")
        self.usu.setGeometry(QRect(30, 190, 261, 31))
        self.usu.setFont(font3)
        self.usu.setStyleSheet(u"border-bottom-color: rgb(137, 206, 206);\n"
"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(137, 206, 206);\n"
"border-top-color: rgb(137, 206, 206);\n"
"border-right-color: rgb(137, 206, 206);\n"
"border-left-color: rgb(137, 206, 206);")
        self.usu.setReadOnly(False)
        self.det = QPlainTextEdit(Registro)
        self.det.setObjectName(u"det")
        self.det.setGeometry(QRect(30, 420, 401, 251))
        font5 = QFont()
        font5.setPointSize(12)
        self.det.setFont(font5)
        self.det.setAutoFillBackground(True)
        self.det.setStyleSheet(u"border-bottom-color: rgb(137, 206, 206);\n"
"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(137, 206, 206);\n"
"border-top-color: rgb(137, 206, 206);\n"
"border-right-color: rgb(137, 206, 206);\n"
"border-left-color: rgb(137, 206, 206);")
        self.equipos = QLabel(Registro)
        self.equipos.setObjectName(u"equipos")
        self.equipos.setGeometry(QRect(700, 130, 201, 41))
        self.equipos.setFont(font2)
        self.equipos.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.equi = QPlainTextEdit(Registro)
        self.equi.setObjectName(u"equi")
        self.equi.setGeometry(QRect(680, 180, 131, 151))
        self.equi.setFont(font5)
        self.equi.setAutoFillBackground(True)
        self.equi.setStyleSheet(u"border-bottom-color: rgb(137, 206, 206);\n"
"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(137, 206, 206);\n"
"border-top-color: rgb(137, 206, 206);\n"
"border-right-color: rgb(137, 206, 206);\n"
"border-left-color: rgb(137, 206, 206);")
        self.fon = QLabel(Registro)
        self.fon.setObjectName(u"fon")
        self.fon.setGeometry(QRect(0, -10, 1241, 821))
        self.fon.setPixmap(QPixmap(u":/p/cla.png"))
        self.fon.setScaledContents(True)
        self.dts = QLabel(Registro)
        self.dts.setObjectName(u"dts")
        self.dts.setGeometry(QRect(510, 360, 261, 41))
        self.dts.setFont(font2)
        self.dts.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dets = QPlainTextEdit(Registro)
        self.dets.setObjectName(u"dets")
        self.dets.setGeometry(QRect(460, 420, 401, 251))
        self.dets.setFont(font5)
        self.dets.setAutoFillBackground(True)
        self.dets.setStyleSheet(u"border-bottom-color: rgb(137, 206, 206);\n"
"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(137, 206, 206);\n"
"border-top-color: rgb(137, 206, 206);\n"
"border-right-color: rgb(137, 206, 206);\n"
"border-left-color: rgb(137, 206, 206);")
        self.fon.raise_()
        self.logo.raise_()
        self.registro.raise_()
        self.tusu.raise_()
        self.nso.raise_()
        self.tarea.raise_()
        self.ttarea.raise_()
        self.ns.raise_()
        self.dt.raise_()
        self.reg.raise_()
        self.tvlan.raise_()
        self.rea.raise_()
        self.val.raise_()
        self.rvlan.raise_()
        self.usu.raise_()
        self.det.raise_()
        self.equipos.raise_()
        self.equi.raise_()
        self.dts.raise_()
        self.dets.raise_()

        self.retranslateUi(Registro)

        QMetaObject.connectSlotsByName(Registro)
    # setupUi

    def retranslateUi(self, Registro):
        Registro.setWindowTitle(QCoreApplication.translate("Registro", u"Registro Tareas", None))
        self.logo.setText("")
        self.registro.setText(QCoreApplication.translate("Registro", u"REGISTRO DE TAREAS", None))
        self.tusu.setText(QCoreApplication.translate("Registro", u"Usuario", None))
#if QT_CONFIG(statustip)
        self.nso.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.tarea.setItemText(0, QCoreApplication.translate("Registro", u"---Seleccione una opci\u00f3n", None))
        self.tarea.setItemText(1, QCoreApplication.translate("Registro", u"Verificaci\u00f3n puerto", None))
        self.tarea.setItemText(2, QCoreApplication.translate("Registro", u"Asignaci\u00f3n VLAN", None))
        self.tarea.setItemText(3, QCoreApplication.translate("Registro", u"Activaci\u00f3n  puertos", None))
        self.tarea.setItemText(4, QCoreApplication.translate("Registro", u"Desactivaci\u00f3n de puertos", None))
        self.tarea.setItemText(5, QCoreApplication.translate("Registro", u"Port security", None))
        self.tarea.setItemText(6, QCoreApplication.translate("Registro", u"Otros", None))

        self.ttarea.setText(QCoreApplication.translate("Registro", u"Tipo de tarea", None))
        self.ns.setText(QCoreApplication.translate("Registro", u"N\u00famero de Ticket", None))
        self.dt.setText(QCoreApplication.translate("Registro", u"Detalles solicitud de tarea", None))
        self.reg.setText(QCoreApplication.translate("Registro", u"REGISTRAR", None))
        self.tvlan.setText(QCoreApplication.translate("Registro", u"VLAN-Campa\u00f1a", None))
        self.rea.setText(QCoreApplication.translate("Registro", u"Tarea realizada", None))
        self.val.setText(QCoreApplication.translate("Registro", u"Tarea en validaci\u00f3n", None))
        self.rvlan.setItemText(0, QCoreApplication.translate("Registro", u"---Seleccione una opci\u00f3n", None))
        self.rvlan.setItemText(1, QCoreApplication.translate("Registro", u"ADMINISTRACI\u00d3N ", None))
        self.rvlan.setItemText(2, QCoreApplication.translate("Registro", u"ADDI ", None))
        self.rvlan.setItemText(3, QCoreApplication.translate("Registro", u"ALKOSTO ", None))
        self.rvlan.setItemText(4, QCoreApplication.translate("Registro", u"BBVA ", None))
        self.rvlan.setItemText(5, QCoreApplication.translate("Registro", u"TUYABOG  ", None))
        self.rvlan.setItemText(6, QCoreApplication.translate("Registro", u"COMPENSAR", None))
        self.rvlan.setItemText(7, QCoreApplication.translate("Registro", u"KERALTY ", None))
        self.rvlan.setItemText(8, QCoreApplication.translate("Registro", u"JUAN VALDEZ ", None))
        self.rvlan.setItemText(9, QCoreApplication.translate("Registro", u"PREVISORA ", None))
        self.rvlan.setItemText(10, QCoreApplication.translate("Registro", u"PARMALAT ", None))
        self.rvlan.setItemText(11, QCoreApplication.translate("Registro", u"TUBOLETA ", None))
        self.rvlan.setItemText(12, QCoreApplication.translate("Registro", u"PAPA JOHNS ", None))
        self.rvlan.setItemText(13, QCoreApplication.translate("Registro", u"NOVONORDISK ", None))
        self.rvlan.setItemText(14, QCoreApplication.translate("Registro", u"SALUD TOTAL ", None))
        self.rvlan.setItemText(15, QCoreApplication.translate("Registro", u"COLPENSIONES ", None))
        self.rvlan.setItemText(16, QCoreApplication.translate("Registro", u"COLMEDICA", None))
        self.rvlan.setItemText(17, QCoreApplication.translate("Registro", u"CONINSA ", None))
        self.rvlan.setItemText(18, QCoreApplication.translate("Registro", u"OTRA", None))

#if QT_CONFIG(statustip)
        self.usu.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.usu.setText("")
        self.det.setPlainText("")
        self.equipos.setText(QCoreApplication.translate("Registro", u"Equipos ", None))
        self.fon.setText("")
        self.dts.setText(QCoreApplication.translate("Registro", u"Descripci\u00f3n de soluci\u00f3n", None))
        self.dets.setPlainText("")
    # retranslateUi

