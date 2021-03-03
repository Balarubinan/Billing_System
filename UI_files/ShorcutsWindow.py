# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShorcutsDisplayWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 536)
        self.ShortcutsTextView = QtWidgets.QPlainTextEdit(Dialog)
        self.ShortcutsTextView.setGeometry(QtCore.QRect(0, 10, 781, 511))
        self.ShortcutsTextView.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.ShortcutsTextView.setReadOnly(True)
        self.ShortcutsTextView.setObjectName("ShortcutsTextView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shorcuts"))
