from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene,
    QGraphicsRectItem, QPushButton, QVBoxLayout, QWidget
)
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWebEngineWidgets import QWebEngineView

class DraggableItem(QGraphicsRectItem,QWebEngineView):
    """ Виджет, который можно перетаскивать и изменять размер """
    
    def __init__(self, x, y, width=100, height=60):
        super().__init__(0, 0, width, height)
        self.setPos(x, y)
        self.setBrush(QBrush(QColor("#3498db")))  # Синий цвет
        self.setFlags(
            QGraphicsRectItem.ItemIsMovable |  # Перемещение
            QGraphicsRectItem.ItemIsSelectable |  # Выделение
            QGraphicsRectItem.ItemIsFocusable  # Фокусировка
        )


    def mousePressEvent(self, event):
        """ При нажатии мыши элемент выделяется """
        self.setBrush(QBrush(QColor("#e74c3c")))  # Меняем цвет (красный)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """ При отпускании мыши возвращаем цвет """
        self.setBrush(QBrush(QColor("#3498db")))  # Обратно в синий
        super().mouseReleaseEvent(event)


class CanvasView(QGraphicsView):
    """ Основное рабочее поле """
    
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)  # ✅ Исправлено
        self.setSceneRect(QRectF(0, 0, 800, 600))  # Размер сцены

    def add_widget(self):
        """ Добавляет новый объект на сцену """
        item = DraggableItem(100, 100)
        self.scene.addItem(item)


class MainWindow(QMainWindow):
    """ Главное окно с кнопками для управления """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редактируемое рабочее поле")
        self.setGeometry(100, 100, 900, 700)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Полотно для работы
        self.canvas = CanvasView()

        # Кнопка "Добавить объект"
        self.add_button = QPushButton("Добавить элемент")
        self.add_button.clicked.connect(self.canvas.add_widget)

        # Размещение кнопки и сцены
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.canvas)


# Запуск приложения
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
