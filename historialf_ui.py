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
        self.hregistro = QLabel(historial)
        self.hregistro.setObjectName(u"hregistro")
        self.hregistro.setGeometry(QRect(480, 10, 461, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.hregistro.setFont(font1)
        self.hbus = QPushButton(historial)
        self.hbus.setObjectName(u"hbus")
        self.hbus.setGeometry(QRect(770, 190, 141, 61))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.hbus.setFont(font2)
        self.hbus.setCursor(QCursor(Qt.PointingHandCursor))
        self.hbus.setStyleSheet(u"background-color: rgb(123, 221, 221);\n"
"border-radius:8px")
        self.fonhis = QLabel(historial)
        self.fonhis.setObjectName(u"fonhis")
        self.fonhis.setGeometry(QRect(0, -20, 1331, 931))
        font3 = QFont()
        font3.setFamilies([u"Lucida Bright"])
        self.fonhis.setFont(font3)
        self.fonhis.setPixmap(QPixmap(u":/p/cla.png"))
        self.fonhis.setScaledContents(True)
        self.hdesdef = QDateEdit(historial)
        self.hdesdef.setObjectName(u"hdesdef")
        self.hdesdef.setGeometry(QRect(260, 200, 171, 41))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(12)
        self.hdesdef.setFont(font4)
        self.hdesdef.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.hdesdef.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.hdesde = QLabel(historial)
        self.hdesde.setObjectName(u"hdesde")
        self.hdesde.setGeometry(QRect(270, 150, 221, 31))
        self.hdesde.setFont(font2)
        self.hhasta = QLabel(historial)
        self.hhasta.setObjectName(u"hhasta")
        self.hhasta.setGeometry(QRect(530, 150, 221, 31))
        self.hhasta.setFont(font2)
        self.hhastaf = QDateEdit(historial)
        self.hhastaf.setObjectName(u"hhastaf")
        self.hhastaf.setGeometry(QRect(520, 200, 181, 41))
        self.hhastaf.setFont(font4)
        self.hhastaf.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.hhastaf.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
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
        self.tablatf.setGeometry(QRect(0, 270, 1330, 505))
        self.tablatf.setMinimumSize(QSize(1330, 505))
        self.tablatf.setMaximumSize(QSize(1041, 401))
        self.tablatf.setSizeIncrement(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(13)
        self.tablatf.setFont(font5)
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
        self.label.setGeometry(QRect(200, 90, 1001, 31))
        font6 = QFont()
        font6.setFamilies([u"Arial Black"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.label.setFont(font6)
        self.fonhis.raise_()
        self.log.raise_()
        self.hregistro.raise_()
        self.hbus.raise_()
        self.hdesdef.raise_()
        self.hdesde.raise_()
        self.hhasta.raise_()
        self.hhastaf.raise_()
        self.tablatf.raise_()
        self.label.raise_()

        self.retranslateUi(historial)

        QMetaObject.connectSlotsByName(historial)
    # setupUi

    def retranslateUi(self, historial):
        historial.setWindowTitle(QCoreApplication.translate("historial", u"Tareas", None))
        self.log.setText("")
        self.hregistro.setText(QCoreApplication.translate("historial", u"HISTORIAL DE TAREAS", None))
        self.hbus.setText(QCoreApplication.translate("historial", u"Buscar", None))
        self.fonhis.setText("")
        self.hdesdef.setDisplayFormat(QCoreApplication.translate("historial", u"d/MM/yyyy", None))
        self.hdesde.setText(QCoreApplication.translate("historial", u"Desde", None))
        self.hhasta.setText(QCoreApplication.translate("historial", u"Hasta", None))
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
        self.label.setText(QCoreApplication.translate("historial", u"\u2022 Buscar tareas teniendo en cuenta solo la fecha de registro", None))
    # retranslateUi

