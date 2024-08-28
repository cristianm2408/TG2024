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
    QWidget)
import imagen_rc
import TG_rc

class Ui_info(object):
    def setupUi(self, info):
        if not info.objectName():
            info.setObjectName(u"info")
        info.resize(639, 287)
        info.setMinimumSize(QSize(639, 287))
        info.setMaximumSize(QSize(639, 287))
        icon = QIcon()
        icon.addFile(u":/p/em.png", QSize(), QIcon.Normal, QIcon.Off)
        info.setWindowIcon(icon)
        info.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.autor = QLabel(info)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(20, 50, 171, 161))
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
        self.label_2 = QLabel(info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 60, 701, 251))
        self.label_2.setMinimumSize(QSize(700, 251))
        self.label_2.setMaximumSize(QSize(701, 251))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.retranslateUi(info)

        QMetaObject.connectSlotsByName(info)
    # setupUi

    def retranslateUi(self, info):
        info.setWindowTitle(QCoreApplication.translate("info", u"Informaci\u00f3n ", None))
        self.autor.setText("")
        self.label.setText(QCoreApplication.translate("info", u"<html><head/><body><p>GESTOR DE TAREAS</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("info", u"<html><head/><body><p><span style=\" font-weight:600;\">Version 1.1.4</span></p><p><span style=\" font-weight:600;\"><br/>Este programa fue dise\u00f1ado para la gesti\u00f3n de tareas </span></p><p align=\"justify\"><span style=\" font-weight:600;\">asignadas para el \u00e1rea de redes en la empresa Emtelco.</span></p><p><span style=\" font-weight:600;\"><br/>Desarrollado por:</span></p><p><span style=\" font-weight:600; text-decoration: underline; color:#00007f;\">Cristian Moreno</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
    # retranslateUi

