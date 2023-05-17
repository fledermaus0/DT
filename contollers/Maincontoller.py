from views.JoinDatasets import MainWindow

class MainController:
    def __init__(self, view):
        self.view = view
        self.view.buttons[0].clicked.connect(self.showView1)

    def h_close(self, event):
        self.viewsetEnabled(True)
        event.accept()
    
    def showView1(self):
        modal_view = MainWindow()
       
        self.view.setEnabled(False)
        modal_view.closeEvent=self.h_close
        modal_view.show()



if __name__ == '__main__':
    controller = MainController()
    controller.view.show()
