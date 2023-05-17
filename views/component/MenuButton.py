from PyQt5.QtWidgets import QPushButton,QSizePolicy
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt, QSize


class MenuButton(QPushButton):
    def __init__(self, text, icon_path, color, parent=None):
        super().__init__(parent)

        self.setText(text)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(56, 56))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(f"""
            QPushButton {{
                outline: none;
                background-color: #fff;
                border: 1px solid color;
                border-radius: 4px;
                color: #000;
                font-size: 16px;
                padding: 12px 16px;

            }}

            QPushButton:hover {{
                background-color: #fff;
                color : {color} ;
                border: 2px solid {color};
                border-radius: 4px;
                font-weight: bold;
            }}
        """)

                
                



