import sys
from PyQt5.QtWidgets import QApplication
from views.home import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()