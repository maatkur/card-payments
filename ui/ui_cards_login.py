# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cards_login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon,
                           QPixmap)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(454, 467)
        icon = QIcon()
        icon.addFile(u"../icons/pagamento-com-cartao-de-credito.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"* {\n"
"	background: #222222;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 436, 171))
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(100, 100))
        self.frame.setStyleSheet(u"background-color:#222222;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(136, 40, 161, 101))
        self.label.setPixmap(QPixmap(f"{os.getenv('LOGO_URL')}"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 149, 436, 271))
        self.frame_2.setStyleSheet(u"background-color:#222222;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.user_entry = QLineEdit(self.frame_2)
        self.user_entry.setObjectName(u"user_entry")
        self.user_entry.setGeometry(QRect(150, 50, 140, 25))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setStrikeOut(False)
        self.user_entry.setFont(font)
        self.user_entry.setAutoFillBackground(False)
        self.user_entry.setStyleSheet(u"border-color:#ea3d2f;\n"
"padding: 20px;\n"
"color: #ffffff;")
        self.user_entry.setMaxLength(3)
        self.user_entry.setFrame(True)
        self.user_entry.setCursorPosition(0)
        self.user_entry.setAlignment(Qt.AlignCenter)
        self.password_entry = QLineEdit(self.frame_2)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setGeometry(QRect(150, 100, 140, 25))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.password_entry.setFont(font1)
        self.password_entry.setStyleSheet(u"color: #ffffff;")
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setAlignment(Qt.AlignCenter)
        self.login_button = QPushButton(self.frame_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(180, 150, 75, 24))
        self.login_button.setFont(font1)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	background-color:#ffffff;\n"
"	color: #222222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb( 115,115, 115);\n"
"}\n"
"")
        self.login_button.setFlat(False)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(9, 430, 436, 31))
        self.frame_3.setStyleSheet(u"background-color:#222222;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.MKOTECH = QLabel(self.frame_3)
        self.MKOTECH.setObjectName(u"MKOTECH")
        self.MKOTECH.setGeometry(QRect(0, 10, 111, 16))
        font2 = QFont()
        font2.setBold(True)
        self.MKOTECH.setFont(font2)
        self.MKOTECH.setCursor(QCursor(Qt.UpArrowCursor))
        self.MKOTECH.setStyleSheet(u"color: #ffffff;")
        self.user_name = QLabel(self.frame_3)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(290, 10, 141, 20))
        font3 = QFont()
        font3.setPointSize(11)
        self.user_name.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.user_entry.setText("")
        self.user_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.MKOTECH.setText(QCoreApplication.translate("MainWindow", u"\u00a9MKOTECH", None))
        self.user_name.setText("")
    # retranslateUi

