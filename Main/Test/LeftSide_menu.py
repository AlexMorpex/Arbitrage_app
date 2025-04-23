from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QGraphicsDropShadowEffect, QFrame
)
from PySide6.QtGui import QColor
import sys

class ShadowTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест тени")
        self.setStyleSheet("background-color: #2c2f3a;")  # Тёмный фон
        self.setFixedSize(600, 400)

        # Основной контейнер
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(100, 100, 100, 100)  # Пространство вокруг "панели"

        # Виджет, к которому добавим тень
        shadow_box = QFrame()
        shadow_box.setFixedSize(200, 200)
        shadow_box.setStyleSheet("background-color: #1a1e2c; border-radius: 10px;")

        # Эффект тени
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setOffset(10, 10)
        shadow.setColor(QColor(0, 0, 0, 180))
        shadow_box.setGraphicsEffect(shadow)

        layout.addWidget(shadow_box)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShadowTestWindow()
    window.show()
    sys.exit(app.exec())
