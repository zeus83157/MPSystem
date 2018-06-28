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
        Form.resize(649, 300)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 281))
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
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "IP管理"))

