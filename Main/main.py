from PySide6.QtWidgets import QApplication, QWidget, QGraphicsRectItem,QGraphicsDropShadowEffect
from PySide6.QtCore import Qt,QSettings
import sys
from MainWindow import *
from TradingViewWidgets import *
from Draggable_Widget import DraggableWidget
from QTabWidget import TabWidget
from WorkSpaceWidget import WorkSpaceWidget
import json
from pathlib import Path
class MainWindow(QMainWindow):
   
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.state_path = Path('./Configs/browser_state.json')

        self.set_charts()
        self.connect_btns()
        self.add_all_shadows()

        self.ui.stackedWidget.setCurrentIndex(3)
        self.load_app_state()

        self.TabWidget = TabWidget()
        self.ui.WorkSpace_page.layout().addWidget(self.TabWidget)

        
    def closeEvent(self, event):
        self.save_app_state()
        super().closeEvent(event)
    
    def save_app_state(self):
        p = Path('./Configs').iterdir()
        for el in p:
            el.unlink()

    def load_app_state(self):
        pass

    def set_charts(self):
        html_code = html_chart('BINANCE','BTCUSDT')

        self.ui.Charts_browser1.setHtml(html_code)
        self.ui.Charts_browser2.setHtml(html_code)
        self.ui.Charts_browser3.setHtml(html_code)
        self.ui.Charts_browser4.setHtml(html_code)
        self.ui.Charts_browser5.setHtml(html_code)
        self.ui.Charts_browser6.setHtml(html_code)

    def connect_btns(self):
        self.ui.Menu_button.clicked.connect(self.toggle_left_menu)

        self.ui.Charts_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.WorkSpace_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.Settings_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.Main_page_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.Account_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.Arbitrage_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(6))
        self.ui.Ai_predictions_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.Exchanges_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(7))

    def add_all_shadows(self):
        self.add_shadow(self.ui.LeftSide_menu)
        self.add_shadow(self.ui.Head)
        self.add_shadow(self.ui.Charts_button)
        self.add_shadow(self.ui.Exchanges_button)
        self.add_shadow(self.ui.Ai_predictions_button)
        self.add_shadow(self.ui.Arbitrage_button)
        self.add_shadow(self.ui.Main_page_button)
        self.add_shadow(self.ui.Menu_button)
        self.add_shadow(self.ui.Settings_button)
        self.add_shadow(self.ui.Settings_button)
        self.add_shadow(self.ui.Account_button)
        self.add_shadow(self.ui.WorkSpace_button)

    def add_shadow(self,elem):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(80)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 150))
        elem.setGraphicsEffect(shadow)
        elem.raise_()

    def toggle_left_menu(self):
        if self.ui.LeftSide_menu.isVisible():
            self.ui.LeftSide_menu.setVisible(False)
        else:
            self.ui.LeftSide_menu.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(0, 0)
    window.showMaximized()
    sys.exit(app.exec())
