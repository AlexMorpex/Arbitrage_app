from PySide6.QtWidgets import QTabWidget, QWidget, QPushButton, QVBoxLayout

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

        self.add_new_tab()
        self.addTab(QWidget(), "+")
        self.currentChanged.connect(self.check_new_tab)

    def add_new_tab(self):
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)
        button = QPushButton("Пример кнопки")
        layout.addWidget(button)

        self.insertTab(self.count() - 1, new_tab, f"Вкладка {self.count()}")

    def check_new_tab(self, index):
        if self.tabText(index) == "+":
            self.add_new_tab()
            self.setCurrentIndex(self.count() - 2)

    def close_tab(self, index):
        if self.tabText(index) != "+":
            self.removeTab(index)
