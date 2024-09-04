# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHeaderView,
    QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import imagen_rc

class Ui_historial(object):
    def setupUi(self, historial):
        if not historial.objectName():
            historial.setObjectName(u"historial")
        historial.resize(1330, 805)
        historial.setMinimumSize(QSize(1330, 805))
        historial.setMaximumSize(QSize(1330, 805))
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
        self.registro = QLabel(historial)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(440, 30, 461, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.registro.setFont(font1)
        self.registro.setPixmap(QPixmap(u":/p/histo.png"))
        self.registro.setScaledContents(True)
        self.fonhisb = QLabel(historial)
        self.fonhisb.setObjectName(u"fonhisb")
        self.fonhisb.setGeometry(QRect(0, 0, 1431, 931))
        font2 = QFont()
        font2.setFamilies([u"Lucida Bright"])
        self.fonhisb.setFont(font2)
        self.fonhisb.setPixmap(QPixmap(u":/p/gra.png"))
        self.fonhisb.setScaledContents(True)
        self.tablab = QTableWidget(historial)
        if (self.tablab.columnCount() < 9):
            self.tablab.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablab.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tablab.setObjectName(u"tablab")
        self.tablab.setGeometry(QRect(0, 150, 1330, 651))
        self.tablab.setMinimumSize(QSize(1330, 651))
        self.tablab.setMaximumSize(QSize(1041, 401))
        self.tablab.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(13)
        self.tablab.setFont(font3)
        self.tablab.setLineWidth(15)
        self.tablab.setAutoScroll(True)
        self.tablab.setIconSize(QSize(23, 0))
        self.tablab.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablab.horizontalHeader().setCascadingSectionResizes(False)
        self.tablab.horizontalHeader().setMinimumSectionSize(87)
        self.tablab.horizontalHeader().setDefaultSectionSize(132)
        self.tablab.verticalHeader().setDefaultSectionSize(66)
        self.fonhisb.raise_()
        self.log.raise_()
        self.registro.raise_()
        self.tablab.raise_()

        self.retranslateUi(historial)

        QMetaObject.connectSlotsByName(historial)
    # setupUi

    def retranslateUi(self, historial):
        historial.setWindowTitle(QCoreApplication.translate("historial", u"Tareas", None))
        self.log.setText("")
        self.registro.setText("")
        self.fonhisb.setText("")
        ___qtablewidgetitem = self.tablab.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("historial", u"Usuario", None));
        ___qtablewidgetitem1 = self.tablab.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("historial", u"VLAN", None));
        ___qtablewidgetitem2 = self.tablab.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("historial", u"Tipo Tarea", None));
        ___qtablewidgetitem3 = self.tablab.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("historial", u"No. Tarea", None));
        ___qtablewidgetitem4 = self.tablab.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("historial", u"Equipos", None));
        ___qtablewidgetitem5 = self.tablab.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("historial", u"Solicitud", None));
        ___qtablewidgetitem6 = self.tablab.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("historial", u"Soluci\u00f3n", None));
        ___qtablewidgetitem7 = self.tablab.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("historial", u"Realizada", None));
        ___qtablewidgetitem8 = self.tablab.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("historial", u"Fecha", None));
    # retranslateUi

