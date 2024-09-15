# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowv1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 453)
        MainWindow.setAutoFillBackground(False)
        self.actionNUEVO = QAction(MainWindow)
        self.actionNUEVO.setObjectName(u"actionNUEVO")
        self.actionIMPORTAR = QAction(MainWindow)
        self.actionIMPORTAR.setObjectName(u"actionIMPORTAR")
        self.actionEXPORTAR = QAction(MainWindow)
        self.actionEXPORTAR.setObjectName(u"actionEXPORTAR")
        self.actionFILTRO_1 = QAction(MainWindow)
        self.actionFILTRO_1.setObjectName(u"actionFILTRO_1")
        self.actionFILTRO_2 = QAction(MainWindow)
        self.actionFILTRO_2.setObjectName(u"actionFILTRO_2")
        self.actionFILTRO_3 = QAction(MainWindow)
        self.actionFILTRO_3.setObjectName(u"actionFILTRO_3")
        self.actionFILTRO_4 = QAction(MainWindow)
        self.actionFILTRO_4.setObjectName(u"actionFILTRO_4")
        self.actionFILTRO_5 = QAction(MainWindow)
        self.actionFILTRO_5.setObjectName(u"actionFILTRO_5")
        self.actionESTILO = QAction(MainWindow)
        self.actionESTILO.setObjectName(u"actionESTILO")
        self.actionSALIR = QAction(MainWindow)
        self.actionSALIR.setObjectName(u"actionSALIR")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 604, 33))
        self.menubar.setStyleSheet(u"background-color: #112C39;")
        self.menuARCHIVO = QMenu(self.menubar)
        self.menuARCHIVO.setObjectName(u"menuARCHIVO")
        self.menuARCHIVO.setStyleSheet(u"")
        self.menuGRABAR = QMenu(self.menubar)
        self.menuGRABAR.setObjectName(u"menuGRABAR")
        self.menuECUALIZACI_N = QMenu(self.menubar)
        self.menuECUALIZACI_N.setObjectName(u"menuECUALIZACI_N")
        self.menuAN_LISIS_DE_FRECUENCIA = QMenu(self.menubar)
        self.menuAN_LISIS_DE_FRECUENCIA.setObjectName(u"menuAN_LISIS_DE_FRECUENCIA")
        self.menuAN_LISIS_DE_FRECUENCIA.setStyleSheet(u"color: 5DF890;")
        self.menuCONFIGURACI_N = QMenu(self.menubar)
        self.menuCONFIGURACI_N.setObjectName(u"menuCONFIGURACI_N")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuARCHIVO.menuAction())
        self.menubar.addAction(self.menuGRABAR.menuAction())
        self.menubar.addAction(self.menuECUALIZACI_N.menuAction())
        self.menubar.addAction(self.menuAN_LISIS_DE_FRECUENCIA.menuAction())
        self.menubar.addAction(self.menuCONFIGURACI_N.menuAction())
        self.menuARCHIVO.addAction(self.actionNUEVO)
        self.menuARCHIVO.addAction(self.actionIMPORTAR)
        self.menuARCHIVO.addAction(self.actionEXPORTAR)
        self.menuECUALIZACI_N.addAction(self.actionFILTRO_1)
        self.menuECUALIZACI_N.addAction(self.actionFILTRO_2)
        self.menuECUALIZACI_N.addAction(self.actionFILTRO_3)
        self.menuECUALIZACI_N.addAction(self.actionFILTRO_4)
        self.menuECUALIZACI_N.addAction(self.actionFILTRO_5)
        self.menuCONFIGURACI_N.addAction(self.actionESTILO)
        self.menuCONFIGURACI_N.addAction(self.actionSALIR)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNUEVO.setText(QCoreApplication.translate("MainWindow", u"NUEVO", None))
        self.actionIMPORTAR.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.actionEXPORTAR.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR", None))
        self.actionFILTRO_1.setText(QCoreApplication.translate("MainWindow", u"FILTRO 1", None))
        self.actionFILTRO_2.setText(QCoreApplication.translate("MainWindow", u"FILTRO 2", None))
        self.actionFILTRO_3.setText(QCoreApplication.translate("MainWindow", u"FILTRO 3", None))
        self.actionFILTRO_4.setText(QCoreApplication.translate("MainWindow", u"FILTRO 4", None))
        self.actionFILTRO_5.setText(QCoreApplication.translate("MainWindow", u"FILTRO 5", None))
        self.actionESTILO.setText(QCoreApplication.translate("MainWindow", u"ESTILO", None))
        self.actionSALIR.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.menuARCHIVO.setTitle(QCoreApplication.translate("MainWindow", u"ARCHIVO", None))
        self.menuGRABAR.setTitle(QCoreApplication.translate("MainWindow", u"GRABAR", None))
        self.menuECUALIZACI_N.setTitle(QCoreApplication.translate("MainWindow", u"ECUALIZACI\u00d3N", None))
        self.menuAN_LISIS_DE_FRECUENCIA.setTitle(QCoreApplication.translate("MainWindow", u"AN\u00c1LISIS DE FRECUENCIA", None))
        self.menuCONFIGURACI_N.setTitle(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
    # retranslateUi

