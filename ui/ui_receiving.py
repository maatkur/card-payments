# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_receiving.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from os import getenv
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 600)
        MainWindow.setStyleSheet(u"background-color: rgb( 240, 240, 240);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 1101, 91))
        self.frame_2.setStyleSheet(u"background-color: rgb( 240, 240, 240);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 22))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 47, 49, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 47, 41, 16))
        self.label_3.setFont(font1)
        self.initial_date = QDateEdit(self.frame_2)
        self.initial_date.setObjectName(u"initial_date")
        self.initial_date.setGeometry(QRect(60, 40, 91, 22))
        self.initial_date.setCalendarPopup(True)
        self.final_date = QDateEdit(self.frame_2)
        self.final_date.setObjectName(u"final_date")
        self.final_date.setGeometry(QRect(200, 40, 91, 22))
        self.final_date.setCalendarPopup(True)
        self.update_button = QPushButton(self.frame_2)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(400, 38, 121, 25))
        icon = QIcon()
        icon.addFile(f"{getenv('ICONS_PATH')}refresh.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.update_button.setIcon(icon)
        self.excel_button = QPushButton(self.frame_2)
        self.excel_button.setObjectName(u"excel_button")
        self.excel_button.setGeometry(QRect(623, 38, 80, 25))
        self.search_button = QPushButton(self.frame_2)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(310, 38, 80, 25))
        icon1 = QIcon()
        icon1.addFile(f"{getenv('ICONS_PATH')}icons8-pesquisar-60.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon1)
        self.clear_button = QPushButton(self.frame_2)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(530, 38, 85, 25))
        icon2 = QIcon()
        icon2.addFile(f"{getenv('ICONS_PATH')}filtro-limpo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon2)
        self.status_combo_box = QComboBox(self.frame_2)
        self.status_combo_box.addItem("")
        self.status_combo_box.addItem("")
        self.status_combo_box.addItem("")
        self.status_combo_box.addItem("")
        self.status_combo_box.setObjectName(u"status_combo_box")
        self.status_combo_box.setGeometry(QRect(720, 40, 111, 22))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(720, 20, 49, 16))
        font2 = QFont()
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 111, 1121, 461))
        self.frame_3.setStyleSheet(u"background-color: rgb( 240, 240, 240);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(3, 3, 1117, 455))
        self.tabWidget.setFont(font2)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.new_table = QTableWidget(self.tab)
        if (self.new_table.columnCount() < 13):
            self.new_table.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        self.new_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.new_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font2);
        self.new_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        self.new_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font2);
        self.new_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font2);
        self.new_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font2);
        self.new_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font2);
        self.new_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font2);
        self.new_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font2);
        self.new_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font2);
        self.new_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font2);
        self.new_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font2);
        self.new_table.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.new_table.setObjectName(u"new_table")
        self.new_table.setGeometry(QRect(5, 5, 1105, 418))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.old_table = QTableWidget(self.tab_2)
        if (self.old_table.columnCount() < 8):
            self.old_table.setColumnCount(8)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font2);
        self.old_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font2);
        self.old_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font2);
        self.old_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font2);
        self.old_table.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font2);
        self.old_table.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font2);
        self.old_table.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font2);
        self.old_table.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font2);
        self.old_table.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        self.old_table.setObjectName(u"old_table")
        self.old_table.setGeometry(QRect(5, 5, 742, 418))
        self.tabWidget.addTab(self.tab_2, "")
        self.total_label = QLabel(self.frame)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setGeometry(QRect(560, 548, 211, 16))
        self.total_label.setFont(font2)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data de recebimento dos pagamentos:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inicial:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Final:", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Atualizar status", None))
        self.excel_button.setText(QCoreApplication.translate("MainWindow", u"Gerar excel", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Nova busca", None))
        self.status_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.status_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Agendado", None))
        self.status_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Pago", None))
        self.status_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Enviado Banco", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        ___qtablewidgetitem = self.new_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtablewidgetitem1 = self.new_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.new_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bandeira", None));
        ___qtablewidgetitem3 = self.new_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem4 = self.new_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem5 = self.new_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem6 = self.new_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data da compra", None));
        ___qtablewidgetitem7 = self.new_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem8 = self.new_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem9 = self.new_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Valor l\u00edquido", None));
        ___qtablewidgetitem10 = self.new_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem11 = self.new_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        ___qtablewidgetitem12 = self.new_table.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Status do recebimento", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Pagamentos atuais", None))
        ___qtablewidgetitem13 = self.old_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem14 = self.old_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem15 = self.old_table.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem16 = self.old_table.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem17 = self.old_table.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem18 = self.old_table.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem19 = self.old_table.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        ___qtablewidgetitem20 = self.old_table.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Status do recebimento", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pagamentos conex\u00e3o", None))
        self.total_label.setText("")
    # retranslateUi

