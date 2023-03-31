# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_card_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(787, 475)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 769, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.initial_date = QDateEdit(self.frame)
        self.initial_date.setObjectName(u"initial_date")
        self.initial_date.setGeometry(QRect(10, 60, 110, 22))
        self.initial_date.setCalendarPopup(True)
        self.final_date = QDateEdit(self.frame)
        self.final_date.setObjectName(u"final_date")
        self.final_date.setGeometry(QRect(140, 60, 110, 22))
        self.final_date.setCalendarPopup(True)
        self.order_entry = QLineEdit(self.frame)
        self.order_entry.setObjectName(u"order_entry")
        self.order_entry.setGeometry(QRect(270, 60, 113, 22))
        self.nsu_authorization_entry = QLineEdit(self.frame)
        self.nsu_authorization_entry.setObjectName(u"nsu_authorization_entry")
        self.nsu_authorization_entry.setGeometry(QRect(400, 60, 113, 22))
        self.search_button = QPushButton(self.frame)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(680, 30, 75, 61))
        icon = QIcon()
        icon.addFile(u"icons/icons8-pesquisar-60.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QSize(40, 60))
        self.by_date_radioButton = QRadioButton(self.frame)
        self.by_date_radioButton.setObjectName(u"by_date_radioButton")
        self.by_date_radioButton.setGeometry(QRect(10, 30, 111, 20))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.by_date_radioButton.setFont(font)
        self.by_order_radioButton = QRadioButton(self.frame)
        self.by_order_radioButton.setObjectName(u"by_order_radioButton")
        self.by_order_radioButton.setGeometry(QRect(270, 30, 101, 20))
        self.by_order_radioButton.setFont(font)
        self.by_nsu_authorization_radioButton = QRadioButton(self.frame)
        self.by_nsu_authorization_radioButton.setObjectName(u"by_nsu_authorization_radioButton")
        self.by_nsu_authorization_radioButton.setGeometry(QRect(400, 30, 89, 20))
        self.by_nsu_authorization_radioButton.setFont(font)
        self.by_store_radioButton = QRadioButton(self.frame)
        self.by_store_radioButton.setObjectName(u"by_store_radioButton")
        self.by_store_radioButton.setGeometry(QRect(530, 30, 131, 20))
        self.by_store_radioButton.setFont(font)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 351, 21))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(530, 60, 120, 22))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 321, 769, 145))
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.cashier_view = QLineEdit(self.frame_2)
        self.cashier_view.setObjectName(u"cashier_view")
        self.cashier_view.setGeometry(QRect(10, 70, 113, 22))
        self.order_view = QLineEdit(self.frame_2)
        self.order_view.setObjectName(u"order_view")
        self.order_view.setGeometry(QRect(10, 20, 113, 22))
        self.order_view.setReadOnly(True)
        self.transaction_view = QLineEdit(self.frame_2)
        self.transaction_view.setObjectName(u"transaction_view")
        self.transaction_view.setGeometry(QRect(250, 70, 113, 22))
        self.nsu_view = QLineEdit(self.frame_2)
        self.nsu_view.setObjectName(u"nsu_view")
        self.nsu_view.setGeometry(QRect(380, 70, 113, 22))
        self.value_view = QLineEdit(self.frame_2)
        self.value_view.setObjectName(u"value_view")
        self.value_view.setGeometry(QRect(130, 20, 113, 22))
        self.value_view.setReadOnly(True)
        self.cash_flow_view = QLineEdit(self.frame_2)
        self.cash_flow_view.setObjectName(u"cash_flow_view")
        self.cash_flow_view.setGeometry(QRect(130, 70, 113, 22))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 49, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 49, 16))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 50, 81, 16))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 50, 131, 16))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 0, 49, 16))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(380, 50, 49, 16))
        self.authorization_view = QLineEdit(self.frame_2)
        self.authorization_view.setObjectName(u"authorization_view")
        self.authorization_view.setGeometry(QRect(500, 70, 113, 22))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(500, 50, 91, 16))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(630, 50, 81, 16))
        self.flags_comboBox = QComboBox(self.frame_2)
        self.flags_comboBox.addItem("")
        self.flags_comboBox.setObjectName(u"flags_comboBox")
        self.flags_comboBox.setGeometry(QRect(630, 70, 121, 22))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.flags_comboBox.setFont(font2)
        self.save_button = QPushButton(self.frame_2)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(230, 110, 181, 24))
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-salvar-96.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon1)
        self.save_button.setIconSize(QSize(30, 22))
        self.delete_button = QPushButton(self.frame_2)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(630, 20, 121, 24))
        icon2 = QIcon()
        icon2.addFile(u"icons/delete.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon2)
        self.excel_button = QPushButton(self.frame_2)
        self.excel_button.setObjectName(u"excel_button")
        self.excel_button.setGeometry(QRect(420, 110, 121, 24))
        icon3 = QIcon()
        icon3.addFile(u"icons/excel.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.excel_button.setIcon(icon3)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(9, 115, 769, 200))
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 200))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_button.setText("")
        self.by_date_radioButton.setText(QCoreApplication.translate("Form", u"Por Per\u00edodo", None))
        self.by_order_radioButton.setText(QCoreApplication.translate("Form", u"Por pedido", None))
        self.by_nsu_authorization_radioButton.setText(QCoreApplication.translate("Form", u"Por NSU", None))
        self.by_store_radioButton.setText(QCoreApplication.translate("Form", u"Por Loja", None))
        self.label.setText(QCoreApplication.translate("Form", u"Selecione o tipo de filtro para a busca:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Todas", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Pedido", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Caixa", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Movimento", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Transa\u00e7\u00e3o", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Valor", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"NSU", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Autoriza\u00e7\u00e3o", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Bandeira", None))
        self.flags_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Selecione", None))

        self.save_button.setText(QCoreApplication.translate("Form", u"Salvar altera\u00e7\u00f5es", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Deletar", None))
        self.excel_button.setText(QCoreApplication.translate("Form", u"Excel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Pedido", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Caixa", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Movimento", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Bandeira", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Valor", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Data", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Unidade", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"NSU", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Autoriza\u00e7\u00e3o", None));
    # retranslateUi

