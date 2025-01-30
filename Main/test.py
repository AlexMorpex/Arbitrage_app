from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow,QFrame
from PySide6.QtWebEngineWidgets import QWebEngineView
from tradingview_widgets import html_chart

class DraggableWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 100)
        self.setStyleSheet(
            "background-color: lightblue; "
            "border: 1px solid red; "  # Жирная красная рамка
            
        )

        self.layout = QVBoxLayout()
        self.chart = QWebEngineView()
        self.layout.addWidget(self.chart)
        self.chart.setHtml(html_chart())
        self.setLayout(self.layout)
        
        
        self.offset = self.mapToGlobal(QPoint())
        print(self.offset)
        self.dragging = False



    def mousePressEvent(self, event):
        """Начало перетаскивания (только если клик в рамке)"""
        global_pos_first = self.mapToGlobal(self.rect().topLeft())
        global_pos_second = self.mapToGlobal(self.rect().bottomRight())
        mouse_pos = self.mapToGlobal(event.position()).toPoint()

        if event.button() == Qt.LeftButton and global_pos_first.x() < mouse_pos.x() < (global_pos_second.x()) \
            and global_pos_first.y() < mouse_pos.y() < global_pos_second.y():

            self.dragging = True
            self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        """Перемещение виджета"""
        if self.dragging and event.buttons() == Qt.LeftButton:
            new_pos = self.mapToParent(event.position().toPoint() - self.offset)
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        """Остановка перетаскивания"""
        if event.button() == Qt.LeftButton:
            self.dragging = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перемещение Виджета")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QFrame()
        self.setCentralWidget(self.central_widget)

        self.add_button = QPushButton("Добавить виджет")
        self.add_button.clicked.connect(self.add_draggable_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.add_button)

    def add_draggable_widget(self):
        """Добавляет новый перемещаемый виджет"""
        widget = DraggableWidget(self)
        widget.move(50, 50)
        widget.show()

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
