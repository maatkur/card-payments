# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDateEdit,
    QFrame, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1261, 729)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 1269, 711))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 1249, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.excel_initial_date = QDateEdit(self.frame_2)
        self.excel_initial_date.setObjectName(u"excel_initial_date")
        self.excel_initial_date.setGeometry(QRect(0, 30, 91, 22))
        font = QFont()
        font.setPointSize(10)
        self.excel_initial_date.setFont(font)
        self.excel_initial_date.setCalendarPopup(True)
        self.excel_search_button = QPushButton(self.frame_2)
        self.excel_search_button.setObjectName(u"excel_search_button")
        self.excel_search_button.setGeometry(QRect(100, 30, 75, 22))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 341, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 374, 1249, 341))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.unconciliated_table = QTableWidget(self.frame_3)
        if (self.unconciliated_table.columnCount() < 12):
            self.unconciliated_table.setColumnCount(12)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font2);
        self.unconciliated_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.unconciliated_table.setObjectName(u"unconciliated_table")
        self.unconciliated_table.setGeometry(QRect(0, 60, 1225, 261))
        self.unconciliated_table.setStyleSheet(u"background-color: rgb(254, 255, 197);")
        self.unconciliated_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.unconciliated_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.unconciliated_initial_date = QDateEdit(self.frame_3)
        self.unconciliated_initial_date.setObjectName(u"unconciliated_initial_date")
        self.unconciliated_initial_date.setGeometry(QRect(0, 30, 91, 22))
        self.unconciliated_initial_date.setFont(font)
        self.unconciliated_initial_date.setCalendarPopup(True)
        self.unconciliated_final_date = QDateEdit(self.frame_3)
        self.unconciliated_final_date.setObjectName(u"unconciliated_final_date")
        self.unconciliated_final_date.setGeometry(QRect(100, 30, 91, 22))
        self.unconciliated_final_date.setFont(font)
        self.unconciliated_final_date.setCalendarPopup(True)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 301, 21))
        self.label.setFont(font1)
        self.unconciliated_search_button = QPushButton(self.frame_3)
        self.unconciliated_search_button.setObjectName(u"unconciliated_search_button")
        self.unconciliated_search_button.setGeometry(QRect(200, 30, 75, 22))
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 67, 1249, 301))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1231, 291))
        self.tabWidget.setFont(font2)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.new_table = QTableWidget(self.tab)
        if (self.new_table.columnCount() < 12):
            self.new_table.setColumnCount(12)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font2);
        self.new_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font2);
        self.new_table.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font2);
        self.new_table.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font2);
        self.new_table.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font2);
        self.new_table.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font2);
        self.new_table.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font2);
        self.new_table.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font2);
        self.new_table.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font2);
        self.new_table.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font2);
        self.new_table.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font2);
        self.new_table.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font2);
        self.new_table.setHorizontalHeaderItem(11, __qtablewidgetitem23)
        self.new_table.setObjectName(u"new_table")
        self.new_table.setGeometry(QRect(0, 0, 1221, 261))
        self.new_table.setStyleSheet(u"background-color: rgb(208, 255, 169);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.old_table = QTableWidget(self.tab_2)
        if (self.old_table.columnCount() < 7):
            self.old_table.setColumnCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font2);
        self.old_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFont(font2);
        self.old_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font2);
        self.old_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFont(font2);
        self.old_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFont(font2);
        self.old_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFont(font2);
        self.old_table.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFont(font2);
        self.old_table.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        self.old_table.setObjectName(u"old_table")
        self.old_table.setGeometry(QRect(0, 0, 741, 261))
        self.old_table.setStyleSheet(u"background-color: rgb(208, 255, 169);")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.not_found_table = QTableWidget(self.tab_3)
        if (self.not_found_table.columnCount() < 7):
            self.not_found_table.setColumnCount(7)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem37.setFont(font2);
        self.not_found_table.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        self.not_found_table.setObjectName(u"not_found_table")
        self.not_found_table.setGeometry(QRect(0, 0, 741, 261))
        self.not_found_table.setStyleSheet(u"background-color: rgb(255, 152, 154);")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.excel_search_button.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data de pagamento segundo operadora", None))
        ___qtablewidgetitem = self.unconciliated_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtablewidgetitem1 = self.unconciliated_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.unconciliated_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bandeira", None));
        ___qtablewidgetitem3 = self.unconciliated_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem4 = self.unconciliated_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem5 = self.unconciliated_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem6 = self.unconciliated_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data da compra", None));
        ___qtablewidgetitem7 = self.unconciliated_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito", None));
        ___qtablewidgetitem8 = self.unconciliated_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem9 = self.unconciliated_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Valor l\u00edquido", None));
        ___qtablewidgetitem10 = self.unconciliated_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem11 = self.unconciliated_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Consultar pagamentos n\u00e3o conciliados", None))
        self.unconciliated_search_button.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem12 = self.new_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtablewidgetitem13 = self.new_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem14 = self.new_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Bandeira", None));
        ___qtablewidgetitem15 = self.new_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem16 = self.new_table.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem17 = self.new_table.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem18 = self.new_table.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Data da compra", None));
        ___qtablewidgetitem19 = self.new_table.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito", None));
        ___qtablewidgetitem20 = self.new_table.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem21 = self.new_table.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Valor l\u00edquido", None));
        ___qtablewidgetitem22 = self.new_table.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem23 = self.new_table.horizontalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Pagamentos atuais", None))
        ___qtablewidgetitem24 = self.old_table.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito", None));
        ___qtablewidgetitem25 = self.old_table.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem26 = self.old_table.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem27 = self.old_table.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem28 = self.old_table.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem29 = self.old_table.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem30 = self.old_table.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pagamentos conex\u00e3o", None))
        ___qtablewidgetitem31 = self.not_found_table.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito", None));
        ___qtablewidgetitem32 = self.not_found_table.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem33 = self.not_found_table.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem34 = self.not_found_table.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem35 = self.not_found_table.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem36 = self.not_found_table.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem37 = self.not_found_table.horizontalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pagamentos n\u00e3o encontrados", None))
    # retranslateUi

