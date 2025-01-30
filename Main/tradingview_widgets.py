def html_chart(exchange='BINANCE',symbol='BTCUSDT'):
    html = f"""
            <div class="tradingview-widget-container" style="height:100%;width:100%">
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
        {{
        "autosize": true,
        "symbol": "{exchange}:{symbol}",
        "interval": "D",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "hide_side_toolbar": false,
        "allow_symbol_change": true,
        "save_image": true,
        "calendar": true,
        "hide_volume": true,
        "support_host": "https://www.tradingview.com"
        }}
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
        </div>
        """
    
    return html

def html_ticker_tape():
    html = f"""
        <div class="tradingview-widget-container">
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
        {{
        "symbols": [
            {{
            "proName": "FOREXCOM:SPXUSD",
            "title": "S&P 500 Index"
            }},
            {{
            "proName": "FOREXCOM:NSXUSD",
            "title": "US 100 Cash CFD"
            }},
            {{
            "description": "BNB",
            "proName": "BINANCE:BNBUSDT"
            }},
            {{
            "description": "Bitcoin",
            "proName": "BINANCE:BTCUSDT"
            }},
            {{
            "description": "Ethereum",
            "proName": "BINANCE:ETHUSDT"
            }}
        ],
        "showSymbolLogo": true,
        "isTransparent": false,
        "displayMode": "adaptive",
        "colorTheme": "dark",
        "locale": "ru"
        }}
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
</div>
    """
    return html

def html_heatmap():
    html = f"""
    <div class="tradingview-widget-container">
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-crypto-coins-heatmap.js" async>
    {{
    "dataSource": "Crypto",
    "blockSize": "market_cap_diluted_calc",
    "blockColor": "Volatility.D",
    "locale": "ru",
    "symbolUrl": "",
    "colorTheme": "dark",
    "hasTopBar": true,
    "isDataSetEnabled": true,
    "isZoomEnabled": true,
    "hasSymbolTooltip": true,
    "isMonoSize": false,
    "width": "100%",
    "height": "100%"
    }}
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
    </div>
        """
    return html


def html_crypto_mkt_screener():
    html = f"""
        <div class="tradingview-widget-container">
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
        {{
        "width": "100%",
        "height": 550,
        "defaultColumn": "performance",
        "screener_type": "crypto_mkt",
        "displayCurrency": "USD",
        "colorTheme": "dark",
        "locale": "ru"
        }}
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
        </div>
    """
    return html

def html_symbol_info(exchange='BINANCE',symbol='BTCUSDT'):
    html = f"""
        <div class="tradingview-widget-container">
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
        {{
        "symbol": "{exchange}:{symbol}",
        "width": "550",
        "locale": "ru",
        "colorTheme": "dark",
        "isTransparent": false
        }}
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
        </div>
    """
    return html

def html_technical_analysis(exchange='BINANCE',symbol='BTCUSDT'):
    html = f"""
        <div class="tradingview-widget-container">
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
            {{
            "interval": "1m",
            "width": "100%",
            "isTransparent": false,
            "height": "100%",
            "symbol": "BINANCE:BTCUSDT",
            "showIntervalTabs": true,
            "displayMode": "multiple",
            "locale": "ru",
            "colorTheme": "dark"
        }}
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
        </div>
    """
    return html

def html_economic_calendar(exchange='BINANCE',symbol='BTCUSDT'):
    html = f"""

    """
    return html

def html_news(exchange='BINANCE',symbol='BTCUSDT'):
    html = f"""

    """
    return html