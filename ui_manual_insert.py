# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_manual_insert.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(255, 190)
        self.cashier_entry = QLineEdit(Form)
        self.cashier_entry.setObjectName(u"cashier_entry")
        self.cashier_entry.setGeometry(QRect(119, 38, 127, 21))
        self.order_entry = QLineEdit(Form)
        self.order_entry.setObjectName(u"order_entry")
        self.order_entry.setGeometry(QRect(119, 10, 127, 21))
        self.order_value_entry = QLineEdit(Form)
        self.order_value_entry.setObjectName(u"order_value_entry")
        self.order_value_entry.setGeometry(QRect(119, 94, 127, 21))
        self.cashflow_entry = QLineEdit(Form)
        self.cashflow_entry.setObjectName(u"cashflow_entry")
        self.cashflow_entry.setGeometry(QRect(119, 66, 127, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 10, 43, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 38, 70, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(9, 66, 104, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(9, 94, 93, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(9, 122, 81, 16))
        self.label_5.setFont(font)
        self.save_button = QPushButton(Form)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(96, 152, 75, 24))
        self.save_button.setFont(font)
        self.order_date = QDateEdit(Form)
        self.order_date.setObjectName(u"order_date")
        self.order_date.setGeometry(QRect(119, 122, 126, 22))
        self.order_date.setCalendarPopup(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pedido:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00b0 do Caixa:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"N\u00b0 do Movimento:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Valor do Pedido:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Data da baixa:", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"Salvar", None))
    # retranslateUi

