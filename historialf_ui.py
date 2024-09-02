# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historialf.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QDialog,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import imagen_rc

class Ui_historial(object):
    def setupUi(self, historial):
        if not historial.objectName():
            historial.setObjectName(u"historial")
        historial.resize(1326, 805)
        historial.setMinimumSize(QSize(1326, 805))
        historial.setMaximumSize(QSize(1326, 805))
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
        self.hbus = QPushButton(historial)
        self.hbus.setObjectName(u"hbus")
        self.hbus.setGeometry(QRect(950, 160, 141, 61))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.hbus.setFont(font1)
        self.hbus.setCursor(QCursor(Qt.PointingHandCursor))
        self.hbus.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #7BDDDD;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0EC2C2;\n"
"}")
        self.fonhis = QLabel(historial)
        self.fonhis.setObjectName(u"fonhis")
        self.fonhis.setGeometry(QRect(0, -20, 1331, 931))
        font2 = QFont()
        font2.setFamilies([u"Lucida Bright"])
        self.fonhis.setFont(font2)
        self.fonhis.setPixmap(QPixmap(u":/p/gra.png"))
        self.fonhis.setScaledContents(True)
        self.hdesdef = QDateEdit(historial)
        self.hdesdef.setObjectName(u"hdesdef")
        self.hdesdef.setGeometry(QRect(380, 170, 171, 41))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(12)
        self.hdesdef.setFont(font3)
        self.hdesdef.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.hdesdef.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.hdesdef.setCalendarPopup(True)
        self.hdesde = QLabel(historial)
        self.hdesde.setObjectName(u"hdesde")
        self.hdesde.setGeometry(QRect(300, 170, 221, 31))
        self.hdesde.setFont(font1)
        self.hhasta = QLabel(historial)
        self.hhasta.setObjectName(u"hhasta")
        self.hhasta.setGeometry(QRect(630, 170, 221, 31))
        self.hhasta.setFont(font1)
        self.hhastaf = QDateEdit(historial)
        self.hhastaf.setObjectName(u"hhastaf")
        self.hhastaf.setGeometry(QRect(700, 170, 181, 41))
        self.hhastaf.setFont(font3)
        self.hhastaf.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.hhastaf.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.hhastaf.setCalendarPopup(True)
        self.tablatf = QTableWidget(historial)
        if (self.tablatf.columnCount() < 9):
            self.tablatf.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablatf.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tablatf.setObjectName(u"tablatf")
        self.tablatf.setGeometry(QRect(0, 270, 1330, 651))
        self.tablatf.setMinimumSize(QSize(1330, 651))
        self.tablatf.setMaximumSize(QSize(1041, 651))
        self.tablatf.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(13)
        self.tablatf.setFont(font4)
        self.tablatf.setLineWidth(15)
        self.tablatf.setAutoScroll(True)
        self.tablatf.setIconSize(QSize(23, 0))
        self.tablatf.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablatf.horizontalHeader().setCascadingSectionResizes(False)
        self.tablatf.horizontalHeader().setMinimumSectionSize(87)
        self.tablatf.horizontalHeader().setDefaultSectionSize(132)
        self.tablatf.verticalHeader().setDefaultSectionSize(66)
        self.label = QLabel(historial)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 90, 1001, 41))
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(16)
        font5.setBold(True)
        self.label.setFont(font5)
        self.registro3 = QLabel(historial)
        self.registro3.setObjectName(u"registro3")
        self.registro3.setGeometry(QRect(440, 10, 461, 61))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Black"])
        font6.setPointSize(19)
        font6.setBold(True)
        self.registro3.setFont(font6)
        self.registro3.setPixmap(QPixmap(u":/p/histo.png"))
        self.registro3.setScaledContents(True)
        self.fonhis.raise_()
        self.log.raise_()
        self.hbus.raise_()
        self.hdesdef.raise_()
        self.hdesde.raise_()
        self.hhasta.raise_()
        self.hhastaf.raise_()
        self.tablatf.raise_()
        self.label.raise_()
        self.registro3.raise_()

        self.retranslateUi(historial)

        QMetaObject.connectSlotsByName(historial)
    # setupUi

    def retranslateUi(self, historial):
        historial.setWindowTitle(QCoreApplication.translate("historial", u"Tareas", None))
        self.log.setText("")
        self.hbus.setText(QCoreApplication.translate("historial", u"Buscar", None))
        self.fonhis.setText("")
        self.hdesdef.setDisplayFormat(QCoreApplication.translate("historial", u"d/MM/yyyy", None))
        self.hdesde.setText(QCoreApplication.translate("historial", u"<html><head/><body><p><span style=\" color:#ffffff;\">Desde</span></p></body></html>", None))
        self.hhasta.setText(QCoreApplication.translate("historial", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hasta</span></p></body></html>", None))
        self.hhastaf.setDisplayFormat(QCoreApplication.translate("historial", u"d/MM/yyyy", None))
        ___qtablewidgetitem = self.tablatf.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("historial", u"Usuario", None));
        ___qtablewidgetitem1 = self.tablatf.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("historial", u"VLAN", None));
        ___qtablewidgetitem2 = self.tablatf.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("historial", u"Tipo Tarea", None));
        ___qtablewidgetitem3 = self.tablatf.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("historial", u"No. Tarea", None));
        ___qtablewidgetitem4 = self.tablatf.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("historial", u"Equipos", None));
        ___qtablewidgetitem5 = self.tablatf.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("historial", u"Solicitud", None));
        ___qtablewidgetitem6 = self.tablatf.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("historial", u"Soluci\u00f3n", None));
        ___qtablewidgetitem7 = self.tablatf.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("historial", u"Realizada", None));
        ___qtablewidgetitem8 = self.tablatf.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("historial", u"Fecha", None));
        self.label.setText(QCoreApplication.translate("historial", u"<html><head/><body><p><span style=\" color:#ffffff;\">- Buscar tareas teniendo en cuenta solo la fecha de registro</span></p></body></html>", None))
        self.registro3.setText("")
    # retranslateUi

