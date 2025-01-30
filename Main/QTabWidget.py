from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QVBoxLayout

class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setTabsClosable(True)  # Позволяет закрывать вкладки
        self.tabCloseRequested.connect(self.close_tab)  # Обработчик закрытия вкладок

        # Создаём первую вкладку
        self.add_new_tab()

        # Добавляем вкладку с "+"
        self.addTab(QWidget(), "+")
        self.currentChanged.connect(self.check_new_tab)

    def add_new_tab(self):
        """Добавляет новую вкладку перед вкладкой с '+' """
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)
        button = QPushButton("Пример кнопки")
        layout.addWidget(button)

        self.insertTab(self.count() - 1, new_tab, f"Вкладка {self.count()}")  # Перед вкладкой "+"

    def check_new_tab(self, index):
        """Проверяет, нажали ли на вкладку с '+', и если да, добавляет новую"""
        if self.tabText(index) == "+":
            self.add_new_tab()
            self.setCurrentIndex(self.count() - 2)  # Переключаемся на новую вкладку

    def close_tab(self, index):
        """Закрывает вкладку (но не даёт закрыть '+')"""
        if self.tabText(index) != "+":
            self.removeTab(index)

app = QApplication([])
window = TabWidget()
window.setWindowTitle("QTabWidget с добавлением вкладок")
window.resize(500, 300)
window.show()
app.exec()
