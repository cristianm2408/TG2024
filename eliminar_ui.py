# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminar.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import imagen_rc
import imagen_rc

class Ui_historial(object):
    def setupUi(self, historial):
        if not historial.objectName():
            historial.setObjectName(u"historial")
        historial.resize(883, 294)
        historial.setMinimumSize(QSize(0, 0))
        historial.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setPointSize(1)
        historial.setFont(font)
        icon = QIcon()
        icon.addFile(u":/p/em.png", QSize(), QIcon.Normal, QIcon.Off)
        historial.setWindowIcon(icon)
        historial.setStyleSheet(u"")
        self.log = QLabel(historial)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(0, 10, 141, 131))
        self.log.setPixmap(QPixmap(u":/p/FOsp.png"))
        self.log.setScaledContents(True)
        self.fonhisb = QLabel(historial)
        self.fonhisb.setObjectName(u"fonhisb")
        self.fonhisb.setEnabled(True)
        self.fonhisb.setGeometry(QRect(0, 0, 1431, 941))
        self.fonhisb.setMinimumSize(QSize(0, 0))
        self.fonhisb.setMaximumSize(QSize(10000, 10000))
        font1 = QFont()
        font1.setFamilies([u"Lucida Bright"])
        self.fonhisb.setFont(font1)
        self.fonhisb.setPixmap(QPixmap(u":/p/cla.png"))
        self.fonhisb.setScaledContents(True)
        self.eliminar = QPushButton(historial)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(600, 100, 141, 61))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.eliminar.setFont(font2)
        self.eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.eliminar.setStyleSheet(u"background-color: rgb(123, 221, 221);\n"
"border-radius:8px")
        self.nticket = QLineEdit(historial)
        self.nticket.setObjectName(u"nticket")
        self.nticket.setGeometry(QRect(290, 120, 211, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.nticket.setFont(font3)
        self.label = QLabel(historial)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 90, 201, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial Black"])
        font4.setPointSize(12)
        self.label.setFont(font4)
        self.fonhisb.raise_()
        self.log.raise_()
        self.eliminar.raise_()
        self.nticket.raise_()
        self.label.raise_()

        self.retranslateUi(historial)

        QMetaObject.connectSlotsByName(historial)
    # setupUi

    def retranslateUi(self, historial):
        historial.setWindowTitle(QCoreApplication.translate("historial", u"Tareas", None))
        self.log.setText("")
        self.fonhisb.setText("")
        self.eliminar.setText(QCoreApplication.translate("historial", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("historial", u"No. TICKET", None))
    # retranslateUi

