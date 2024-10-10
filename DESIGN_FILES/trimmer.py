# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuttter.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ContenedorEncabezado_2 = QFrame(self.centralwidget)
        self.ContenedorEncabezado_2.setObjectName(u"ContenedorEncabezado_2")
        self.ContenedorEncabezado_2.setGeometry(QRect(-20, 0, 841, 80))
        self.ContenedorEncabezado_2.setStyleSheet(u"QFrame {\n"
"	background-color: #112C39;\n"
"	width: 711px;\n"
"	height: 89px;\n"
"}")
        self.ContenedorEncabezado_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContenedorEncabezado_2.setFrameShadow(QFrame.Shadow.Raised)
        self.TituloPantalla_2 = QLabel(self.ContenedorEncabezado_2)
        self.TituloPantalla_2.setObjectName(u"TituloPantalla_2")
        self.TituloPantalla_2.setGeometry(QRect(270, 30, 351, 21))
        self.TituloPantalla_2.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 24px;\n"
"	color: #5DF890;\n"
"	font-weight: bold;\n"
"}")
        self.ContenedorPrincipal_3 = QFrame(self.centralwidget)
        self.ContenedorPrincipal_3.setObjectName(u"ContenedorPrincipal_3")
        self.ContenedorPrincipal_3.setGeometry(QRect(-10, 80, 921, 501))
        self.ContenedorPrincipal_3.setStyleSheet(u"QFrame{\n"
"	background-color: #113E53;\n"
"}")
        self.ContenedorPrincipal_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContenedorPrincipal_3.setFrameShadow(QFrame.Shadow.Raised)
        self.Duracion_3 = QLabel(self.ContenedorPrincipal_3)
        self.Duracion_3.setObjectName(u"Duracion_3")
        self.Duracion_3.setGeometry(QRect(220, 120, 101, 21))
        self.Duracion_3.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 20px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.TiempoGrabacion_3 = QSlider(self.ContenedorPrincipal_3)
        self.TiempoGrabacion_3.setObjectName(u"TiempoGrabacion_3")
        self.TiempoGrabacion_3.setGeometry(QRect(330, 120, 221, 22))
        self.TiempoGrabacion_3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    background: #D8D8D8;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #5DF890; /* Color del handle */\n"
"    border: 1px solid #5DF890;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    margin: -7px 0; /* Para centrar el handle en el groove */\n"
"    border-radius: 9px; /* Bordes redondeados */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #112C39; /* Color del handle cuando el cursor pasa encima */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #5DF890; /* Color de la parte ya deslizada */\n"
"    border: 1px solid #5DF890;\n"
"    height: 4px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #D8D8D8; /* Color de la parte no deslizada */\n"
"    border: 1px solid #D8D8D8;\n"
"    height: 4px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.TiempoGrabacion_3.setMinimum(10)
        self.TiempoGrabacion_3.setMaximum(40)
        self.TiempoGrabacion_3.setOrientation(Qt.Orientation.Horizontal)
        self.SegundosGrabacion_3 = QLabel(self.ContenedorPrincipal_3)
        self.SegundosGrabacion_3.setObjectName(u"SegundosGrabacion_3")
        self.SegundosGrabacion_3.setGeometry(QRect(570, 120, 81, 21))
        self.SegundosGrabacion_3.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 14px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.IniciarGrabacion_3 = QPushButton(self.ContenedorPrincipal_3)
        self.IniciarGrabacion_3.setObjectName(u"IniciarGrabacion_3")
        self.IniciarGrabacion_3.setGeometry(QRect(240, 200, 161, 24))
        self.IniciarGrabacion_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #5DF890; /* Color de fondo verde */\n"
"    border: 2px solid #5DF890; /* Borde verde oscuro */\n"
"	font-family: \"Montserrat\";\n"
"    color: D8D8D8; /* Color de texto blanco */\n"
"}\n"
"\n"
"")
        self.Duracion_4 = QLabel(self.ContenedorPrincipal_3)
        self.Duracion_4.setObjectName(u"Duracion_4")
        self.Duracion_4.setGeometry(QRect(220, 30, 101, 21))
        self.Duracion_4.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 20px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.SegundosGrabacion_4 = QLabel(self.ContenedorPrincipal_3)
        self.SegundosGrabacion_4.setObjectName(u"SegundosGrabacion_4")
        self.SegundosGrabacion_4.setGeometry(QRect(330, 30, 301, 21))
        self.SegundosGrabacion_4.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 14px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.Duracion_5 = QLabel(self.ContenedorPrincipal_3)
        self.Duracion_5.setObjectName(u"Duracion_5")
        self.Duracion_5.setGeometry(QRect(220, 70, 181, 21))
        self.Duracion_5.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 20px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.SegundosGrabacion_5 = QLabel(self.ContenedorPrincipal_3)
        self.SegundosGrabacion_5.setObjectName(u"SegundosGrabacion_5")
        self.SegundosGrabacion_5.setGeometry(QRect(430, 70, 201, 21))
        self.SegundosGrabacion_5.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 14px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.IniciarGrabacion_4 = QPushButton(self.ContenedorPrincipal_3)
        self.IniciarGrabacion_4.setObjectName(u"IniciarGrabacion_4")
        self.IniciarGrabacion_4.setGeometry(QRect(430, 200, 161, 24))
        self.IniciarGrabacion_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #5DF890; /* Color de fondo verde */\n"
"    border: 2px solid #5DF890; /* Borde verde oscuro */\n"
"	font-family: \"Montserrat\";\n"
"    color: D8D8D8; /* Color de texto blanco */\n"
"}\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TituloPantalla_2.setText(QCoreApplication.translate("MainWindow", u"\u00a1AJUSTA TU CREACI\u00d3N!", None))
        self.Duracion_3.setText(QCoreApplication.translate("MainWindow", u"Recorte:", None))
        self.SegundosGrabacion_3.setText("")
        self.IniciarGrabacion_3.setText(QCoreApplication.translate("MainWindow", u"RECORTAR Y GUARDAR", None))
        self.Duracion_4.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.SegundosGrabacion_4.setText("")
        self.Duracion_5.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n actual:", None))
        self.SegundosGrabacion_5.setText("")
        self.IniciarGrabacion_4.setText(QCoreApplication.translate("MainWindow", u"RECORTAR Y CARGAR", None))
    # retranslateUi

