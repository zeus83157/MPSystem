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
        Form.resize(620, 113)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 91))
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
        self.StopButton.setObjectName("StopButton")
        self.verticalLayout.addWidget(self.StopButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MPSystem-Server"))
        self.label_2.setText(_translate("Form", "IP"))
        self.label_3.setText(_translate("Form", "Port"))
        self.StartButton.setText(_translate("Form", "Start"))
        self.StopButton.setText(_translate("Form", "Stop"))

