# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 308)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 18pt \"Agency FB\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.IPlineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.IPlineEdit.setEnabled(False)
        self.IPlineEdit.setObjectName("IPlineEdit")
        self.horizontalLayout.addWidget(self.IPlineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 18pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.PortlineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PortlineEdit.setObjectName("PortlineEdit")
        self.horizontalLayout.addWidget(self.PortlineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.StartButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartButton.setObjectName("StartButton")
        self.verticalLayout.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StopButton.setEnabled(False)
        self.StopButton.setObjectName("StopButton")
        self.verticalLayout.addWidget(self.StopButton)
        self.SStextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.SStextEdit.setEnabled(True)
        self.SStextEdit.setReadOnly(True)
        self.SStextEdit.setObjectName("SStextEdit")
        self.verticalLayout.addWidget(self.SStextEdit)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 601, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget.setEnabled(False)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 281, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.DradioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.DradioButton_2.setGeometry(QtCore.QRect(10, 20, 83, 31))
        self.DradioButton_2.setChecked(True)
        self.DradioButton_2.setObjectName("DradioButton_2")
        self.EradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.EradioButton.setGeometry(QtCore.QRect(130, 20, 83, 31))
        self.EradioButton.setObjectName("EradioButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 601, 234))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_9.addWidget(self.listWidget_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MPSystem-Server"))
        self.label_2.setText(_translate("Form", "IP"))
        self.label_3.setText(_translate("Form", "Port"))
        self.StartButton.setText(_translate("Form", "Start"))
        self.StopButton.setText(_translate("Form", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "伺服器設定"))
        self.label.setText(_translate("Form", "目標  IP："))
        self.pushButton.setText(_translate("Form", "加入"))
        self.label_4.setText(_translate("Form", "白名單："))
        self.pushButton_2.setText(_translate("Form", "移除"))
        self.DradioButton_2.setText(_translate("Form", "停用"))
        self.EradioButton.setText(_translate("Form", "啟用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "IP管理"))
        self.label_6.setText(_translate("Form", "現在播放："))
        self.label_5.setText(_translate("Form", "待播列表："))
        self.pushButton_3.setText(_translate("Form", "刪歌"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "媒體管理"))

