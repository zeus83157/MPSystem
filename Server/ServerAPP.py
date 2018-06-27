import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ServerUI import Ui_Form
import socket
import threading
import pafy
import vlc

class ServerTask (threading.Thread):
		def __init__(self, ip, port):
			threading.Thread.__init__(self)
			self.ip = ip
			self.port = port
			self.status = True

		def run(self):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind((self.ip, self.port))
			s.listen(5)
			while True:
				if not self.status:
					break
				conn, addr = s.accept()

				while True:
					if not self.status:
						break
					data = conn.recv(1024)
					if (not data): 
						break
					data = str(data, encoding = "utf-8")
					print(data)
					conn.send(bytes("Hello" + data, encoding = "utf8"))
		def stop(self):
			self.status = False
		

class AppWindow(QDialog):
	def __init__(self):

		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.ui.IPlineEdit.setText(self.GetIp())
		self.ui.StartButton.clicked.connect(self.StartButton_Clicked)
		self.ui.StopButton.clicked.connect(self.StopButton_Clicked)

		self.show()

	def GetIp(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 80))
			ip = s.getsockname()[0]
		finally:
			s.close()
		return ip

	def StartButton_Clicked(self):
		ip = self.ui.IPlineEdit.text()
		port = self.ui.PortlineEdit.text()
		port = int(port)
		self.stask = ServerTask(ip,port)
		self.stask.start()

	def StopButton_Clicked(self):
		self.stask.stop()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())