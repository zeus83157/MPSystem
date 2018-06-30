import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui
from ServerUI import Ui_Form
import socket
import threading
import pafy
import vlc
import time
import datetime
import json

global urllist, wiplist, ipmstatus, songnamelist, w
urllist = []
wiplist = []
songnamelist = []
ipmstatus = False

class ServerTask (threading.Thread):
	def __init__(self, ip, port):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.status = True

	def run(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((self.ip, self.port))
		s.listen(1)

		global wiplist,ipmstatus

		while True:
			if not self.status:
				break
			conn, addr = s.accept()

			while True:
				if not self.status:
					break
				data = conn.recv(1024)
				

				if not data: 
					break
				data = str(data, encoding = "utf-8")

				if not ipmstatus or addr[0] in wiplist:
					data = data.replace("\n", "");
					data = json.loads(data)
					self.AddSong(data["url"],data["songname"])
					conn.send(bytes("Success！", encoding = "utf8"))
				

				else:
					conn.send(bytes("Server IP管理功能已啟動\n您的IP不在Server白名單\n請與Server端聯繫", encoding = "utf8"))

		s.shutdown(2)
		s.close()
		
	def stop(self):
		self.status = False
		
	def AddSong(self,url,songname):
		global urllist,songnamelist
		video = pafy.new(url)
		best = video.getbest()
		playurl = best.url
		urllist.append(playurl)
		songnamelist.append(songname)


		w.ui.WTPlistWidget.clear()
		w.ui.WTPlistWidget.addItems(songnamelist)

class MP(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.status = True
		Instance = vlc.Instance()
		self.player = Instance.media_player_new()

	def run(self):
		global urllist,songnamelist
		while self.status:
			if len(urllist) > 0:
				if self.player.get_state() == vlc.State.NothingSpecial or self.player.get_state() == vlc.State.Ended:
					if self.player.get_state() == vlc.State.Ended:
						self.player.stop()
					Instance = vlc.Instance()
					self.player = Instance.media_player_new()
					url = urllist.pop(0)
					Media = Instance.media_new(url)
					Media.get_mrl()
					self.player.set_media(Media)
					self.player.play()

					songname = songnamelist.pop(0)
					w.ui.CurrentSonglineEdit.setText(songname)
					w.ui.WTPlistWidget.clear()
					w.ui.WTPlistWidget.addItems(songnamelist)

					time.sleep(5)
		urllist.clear()
		songnamelist.clear()

	def stop(self):
		self.player.stop()
		self.status = False

		w.ui.WTPlistWidget.clear()
		w.ui.CurrentSonglineEdit.setText("")
			
		

class AppWindow(QDialog):
	def __init__(self):
		
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.ui.IPlineEdit.setText(self.GetIp())
		self.ui.StartButton.clicked.connect(self.StartButton_Clicked)
		self.ui.StopButton.clicked.connect(self.StopButton_Clicked)
		self.ui.EradioButton.toggled.connect(self.EDradioButton_Toggled)
		self.ui.IIPpushButton.clicked.connect(self.IIPpushButton_Clicked)
		self.ui.DIPpushButton.clicked.connect(self.DIPpushButton_Clicked)

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

		if port.isdigit():
			self.ui.StopButton.setEnabled(True)
			self.ui.StartButton.setEnabled(False)
			port = int(port)
			self.stask = ServerTask(ip,port)
			self.stask.start()
			self.mp = MP()
			self.mp.start()
			if self.stask.status:
				self.WriteMessage("伺服器啟動")
		else:
			self.WriteMessage("Port輸入錯誤")

	def StopButton_Clicked(self):
		self.stask.stop()
		self.mp.stop()

		if not self.stask.status:
			self.ui.StartButton.setEnabled(True)
			self.ui.StopButton.setEnabled(False)
			self.WriteMessage("伺服器關閉")

	def WriteMessage(self,msg):
		temp = self.ui.SStextEdit.toPlainText()
		self.ui.SStextEdit.setText(temp + datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S]  ") + msg + "\n")
		self.ui.SStextEdit.moveCursor(QtGui.QTextCursor.End)

	def EDradioButton_Toggled(self):
		global ipmstatus,wiplist
		if self.ui.EradioButton.isChecked():
			self.WriteMessage("IP管理已啟用")
			self.ui.TarIPlineEdit.setEnabled(True)
			self.ui.IIPpushButton.setEnabled(True)
			self.ui.WlistWidget.setEnabled(True)
			self.ui.DIPpushButton.setEnabled(True)

			ipmstatus = True

			self.ReloadIPList()


		if self.ui.DradioButton.isChecked():
			self.WriteMessage("IP管理已停用")
			self.ui.TarIPlineEdit.setEnabled(False)
			self.ui.IIPpushButton.setEnabled(False)
			self.ui.WlistWidget.setEnabled(False)
			self.ui.DIPpushButton.setEnabled(False)

			ipmstatus = False

	def ReloadIPList(self):
		self.ui.WlistWidget.clear()
		self.ui.WlistWidget.addItems(wiplist)

	def IIPpushButton_Clicked(self):
		global wiplist
		targetIP = self.ui.TarIPlineEdit.text()
		if not targetIP in wiplist:
			wiplist.append(targetIP)
			self.WriteMessage("白名單加入" + targetIP)
			self.ReloadIPList()

	def DIPpushButton_Clicked(self):
		global wiplist
		listItems = self.ui.WlistWidget.selectedItems()     
		for item in listItems:
			wiplist.remove(item.text())
			self.ui.WlistWidget.takeItem(self.ui.WlistWidget.row(item))
			self.WriteMessage("白名單移除" + item.text())




app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())