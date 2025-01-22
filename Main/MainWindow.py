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
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1181, 630)
        MainWindow.setMinimumSize(QSize(1040, 630))
        MainWindow.setStyleSheet(u"")
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setMinimumSize(QSize(1040, 624))
        self.MainWidget.setStyleSheet(u"border:1px solid;\n"
"border-color: rgb(0, 255, 0);")
        self.verticalLayout = QVBoxLayout(self.MainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Head = QWidget(self.MainWidget)
        self.Head.setObjectName(u"Head")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Head.sizePolicy().hasHeightForWidth())
        self.Head.setSizePolicy(sizePolicy)
        self.Head.setMinimumSize(QSize(0, 70))
        self.Head.setMaximumSize(QSize(16777215, 70))
        self.Head.setStyleSheet(u"layout-spacing:10px;\n"
"background-color: rgb(0, 26, 24);\n"
"color:white;")
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
        self.Body.setStyleSheet(u"color:white;")
        self.horizontalLayout = QHBoxLayout(self.Body)
        self.horizontalLayout.setSpacing(0)
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
        self.LeftSide_menu.setStyleSheet(u"background-color: rgb(0, 55, 50);\n"
"color:white;")
        self.verticalLayout_2 = QVBoxLayout(self.LeftSide_menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.Charts_button = QPushButton(self.LeftSide_menu)
        self.Charts_button.setObjectName(u"Charts_button")
        sizePolicy1.setHeightForWidth(self.Charts_button.sizePolicy().hasHeightForWidth())
        self.Charts_button.setSizePolicy(sizePolicy1)
        self.Charts_button.setMinimumSize(QSize(165, 50))
        self.Charts_button.setMaximumSize(QSize(180, 50))

        self.verticalLayout_2.addWidget(self.Charts_button)

        self.Exchanges_button = QPushButton(self.LeftSide_menu)
        self.Exchanges_button.setObjectName(u"Exchanges_button")
        self.Exchanges_button.setMinimumSize(QSize(165, 50))
        self.Exchanges_button.setMaximumSize(QSize(180, 50))

        self.verticalLayout_2.addWidget(self.Exchanges_button)

        self.Ai_predictions_button = QPushButton(self.LeftSide_menu)
        self.Ai_predictions_button.setObjectName(u"Ai_predictions_button")
        self.Ai_predictions_button.setMinimumSize(QSize(165, 50))
        self.Ai_predictions_button.setMaximumSize(QSize(180, 50))

        self.verticalLayout_2.addWidget(self.Ai_predictions_button)

        self.Arbitrage_button = QPushButton(self.LeftSide_menu)
        self.Arbitrage_button.setObjectName(u"Arbitrage_button")
        self.Arbitrage_button.setMinimumSize(QSize(165, 50))
        self.Arbitrage_button.setMaximumSize(QSize(180, 50))

        self.verticalLayout_2.addWidget(self.Arbitrage_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.LeftSide_menu)

        self.Main_menu = QWidget(self.Body)
        self.Main_menu.setObjectName(u"Main_menu")
        self.Main_menu.setStyleSheet(u"background-color:rgb(49, 80, 77);\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.Main_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self._for_charts = QWidget(self.Main_menu)
        self._for_charts.setObjectName(u"_for_charts")
        self.horizontalLayout_3 = QHBoxLayout(self._for_charts)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 5, 5)
        self.label = QLabel(self._for_charts)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))
        self.label.setMaximumSize(QSize(80, 16777215))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.SymbolLineEdit = QLineEdit(self._for_charts)
        self.SymbolLineEdit.setObjectName(u"SymbolLineEdit")
        self.SymbolLineEdit.setMinimumSize(QSize(80, 0))
        self.SymbolLineEdit.setMaximumSize(QSize(80, 20))
        self.SymbolLineEdit.setStyleSheet(u"color:white;")
        self.SymbolLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.SymbolLineEdit)

        self.label_2 = QLabel(self._for_charts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 20))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.ExchangeLineEdit = QLineEdit(self._for_charts)
        self.ExchangeLineEdit.setObjectName(u"ExchangeLineEdit")
        self.ExchangeLineEdit.setMinimumSize(QSize(80, 0))
        self.ExchangeLineEdit.setMaximumSize(QSize(80, 20))
        self.ExchangeLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.ExchangeLineEdit)

        self.ApplySymbol_button = QPushButton(self._for_charts)
        self.ApplySymbol_button.setObjectName(u"ApplySymbol_button")
        self.ApplySymbol_button.setMinimumSize(QSize(80, 0))
        self.ApplySymbol_button.setMaximumSize(QSize(70, 20))
        self.ApplySymbol_button.setStyleSheet(u"Color: white;")

        self.horizontalLayout_3.addWidget(self.ApplySymbol_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self._for_charts)

        self.stackedWidget = QStackedWidget(self.Main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Charts_page = QWidget()
        self.Charts_page.setObjectName(u"Charts_page")
        self.gridLayout_2 = QGridLayout(self.Charts_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Charts_browser1 = QWebEngineView(self.Charts_page)
        self.Charts_browser1.setObjectName(u"Charts_browser1")
        self.Charts_browser1.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser1, 1, 1, 1, 1)

        self.Charts_browser3 = QWebEngineView(self.Charts_page)
        self.Charts_browser3.setObjectName(u"Charts_browser3")
        self.Charts_browser3.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser3, 1, 3, 1, 1)

        self.Charts_browser2 = QWebEngineView(self.Charts_page)
        self.Charts_browser2.setObjectName(u"Charts_browser2")
        self.Charts_browser2.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser2, 1, 2, 1, 1)

        self.Charts_browser4 = QWebEngineView(self.Charts_page)
        self.Charts_browser4.setObjectName(u"Charts_browser4")
        self.Charts_browser4.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser4, 2, 1, 1, 1)

        self.Charts_browser5 = QWebEngineView(self.Charts_page)
        self.Charts_browser5.setObjectName(u"Charts_browser5")
        self.Charts_browser5.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser5, 2, 2, 1, 1)

        self.Charts_browser6 = QWebEngineView(self.Charts_page)
        self.Charts_browser6.setObjectName(u"Charts_browser6")
        self.Charts_browser6.setUrl(QUrl(u"about:blank"))

        self.gridLayout_2.addWidget(self.Charts_browser6, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.Charts_page)
        self.Settings_page = QWidget()
        self.Settings_page.setObjectName(u"Settings_page")
        self.stackedWidget.addWidget(self.Settings_page)
        self.Main_page = QWidget()
        self.Main_page.setObjectName(u"Main_page")
        self.stackedWidget.addWidget(self.Main_page)
        self.Account_page = QWidget()
        self.Account_page.setObjectName(u"Account_page")
        self.stackedWidget.addWidget(self.Account_page)
        self.Ai_predictions_page = QWidget()
        self.Ai_predictions_page.setObjectName(u"Ai_predictions_page")
        self.stackedWidget.addWidget(self.Ai_predictions_page)
        self.Arbitrage_pairs_page = QWidget()
        self.Arbitrage_pairs_page.setObjectName(u"Arbitrage_pairs_page")
        self.stackedWidget.addWidget(self.Arbitrage_pairs_page)
        self.Exchenges_page = QWidget()
        self.Exchenges_page.setObjectName(u"Exchenges_page")
        self.stackedWidget.addWidget(self.Exchenges_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Main_menu)


        self.verticalLayout.addWidget(self.Body)

        self.Footer = QWidget(self.MainWidget)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 60))
        self.Footer.setMaximumSize(QSize(16777215, 60))
        self.Footer.setStyleSheet(u"background-color:rgb(0, 26, 24)")

        self.verticalLayout.addWidget(self.Footer)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Symbol", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Exchange", None))
        self.ApplySymbol_button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

