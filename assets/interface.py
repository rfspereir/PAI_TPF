# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageLayout = QHBoxLayout()
        self.imageLayout.setObjectName(u"imageLayout")
        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelImagemOriginalTitulo = QLabel(self.centralwidget)
        self.labelImagemOriginalTitulo.setObjectName(u"labelImagemOriginalTitulo")
        self.labelImagemOriginalTitulo.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.labelImagemOriginalTitulo)

        self.labelImagemOriginal = QLabel(self.centralwidget)
        self.labelImagemOriginal.setObjectName(u"labelImagemOriginal")
        self.labelImagemOriginal.setMinimumSize(QSize(350, 300))
        self.labelImagemOriginal.setFrameShape(QFrame.Box)
        self.labelImagemOriginal.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.labelImagemOriginal)


        self.imageLayout.addLayout(self.vboxLayout)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.labelImagemProcessadaTitulo = QLabel(self.centralwidget)
        self.labelImagemProcessadaTitulo.setObjectName(u"labelImagemProcessadaTitulo")
        self.labelImagemProcessadaTitulo.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.labelImagemProcessadaTitulo)

        self.labelImagemProcessada = QLabel(self.centralwidget)
        self.labelImagemProcessada.setObjectName(u"labelImagemProcessada")
        self.labelImagemProcessada.setMinimumSize(QSize(350, 300))
        self.labelImagemProcessada.setFrameShape(QFrame.Box)
        self.labelImagemProcessada.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.labelImagemProcessada)


        self.imageLayout.addLayout(self.vboxLayout1)


        self.verticalLayout.addLayout(self.imageLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnCarregarImagem = QPushButton(self.centralwidget)
        self.btnCarregarImagem.setObjectName(u"btnCarregarImagem")

        self.buttonLayout.addWidget(self.btnCarregarImagem)

        self.btnProcessar = QPushButton(self.centralwidget)
        self.btnProcessar.setObjectName(u"btnProcessar")

        self.buttonLayout.addWidget(self.btnProcessar)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.labelResultado = QLabel(self.centralwidget)
        self.labelResultado.setObjectName(u"labelResultado")
        self.labelResultado.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelResultado)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Classificador de Fissuras - Rafael Felipe", None))
        self.labelImagemOriginalTitulo.setText(QCoreApplication.translate("MainWindow", u"Imagem Original", None))
        self.labelImagemOriginal.setText(QCoreApplication.translate("MainWindow", u"Imagem Original", None))
        self.labelImagemProcessadaTitulo.setText(QCoreApplication.translate("MainWindow", u"Imagem com Detec\u00e7\u00e3o", None))
        self.labelImagemProcessada.setText(QCoreApplication.translate("MainWindow", u"Imagem com Detec\u00e7\u00e3o", None))
        self.btnCarregarImagem.setText(QCoreApplication.translate("MainWindow", u"Carregar Imagem", None))
        self.btnProcessar.setText(QCoreApplication.translate("MainWindow", u"Processar", None))
        self.labelResultado.setText(QCoreApplication.translate("MainWindow", u"Resultado: (Aguardando imagem)", None))
        self.labelResultado.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-weight: bold; font-size: 14px;", None))
    # retranslateUi

