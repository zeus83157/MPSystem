import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ClientUI import Ui_Form
import socket
import threading


class ClientTask(threading.Thread):
	def __init__(self, ip, port, url):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.url = url

	def run(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((self.ip, self.port))
			cmd = self.url
			s.send(bytes(cmd, encoding = "utf8"))
			data = s.recv(1024)
			data = str(data, encoding = "utf-8")
			print (data)
			s.close()
		except Exception as e:
			print(e)

class AppWindow(QDialog):
	def __init__(self):

		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.SubmitButton.clicked.connect(self.SubmitButton_Clicked)
		self.show()


	def SubmitButton_Clicked(self):
		ip = self.ui.IPlineEdit.text()
		port = int(self.ui.PortlineEdit.text())
		url = self.ui.UrllineEdit.text()

		ctask = ClientTask(ip, port, url)
		ctask.start()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())