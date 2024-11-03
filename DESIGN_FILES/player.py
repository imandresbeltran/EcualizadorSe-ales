# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EQ.ui'
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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ContenedorPrincipal_4 = QFrame(self.centralwidget)
        self.ContenedorPrincipal_4.setObjectName(u"ContenedorPrincipal_4")
        self.ContenedorPrincipal_4.setGeometry(QRect(-50, -20, 921, 641))
        self.ContenedorPrincipal_4.setStyleSheet(u"QFrame{\n"
"	background-color: #113E53;\n"
"}")
        self.ContenedorPrincipal_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContenedorPrincipal_4.setFrameShadow(QFrame.Shadow.Raised)
        self.ContenedorEncabezado_3 = QFrame(self.ContenedorPrincipal_4)
        self.ContenedorEncabezado_3.setObjectName(u"ContenedorEncabezado_3")
        self.ContenedorEncabezado_3.setGeometry(QRect(50, 439, 841, 161))
        self.ContenedorEncabezado_3.setStyleSheet(u"QFrame {\n"
"	background-color: #112C39;\n"
"	width: 711px;\n"
"	height: 89px;\n"
"}")
        self.ContenedorEncabezado_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContenedorEncabezado_3.setFrameShadow(QFrame.Shadow.Raised)
        self.ContadorTiempo = QSlider(self.ContenedorEncabezado_3)
        self.ContadorTiempo.setObjectName(u"ContadorTiempo")
        self.ContadorTiempo.setGeometry(QRect(40, 50, 501, 22))
        self.ContadorTiempo.setStyleSheet(u"QSlider::groove:horizontal{\n"
"\n"
"height: 10px;\n"
"width: 460px;\n"
"background: #D9D9D9;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"background: #5DF890;\n"
"width: 20px;\n"
"height: 20px;\n"
"margin: -7px -7px;\n"
"border-radius: 10px;\n"
"}")
        self.ContadorTiempo.setOrientation(Qt.Orientation.Horizontal)
        self.pushButton_Seek_Backward = QPushButton(self.ContenedorEncabezado_3)
        self.pushButton_Seek_Backward.setObjectName(u"pushButton_Seek_Backward")
        self.pushButton_Seek_Backward.setGeometry(QRect(130, 80, 50, 50))
        self.pushButton_Seek_Backward.setStyleSheet(u"QPushButton{\n"
"\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #5DF890;\n"
"color: #5DF890;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 50px;\n"
"max-height: 50px;\n"
"padding: 0px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.pushButton_Seek_Backward.setIcon(icon)
        self.pushButton_Stop = QPushButton(self.ContenedorEncabezado_3)
        self.pushButton_Stop.setObjectName(u"pushButton_Stop")
        self.pushButton_Stop.setGeometry(QRect(200, 80, 50, 50))
        self.pushButton_Stop.setStyleSheet(u"QPushButton{\n"
"\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #5DF890;\n"
"color: #5DF890;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 50px;\n"
"max-height: 50px;\n"
"padding: 0px;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.pushButton_Stop.setIcon(icon1)
        self.pushButton_Play = QPushButton(self.ContenedorEncabezado_3)
        self.pushButton_Play.setObjectName(u"pushButton_Play")
        self.pushButton_Play.setGeometry(QRect(270, 80, 50, 50))
        self.pushButton_Play.setStyleSheet(u"QPushButton{\n"
"\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #D9D9D9;\n"
"color: #D9D9D9;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 50px;\n"
"max-height: 50px;\n"
"padding: 0px;\n"
"}")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.pushButton_Play.setIcon(icon2)
        self.pushButton_Play.setCheckable(False)
        self.pushButton_Pause = QPushButton(self.ContenedorEncabezado_3)
        self.pushButton_Pause.setObjectName(u"pushButton_Pause")
        self.pushButton_Pause.setGeometry(QRect(340, 80, 50, 50))
        self.pushButton_Pause.setStyleSheet(u"QPushButton{\n"
"\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #5DF890;\n"
"color: #5DF890;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 50px;\n"
"max-height: 50px;\n"
"padding: 0px;\n"
"}")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.pushButton_Pause.setIcon(icon3)
        self.pushButton_Seek_Forward = QPushButton(self.ContenedorEncabezado_3)
        self.pushButton_Seek_Forward.setObjectName(u"pushButton_Seek_Forward")
        self.pushButton_Seek_Forward.setGeometry(QRect(410, 80, 50, 50))
        self.pushButton_Seek_Forward.setStyleSheet(u"QPushButton{\n"
"\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #5DF890;\n"
"color: #5DF890;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 50px;\n"
"max-height: 50px;\n"
"padding: 0px;\n"
"}")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.pushButton_Seek_Forward.setIcon(icon4)
        self.ContadorTiempo_2 = QSlider(self.ContenedorEncabezado_3)
        self.ContadorTiempo_2.setObjectName(u"ContadorTiempo_2")
        self.ContadorTiempo_2.setGeometry(QRect(670, 110, 121, 22))
        self.ContadorTiempo_2.setStyleSheet(u"QSlider::groove:horizontal{\n"
"\n"
"height: 10px;\n"
"width: 100px;\n"
"background: #D9D9D9;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"background: #5DF890;\n"
"width: 20px;\n"
"height: 20px;\n"
"margin: -7px -7px;\n"
"border-radius: 10px;\n"
"}")
        self.ContadorTiempo_2.setOrientation(Qt.Orientation.Horizontal)
        self.pushButton_Volume = QPushButton(self.ContenedorEncabezado_3)
        self.pushButton_Volume.setObjectName(u"pushButton_Volume")
        self.pushButton_Volume.setGeometry(QRect(630, 110, 30, 30))
        self.pushButton_Volume.setStyleSheet(u"QPushButton{\n"
"\n"
"border: none;\n"
"border-radius: 15px;\n"
"background-color: #5DF890;\n"
"color: #5DF890;\n"
"min-width: 30px;\n"
"max-width: 30px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"padding: 0px;\n"
"}")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioVolumeHigh))
        self.pushButton_Volume.setIcon(icon5)
        self.Label_Start = QLabel(self.ContenedorEncabezado_3)
        self.Label_Start.setObjectName(u"Label_Start")
        self.Label_Start.setGeometry(QRect(40, 80, 49, 16))
        font = QFont()
        font.setBold(True)
        self.Label_Start.setFont(font)
        self.Label_Start_2 = QLabel(self.ContenedorEncabezado_3)
        self.Label_Start_2.setObjectName(u"Label_Start_2")
        self.Label_Start_2.setGeometry(QRect(500, 80, 49, 16))
        self.Label_Start_2.setFont(font)
        self.comboBox = QComboBox(self.ContenedorEncabezado_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(620, 40, 141, 31))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #5DF890; /* Borde del combobox */\n"
