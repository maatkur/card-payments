# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_payments_conciliation.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDateEdit,
    QFrame, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 729)
        icon = QIcon()
        icon.addFile(f"{getenv('ICONS_PATH')}pagamento-com-cartao-de-credito.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.frame_2.setStyleSheet(u"background-color: rgb( 240, 240, 240);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.conciliation_initial_date = QDateEdit(self.frame_2)
        self.conciliation_initial_date.setObjectName(u"conciliation_initial_date")
        self.conciliation_initial_date.setGeometry(QRect(60, 25, 91, 22))
        font = QFont()
        font.setPointSize(10)
        self.conciliation_initial_date.setFont(font)
        self.conciliation_initial_date.setCalendarPopup(True)
        self.conciliation_search_button = QPushButton(self.frame_2)
        self.conciliation_search_button.setObjectName(u"conciliation_search_button")
        self.conciliation_search_button.setGeometry(QRect(320, 23, 80, 25))
        icon1 = QIcon()
        icon1.addFile(f"{getenv('ICONS_PATH')}icons8-pesquisar-60.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.conciliation_search_button.setIcon(icon1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 341, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.clear_button = QPushButton(self.frame_2)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(408, 23, 85, 25))
        icon2 = QIcon()
        icon2.addFile(f"{getenv('ICONS_PATH')}filtro-limpo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon2)
        self.conciliate_button = QPushButton(self.frame_2)
        self.conciliate_button.setObjectName(u"conciliate_button")
        self.conciliate_button.setGeometry(QRect(499, 23, 161, 25))
        icon3 = QIcon()
        icon3.addFile(f"{getenv('ICONS_PATH')}acordo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.conciliate_button.setIcon(icon3)
        self.conciliate_button.setIconSize(QSize(20, 20))
        self.conciliation_final_date = QDateEdit(self.frame_2)
        self.conciliation_final_date.setObjectName(u"conciliation_final_date")
        self.conciliation_final_date.setGeometry(QRect(200, 25, 91, 22))
        self.conciliation_final_date.setCalendarPopup(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 49, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 30, 36, 16))
        self.label_4.setFont(font2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 364, 1249, 351))
        self.frame_3.setStyleSheet(u"background-color: rgb( 240, 240, 240);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.unconciliated_initial_date = QDateEdit(self.frame_3)
        self.unconciliated_initial_date.setObjectName(u"unconciliated_initial_date")
        self.unconciliated_initial_date.setGeometry(QRect(60, 22, 91, 22))
        self.unconciliated_initial_date.setFont(font)
        self.unconciliated_initial_date.setCalendarPopup(True)
        self.unconciliated_final_date = QDateEdit(self.frame_3)
        self.unconciliated_final_date.setObjectName(u"unconciliated_final_date")
        self.unconciliated_final_date.setGeometry(QRect(200, 22, 91, 22))
        self.unconciliated_final_date.setFont(font)
        self.unconciliated_final_date.setCalendarPopup(True)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -2, 301, 21))
        self.label.setFont(font1)
        self.unconciliated_search_button = QPushButton(self.frame_3)
        self.unconciliated_search_button.setObjectName(u"unconciliated_search_button")
        self.unconciliated_search_button.setGeometry(QRect(320, 20, 80, 25))
        self.unconciliated_search_button.setIcon(icon1)
        self.unconciliated_tab = QTabWidget(self.frame_3)
        self.unconciliated_tab.setObjectName(u"unconciliated_tab")
        self.unconciliated_tab.setGeometry(QRect(0, 50, 991, 291))
        font3 = QFont()
        font3.setBold(True)
        self.unconciliated_tab.setFont(font3)
        self.unconciliated_tab.setTabPosition(QTabWidget.South)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.unconciliated_table = QTableWidget(self.tab_4)
        if (self.unconciliated_table.columnCount() < 12):
            self.unconciliated_table.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font3);
        self.unconciliated_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.unconciliated_table.setObjectName(u"unconciliated_table")
        self.unconciliated_table.setGeometry(QRect(0, 0, 981, 261))
        self.unconciliated_table.setStyleSheet(u"background-color: rgb(254, 255, 197);")
        self.unconciliated_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.unconciliated_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.unconciliated_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.total_conciliation_label_2 = QLabel(self.tab_4)
        self.total_conciliation_label_2.setObjectName(u"total_conciliation_label_2")
        self.total_conciliation_label_2.setGeometry(QRect(320, 270, 201, 20))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.total_conciliation_label_2.setFont(font4)
        self.unconciliated_tab.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.old_unconciliated_table = QTableWidget(self.tab_5)
        if (self.old_unconciliated_table.columnCount() < 7):
            self.old_unconciliated_table.setColumnCount(7)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font3);
        self.old_unconciliated_table.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        self.old_unconciliated_table.setObjectName(u"old_unconciliated_table")
        self.old_unconciliated_table.setGeometry(QRect(0, 0, 621, 261))
        self.old_unconciliated_table.setStyleSheet(u"background-color: rgb(254, 255, 197);")
        self.old_unconciliated_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.unconciliated_tab.addTab(self.tab_5, "")
        self.total_unconciliated_label = QLabel(self.frame_3)
        self.total_unconciliated_label.setObjectName(u"total_unconciliated_label")
        self.total_unconciliated_label.setGeometry(QRect(740, 318, 241, 20))
        self.total_unconciliated_label.setFont(font4)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 28, 49, 16))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 28, 36, 16))
        self.label_6.setFont(font2)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 67, 1249, 301))
        self.frame_4.setStyleSheet(u"background-color: rgb( 240, 240, 240);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.conciliation_tab = QTabWidget(self.frame_4)
        self.conciliation_tab.setObjectName(u"conciliation_tab")
        self.conciliation_tab.setGeometry(QRect(0, 0, 991, 291))
        self.conciliation_tab.setFont(font3)
        self.conciliation_tab.setTabPosition(QTabWidget.South)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.new_table = QTableWidget(self.tab)
        if (self.new_table.columnCount() < 12):
            self.new_table.setColumnCount(12)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font3);
        self.new_table.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font3);
        self.new_table.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font3);
        self.new_table.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font3);
        self.new_table.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font3);
        self.new_table.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font3);
        self.new_table.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFont(font3);
        self.new_table.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font3);
        self.new_table.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFont(font3);
        self.new_table.setHorizontalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFont(font3);
        self.new_table.setHorizontalHeaderItem(9, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFont(font3);
        self.new_table.setHorizontalHeaderItem(10, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFont(font3);
        self.new_table.setHorizontalHeaderItem(11, __qtablewidgetitem30)
        self.new_table.setObjectName(u"new_table")
        self.new_table.setGeometry(QRect(0, 0, 981, 261))
        self.new_table.setStyleSheet(u"background-color: rgb(208, 255, 169);")
        self.new_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.new_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.conciliation_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.old_table = QTableWidget(self.tab_2)
        if (self.old_table.columnCount() < 7):
            self.old_table.setColumnCount(7)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFont(font3);
        self.old_table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font3);
        self.old_table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font3);
        self.old_table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font3);
        self.old_table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font3);
        self.old_table.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font3);
        self.old_table.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem37.setFont(font3);
        self.old_table.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        self.old_table.setObjectName(u"old_table")
        self.old_table.setGeometry(QRect(0, 0, 621, 261))
        self.old_table.setStyleSheet(u"background-color: rgb(208, 255, 169);")
        self.old_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.old_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.conciliation_tab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.not_found_table = QTableWidget(self.tab_3)
        if (self.not_found_table.columnCount() < 10):
            self.not_found_table.setColumnCount(10)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem38.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem39.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem40.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem41.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem42.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem43.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem44.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem45.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(7, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem46.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(8, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem47.setFont(font3);
        self.not_found_table.setHorizontalHeaderItem(9, __qtablewidgetitem47)
        self.not_found_table.setObjectName(u"not_found_table")
        self.not_found_table.setGeometry(QRect(0, 0, 921, 261))
        self.not_found_table.setStyleSheet(u"background-color: rgb(255, 152, 154);")
        self.not_found_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.not_found_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.conciliation_tab.addTab(self.tab_3, "")
        self.total_conciliation_label = QLabel(self.frame_4)
        self.total_conciliation_label.setObjectName(u"total_conciliation_label")
        self.total_conciliation_label.setGeometry(QRect(790, 270, 201, 20))
        self.total_conciliation_label.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.unconciliated_tab.setCurrentIndex(0)
        self.conciliation_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.conciliation_search_button.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data de pagamento segundo operadora", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Nova busca", None))
        self.conciliate_button.setText(QCoreApplication.translate("MainWindow", u"Conciliar pagamentos ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Inicial:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Final:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Consultar pagamentos n\u00e3o conciliados", None))
        self.unconciliated_search_button.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
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
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem8 = self.unconciliated_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem9 = self.unconciliated_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Valor l\u00edquido", None));
        ___qtablewidgetitem10 = self.unconciliated_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem11 = self.unconciliated_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.total_conciliation_label_2.setText("")
        self.unconciliated_tab.setTabText(self.unconciliated_tab.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"N\u00e3o conciliados atuais", None))
        ___qtablewidgetitem12 = self.old_unconciliated_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem13 = self.old_unconciliated_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem14 = self.old_unconciliated_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem15 = self.old_unconciliated_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem16 = self.old_unconciliated_table.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem17 = self.old_unconciliated_table.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem18 = self.old_unconciliated_table.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.unconciliated_tab.setTabText(self.unconciliated_tab.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"N\u00e3o conciliados conex\u00e3o", None))
        self.total_unconciliated_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Inicial:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Final:", None))
        ___qtablewidgetitem19 = self.new_table.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtablewidgetitem20 = self.new_table.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem21 = self.new_table.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Bandeira", None));
        ___qtablewidgetitem22 = self.new_table.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem23 = self.new_table.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem24 = self.new_table.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem25 = self.new_table.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Data da compra", None));
        ___qtablewidgetitem26 = self.new_table.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem27 = self.new_table.horizontalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem28 = self.new_table.horizontalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Valor l\u00edquido", None));
        ___qtablewidgetitem29 = self.new_table.horizontalHeaderItem(10)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem30 = self.new_table.horizontalHeaderItem(11)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.conciliation_tab.setTabText(self.conciliation_tab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Pagamentos atuais", None))
        ___qtablewidgetitem31 = self.old_table.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem32 = self.old_table.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem33 = self.old_table.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem34 = self.old_table.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem35 = self.old_table.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem36 = self.old_table.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem37 = self.old_table.horizontalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.conciliation_tab.setTabText(self.conciliation_tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pagamentos conex\u00e3o", None))
        ___qtablewidgetitem38 = self.not_found_table.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem39 = self.not_found_table.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Bandeira", None));
        ___qtablewidgetitem40 = self.not_found_table.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Data do cr\u00e9dito pela operadora", None));
        ___qtablewidgetitem41 = self.not_found_table.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Taxa", None));
        ___qtablewidgetitem42 = self.not_found_table.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Data da compra", None));
        ___qtablewidgetitem43 = self.not_found_table.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None));
        ___qtablewidgetitem44 = self.not_found_table.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 da parcela", None));
        ___qtablewidgetitem45 = self.not_found_table.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Valor da parcela", None));
        ___qtablewidgetitem46 = self.not_found_table.horizontalHeaderItem(8)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"NSU", None));
        ___qtablewidgetitem47 = self.not_found_table.horizontalHeaderItem(9)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Autoriza\u00e7\u00e3o", None));
        self.conciliation_tab.setTabText(self.conciliation_tab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pagamentos n\u00e3o encontrados", None))
        self.total_conciliation_label.setText("")
    # retranslateUi

