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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 624)
        MainWindow.setMinimumSize(QSize(800, 500))
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
"background-color: rgb(0, 26, 24)")
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
        self.Body.setStyleSheet(u"")
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
        self.LeftSide_menu.setStyleSheet(u"background-color: rgb(0, 55, 50);")
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
        self.stackedWidget = QStackedWidget(self.Main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(120, 50, 165, 125))
        self.Charts_page = QWidget()
        self.Charts_page.setObjectName(u"Charts_page")
        self.stackedWidget.addWidget(self.Charts_page)
        self.Exchenges_page = QWidget()
        self.Exchenges_page.setObjectName(u"Exchenges_page")
        self.stackedWidget.addWidget(self.Exchenges_page)

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
    # retranslateUi

