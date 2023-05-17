from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

class FileDropView(QWidget):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton("Drop File Here")
        layout.addWidget(self.button)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.button.setText(f"Dropped File: {file_path}")

class FileSearchView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton("Search File")
        layout.addWidget(self.button)

        self.button.clicked.connect(self.searchFile)

    def searchFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            self.button.setText(f"Selected File: {file_path}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Views Example")
        self.setGeometry(300, 300, 400, 200)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        file_drop_view = FileDropView()
        file_search_view = FileSearchView()

        layout.addWidget(file_drop_view)
        layout.addWidget(file_search_view)

        self.setCentralWidget(central_widget)

