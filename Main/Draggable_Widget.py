from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget,QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from PySide6.QtWebEngineWidgets import QWebEngineView
from TradingViewWidgets import *
from pathlib import Path
import json

BASE_HTML = html_chart()

class DraggableWidget(QFrame):
    def __init__(self,parent=None,html=BASE_HTML,height=100,width=500,maxh=20,maxw=50,tab_counter=0,widget_counter=0):
        super().__init__(parent)
        print(f'Created Draggable Widget {tab_counter} {widget_counter}')
        self.tab_counter = tab_counter
        self.widget_counter = widget_counter
        self.info_path = Path('./Configs/DraggableWidgets.json')
        self.resize(width,height)
        self.setMaximumHeight(maxh)
        self.setMaximumWidth(maxw)
        self.setMinimumWidth(30)
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

        self.add_info_about_widget()

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

    def add_info_about_widget(self):

        if self.info_path.exists():
            with open (self.info_path,'r',encoding='utf-8') as f:
                data = json.load(f)
            with open(self.info_path, 'w',encoding='utf-8') as f:
                data[f'Widget {self.tab_counter}{self.widget_counter}'] = {
                        'tab_counter':self.tab_counter,
                        'widget_counter':self.widget_counter,
                        'pos_x':self.mapToParent(self.pos()).x(),
                        'pos_y':self.mapToParent(self.pos()).y()
                        }
                json.dump(data, f, indent=4, ensure_ascii=False)
        else:   
            with open(self.info_path, 'x', encoding='utf-8') as f:
                data = {f'Widget {self.tab_counter}{self.widget_counter}':
                        {
                        'tab_counter':self.tab_counter,
                        'widget_counter':self.widget_counter,
                        'pos_x':self.mapToParent(self.pos()).x(),
                        'pos_y':self.mapToParent(self.pos()).y()
                        }
                    }
                json.dump(data, f, indent=4, ensure_ascii=False)

    def delete_info_about_widget(self):
        with open (self.info_path,'r',encoding='utf-8') as f:
            data = json.load(f)
        with open(self.info_path, 'w',encoding='utf-8') as f:
            data.pop(f'Widget {self.tab_counter}{self.widget_counter}')
            json.dump(data, f, indent=4, ensure_ascii=False)
            
    def closeEvent(self, event):
        self.delete_info_about_widget()
        return super().closeEvent(event)