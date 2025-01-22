from PySide6.QtWidgets import QApplication, QWidget
import sys
from MainWindow import *


class MainWindow(QMainWindow):
   
    def __init__(self):
        QMainWindow.__init__(self)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Menu_button.clicked.connect(self.toggle_left_menu)
        self.ui.ApplySymbol_button.clicked.connect(self.draw_chart)

        exchange = 'Binance'
        symbol = 'BTCUSDT'
        html_code = f"""
        <div id="tradingview-widget-container"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({{
            "container_id": "tradingview-widget-container",
            "symbol": "{exchange}:{symbol}",
            "interval": "D",
            "theme": "dark",
            "locale": "ru",
            "width": "100%",
            "height": "100%",
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
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
            }}
        </style>
        """

        self.ui.Charts_browser1.setHtml(html_code)
        self.ui.Charts_browser2.setHtml(html_code)
        self.ui.Charts_browser3.setHtml(html_code)
        self.ui.Charts_browser4.setHtml(html_code)
        self.ui.Charts_browser5.setHtml(html_code)
        self.ui.Charts_browser6.setHtml(html_code)

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
            "locale": "ru",
            "width": "100%",
            "height": "100%",
            "exchange": "OKX",
            "studies": [
                "RSI@tv-basicstudies", 
                "BollingerBands@tv-basicstudies"
            ],
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
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden; /* Отключает прокрутку */
            }}
        </style>
        """

        self.ui.Charts_browser1.setHtml(html_code)
        self.ui.Charts_browser2.setHtml(html_code)
        self.ui.Charts_browser3.setHtml(html_code)
        self.ui.Charts_browser4.setHtml(html_code)
        self.ui.Charts_browser5.setHtml(html_code)
        self.ui.Charts_browser6.setHtml(html_code)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(0, 0)
    window.showMaximized()
    sys.exit(app.exec())
