# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrartarea.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import imagen_rc
import imagen_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(631, 800)
        Dialog.setStyleSheet(u"background-color: rgb(203, 203, 203);")
        self.em = QLabel(Dialog)
        self.em.setObjectName(u"em")
        self.em.setGeometry(QRect(0, 0, 121, 111))
        self.em.setPixmap(QPixmap(u":/p/FOsp.png"))
        self.em.setScaledContents(True)
        self.de = QLabel(Dialog)
        self.de.setObjectName(u"de")
        self.de.setGeometry(QRect(40, 350, 181, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.de.setFont(font)
        self.tta = QComboBox(Dialog)
        self.tta.addItem("")
        self.tta.addItem("")
        self.tta.addItem("")
        self.tta.addItem("")
        self.tta.addItem("")
        self.tta.addItem("")
        self.tta.addItem("")
        self.tta.setObjectName(u"tta")
        self.tta.setGeometry(QRect(40, 280, 261, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.tta.setFont(font1)
        self.tta.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tt = QLabel(Dialog)
        self.tt.setObjectName(u"tt")
        self.tt.setGeometry(QRect(40, 250, 151, 16))
        self.tt.setFont(font)
        self.det = QLineEdit(Dialog)
        self.det.setObjectName(u"det")
        self.det.setGeometry(QRect(40, 380, 571, 291))
        self.det.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.det.setReadOnly(False)
        self.regis = QLabel(Dialog)
        self.regis.setObjectName(u"regis")
        self.regis.setGeometry(QRect(130, 40, 401, 31))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.regis.setFont(font2)
        self.nso = QLineEdit(Dialog)
        self.nso.setObjectName(u"nso")
        self.nso.setGeometry(QRect(370, 280, 241, 31))
        self.nso.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.nso.setReadOnly(False)
        self.tip = QComboBox(Dialog)
        self.tip.addItem("")
        self.tip.addItem("")
        self.tip.addItem("")
        self.tip.addItem("")
        self.tip.setObjectName(u"tip")
        self.tip.setGeometry(QRect(40, 180, 261, 31))
        self.tip.setFont(font1)
        self.tip.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.numd = QLabel(Dialog)
        self.numd.setObjectName(u"numd")
        self.numd.setGeometry(QRect(370, 150, 201, 16))
        self.numd.setFont(font)
        self.reg = QPushButton(Dialog)
        self.reg.setObjectName(u"reg")
        self.reg.setGeometry(QRect(250, 700, 121, 51))
        self.reg.setFont(font)
        self.reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg.setStyleSheet(u"background-color: rgb(123, 221, 221);\n"
"border-radius:8px")
        self.tipd = QLabel(Dialog)
        self.tipd.setObjectName(u"tipd")
        self.tipd.setGeometry(QRect(40, 150, 181, 16))
        self.tipd.setFont(font)
        self.ns = QLabel(Dialog)
        self.ns.setObjectName(u"ns")
        self.ns.setGeometry(QRect(380, 240, 181, 16))
        self.ns.setFont(font)
        self.num = QLineEdit(Dialog)
        self.num.setObjectName(u"num")
        self.num.setGeometry(QRect(370, 180, 241, 31))
        self.num.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.num.setReadOnly(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.em.setText("")
        self.de.setText(QCoreApplication.translate("Dialog", u"Detalles de tarea", None))
        self.tta.setItemText(0, QCoreApplication.translate("Dialog", u"---Seleccione una opci\u00f3n", None))
        self.tta.setItemText(1, QCoreApplication.translate("Dialog", u"Verificaci\u00f3n puerto", None))
        self.tta.setItemText(2, QCoreApplication.translate("Dialog", u"Asignaci\u00f3n VLAN", None))
        self.tta.setItemText(3, QCoreApplication.translate("Dialog", u"Activaci\u00f3n  puertos", None))
        self.tta.setItemText(4, QCoreApplication.translate("Dialog", u"Desactivaci\u00f3n de puertos", None))
        self.tta.setItemText(5, QCoreApplication.translate("Dialog", u"Port security", None))
        self.tta.setItemText(6, QCoreApplication.translate("Dialog", u"Otros", None))

        self.tt.setText(QCoreApplication.translate("Dialog", u"Tipo de tarea", None))
#if QT_CONFIG(statustip)
        self.det.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.regis.setText(QCoreApplication.translate("Dialog", u"REGISTRO DE TAREAS", None))
#if QT_CONFIG(statustip)
        self.nso.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.tip.setItemText(0, QCoreApplication.translate("Dialog", u"---Seleccione una opci\u00f3n", None))
        self.tip.setItemText(1, QCoreApplication.translate("Dialog", u"CC  - C\u00e9dula de Ciudadan\u00eda", None))
        self.tip.setItemText(2, QCoreApplication.translate("Dialog", u"TI - Tarjeta de Identidad", None))
        self.tip.setItemText(3, QCoreApplication.translate("Dialog", u"RC - Registro Civil", None))

        self.numd.setText(QCoreApplication.translate("Dialog", u"N\u00famero de documento", None))
        self.reg.setText(QCoreApplication.translate("Dialog", u"REGISTRAR", None))
        self.tipd.setText(QCoreApplication.translate("Dialog", u"Tipo de documento", None))
        self.ns.setText(QCoreApplication.translate("Dialog", u"N\u00famero de solicitud", None))
#if QT_CONFIG(statustip)
        self.num.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

