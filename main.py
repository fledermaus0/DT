import sys
from PyQt5.QtWidgets import QApplication
from views.home import MainWindow
from contollers.Maincontoller import MainController

app = QApplication(sys.argv)
window = MainWindow()
con = MainController(window)

window.show()
app.exec_()