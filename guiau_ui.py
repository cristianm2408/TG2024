# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiau.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QTextEdit, QWidget)
import imagen_rc

class Ui_guia(object):
    def setupUi(self, guia):
        if not guia.objectName():
            guia.setObjectName(u"guia")
        guia.resize(1099, 857)
        guia.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.label = QLabel(guia)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 20, 381, 41))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.textEdit = QTextEdit(guia)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 140, 1001, 701))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background-color: rgb(238, 235, 255);")
        self.label_2 = QLabel(guia)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 1291, 81))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_2.setFont(font2)

        self.retranslateUi(guia)

        QMetaObject.connectSlotsByName(guia)
    # setupUi

    def retranslateUi(self, guia):
        guia.setWindowTitle(QCoreApplication.translate("guia", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("guia", u"MANUAL DE USUARIO", None))
        self.textEdit.setHtml(QCoreApplication.translate("guia", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Nirmala UI'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("guia", u"Acontinuaci\u00f3n se presenta la gu\u00eda de usuario para el registro de tareas diarias y  respectiva busqueda de tareas registradas en el historial", None))
    # retranslateUi

