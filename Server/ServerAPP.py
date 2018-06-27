import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ServerUI import Ui_Form
import socket

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