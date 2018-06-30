# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 227)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 208))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.IPlineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.IPlineEdit.setObjectName("IPlineEdit")
        self.horizontalLayout.addWidget(self.IPlineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.PortlineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PortlineEdit.setObjectName("PortlineEdit")
        self.horizontalLayout.addWidget(self.PortlineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.UrllineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.UrllineEdit.setObjectName("UrllineEdit")
        self.horizontalLayout_2.addWidget(self.UrllineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.SubmitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.verticalLayout.addWidget(self.SubmitButton)
        self.CStextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.CStextEdit.setFont(font)
        self.CStextEdit.setObjectName("CStextEdit")
        self.verticalLayout.addWidget(self.CStextEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MPSystem-Client"))
        self.label_2.setText(_translate("Form", "IP"))
        self.label_3.setText(_translate("Form", "Port"))
        self.label.setText(_translate("Form", "YoutubeUrl"))
        self.SubmitButton.setText(_translate("Form", "Submit"))

