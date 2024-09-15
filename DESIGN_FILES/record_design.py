# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordoptions.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_RecordOptions(object):
    def setupUi(self, RecordOptions):
        if not RecordOptions.objectName():
            RecordOptions.setObjectName(u"RecordOptions")
        RecordOptions.resize(800, 600)
        RecordOptions.setStyleSheet(u"QMainWindow{\n"
"	background-color: #112C39;\n"
"}")
        self.centralwidget = QWidget(RecordOptions)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ContenedorEncabezado = QFrame(self.centralwidget)
        self.ContenedorEncabezado.setObjectName(u"ContenedorEncabezado")
        self.ContenedorEncabezado.setGeometry(QRect(0, 0, 811, 80))
        self.ContenedorEncabezado.setStyleSheet(u"QFrame {\n"
"	background-color: #112C39;\n"
"	width: 711px;\n"
"	height: 89px;\n"
"}")
        self.ContenedorEncabezado.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContenedorEncabezado.setFrameShadow(QFrame.Shadow.Raised)
        self.TituloPantalla = QLabel(self.ContenedorEncabezado)
        self.TituloPantalla.setObjectName(u"TituloPantalla")
        self.TituloPantalla.setGeometry(QRect(220, 30, 351, 21))
        self.TituloPantalla.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 24px;\n"
"	color: #5DF890;\n"
"	font-weight: bold;\n"
"}")
        self.ContenedorPrincipal = QFrame(self.centralwidget)
        self.ContenedorPrincipal.setObjectName(u"ContenedorPrincipal")
        self.ContenedorPrincipal.setGeometry(QRect(0, 80, 811, 501))
        self.ContenedorPrincipal.setStyleSheet(u"QFrame{\n"
"	background-color: #113E53;\n"
"}")
        self.ContenedorPrincipal.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContenedorPrincipal.setFrameShadow(QFrame.Shadow.Raised)
        self.Duracion = QLabel(self.ContenedorPrincipal)
        self.Duracion.setObjectName(u"Duracion")
        self.Duracion.setGeometry(QRect(180, 70, 151, 21))
        self.Duracion.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 20px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.TiempoGrabacion = QSlider(self.ContenedorPrincipal)
        self.TiempoGrabacion.setObjectName(u"TiempoGrabacion")
        self.TiempoGrabacion.setGeometry(QRect(360, 70, 221, 22))
        self.TiempoGrabacion.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.TiempoGrabacion.setMinimum(10)
        self.TiempoGrabacion.setMaximum(40)
        self.TiempoGrabacion.setOrientation(Qt.Orientation.Horizontal)
        self.SegundosGrabacion = QLabel(self.ContenedorPrincipal)
        self.SegundosGrabacion.setObjectName(u"SegundosGrabacion")
        self.SegundosGrabacion.setGeometry(QRect(620, 70, 81, 21))
        self.SegundosGrabacion.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 14px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.FormatoGrabacion = QLabel(self.ContenedorPrincipal)
        self.FormatoGrabacion.setObjectName(u"FormatoGrabacion")
        self.FormatoGrabacion.setGeometry(QRect(190, 110, 111, 21))
        self.FormatoGrabacion.setStyleSheet(u"QLabel{\n"
"	font-family: \"Montserrat\";\n"
"	font-size: 20px;\n"
"	color: #D8D8D8;\n"
"	font-weight: bold;\n"
"}")
        self.SeleccionFormatoGrabacion = QComboBox(self.ContenedorPrincipal)
        self.SeleccionFormatoGrabacion.addItem("")
        self.SeleccionFormatoGrabacion.addItem("")
        self.SeleccionFormatoGrabacion.setObjectName(u"SeleccionFormatoGrabacion")
        self.SeleccionFormatoGrabacion.setGeometry(QRect(390, 120, 141, 22))
        self.SeleccionFormatoGrabacion.setStyleSheet(u"QComboBox {\n"
"    font-family: \"Montserrat\";            /* Tipograf\u00eda */\n"
"    font-size: 14px;               /* Tama\u00f1o de la fuente */\n"
"    color: white;                  /* Color del texto */\n"
"    background-color: #112C39;     /* Color de fondo */\n"
"    border: 1px solid #112C39;     /* Borde del ComboBox */\n"
"    border-radius: 5px;            /* Bordes redondeados */\n"
"    padding: 5px;                  /* Espacio interno */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #5DF890;\n"
"    border-left-style: solid;\n"
"    background-color: #5DF890;    /* Fondo del bot\u00f3n desplegable */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-family: \"Montserrat\";            /* Tipograf\u00eda del desplegable */\n"
"    font-size: 14px;               /* Tama\u00f1o del texto del desplegable */\n"
"    color: #112C39;       "
                        "           /* Color del texto en el desplegable */\n"
"    background-color: #D8D8D8;     /* Fondo del desplegable */\n"
"    selection-background-color: #5DF890;  /* Fondo al seleccionar un elemento */\n"
"    selection-color: white;      /* Color del texto del elemento seleccionado */\n"
"    border: 1px solid #5DF890;     /* Borde del desplegable */\n"
"}\n"
"")
        self.SeleccionFormatoGrabacion.setEditable(False)
        self.IniciarGrabacion = QPushButton(self.ContenedorPrincipal)
        self.IniciarGrabacion.setObjectName(u"IniciarGrabacion")
        self.IniciarGrabacion.setGeometry(QRect(310, 200, 75, 24))
        self.IniciarGrabacion.setStyleSheet(u"QPushButton {\n"
"    background-color: #5DF890; /* Color de fondo verde */\n"
"    border: 2px solid #5DF890; /* Borde verde oscuro */\n"
"	font-family: \"Montserrat\";\n"
"    color: D8D8D8; /* Color de texto blanco */\n"
"}\n"
"\n"
"")
        RecordOptions.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(RecordOptions)
        self.statusbar.setObjectName(u"statusbar")
        RecordOptions.setStatusBar(self.statusbar)

        self.retranslateUi(RecordOptions)
        self.TiempoGrabacion.valueChanged.connect(self.SegundosGrabacion.setNum)

        QMetaObject.connectSlotsByName(RecordOptions)
    # setupUi

    def retranslateUi(self, RecordOptions):
        RecordOptions.setWindowTitle(QCoreApplication.translate("RecordOptions", u"MainWindow", None))
        self.TituloPantalla.setText(QCoreApplication.translate("RecordOptions", u"\u00a1GRABA TU OBRA DE ARTE!", None))
        self.Duracion.setText(QCoreApplication.translate("RecordOptions", u"DURACI\u00d3N (s)", None))
        self.SegundosGrabacion.setText("")
        self.FormatoGrabacion.setText(QCoreApplication.translate("RecordOptions", u"FORMATO", None))
        self.SeleccionFormatoGrabacion.setItemText(0, QCoreApplication.translate("RecordOptions", u".MP3", None))
        self.SeleccionFormatoGrabacion.setItemText(1, QCoreApplication.translate("RecordOptions", u".WAV", None))

        self.IniciarGrabacion.setText(QCoreApplication.translate("RecordOptions", u"GRABAR", None))
    # retranslateUi

