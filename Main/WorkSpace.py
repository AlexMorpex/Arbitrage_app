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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_WorkSpaceWidget(object):
    def setupUi(self, WorkSpaceWidget):
        if not WorkSpaceWidget.objectName():
            WorkSpaceWidget.setObjectName(u"WorkSpaceWidget")
        WorkSpaceWidget.resize(847, 562)
        WorkSpaceWidget.setStyleSheet(u"border:1px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"")
        self.gridLayout = QGridLayout(WorkSpaceWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WorkSpaceWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ChartsToolsMenu = QPushButton(self.frame)
        self.ChartsToolsMenu.setObjectName(u"ChartsToolsMenu")
        self.ChartsToolsMenu.setMinimumSize(QSize(54, 46))
        self.ChartsToolsMenu.setMaximumSize(QSize(54, 46))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ChartsToolsMenu.setIcon(icon)
        self.ChartsToolsMenu.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.ChartsToolsMenu, 0, 0, 1, 1)

        self.ToolsMenu_Left = QWidget(self.frame)
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


        self.gridLayout_2.addWidget(self.ToolsMenu_Left, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 195, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.DraggableLayout = QGridLayout()
        self.DraggableLayout.setObjectName(u"DraggableLayout")

        self.gridLayout_2.addLayout(self.DraggableLayout, 0, 1, 3, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(WorkSpaceWidget)

        QMetaObject.connectSlotsByName(WorkSpaceWidget)
    # setupUi

    def retranslateUi(self, WorkSpaceWidget):
        WorkSpaceWidget.setWindowTitle(QCoreApplication.translate("WorkSpaceWidget", u"WorkSpaceWidget", None))
        self.ChartsToolsMenu.setText("")
        self.SymbolINfoBtn.setText("")
        self.CalendarBtn.setText("")
        self.ChartBtn.setText("")
        self.HeatMapBtn.setText("")
        self.NewsBtn.setText("")
        self.ScreenerBtn.setText("")
        self.AnalysisBtn.setText("")
        self.TickerTapeBtn.setText("")
    # retranslateUi

