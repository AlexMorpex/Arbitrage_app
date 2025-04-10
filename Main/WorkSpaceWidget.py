# WorkSpaceWidget.py
from PySide6.QtWidgets import QWidget
from WorkSpace import  Ui_WorkSpaceWidget
from Draggable_Widget import DraggableWidget
from TradingViewWidgets import *

class WorkSpaceWidget(QWidget, Ui_WorkSpaceWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация UI
        self.draggable_widgets = []

        self.ChartsToolsMenu.clicked.connect(self.toggle_ToolsMenu)
        self.SymbolINfoBtn.clicked.connect(lambda:self.add_draggable_widget(html_symbol_info(),height=210,width=390,maxh=220,maxw=420))
        self.CalendarBtn.clicked.connect(lambda:self.add_draggable_widget(html_economic_calendar(),height=710,width=311,maxh=800,maxw=320))
        self.ChartBtn.clicked.connect(lambda:self.add_draggable_widget(html_chart(),height=500,width=800,maxh=700,maxw=1100))
        self.HeatMapBtn.clicked.connect(lambda:self.add_draggable_widget(html_heatmap(),height=500,width=800,maxh=700,maxw=700))
        self.NewsBtn.clicked.connect(lambda:self.add_draggable_widget(html_news(),height=500,width=500,maxh=600,maxw=500))
        self.ScreenerBtn.clicked.connect(lambda:self.add_draggable_widget(html_crypto_mkt_screener(),height=575,width=900,maxh=575,maxw=900))
        self.AnalysisBtn.clicked.connect(lambda:self.add_draggable_widget(html_technical_analysis(),height=480,width=1100,maxh=480,maxw=1100))
        self.TickerTapeBtn.clicked.connect(lambda:self.add_draggable_widget(html_ticker_tape(),height=76,width=800,maxh=76,maxw=1700))
        
        

    def add_draggable_widget(self,html,height=100,width=500,maxh=20,maxw=50):
# Получаем текущую страницу `stackedWidget`
        current_page = self.frame
        
        # Создаём новый DraggableWidget с `current_page` в качестве родителя
        widget = DraggableWidget(current_page,html,height=height,width=width,maxh=maxh,maxw=maxw)
        
        # Смещение каждого нового виджета
        offset = 20 * len(current_page.findChildren(DraggableWidget))  

        widget.move(100 + offset, 100 + offset)  # Размещаем с небольшим смещением
        widget.show()  # Показываем
        widget.raise_()  # Поднимаем поверх других 

    def toggle_ToolsMenu(self):
        if self.ToolsMenu_Left.isVisible():
            self.ToolsMenu_Left.setVisible(False)
            self.ChartsToolsMenu.raise_()
        else:
            self.ToolsMenu_Left.setVisible(True)
            self.ChartsToolsMenu.raise_()
            self.ToolsMenu_Left.raise_()
