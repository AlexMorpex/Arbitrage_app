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
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1181, 649)
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
        self.verticalLayout_4 = QVBoxLayout(self.Ai_predictions_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.Ai_predictions_page)
        self.Arbitrage_pairs_page = QWidget()
        self.Arbitrage_pairs_page.setObjectName(u"Arbitrage_pairs_page")
        self.stackedWidget.addWidget(self.Arbitrage_pairs_page)
        self.Exchenges_page = QWidget()
        self.Exchenges_page.setObjectName(u"Exchenges_page")
        self.gridLayout = QGridLayout(self.Exchenges_page)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.DraggableLayout = QGridLayout()
        self.DraggableLayout.setObjectName(u"DraggableLayout")

        self.gridLayout.addLayout(self.DraggableLayout, 1, 1, 2, 2)

        self.ChartsToolsMenu = QPushButton(self.Exchenges_page)
        self.ChartsToolsMenu.setObjectName(u"ChartsToolsMenu")
        self.ChartsToolsMenu.setMinimumSize(QSize(54, 46))
        self.ChartsToolsMenu.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ChartsToolsMenu.setIcon(icon)
        self.ChartsToolsMenu.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.ChartsToolsMenu, 0, 0, 1, 1)

        self.ToolsMenu_Right = QWidget(self.Exchenges_page)
        self.ToolsMenu_Right.setObjectName(u"ToolsMenu_Right")
        self.ToolsMenu_Right.setMinimumSize(QSize(350, 46))
        self.ToolsMenu_Right.setMaximumSize(QSize(350, 46))
        self.horizontalLayout_3 = QHBoxLayout(self.ToolsMenu_Right)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CryptoPairLabel = QLabel(self.ToolsMenu_Right)
        self.CryptoPairLabel.setObjectName(u"CryptoPairLabel")
        self.CryptoPairLabel.setMinimumSize(QSize(0, 0))
        self.CryptoPairLabel.setMaximumSize(QSize(80, 28))
        self.CryptoPairLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.CryptoPairLabel)

        self.lineEdit = QLineEdit(self.ToolsMenu_Right)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(80, 28))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.EchangeLabel = QLabel(self.ToolsMenu_Right)
        self.EchangeLabel.setObjectName(u"EchangeLabel")
        self.EchangeLabel.setMinimumSize(QSize(0, 0))
        self.EchangeLabel.setMaximumSize(QSize(80, 28))
        self.EchangeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.EchangeLabel)

        self.lineEdit_2 = QLineEdit(self.ToolsMenu_Right)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QSize(80, 28))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.ToolsMenu_Right, 0, 1, 1, 1)

        self.ToolsMenu_Left = QWidget(self.Exchenges_page)
        self.ToolsMenu_Left.setObjectName(u"ToolsMenu_Left")
        self.ToolsMenu_Left.setMinimumSize(QSize(54, 316))
        self.verticalLayout_5 = QVBoxLayout(self.ToolsMenu_Left)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SymbolINfoBtn = QPushButton(self.ToolsMenu_Left)
        self.SymbolINfoBtn.setObjectName(u"SymbolINfoBtn")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/symbol-info.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SymbolINfoBtn.setIcon(icon1)
        self.SymbolINfoBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.SymbolINfoBtn)

        self.CalendarBtn = QPushButton(self.ToolsMenu_Left)
        self.CalendarBtn.setObjectName(u"CalendarBtn")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/calendar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CalendarBtn.setIcon(icon2)
        self.CalendarBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.CalendarBtn)

        self.ChartBtn = QPushButton(self.ToolsMenu_Left)
        self.ChartBtn.setObjectName(u"ChartBtn")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/candle-chart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ChartBtn.setIcon(icon3)
        self.ChartBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.ChartBtn)

        self.HeatMapBtn = QPushButton(self.ToolsMenu_Left)
        self.HeatMapBtn.setObjectName(u"HeatMapBtn")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/heat-map.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HeatMapBtn.setIcon(icon4)
        self.HeatMapBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.HeatMapBtn)

        self.NewsBtn = QPushButton(self.ToolsMenu_Left)
        self.NewsBtn.setObjectName(u"NewsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/news.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.NewsBtn.setIcon(icon5)
        self.NewsBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.NewsBtn)

        self.ScreenerBtn = QPushButton(self.ToolsMenu_Left)
        self.ScreenerBtn.setObjectName(u"ScreenerBtn")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/icons/screener.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ScreenerBtn.setIcon(icon6)
        self.ScreenerBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.ScreenerBtn)

        self.AnalysisBtn = QPushButton(self.ToolsMenu_Left)
        self.AnalysisBtn.setObjectName(u"AnalysisBtn")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/icons/technical-analysis.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AnalysisBtn.setIcon(icon7)
        self.AnalysisBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.AnalysisBtn)

        self.TickerTapeBtn = QPushButton(self.ToolsMenu_Left)
        self.TickerTapeBtn.setObjectName(u"TickerTapeBtn")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/icons/tickertape.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TickerTapeBtn.setIcon(icon8)
        self.TickerTapeBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.TickerTapeBtn)


        self.gridLayout.addWidget(self.ToolsMenu_Left, 1, 0, 1, 1)

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

        self.stackedWidget.setCurrentIndex(4)


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
        self.ChartsToolsMenu.setText("")
        self.CryptoPairLabel.setText(QCoreApplication.translate("MainWindow", u" Crypto Pair ", None))
        self.EchangeLabel.setText(QCoreApplication.translate("MainWindow", u" Exchange ", None))
        self.SymbolINfoBtn.setText("")
        self.CalendarBtn.setText("")
        self.ChartBtn.setText("")
        self.HeatMapBtn.setText("")
        self.NewsBtn.setText("")
        self.ScreenerBtn.setText("")
        self.AnalysisBtn.setText("")
        self.TickerTapeBtn.setText("")
    # retranslateUi

