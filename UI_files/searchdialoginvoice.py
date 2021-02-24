# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_dialog_invoice.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UI_files.calenderpopup import Ui_CalenderInputDialog
from UI_files.STable import STable


class Ui_SearchInvoiceDialog(object):
    def setupUi(self, SearchInvoiceDialog):
        SearchInvoiceDialog.setObjectName("SearchInvoiceDialog")
        SearchInvoiceDialog.resize(1109, 726)
        self.ResultTableView = QtWidgets.QTableView(SearchInvoiceDialog)
        self.ResultTableView.setGeometry(QtCore.QRect(480, 20, 601, 681))
        self.ResultTableView.setObjectName("ResultTableView")
        self.label = QtWidgets.QLabel(SearchInvoiceDialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.InvoiceSearchButton = QtWidgets.QPushButton(SearchInvoiceDialog)
        self.InvoiceSearchButton.setGeometry(QtCore.QRect(150, 270, 161, 51))
        self.InvoiceSearchButton.setObjectName("InvoiceSearchButton")
        self.label_2 = QtWidgets.QLabel(SearchInvoiceDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SearchInvoiceDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.StartDateCal = QtWidgets.QPushButton(SearchInvoiceDialog)
        self.StartDateCal.setGeometry(QtCore.QRect(380, 120, 81, 28))
        self.StartDateCal.setObjectName("StartDateCal")
        self.EndDateCal = QtWidgets.QPushButton(SearchInvoiceDialog)
        self.EndDateCal.setGeometry(QtCore.QRect(380, 173, 81, 28))
        self.EndDateCal.setObjectName("EndDateCal")
        self.PrintInvoiceResults = QtWidgets.QPushButton(SearchInvoiceDialog)
        self.PrintInvoiceResults.setGeometry(QtCore.QRect(20, 477, 121, 51))
        self.PrintInvoiceResults.setObjectName("PrintInvoiceResults")
        self.DeleteInvoiceResults = QtWidgets.QPushButton(SearchInvoiceDialog)
        self.DeleteInvoiceResults.setGeometry(QtCore.QRect(180, 477, 130, 51))
        self.DeleteInvoiceResults.setObjectName("DeleteInvoiceResults")
        self.pushButton_6 = QtWidgets.QPushButton(SearchInvoiceDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 477, 111, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.StartDateInvoiceInput = QtWidgets.QDateEdit(SearchInvoiceDialog)
        self.StartDateInvoiceInput.setGeometry(QtCore.QRect(184, 118, 181, 31))
        self.StartDateInvoiceInput.setObjectName("StartDateInvoiceInput")
        self.EndDateInvoiveInput = QtWidgets.QDateEdit(SearchInvoiceDialog)
        self.EndDateInvoiveInput.setGeometry(QtCore.QRect(184, 170, 181, 31))
        self.EndDateInvoiveInput.setObjectName("EndDateInvoiveInput")

        self.retranslateUi(SearchInvoiceDialog)
        self.pushButton_6.clicked.connect(SearchInvoiceDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SearchInvoiceDialog)

        # added code
        self.StartDateCal.clicked.connect(self.save_start)
        self.EndDateCal.clicked.connect(self.save_end)
        self.end_date,self.start_date=None,None
        self.resultTable=STable(self.ResultTableView)
        self.resultTable.init_table(row=0,cols=5)
        # astectic purposes
        for x in range(10):
            self.resultTable.insert_row(["333"]*5)

    def retranslateUi(self, SearchInvoiceDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchInvoiceDialog.setWindowTitle(_translate("SearchInvoiceDialog", "Search Invoices"))
        self.label.setText(_translate("SearchInvoiceDialog", "Search By Date:"))
        self.InvoiceSearchButton.setText(_translate("SearchInvoiceDialog", "SEARCH"))
        self.label_2.setText(_translate("SearchInvoiceDialog", "Start Date:"))
        self.label_3.setText(_translate("SearchInvoiceDialog", "End Date:"))
        self.StartDateCal.setText(_translate("SearchInvoiceDialog", "Calender"))
        self.EndDateCal.setText(_translate("SearchInvoiceDialog", "Calender"))
        self.PrintInvoiceResults.setText(_translate("SearchInvoiceDialog", "PRINT RESULTS"))
        self.DeleteInvoiceResults.setText(_translate("SearchInvoiceDialog", "DELETE RESULTS"))
        self.pushButton_6.setText(_translate("SearchInvoiceDialog", "OKAY"))

    def save_start(self):
        Diag=QtWidgets.QDialog()
        cal_window=Ui_CalenderInputDialog()
        cal_window.setupUi(Diag)
        Diag.exec_()
        val=cal_window.calendarWidget.selectedDate()
        self.StartDateInvoiceInput.setDate(val)
        self.start_date=val

    def save_end(self):

        Diag=QtWidgets.QDialog()
        cal_window=Ui_CalenderInputDialog()
        cal_window.setupUi(Diag)
        Diag.exec_()
        val=cal_window.calendarWidget.selectedDate()
        self.EndDateInvoiveInput.setDate(val)
        self.end_date=val