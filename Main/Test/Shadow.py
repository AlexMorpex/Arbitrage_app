from PySide6.QtWidgets import QApplication, QPushButton, QGraphicsDropShadowEffect, QWidget, QVBoxLayout
from PySide6.QtGui import QColor
import sys

app = QApplication([])

window = QWidget()
layout = QVBoxLayout(window)

button = QPushButton("Test Shadow")
shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(20)
shadow.setOffset(10, 10)
shadow.setColor(QColor(0, 0, 0, 150))
button.setGraphicsEffect(shadow)

layout.addWidget(button)
window.setLayout(layout)
window.show()

sys.exit(app.exec())
