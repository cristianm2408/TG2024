# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
import TG_rc

class Ui_info(object):
    def setupUi(self, info):
        if not info.objectName():
            info.setObjectName(u"info")
        info.resize(588, 279)
        info.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.autor = QLabel(info)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(10, 50, 171, 161))
        self.autor.setPixmap(QPixmap(u":/p/8083308.png"))
        self.autor.setScaledContents(True)
        self.label = QLabel(info)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 10, 301, 41))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.textEdit = QTextEdit(info)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(210, 60, 371, 221))
        self.textEdit.setStyleSheet(u"")

        self.retranslateUi(info)

        QMetaObject.connectSlotsByName(info)
    # setupUi

    def retranslateUi(self, info):
        info.setWindowTitle(QCoreApplication.translate("info", u"Dialog", None))
        self.autor.setText("")
        self.label.setText(QCoreApplication.translate("info", u"<html><head/><body><p>GESTOR DE TAREAS</p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("info", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Version 1.1.4</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Este programa fue dise\u00f1ado para la gesti\u00f3n de tareas asignadas para el \u00e1rea de redes en la empresa Emtelco.</span></p>\n"
"<p style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Desarrollado por:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Cristian Moreno</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p></body></html>", None))
    # retranslateUi

