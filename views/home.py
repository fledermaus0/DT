
from PyQt5.QtWidgets import  QMainWindow,QWidget, QVBoxLayout, QLabel, QPushButton ,QGridLayout
from PyQt5.QtGui import QIcon, QGuiApplication, QPixmap,QFont
from PyQt5.QtCore import Qt
from views.component.MenuButton import MenuButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.setWindowTitle("Datasets Tool")  
        self.setWindowIcon(QIcon("/icons/logo.png")) 
        self.set_default_size()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.create_sections(layout)
        

    def set_default_size(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        default_width = int(screen_geometry.width() * 0.8)  # Set the width as 70% of the screen width
        default_height = int(screen_geometry.height() * 0.8)  # Set the height as 70% of the screen height

        self.setGeometry(screen_geometry.center().x() - default_width // 2,
                          screen_geometry.center().y() - default_height // 2,
                          default_width, default_height)

    def create_sections(self, layout):
        
        
        section1 = QLabel()
        section1.setAlignment(Qt.AlignCenter)
        section1.setMinimumHeight(int(self.height() * 0.2))
        section1.setMaximumHeight(int(self.height() * 0.2))

        pixmap = QPixmap("icons/logo.svg")
        if not pixmap.isNull():
            section1.setPixmap(pixmap.scaled(section1.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            section1.setText("Logo Image Not Found")

        layout.addWidget(section1)

        section2 = QWidget()
        section2.setStyleSheet("background-color: green;")  
        section2_layout = QGridLayout(section2)
        for i in range(4):
            for j in range(4):

                button = MenuButton(f"Button {i*12 + j + 1}", "icons/logo.png", "#007bff", "#00aaff")
                self.buttons.append(button)
                section2_layout.addWidget(button, i, j)

        layout.addWidget(section2)

        section3 = QLabel("© fledermaus. All rights reserved.")
        section3.setAlignment(Qt.AlignCenter)
        section3.setStyleSheet("background-color: gray;")  # Customize the background color
        section3.setFont(QFont("Arial", 12))  # Customize the font
        section3.setMinimumHeight(int(self.height() * 0.1))
        section3.setMaximumHeight(int(self.height() * 0.1))
        layout.addWidget(section3)         

        @property
        def Button(self,index):
            return self.buttons[index]
        
    