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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
import imagen_rc

class Ui_guia(object):
    def setupUi(self, guia):
        if not guia.objectName():
            guia.setObjectName(u"guia")
        guia.resize(1300, 857)
        guia.setMinimumSize(QSize(1300, 857))
        guia.setMaximumSize(QSize(1300, 857))
        icon = QIcon()
        icon.addFile(u":/p/em.png", QSize(), QIcon.Normal, QIcon.Off)
        guia.setWindowIcon(icon)
        guia.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.manual = QLabel(guia)
        self.manual.setObjectName(u"manual")
        self.manual.setGeometry(QRect(450, 30, 391, 61))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.manual.setFont(font)
        self.manual.setPixmap(QPixmap(u":/p/man.png"))
        self.manual.setScaledContents(True)
        self.fonhis = QLabel(guia)
        self.fonhis.setObjectName(u"fonhis")
        self.fonhis.setGeometry(QRect(-10, -10, 1311, 951))
        self.fonhis.setPixmap(QPixmap(u":/p/gra.png"))
        self.fonhis.setScaledContents(True)
        self.guiausuario = QScrollArea(guia)
        self.guiausuario.setObjectName(u"guiausuario")
        self.guiausuario.setGeometry(QRect(10, 110, 1281, 741))
        self.guiausuario.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -10646, 1297, 11364))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.guia1 = QLabel(self.scrollAreaWidgetContents)
        self.guia1.setObjectName(u"guia1")
        self.guia1.setMinimumSize(QSize(500, 1400))

        self.verticalLayout.addWidget(self.guia1)

        self.guia2 = QLabel(self.scrollAreaWidgetContents)
        self.guia2.setObjectName(u"guia2")

        self.verticalLayout.addWidget(self.guia2)

        self.guia3 = QLabel(self.scrollAreaWidgetContents)
        self.guia3.setObjectName(u"guia3")

        self.verticalLayout.addWidget(self.guia3)

        self.guia4 = QLabel(self.scrollAreaWidgetContents)
        self.guia4.setObjectName(u"guia4")

        self.verticalLayout.addWidget(self.guia4)

        self.guia5 = QLabel(self.scrollAreaWidgetContents)
        self.guia5.setObjectName(u"guia5")

        self.verticalLayout.addWidget(self.guia5)

        self.guia6 = QLabel(self.scrollAreaWidgetContents)
        self.guia6.setObjectName(u"guia6")

        self.verticalLayout.addWidget(self.guia6)

        self.guia7 = QLabel(self.scrollAreaWidgetContents)
        self.guia7.setObjectName(u"guia7")

        self.verticalLayout.addWidget(self.guia7)

        self.guiausuario.setWidget(self.scrollAreaWidgetContents)
        self.fonhis.raise_()
        self.manual.raise_()
        self.guiausuario.raise_()

        self.retranslateUi(guia)

        QMetaObject.connectSlotsByName(guia)
    # setupUi

    def retranslateUi(self, guia):
        guia.setWindowTitle(QCoreApplication.translate("guia", u"Guia de Usuario", None))
        self.manual.setText("")
        self.fonhis.setText("")
        self.guia1.setText(QCoreApplication.translate("guia", u"<html><head/><body><p><img src=\":/p/guia1.jpg\"/></p></body></html>", None))
        self.guia2.setText(QCoreApplication.translate("guia", u"<html><head/><body><p><img src=\":/p/guia2.jpg\"/></p></body></html>", None))
        self.guia3.setText(QCoreApplication.translate("guia", u"<html><head/><body><p align=\"center\"><img src=\":/p/guia3.jpg\"/></p></body></html>", None))
        self.guia4.setText(QCoreApplication.translate("guia", u"<html><head/><body><p align=\"center\"><img src=\":/p/guia4.jpg\"/></p></body></html>", None))
        self.guia5.setText(QCoreApplication.translate("guia", u"<html><head/><body><p><img src=\":/p/guia5.jpg\"/></p></body></html>", None))
        self.guia6.setText(QCoreApplication.translate("guia", u"<html><head/><body><p align=\"center\"><img src=\":/p/guia6.jpg\"/></p></body></html>", None))
        self.guia7.setText(QCoreApplication.translate("guia", u"<html><head/><body><p align=\"center\"><img src=\":/p/guia7.jpg\"/></p></body></html>", None))
    # retranslateUi