"    border-radius: 5px; /* Bordes redondeados */\n"
"    background-color: #5DF890; /* Color de fondo */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    font-size: 14px; /* Tama\u00f1o de la fuente */\n"
"    color: #FFFFFF; /* Color del texto */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none; /* Sin borde para la parte desplegable */\n"
"}\n"
"\n"
"QComboBox::arrow {\n"
"    image: url('path/to/arrow/image.png'); /* Cambiar la flecha por una imagen personalizada */\n"
"    width: 10px; /* Ancho de la flecha */\n"
"    height: 10px; /* Alto de la flecha */\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    background-color: #F0F0F0; /* Color de fondo de los elementos del men\u00fa desplegable */\n"
"    color: #333333; /* Color del texto de los elementos */\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    background-color: #4A90E2; /* Color de fondo al seleccionar un elemento */\n"
"    color: #FFFFFF; /* Color del texto al se"
                        "leccionar un elemento */\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.original_signal_widget = QWidget(self.centralwidget)
        self.original_signal_widget.setGeometry(QRect(10, 50, 450, 400))

        self.original_signal_widget.setObjectName("original_signal_widget")

        self.equalized_signal_widget = QWidget(self.centralwidget)
        self.equalized_signal_widget.setGeometry(QRect(440,50,450,400))

        self.equalized_signal_widget.setObjectName("equalized_signal_widget")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Seek_Backward.setText("")
        self.pushButton_Stop.setText("")
        self.pushButton_Play.setText("")
        self.pushButton_Pause.setText("")
        self.pushButton_Seek_Forward.setText("")
        self.pushButton_Volume.setText("")
        self.Label_Start.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.Label_Start_2.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pop", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Rock", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Jazz", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Classical", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Bass Boost", None))

    # retranslateUi

