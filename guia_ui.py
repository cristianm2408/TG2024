# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guia.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import imagen_rc

class Ui_guia(object):
    def setupUi(self, guia):
        if not guia.objectName():
            guia.setObjectName(u"guia")
        guia.resize(403, 229)
        guia.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.label = QLabel(guia)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 381, 41))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.foto = QLabel(guia)
        self.foto.setObjectName(u"foto")
        self.foto.setGeometry(QRect(180, 70, 61, 61))
        self.foto.setPixmap(QPixmap(u":/p/manual.png"))
        self.foto.setScaledContents(True)
        self.mostrar = QPushButton(guia)
        self.mostrar.setObjectName(u"mostrar")
        self.mostrar.setGeometry(QRect(90, 150, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(8)
        self.mostrar.setFont(font1)
        self.mostrar.setStyleSheet(u"background-color: rgb(255, 235, 116);")

        self.retranslateUi(guia)

        QMetaObject.connectSlotsByName(guia)
    # setupUi

    def retranslateUi(self, guia):
        guia.setWindowTitle(QCoreApplication.translate("guia", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("guia", u"MANUAL DE USUARIO", None))
        self.foto.setText("")
        self.mostrar.setText(QCoreApplication.translate("guia", u"MOSTRAR MANUAL DE USUARIO", None))
    # retranslateUi

