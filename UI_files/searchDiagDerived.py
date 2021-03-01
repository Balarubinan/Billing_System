from PyQt5 import QtWidgets

from UI_files.calenderpopup import Ui_CalenderInputDialog
from UI_files.searchdialoginvoice2 import Ui_SearchInvoiceDialog
from UI_files.STable import STable
from SRC.DatabaseFiles.DatabaseFunctions import fetch_from_invoice,write_to_invoice

from datetime import datetime

# the station param will be suppiled
class SearchBox(Ui_SearchInvoiceDialog):
    def __init__(self):
        super(SearchBox, self).__init__()
        self.setupUi(self)
        self.StartDateCal.clicked.connect(self.save_start)
        self.EndDateCal.clicked.connect(self.save_end)
        self.end_date, self.start_date = self.StartDateInvoiceInput.date(),self.EndDateInvoiveInput.date()
        self.resultTable = STable(self.ResultTableView)
        self.resultTable.init_table(cols=11, headers
        =['SNO', 'DATE', 'CLR', 'TO STATION', 'CONSIGNER', 'CONSIGNEE',
          'FREIGHT', 'TOTAL AMT', 'VEH NUMBER', 'INV NO', 'ITEMS'])
        self.InvoiceSearchButton.clicked.connect(self.on_search_clicked)
        # astectic purposes
        # for x in range(10):
        #     self.resultTable.insert_row(["333"] * 5)

    def save_start(self):
        Diag = QtWidgets.QDialog()
        cal_window = Ui_CalenderInputDialog()
        cal_window.setupUi(Diag)
        Diag.exec_()
        val = cal_window.calendarWidget.selectedDate()
        self.StartDateInvoiceInput.setDate(val)
        self.start_date = val


    def save_end(self):
        Diag = QtWidgets.QDialog()
        cal_window = Ui_CalenderInputDialog()
        cal_window.setupUi(Diag)
        Diag.exec_()
        val = cal_window.calendarWidget.selectedDate()
        self.EndDateInvoiveInput.setDate(val)
        self.end_date = val

    def on_search_clicked(self):
        try:
            # data_dict = {
            #     "CNE": "Bala", "CNR": "BAla e", "ToStation": "madurai", "LRType": "PAID", "Items":[],
            #     "branch": "A", "date":datetime(year=2000,day=2,month=11), "CLR": "123", "inv_no": "34", "Totalamt": 1000, "Freight": 500
            # }
            # write_to_invoice(data_dict)
            if len(self.lineEdit.text())>0:
                station=self.lineEdit.text()
            else:
                station=None
            results=fetch_from_invoice(sdate=self.start_date.toPyDate(),edate=self.end_date.toPyDate(),station=station,
                                       branch=self.comboBox.currentText())
            print("fetched",results)
            # print("fetched", len(results))
            for sno,invoice in enumerate(results):
                self.resultTable.insert_row([sno,invoice.date,invoice.CLR,invoice.ToStation,invoice.CNR,
                    invoice.CNE,invoice.Freight,invoice.Totalamt,invoice.inv_no,invoice.Items])
        except(Exception) as e:
            print('ERR SEARCH DIAG ',e)





