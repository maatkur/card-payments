# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_quick_management.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(310, 114)
        icon = QIcon()
        icon.addFile(u"../icons/pagamento-com-cartao-de-credito.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 291, 96))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nsu_edit = QLineEdit(self.frame)
        self.nsu_edit.setObjectName(u"nsu_edit")
        self.nsu_edit.setGeometry(QRect(20, 30, 113, 21))
        self.authorization_edit = QLineEdit(self.frame)
        self.authorization_edit.setObjectName(u"authorization_edit")
        self.authorization_edit.setGeometry(QRect(160, 30, 113, 21))
        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(110, 60, 75, 24))
        font = QFont()
        font.setBold(True)
        self.save_button.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../icons/icons8-salvar-96.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 49, 16))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 10, 101, 16))
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NSU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None))
    # retranslateUi

