# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calender_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalenderInputDialog(object):
    def setupUi(self, CalenderInputDialog):
        CalenderInputDialog.setObjectName("CalenderInputDialog")
        CalenderInputDialog.resize(446, 325)
        self.calendarWidget = QtWidgets.QCalendarWidget(CalenderInputDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 5, 421, 241))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(CalenderInputDialog)
        self.pushButton.setGeometry(QtCore.QRect(117, 260, 210, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(CalenderInputDialog)
        self.pushButton.clicked.connect(CalenderInputDialog.close)
        QtCore.QMetaObject.connectSlotsByName(CalenderInputDialog)

    def retranslateUi(self, CalenderInputDialog):
        _translate = QtCore.QCoreApplication.translate
        CalenderInputDialog.setWindowTitle(_translate("CalenderInputDialog", "Select Date"))
        self.pushButton.setText(_translate("CalenderInputDialog", "OKAY"))
