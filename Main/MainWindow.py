# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1181, 649)
        MainWindow.setMinimumSize(QSize(1040, 630))
        MainWindow.setStyleSheet(u"/* === \u0413\u041b\u041e\u0411\u0410\u041b\u042c\u041d\u042b\u0415 \u0426\u0412\u0415\u0422\u0410 === */\n"
"QWidget {\n"
"    background-color: #171a26;\n"
"	color: #E0E0E0;\n"
"	font: 900 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* === \u041b\u0415\u0412\u0410\u042f \u041f\u0410\u041d\u0415\u041b\u042c === */\n"
"QWidget#LeftSide_menu {\n"
"    background-color: #1a1e2c;\n"
"}\n"
"\n"
"/* === \u041a\u041d\u041e\u041f\u041a\u0418 \u0411\u041e\u041a\u041e\u0412\u041e\u0413\u041e \u041c\u0415\u041d\u042e === */\n"
"QWidget#LeftSide_menu QPushButton {\n"
"    background-color: #2A2D3A;\n"
"    border: 1px solid #2A2D3A;\n"
"    color: #E0E0E0;\n"
"    padding: 6px 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QWidget#LeftSide_menu QPushButton:hover {\n"
"    background-color: #3A8DFF;\n"
"}\n"
"\n"
"QWidget#LeftSide_menu QPushButton:pressed {\n"
"    background-color: #2C3E50;\n"
"    color: white;\n"
"}\n"
"\n"
"/* === \u0413\u041b\u0410\u0412\u041d\u0410\u042f \u0412\u0415\u0420\u0425\u041d\u042f\u042f \u041f\u0410\u041d"
                        "\u0415\u041b\u042c === */\n"
"QWidget#Head {\n"
"    background-color: #1a1e2c;\n"
"}\n"
"\n"
"/* === \u041a\u041d\u041e\u041f\u041a\u0418 \u0412\u0415\u0420\u0425\u041d\u0415\u0419 \u041f\u0410\u041d\u0415\u041b\u0418 === */\n"
"QWidget#Head QPushButton{\n"
"    background-color: #2A2D3A;\n"
"    color: #E0E0E0;\n"
"    border-radius: 4px;\n"
"    padding: 4px 10px;\n"
"}\n"
"QWidget#Head QPushButton:hover {\n"
"    background-color: #3A8DFF;\n"
"    color: white;\n"
"}\n"
"\n"
"QWidget#Footer {\n"
"background-color:#1a1e2c;\n"
"}\n"
"\n"
"/* === \u0422\u0410\u0411\u041b\u0418\u0426\u042b, \u0412\u0412\u041e\u0414\u042b \u0418 \u0414\u0420\u0423\u0413\u041e\u0415 === */\n"
"QLineEdit, QComboBox, QTableView {\n"
"    background-color: #1A1D2E;\n"
"    border: 1px solid #2A2D3A;\n"
"    color: #E0E0E0;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"QLineEdit:focus, QComboBox:focus {\n"
"    border: 1px solid #3A8DFF;\n"
"}\n"
"\n"
"/* === \u0412\u0421\u041f\u041e\u041c\u041e\u0413\u0410\u0422\u0415"
                        "\u041b\u042c\u041d\u042b\u0415 \u0426\u0412\u0415\u0422\u0410 === */\n"
"QLabel[status=\"positive\"] {\n"
"    color: #00C853; /* \u043f\u0440\u0438\u0431\u044b\u043b\u044c */\n"
"}\n"
"QLabel[status=\"negative\"] {\n"
"    color: #D32F2F; /* \u0443\u0431\u044b\u0442\u043e\u043a */\n"
"}\n"
"")
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setMinimumSize(QSize(1040, 624))
        self.MainWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.MainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 20, 10, 0)
        self.Head = QWidget(self.MainWidget)
        self.Head.setObjectName(u"Head")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Head.sizePolicy().hasHeightForWidth())
        self.Head.setSizePolicy(sizePolicy)
        self.Head.setMinimumSize(QSize(0, 70))
        self.Head.setMaximumSize(QSize(16777215, 70))
        self.Head.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.Head)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.Menu_button = QPushButton(self.Head)
        self.Menu_button.setObjectName(u"Menu_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Menu_button.sizePolicy().hasHeightForWidth())
        self.Menu_button.setSizePolicy(sizePolicy1)
        self.Menu_button.setMinimumSize(QSize(50, 50))
        self.Menu_button.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.Menu_button)

        self.Main_page_button = QPushButton(self.Head)
        self.Main_page_button.setObjectName(u"Main_page_button")
        self.Main_page_button.setMinimumSize(QSize(150, 50))
        self.Main_page_button.setMaximumSize(QSize(150, 150))
        self.Main_page_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.Main_page_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.Settings_button = QPushButton(self.Head)
        self.Settings_button.setObjectName(u"Settings_button")
        self.Settings_button.setMinimumSize(QSize(50, 50))
        self.Settings_button.setMaximumSize(QSize(50, 50))
        self.Settings_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.Settings_button)

        self.Mode_button = QPushButton(self.Head)
        self.Mode_button.setObjectName(u"Mode_button")
        self.Mode_button.setMinimumSize(QSize(50, 50))
        self.Mode_button.setMaximumSize(QSize(50, 50))
        self.Mode_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.Mode_button)

        self.Account_button = QPushButton(self.Head)
        self.Account_button.setObjectName(u"Account_button")
        self.Account_button.setMinimumSize(QSize(50, 50))
        self.Account_button.setMaximumSize(QSize(50, 50))
        self.Account_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.Account_button)


        self.verticalLayout.addWidget(self.Head)

        self.Body = QWidget(self.MainWidget)
        self.Body.setObjectName(u"Body")
        self.Body.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.Body)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftSide_menu = QWidget(self.Body)
        self.LeftSide_menu.setObjectName(u"LeftSide_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LeftSide_menu.sizePolicy().hasHeightForWidth())
        self.LeftSide_menu.setSizePolicy(sizePolicy2)
        self.LeftSide_menu.setMaximumSize(QSize(185, 16777215))
        self.LeftSide_menu.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.LeftSide_menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.Charts_button = QPushButton(self.LeftSide_menu)
        self.Charts_button.setObjectName(u"Charts_button")
        sizePolicy1.setHeightForWidth(self.Charts_button.sizePolicy().hasHeightForWidth())
        self.Charts_button.setSizePolicy(sizePolicy1)
        self.Charts_button.setMinimumSize(QSize(150, 50))
        self.Charts_button.setMaximumSize(QSize(120, 50))
        self.Charts_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.Charts_button)

        self.Exchanges_button = QPushButton(self.LeftSide_menu)
        self.Exchanges_button.setObjectName(u"Exchanges_button")
        self.Exchanges_button.setMinimumSize(QSize(150, 50))
        self.Exchanges_button.setMaximumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.Exchanges_button)

        self.Ai_predictions_button = QPushButton(self.LeftSide_menu)
        self.Ai_predictions_button.setObjectName(u"Ai_predictions_button")
        self.Ai_predictions_button.setMinimumSize(QSize(150, 50))
        self.Ai_predictions_button.setMaximumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.Ai_predictions_button)

        self.Arbitrage_button = QPushButton(self.LeftSide_menu)
        self.Arbitrage_button.setObjectName(u"Arbitrage_button")
        self.Arbitrage_button.setMinimumSize(QSize(150, 50))
        self.Arbitrage_button.setMaximumSize(QSize(180, 50))

        self.verticalLayout_2.addWidget(self.Arbitrage_button)

        self.WorkSpace_button = QPushButton(self.LeftSide_menu)
        self.WorkSpace_button.setObjectName(u"WorkSpace_button")
        self.WorkSpace_button.setMinimumSize(QSize(150, 50))

        self.verticalLayout_2.addWidget(self.WorkSpace_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.LeftSide_menu)

        self.Main_menu = QWidget(self.Body)
        self.Main_menu.setObjectName(u"Main_menu")
        self.Main_menu.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.Main_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.stackedWidget = QStackedWidget(self.Main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Charts_page = QWidget()
        self.Charts_page.setObjectName(u"Charts_page")
        self.gridLayout_2 = QGridLayout(self.Charts_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Charts_browser5 = QWebEngineView(self.Charts_page)
        self.Charts_browser5.setObjectName(u"Charts_browser5")
        self.Charts_browser5.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser5, 1, 2, 1, 1)

        self.Charts_browser6 = QWebEngineView(self.Charts_page)
        self.Charts_browser6.setObjectName(u"Charts_browser6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Charts_browser6.sizePolicy().hasHeightForWidth())
        self.Charts_browser6.setSizePolicy(sizePolicy3)
        self.Charts_browser6.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser6, 1, 3, 1, 1)

        self.Charts_browser1 = QWebEngineView(self.Charts_page)
        self.Charts_browser1.setObjectName(u"Charts_browser1")
        self.Charts_browser1.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser1, 0, 1, 1, 1)

        self.Charts_browser3 = QWebEngineView(self.Charts_page)
        self.Charts_browser3.setObjectName(u"Charts_browser3")
        self.Charts_browser3.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser3, 0, 3, 1, 1)

        self.Charts_browser4 = QWebEngineView(self.Charts_page)
        self.Charts_browser4.setObjectName(u"Charts_browser4")
        self.Charts_browser4.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser4, 1, 1, 1, 1)

        self.Charts_browser2 = QWebEngineView(self.Charts_page)
        self.Charts_browser2.setObjectName(u"Charts_browser2")
        self.Charts_browser2.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser2, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.Charts_page)
        self.WorkSpace_page = QWidget()
        self.WorkSpace_page.setObjectName(u"WorkSpace_page")
        self.horizontalLayout_4 = QHBoxLayout(self.WorkSpace_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget.addWidget(self.WorkSpace_page)
        self.Settings_page = QWidget()
        self.Settings_page.setObjectName(u"Settings_page")
        self.horizontalLayout_9 = QHBoxLayout(self.Settings_page)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.Settings_page)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.Settings_page)
        self.Main_page = QWidget()
        self.Main_page.setObjectName(u"Main_page")
        self.horizontalLayout_8 = QHBoxLayout(self.Main_page)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.Main_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.Main_page)
        self.Account_page = QWidget()
        self.Account_page.setObjectName(u"Account_page")
        self.horizontalLayout_5 = QHBoxLayout(self.Account_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.Account_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.stackedWidget.addWidget(self.Account_page)
        self.Ai_predictions_page = QWidget()
        self.Ai_predictions_page.setObjectName(u"Ai_predictions_page")
        self.horizontalLayout_3 = QHBoxLayout(self.Ai_predictions_page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Ai_predictions_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.Ai_predictions_page)
        self.Arbitrage_pairs_page = QWidget()
        self.Arbitrage_pairs_page.setObjectName(u"Arbitrage_pairs_page")
        self.horizontalLayout_6 = QHBoxLayout(self.Arbitrage_pairs_page)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.Arbitrage_pairs_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.Arbitrage_pairs_page)
        self.Exchenges_page = QWidget()
        self.Exchenges_page.setObjectName(u"Exchenges_page")
        self.horizontalLayout_7 = QHBoxLayout(self.Exchenges_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.Exchenges_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.Exchenges_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Main_menu)


        self.verticalLayout.addWidget(self.Body)

        self.Footer = QWidget(self.MainWidget)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 30))
        self.Footer.setMaximumSize(QSize(16777215, 60))
        self.Footer.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Footer)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Arbitrage app", None))
        self.Menu_button.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Main_page_button.setText(QCoreApplication.translate("MainWindow", u"Arbitrage app", None))
        self.Settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Mode_button.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.Account_button.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.LeftSide_menu.setProperty(u"Animation", "")
        self.Charts_button.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.Exchanges_button.setText(QCoreApplication.translate("MainWindow", u"Exchanges", None))
        self.Ai_predictions_button.setText(QCoreApplication.translate("MainWindow", u"Ai predictions", None))
        self.Arbitrage_button.setText(QCoreApplication.translate("MainWindow", u"Arbitrage pairs", None))
        self.WorkSpace_button.setText(QCoreApplication.translate("MainWindow", u"Work Space", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Settings_page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Main_page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Account page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ai predictions page", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Arbitage_pairs_page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Exchenges_page", None))
    # retranslateUi

