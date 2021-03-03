# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login Form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(803, 263)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 160, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.LoginPassInput = QtWidgets.QLineEdit(Dialog)
        self.LoginPassInput.setGeometry(QtCore.QRect(420, 150, 311, 41))
        self.LoginPassInput.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.LoginPassInput.setInputMask("")
        self.LoginPassInput.setObjectName("LoginPassInput")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(330, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.LoginUserNameInput = QtWidgets.QLineEdit(Dialog)
        self.LoginUserNameInput.setGeometry(QtCore.QRect(420, 90, 311, 41))
        self.LoginUserNameInput.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.LoginUserNameInput.setObjectName("LoginUserNameInput")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 821, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.LoginForgotButton = QtWidgets.QPushButton(Dialog)
        self.LoginForgotButton.setGeometry(QtCore.QRect(30, 220, 111, 28))
        self.LoginForgotButton.setObjectName("LoginForgotButton")
        self.LoginButton = QtWidgets.QPushButton(Dialog)
        self.LoginButton.setGeometry(QtCore.QRect(640, 220, 93, 28))
        self.LoginButton.setObjectName("LoginButton")
        self.LoginExitButton = QtWidgets.QPushButton(Dialog)
        self.LoginExitButton.setGeometry(QtCore.QRect(540, 220, 93, 28))
        self.LoginExitButton.setObjectName("LoginExitButton")

        self.retranslateUi(Dialog)
        self.LoginExitButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "PASSWORD:"))
        self.label_4.setText(_translate("Dialog", "USER NAME:"))
        self.label_5.setText(_translate("Dialog", "LOGIN"))
        self.LoginForgotButton.setText(_translate("Dialog", "Forgot Password"))
        self.LoginButton.setText(_translate("Dialog", "Login"))
        self.LoginExitButton.setText(_translate("Dialog", "Exit"))
