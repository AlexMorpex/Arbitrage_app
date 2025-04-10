# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkSpace.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(815, 562)
        Form.setStyleSheet(u"border:1px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ChartsToolsMenu = QPushButton(Form)
        self.ChartsToolsMenu.setObjectName(u"ChartsToolsMenu")
        self.ChartsToolsMenu.setMinimumSize(QSize(54, 46))
        self.ChartsToolsMenu.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ChartsToolsMenu.setIcon(icon)
        self.ChartsToolsMenu.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.ChartsToolsMenu, 0, 0, 1, 1)

        self.ToolsMenu_Right = QWidget(Form)
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

        self.horizontalSpacer = QSpacerItem(378, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.ToolsMenu_Left = QWidget(Form)
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

        self.DraggableLayout = QGridLayout()
        self.DraggableLayout.setObjectName(u"DraggableLayout")

        self.gridLayout.addLayout(self.DraggableLayout, 1, 1, 2, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 167, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ChartsToolsMenu.setText("")
        self.CryptoPairLabel.setText(QCoreApplication.translate("Form", u" Crypto Pair ", None))
        self.EchangeLabel.setText(QCoreApplication.translate("Form", u" Exchange ", None))
        self.SymbolINfoBtn.setText("")
        self.CalendarBtn.setText("")
        self.ChartBtn.setText("")
        self.HeatMapBtn.setText("")
        self.NewsBtn.setText("")
        self.ScreenerBtn.setText("")
        self.AnalysisBtn.setText("")
        self.TickerTapeBtn.setText("")
    # retranslateUi

