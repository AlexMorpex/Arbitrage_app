from PySide6.QtWidgets import QApplication, QWidget
import sys
from MainWindow import *


class MainWindow(QMainWindow):

    exchange = self.ui.ExchangeLineEdit.text()
    symbol = self.ui.SymbolLineEdit.text()
    html_code = f"""

    <div id="tradingview-widget-container"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget({{
        "container_id": "tradingview-widget-container",
        "symbol": "{exchange}:{symbol}",
        "interval": "D",
        "theme": "dark",
        "locale": "en",
        "width": "100%",
        "height": "98%",
        "exchange": "OKX",
        "studies": ["MASimple@tv-basicstudies"],
        "overrides": {{
            "mainSeriesProperties.showCountdown": true,
            "paneProperties.background": "#1e222d",
            "paneProperties.vertGridProperties.color": "#2a2e39",
            "paneProperties.horzGridProperties.color": "#2a2e39",
            "symbolWatermarkProperties.transparency": 90,
            "scalesProperties.textColor": "#AAA"
        }},
        "drawing_tools": true
    }});
    </script>
    """

            
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Menu_button.clicked.connect(self.toggle_left_menu)
        self.ui.ApplySymbol_button.clicked.connect(self.draw_chart)

        self.ui.Charts_browser.page().setBackgroundColor(Qt.transparent)
        self.ui.Charts_browser.setHtml(self.html_code)

    def toggle_left_menu(self):
        if self.ui.LeftSide_menu.isVisible():
            self.ui.LeftSide_menu.setVisible(False)
        else:
            self.ui.LeftSide_menu.setVisible(True)

    def draw_chart(self):
        exchange = self.ui.ExchangeLineEdit.text()
        symbol = self.ui.SymbolLineEdit.text()
        html_code = f"""

    <div id="tradingview-widget-container"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget({{
        "container_id": "tradingview-widget-container",
        "symbol": "{exchange}:{symbol}",
        "interval": "D",
        "theme": "dark",
        "locale": "en",
        "width": "100%",
        "height": "98%",
        "exchange": "OKX",
        "studies": ["MASimple@tv-basicstudies"],
        "overrides": {{
            "mainSeriesProperties.showCountdown": true,
            "paneProperties.background": "#1e222d",
            "paneProperties.vertGridProperties.color": "#2a2e39",
            "paneProperties.horzGridProperties.color": "#2a2e39",
            "symbolWatermarkProperties.transparency": 90,
            "scalesProperties.textColor": "#AAA"
        }},
        "drawing_tools": true
    }});
    </script>
    """

        self.ui.Charts_browser.setHtml(html_code)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(0, 0)
    window.showMaximized()
    sys.exit(app.exec())
