from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QGraphicsDropShadowEffect
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QColor

class WebWidget(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Создаем сцену
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Создаем QWebEngineView для отображения HTML
        self.webview = QWebEngineView()
        self.webview.setUrl("https://www.example.com")  # Устанавливаем URL для отображения

        # Создаем прокси-виджет для встраивания веб-страницы в сцену
        self.proxy_widget = QGraphicsProxyWidget()  # не передаем self сюда
        self.proxy_widget.setWidget(self.webview)  # Вставляем QWebEngineView
        self.proxy_widget.setFlag(QGraphicsProxyWidget.ItemIsMovable)  # Флаг для перемещения

        # Устанавливаем размеры и позицию прокси-виджета
        self.proxy_widget.setGeometry(QRectF(50, 50, 800, 600))  # Позиция и размер

        # Добавляем прокси-виджет в сцену
        self.scene.addItem(self.proxy_widget)

        # Добавляем рамку вокруг прокси-виджета для теста
        self.setGraphicsEffect(self.createBorderEffect())

    def createBorderEffect(self):
        # Добавляем эффект рамки
        border_effect = QGraphicsDropShadowEffect()
        border_effect.setColor(QColor(0, 0, 0))  # Черная рамка
        border_effect.setOffset(0, 0)  # Положение тени
        border_effect.setBlurRadius(5)  # Радиус размытия
        return border_effect

    def resizeEvent(self, event):
        # Перерисовываем QWebEngineView при изменении размера
        self.webview.setGeometry(self.proxy_widget.geometry().toRect())
        super().resizeEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Movable Web Browser in Graphics View")

        # Создаем экземпляр WebWidget и устанавливаем его как центральный виджет
        self.web_widget = WebWidget()
        self.setCentralWidget(self.web_widget)


# Запуск приложения
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
