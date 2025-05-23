from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from WorkSpaceWidget import WorkSpaceWidget

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        print('Created Tab Widget')

        self.tabs = 0
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.add_new_tab()
        self.addTab(QWidget(), "+")
        self.currentChanged.connect(self.check_new_tab)
        self.make_css_create_again()


    def make_css_create_again(self):
        self.setStyleSheet("""
            QTabBar::tab {
                background: #2b2b2b;
                color: white;
                padding: 8px 16px;
                border: 1px solid #444;
                border-bottom: none;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                margin-right: 2px;
            }

            QTabBar::tab:selected {
                background: #444;
                color: #00ff88;
            }

            QTabBar::tab:hover {
                background: #3d3d3d;
            }

            # QTabBar::close-button {
            #     image: url(:/icons/close.png); /* или использовать стандартное поведение */
            #     subcontrol-position: right;
            # }

            # QTabBar::close-button:hover {
            #     image: url(:/icons/close-hover.png);
            # }
            """)
        
    def add_new_tab(self):
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)

        if self.count()<1:
            self.insertTab(self.count(),new_tab,f"Page 1")
            WorkSpace = WorkSpaceWidget(f"Page 1")
            layout.addWidget(WorkSpace)
            self.tabs+=1
        else:
            self.tabs+=1
            WorkSpace = WorkSpaceWidget(f"Page {self.tabs}")
            layout.addWidget(WorkSpace)
            self.insertTab(self.count() - 1, new_tab, f"Page {self.tabs}")

                
    def check_new_tab(self, index):
        if self.tabText(index) == "+":
            self.add_new_tab()
            self.setCurrentIndex(self.count() - 2)

    def close_tab(self, index):
        if self.tabText(index) != "+":
            self.setCurrentIndex(self.currentIndex()-1)
            print('удаляю',self.tabText(index))
            self.removeTab(index)
