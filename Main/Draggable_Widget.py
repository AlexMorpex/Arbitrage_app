from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget,QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from PySide6.QtWebEngineWidgets import QWebEngineView
from TradingViewWidgets import *

BASE_HTML = html_chart()
class DraggableWidget(QFrame):
    def __init__(self,parent=None,html=BASE_HTML,height=100,width=500,mh=20,mw=50):
        super().__init__(parent)
        self.resize(width,height)
        self.setMaximumHeight(height+mh)
        self.setMaximumWidth(width+mw)
        self.setMinimumWidth(90)
        self.setMinimumHeight(30)

        self.setStyleSheet("border: 1px; background-color: #1d1d1d;")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 10,10)
        
        self.top_bar = QWidget()
        self.top_bar.setFixedHeight(15)
        self.top_layout = QHBoxLayout(self.top_bar)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.addStretch()
        
        self.close_button = QPushButton("\u2716")
        self.close_button.setFixedSize(20, 20)
        self.close_button.setStyleSheet("border: none; font-size: 14px; color: white;")
        self.close_button.clicked.connect(self.close)
        
        self.top_layout.addWidget(self.close_button)
        self.main_layout.addWidget(self.top_bar)

        self.chart = QWebEngineView()
        self.chart.setHtml(html)
        self.main_layout.addWidget(self.chart)

        self.dragging = False
        self.resizing = False
        self.resize_direction = None
        self.offset = QPointF()
        self.setMouseTracking(True)  # Enable mouse tracking

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
            if  self.pos().x() < 0:
                self.move(1,self.pos().y())
                self.dragging=False
            elif self.pos().y() < 0:
                self.move(self.pos().x(),1)
                self.dragging=False
            elif self.pos().x()+self.width() > self.parentWidget().width():
                self.move(self.parentWidget().width()-self.width(),self.pos().y())
                self.dragging=False
            else:     
                self.move(self.mapToParent(event.position().toPoint() - self.offset))
        self.update_cursor(event.position().toPoint())
        print(f"""self.parentWidget().width() : {self.parentWidget().width()}'\n'
                  self.width() : {self.width()} '\n'
                  self.pos().x()+self.width() : {self.pos().x()+self.width()}
              """)


        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.resizing = False

    def enterEvent(self, event):
        if hasattr(QCursor, "pos"):
            self.update_cursor(self.mapFromGlobal(QCursor.pos()))

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

        new_width = max(self.minimumWidth(), self.width() + (dx if right else -dx if left else 0))
        new_height = max(self.minimumHeight(), self.height() + (dy if bottom else -dy if top else 0))
        
        if right or bottom:
            self.resize(new_width, new_height)

    def update_cursor(self, pos, margin=10):
        left, right, top, bottom = self.get_resize_direction(pos, margin)
        
        if right and bottom:
            self.setCursor(Qt.SizeFDiagCursor)
        elif right:
            self.setCursor(Qt.SizeHorCursor)
        elif bottom:
            self.setCursor(Qt.SizeVerCursor)
        else:
            self.setCursor(Qt.ArrowCursor)