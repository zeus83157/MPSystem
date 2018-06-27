import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ClientUI import Ui_Form

class AppWindow(QDialog):
    def __init__(self):

        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())