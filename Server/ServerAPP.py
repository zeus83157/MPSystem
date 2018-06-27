import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ServerUI import Ui_Form
import socket
import threading
import pafy
import vlc
import time

global urllist
urllist = []

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
				self.AddSong(data)
				conn.send(bytes("Success！", encoding = "utf8"))
		
	def stop(self):
		self.status = False
		
	def AddSong(self,url):

		global urllist
		video = pafy.new(url)
		best = video.getbest()
		playurl = best.url
		urllist.append(playurl)
		print(len(urllist))

class MP(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.status = True
		Instance = vlc.Instance()
		self.player = Instance.media_player_new()

	def run(self):
		global urllist
		while self.status:
			if(len(urllist) > 0):
				if(self.player.get_state() == vlc.State.NothingSpecial or self.player.get_state() == vlc.State.Ended):
					if self.player.get_state() == vlc.State.Ended:
						self.player.stop()
					Instance = vlc.Instance()
					self.player = Instance.media_player_new()
					url = urllist.pop(0)
					Media = Instance.media_new(url)
					Media.get_mrl()
					self.player.set_media(Media)
					self.player.play()

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
		self.mp = MP()
		self.mp.start()

	def StopButton_Clicked(self):
		self.stask.stop()
		self.mp.stop()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())