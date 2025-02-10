from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsProxyWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

app = QApplication([])

# Создаем графическую сцену и представление
scene = QGraphicsScene()
view = QGraphicsView(scene)
view.setGeometry(100, 100, 800, 600)

# Создаем QWebEngineView
web_view = QWebEngineView()
web_view.setUrl("https://www.google.com")  # Загружаем страницу

# Оборачиваем его в QGraphicsProxyWidget и добавляем на сцену
proxy = QGraphicsProxyWidget()
proxy.setWidget(web_view)
scene.addItem(proxy)

view.show()
app.exec()
