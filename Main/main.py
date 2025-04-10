from PySide6.QtWidgets import QApplication, QWidget, QGraphicsRectItem
from PySide6.QtCore import Qt
import sys
from MainWindow import *
from TradingViewWidgets import *
from Draggable_Widget import DraggableWidget
from QTabWidget import TabWidget
from WorkSpaceWidget import WorkSpaceWidget
class MainWindow(QMainWindow):
   
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Menu_button.clicked.connect(self.toggle_left_menu)

        html_code = html_chart('BINANCE','BTCUSDT')
        self.ui.stackedWidget.setCurrentIndex(6)
        self.draggable_widgets = []  # Инициализируем список для хранения виджетов

        self.ui.Charts_browser1.setHtml(html_code)
        self.ui.Charts_browser2.setHtml(html_code)
        self.ui.Charts_browser3.setHtml(html_code)
        self.ui.Charts_browser4.setHtml(html_code)
        self.ui.Charts_browser5.setHtml(html_code)
        self.ui.Charts_browser6.setHtml(html_code)

        self.ui.Charts_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.Settings_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.Main_page_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.Account_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.Ai_predictions_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.Arbitrage_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.Exchanges_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(6))
        
        self.ui.Ai_predictions_page.layout().addWidget(TabWidget())


# TODO 
#      2 Размеры виджетов довести до ума

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
