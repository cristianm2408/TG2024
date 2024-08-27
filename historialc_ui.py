# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historialc.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import imagen_rc
import imagen_rc

class Ui_historial(object):
    def setupUi(self, historial):
        if not historial.objectName():
            historial.setObjectName(u"historial")
        historial.resize(1319, 805)
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
        self.registro.setGeometry(QRect(530, 20, 461, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.registro.setFont(font1)
        self.buscarv = QPushButton(historial)
        self.buscarv.setObjectName(u"buscarv")
        self.buscarv.setGeometry(QRect(630, 210, 141, 61))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.buscarv.setFont(font2)
        self.buscarv.setCursor(QCursor(Qt.PointingHandCursor))
        self.buscarv.setStyleSheet(u"background-color: rgb(123, 221, 221);\n"
"border-radius:8px")
        self.vlan = QLabel(historial)
        self.vlan.setObjectName(u"vlan")
        self.vlan.setGeometry(QRect(300, 180, 241, 41))
        self.vlan.setFont(font2)
        self.fonhis = QLabel(historial)
        self.fonhis.setObjectName(u"fonhis")
        self.fonhis.setGeometry(QRect(0, -20, 1331, 931))
        font3 = QFont()
        font3.setFamilies([u"Lucida Bright"])
        self.fonhis.setFont(font3)
        self.fonhis.setPixmap(QPixmap(u":/p/cla.png"))
        self.fonhis.setScaledContents(True)
        self.texto = QLabel(historial)
        self.texto.setObjectName(u"texto")
        self.texto.setGeometry(QRect(270, 120, 811, 31))
        font4 = QFont()
        font4.setPointSize(14)
        self.texto.setFont(font4)
        self.nvlan = QComboBox(historial)
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.addItem("")
        self.nvlan.setObjectName(u"nvlan")
        self.nvlan.setGeometry(QRect(290, 230, 251, 41))
        font5 = QFont()
        font5.setPointSize(11)
        self.nvlan.setFont(font5)
        self.nvlan.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.tablav = QTableWidget(historial)
        if (self.tablav.columnCount() < 9):
            self.tablav.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablav.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tablav.setObjectName(u"tablav")
        self.tablav.setGeometry(QRect(0, 320, 1330, 505))
        self.tablav.setMinimumSize(QSize(1330, 505))
        self.tablav.setMaximumSize(QSize(1041, 401))
        self.tablav.setSizeIncrement(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(13)
        self.tablav.setFont(font6)
        self.tablav.setLineWidth(15)
        self.tablav.setAutoScroll(True)
        self.tablav.setIconSize(QSize(23, 0))
        self.tablav.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablav.horizontalHeader().setCascadingSectionResizes(False)
        self.tablav.horizontalHeader().setMinimumSectionSize(87)
        self.tablav.horizontalHeader().setDefaultSectionSize(132)
        self.tablav.verticalHeader().setDefaultSectionSize(66)
        self.fonhis.raise_()
        self.log.raise_()
        self.registro.raise_()
        self.buscarv.raise_()
        self.vlan.raise_()
        self.texto.raise_()
        self.nvlan.raise_()
        self.tablav.raise_()

        self.retranslateUi(historial)

        QMetaObject.connectSlotsByName(historial)
    # setupUi

    def retranslateUi(self, historial):
        historial.setWindowTitle(QCoreApplication.translate("historial", u"Dialog", None))
        self.log.setText("")
        self.registro.setText(QCoreApplication.translate("historial", u"HISTORIAL DE TAREAS", None))
        self.buscarv.setText(QCoreApplication.translate("historial", u"Buscar", None))
        self.vlan.setText(QCoreApplication.translate("historial", u"VLAN-Campa\u00f1a", None))
        self.fonhis.setText("")
        self.texto.setText(QCoreApplication.translate("historial", u"Buscar tareas teniendo en cuenta VLAN-Campa\u00f1a y fecha de registro", None))
        self.nvlan.setItemText(0, QCoreApplication.translate("historial", u"---Seleccione una opci\u00f3n", None))
        self.nvlan.setItemText(1, QCoreApplication.translate("historial", u"ADMINISTRACI\u00d3N ", None))
        self.nvlan.setItemText(2, QCoreApplication.translate("historial", u"ADDI ", None))
        self.nvlan.setItemText(3, QCoreApplication.translate("historial", u"ALKOSTO ", None))
        self.nvlan.setItemText(4, QCoreApplication.translate("historial", u"BBVA ", None))
        self.nvlan.setItemText(5, QCoreApplication.translate("historial", u"TUYABOG  ", None))
        self.nvlan.setItemText(6, QCoreApplication.translate("historial", u"COMPENSAR", None))
        self.nvlan.setItemText(7, QCoreApplication.translate("historial", u"KERALTY ", None))
        self.nvlan.setItemText(8, QCoreApplication.translate("historial", u"JUAN VALDEZ ", None))
        self.nvlan.setItemText(9, QCoreApplication.translate("historial", u"PREVISORA ", None))
        self.nvlan.setItemText(10, QCoreApplication.translate("historial", u"PARMALAT ", None))
        self.nvlan.setItemText(11, QCoreApplication.translate("historial", u"TUBOLETA ", None))
        self.nvlan.setItemText(12, QCoreApplication.translate("historial", u"PAPA JOHNS ", None))
        self.nvlan.setItemText(13, QCoreApplication.translate("historial", u"NOVONORDISK ", None))
        self.nvlan.setItemText(14, QCoreApplication.translate("historial", u"SALUD TOTAL ", None))
        self.nvlan.setItemText(15, QCoreApplication.translate("historial", u"COLPENSIONES ", None))
        self.nvlan.setItemText(16, QCoreApplication.translate("historial", u"COLMEDICA", None))
        self.nvlan.setItemText(17, QCoreApplication.translate("historial", u"CONINSA ", None))
        self.nvlan.setItemText(18, QCoreApplication.translate("historial", u"OTRA", None))

        ___qtablewidgetitem = self.tablav.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("historial", u"Usuario", None));
        ___qtablewidgetitem1 = self.tablav.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("historial", u"VLAN", None));
        ___qtablewidgetitem2 = self.tablav.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("historial", u"Tipo Tarea", None));
        ___qtablewidgetitem3 = self.tablav.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("historial", u"No. Tarea", None));
        ___qtablewidgetitem4 = self.tablav.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("historial", u"Equipos", None));
        ___qtablewidgetitem5 = self.tablav.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("historial", u"Solicitud", None));
        ___qtablewidgetitem6 = self.tablav.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("historial", u"Soluci\u00f3n", None));
        ___qtablewidgetitem7 = self.tablav.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("historial", u"Realizada", None));
        ___qtablewidgetitem8 = self.tablav.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("historial", u"Fecha", None));
    # retranslateUi

