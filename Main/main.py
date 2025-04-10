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
        self.ui.Ai_predictions_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.Arbitrage_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.Settings_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.Account_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.Exchanges_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(6))

        self.ui.ChartsToolsMenu.clicked.connect(self.toggle_ToolsMenu)
        self.ui.SymbolINfoBtn.clicked.connect(lambda:self.add_draggable_widget(html_symbol_info(),height=200,width=400))
        self.ui.CalendarBtn.clicked.connect(lambda:self.add_draggable_widget(html_economic_calendar(),height=600,width=250))
        self.ui.ChartBtn.clicked.connect(lambda:self.add_draggable_widget(html_chart(),height=400,width=400,mh=300,mw=600))
        self.ui.HeatMapBtn.clicked.connect(lambda:self.add_draggable_widget(html_heatmap()))
        self.ui.NewsBtn.clicked.connect(lambda:self.add_draggable_widget(html_news()))
        self.ui.ScreenerBtn.clicked.connect(lambda:self.add_draggable_widget(html_crypto_mkt_screener()))
        self.ui.AnalysisBtn.clicked.connect(lambda:self.add_draggable_widget(html_technical_analysis()))
        self.ui.TickerTapeBtn.clicked.connect(lambda:self.add_draggable_widget(html_ticker_tape()))
        
        WorkSpaceTabWidget = TabWidget()
        # Создаём экземпляр нового виджета
        workspace_widget = WorkSpaceWidget()  
        
        # Добавляем виджет в layout
        self.ui.Ai_predictions_page.layout().addWidget(workspace_widget)  # Ис
        self.ui.Ai_predictions_page.layout().addWidget(WorkSpaceTabWidget)


# TODO 1 Переделать индексы кнопок для переключения (некорректные)
#      2 Размеры виджетов довести до ума
#      3 Впихнуть в табвиджет рабочее поле 



    def toggle_left_menu(self):
        if self.ui.LeftSide_menu.isVisible():
            self.ui.LeftSide_menu.setVisible(False)
        else:
            self.ui.LeftSide_menu.setVisible(True)

    def change_page(self,index):
        self.ui.stackedWidget.setCurrentIndex(0)

    def toggle_ToolsMenu(self):
        if self.ui.ToolsMenu_Right.isVisible():
            self.ui.ToolsMenu_Left.setVisible(False)
            self.ui.ToolsMenu_Right.setVisible(False)
        else:
            self.ui.ToolsMenu_Left.setVisible(True)
            self.ui.ToolsMenu_Right.setVisible(True)

    def add_draggable_widget(self,html,height=100,width=500,mh=20,mw=50):
    # Получаем текущую страницу `stackedWidget`
        current_page = self.ui.stackedWidget.currentWidget()
        
        # Создаём новый DraggableWidget с `current_page` в качестве родителя
        widget = DraggableWidget(current_page,html,height=height,width=width,mh=mh,mw=mw)
        
        # Смещение каждого нового виджета
        offset = 20 * len(current_page.findChildren(DraggableWidget))  

        widget.move(100 + offset, 100 + offset)  # Размещаем с небольшим смещением
        widget.show()  # Показываем
        widget.raise_()  # Поднимаем поверх других
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(0, 0)
    window.showMaximized()
    sys.exit(app.exec())
