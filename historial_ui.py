# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historial.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
import imagen_rc
import imagen_rc

class Ui_historial(object):
    def setupUi(self, historial):
        if not historial.objectName():
            historial.setObjectName(u"historial")
        historial.resize(1324, 805)
        font = QFont()
        font.setPointSize(1)
        historial.setFont(font)
        historial.setStyleSheet(u"")
        self.log = QLabel(historial)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(0, 10, 141, 131))
        self.log.setPixmap(QPixmap(u":/p/FOsp.png"))
        self.log.setScaledContents(True)
        self.registro = QLabel(historial)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(520, 20, 461, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.registro.setFont(font1)
        self.bus = QPushButton(historial)
        self.bus.setObjectName(u"bus")
        self.bus.setGeometry(QRect(610, 300, 131, 51))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.bus.setFont(font2)
        self.bus.setCursor(QCursor(Qt.PointingHandCursor))
        self.bus.setStyleSheet(u"background-color: rgb(123, 221, 221);\n"
"border-radius:8px")
        self.nusu = QLabel(historial)
        self.nusu.setObjectName(u"nusu")
        self.nusu.setGeometry(QRect(300, 180, 241, 41))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.nusu.setFont(font3)
        self.fonhis = QLabel(historial)
        self.fonhis.setObjectName(u"fonhis")
        self.fonhis.setGeometry(QRect(0, -20, 1331, 931))
        font4 = QFont()
        font4.setFamilies([u"Lucida Bright"])
        self.fonhis.setFont(font4)
        self.fonhis.setPixmap(QPixmap(u":/p/cla.png"))
        self.fonhis.setScaledContents(True)
        self.fdesde = QDateEdit(historial)
        self.fdesde.setObjectName(u"fdesde")
        self.fdesde.setGeometry(QRect(650, 230, 161, 31))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(12)
        self.fdesde.setFont(font5)
        self.fdesde.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.fdesde.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.tdesde = QLabel(historial)
        self.tdesde.setObjectName(u"tdesde")
        self.tdesde.setGeometry(QRect(660, 180, 221, 31))
        self.tdesde.setFont(font3)
        self.thasta = QLabel(historial)
        self.thasta.setObjectName(u"thasta")
        self.thasta.setGeometry(QRect(860, 180, 221, 31))
        self.thasta.setFont(font3)
        self.fhasta = QDateEdit(historial)
        self.fhasta.setObjectName(u"fhasta")
        self.fhasta.setGeometry(QRect(860, 230, 161, 31))
        self.fhasta.setFont(font5)
        self.fhasta.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.fhasta.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.label = QLabel(historial)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 120, 651, 31))
        font6 = QFont()
        font6.setPointSize(13)
        self.label.setFont(font6)
        self.tablat = QTableWidget(historial)
        if (self.tablat.columnCount() < 9):
            self.tablat.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablat.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tablat.setObjectName(u"tablat")
        self.tablat.setGeometry(QRect(0, 400, 1330, 505))
        self.tablat.setMinimumSize(QSize(1330, 505))
        self.tablat.setMaximumSize(QSize(1041, 401))
        self.tablat.setSizeIncrement(QSize(0, 0))
        self.tablat.setFont(font6)
        self.tablat.setLineWidth(15)
        self.tablat.setAutoScroll(True)
        self.tablat.setIconSize(QSize(23, 0))
        self.tablat.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablat.horizontalHeader().setCascadingSectionResizes(False)
        self.tablat.horizontalHeader().setMinimumSectionSize(87)
        self.tablat.horizontalHeader().setDefaultSectionSize(132)
        self.tablat.verticalHeader().setDefaultSectionSize(66)
        self.cusu = QLineEdit(historial)
        self.cusu.setObjectName(u"cusu")
        self.cusu.setGeometry(QRect(300, 230, 231, 31))
        font7 = QFont()
        font7.setPointSize(12)
        self.cusu.setFont(font7)
        self.fonhis.raise_()
        self.log.raise_()
        self.registro.raise_()
        self.bus.raise_()
        self.nusu.raise_()
        self.fdesde.raise_()
        self.tdesde.raise_()
        self.thasta.raise_()
        self.fhasta.raise_()
        self.label.raise_()
        self.tablat.raise_()
        self.cusu.raise_()

        self.retranslateUi(historial)

        QMetaObject.connectSlotsByName(historial)
    # setupUi

    def retranslateUi(self, historial):
        historial.setWindowTitle(QCoreApplication.translate("historial", u"Dialog", None))
        self.log.setText("")
        self.registro.setText(QCoreApplication.translate("historial", u"HISTORIAL DE TAREAS", None))
        self.bus.setText(QCoreApplication.translate("historial", u"Buscar", None))
        self.nusu.setText(QCoreApplication.translate("historial", u"Nombre de usuario", None))
        self.fonhis.setText("")
        self.fdesde.setDisplayFormat(QCoreApplication.translate("historial", u"d/MM/yyyy", None))
        self.tdesde.setText(QCoreApplication.translate("historial", u"Desde", None))
        self.thasta.setText(QCoreApplication.translate("historial", u"Hasta", None))
        self.fhasta.setDisplayFormat(QCoreApplication.translate("historial", u"d/MM/yyyy", None))
        self.label.setText(QCoreApplication.translate("historial", u"Buscar tareas teniendo en cuenta el usuario y fecha de registro", None))
        ___qtablewidgetitem = self.tablat.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("historial", u"Usuario", None));
        ___qtablewidgetitem1 = self.tablat.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("historial", u"VLAN", None));
        ___qtablewidgetitem2 = self.tablat.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("historial", u"Tipo Tarea", None));
        ___qtablewidgetitem3 = self.tablat.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("historial", u"No. Tarea", None));
        ___qtablewidgetitem4 = self.tablat.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("historial", u"Equipos", None));
        ___qtablewidgetitem5 = self.tablat.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("historial", u"Solicitud", None));
        ___qtablewidgetitem6 = self.tablat.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("historial", u"Soluci\u00f3n", None));
        ___qtablewidgetitem7 = self.tablat.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("historial", u"Realizada", None));
        ___qtablewidgetitem8 = self.tablat.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("historial", u"Fecha", None));
    # retranslateUi

