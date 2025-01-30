from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QVBoxLayout, QWidget, QGraphicsItem
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, QRectF

class WebGraphicsRectItem(QGraphicsRectItem):
    def __init__(self, rect, webview):
        super().__init__(rect)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.webview = webview
        self.setZValue(1)  # Установим z-уровень, чтобы веб-страница отображалась поверх прямоугольника
        self.setBrush(Qt.transparent)  # Прозрачный фон для прямоугольника

    def paint(self, painter, option, widget=None):
        # Рисуем прямоугольник (можно добавить фон или стиль, если нужно)
        painter.setPen(Qt.black)
        painter.drawRect(self.rect())


class WebWidget(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Создание QWebEngineView для отображения HTML
        self.webview = QWebEngineView()
        self.webview.setUrl("https://www.example.com")  # Устанавливаем URL для отображения

        # Создание WebGraphicsRectItem и добавление его в сцену
        self.rect_item = WebGraphicsRectItem(QRectF(50, 50, 400, 300), self.webview)
        self.scene.addItem(self.rect_item)

        # Устанавливаем виджет QWebEngineView внутри QGraphicsItem
        self.webview.setGeometry(self.rect_item.rect().toRect())  # Размер и положение webview
        self.webview.show()

        # Добавление WebGraphicsRectItem в сцену
        self.scene.addItem(self.rect_item)

    def resizeEvent(self, event):
        # Перерисовываем QWebEngineView при изменении размера
        self.webview.setGeometry(self.rect_item.rect().toRect())
        super().resizeEvent(event)