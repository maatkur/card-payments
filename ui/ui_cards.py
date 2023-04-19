# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cards.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 268)
        icon = QIcon()
        icon.addFile(u"icons/pagamento-com-cartao-de-credito.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"* {\n"
"  font-family: Arial;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(325, 16777215))
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.search_order_entry = QLineEdit(self.frame_2)
        self.search_order_entry.setObjectName(u"search_order_entry")
        self.search_order_entry.setGeometry(QRect(0, 25, 100, 23))
        self.search_order_entry.setMaximumSize(QSize(100, 16777215))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 71, 16))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.search_button = QPushButton(self.frame_2)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(100, 25, 38, 23))
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-pesquisar-60.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QSize(16, 16))
        self.refresh_button = QPushButton(self.frame_2)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(150, 25, 38, 23))
        icon2 = QIcon()
        icon2.addFile(u"icons/refresh.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_button.setIcon(icon2)
        self.refresh_button.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.frame_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 15))
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.initial_date = QDateEdit(self.frame)
        self.initial_date.setObjectName(u"initial_date")
        self.initial_date.setMaximumSize(QSize(100, 20))
        self.initial_date.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.initial_date)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 15))
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.final_date = QDateEdit(self.frame)
        self.final_date.setObjectName(u"final_date")
        self.final_date.setMaximumSize(QSize(100, 20))
        self.final_date.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.final_date)

        self.excel_report_button = QPushButton(self.frame)
        self.excel_report_button.setObjectName(u"excel_report_button")
        self.excel_report_button.setFont(font)
        self.excel_report_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/excel.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.excel_report_button.setIcon(icon3)
        self.excel_report_button.setIconSize(QSize(20, 20))
        self.excel_report_button.setAutoDefault(False)
        self.excel_report_button.setFlat(False)

        self.verticalLayout.addWidget(self.excel_report_button)

        self.add_card_payment_button = QPushButton(self.frame)
        self.add_card_payment_button.setObjectName(u"add_card_payment_button")
        self.add_card_payment_button.setFont(font)
        self.add_card_payment_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"icons/adicionar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.add_card_payment_button.setIcon(icon4)
        self.add_card_payment_button.setIconSize(QSize(20, 20))
        self.add_card_payment_button.setAutoDefault(False)
        self.add_card_payment_button.setFlat(False)

        self.verticalLayout.addWidget(self.add_card_payment_button)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.excel_report_button.setDefault(False)
        self.add_card_payment_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pedido:", None))
        self.search_button.setText("")
        self.refresh_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo para o relat\u00f3rio:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Inicial", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data Final", None))
        self.excel_report_button.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.add_card_payment_button.setText(QCoreApplication.translate("MainWindow", u"Adicionar Pagamento ", None))
    # retranslateUi
