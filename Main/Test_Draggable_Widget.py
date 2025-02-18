from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QApplication, QWidget,QSpacerItem,QSizePolicy,\
QSpacerItem,QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QFrame
from PySide6.QtWebEngineWidgets import QWebEngineView
from TradingViewWidgets import html_chart

class DraggableWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 150)
        self.resize(400, 300)
        self.setStyleSheet("""
                           border: 0px solid red;
                           background-color: white;
                            border-radius:5px;
                           """)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 5, 5)
        
        self.top_bar = QWidget()
        self.top_bar.setFixedHeight(25)
        self.top_layout = QHBoxLayout(self.top_bar)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.addStretch()
        
        self.close_button = QPushButton("✖")
        self.close_button.setFixedSize(20, 20)
        self.close_button.setStyleSheet("border: none; font-size: 14px; color: black;")
        self.close_button.clicked.connect(self.close)
        
        self.top_layout.addWidget(self.close_button)
        self.main_layout.addWidget(self.top_bar)

        self.chart = QWebEngineView()
        self.chart.setHtml(html_chart())
        self.main_layout.addWidget(self.chart)

        self.dragging = False
        self.resizing = False
        self.resize_direction = None
        self.offset = QPointF()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resize_direction = self.get_resize_direction(event.position().toPoint())
            if any(self.resize_direction):
                self.resizing = True
            else:
                self.dragging = True
                self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.resizing:
            self.resize_widget(event)
        elif self.dragging:
            self.move(self.mapToParent(event.position().toPoint() - self.offset))
        self.update_cursor(event.position().toPoint())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.resizing = False

    def get_resize_direction(self, pos, margin=10):
        left = pos.x() < margin
        right = pos.x() > self.width() - margin
        top = pos.y() < margin
        bottom = pos.y() > self.height() - margin
        return (left, right, top, bottom)

    def resize_widget(self, event):
        dx = event.position().toPoint().x() - self.width()
        dy = event.position().toPoint().y() - self.height()
        left, right, top, bottom = self.resize_direction

        new_x = self.x() - dx if left else self.x()
        new_y = self.y() - dy if top else self.y()
        new_width = max(self.minimumWidth(), self.width() + (dx if right else -dx if left else 0))
        new_height = max(self.minimumHeight(), self.height() + (dy if bottom else -dy if top else 0))
        
        if left or top:
            self.setGeometry(new_x, new_y, new_width, new_height)
        else:
            self.resize(new_width, new_height)

    def update_cursor(self, pos, margin=10):
        left, right, top, bottom = self.get_resize_direction(pos, margin)
        
        if left and top or right and bottom:
            self.setCursor(Qt.SizeFDiagCursor)
        elif right and top or left and bottom:
            self.setCursor(Qt.SizeBDiagCursor)
        elif left or right:
            self.setCursor(Qt.SizeHorCursor)
        elif top or bottom:
            self.setCursor(Qt.SizeVerCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перемещение и Изменение Размеров Виджета")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
    
        self.add_button = QPushButton("Добавить виджет")
        self.add_button.clicked.connect(self.add_draggable_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.add_button)

        self.layout.addWidget(DraggableWidget())


    def add_draggable_widget(self):
        """Добавляет новый перемещаемый и изменяемый виджет"""
        widget = DraggableWidget(self)
        widget.move(50, 50)
        widget.show()

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
