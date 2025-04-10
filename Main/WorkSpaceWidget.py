# WorkSpaceWidget.py
from PySide6.QtWidgets import QWidget
from WorkSpace import Ui_Form  # Это импорт интерфейса

class WorkSpaceWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация UI
