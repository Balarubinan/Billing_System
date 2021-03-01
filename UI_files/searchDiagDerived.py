from PyQt5 import QtWidgets, QtGui

from UI_files.calenderpopup import Ui_CalenderInputDialog
from UI_files.searchdialoginvoice2 import Ui_SearchInvoiceDialog
from UI_files.STable import STable
from SRC.DatabaseFiles.DatabaseFunctions import fetch_from_invoice, write_to_invoice, del_by_using_record

from datetime import datetime

# the station param will be suppiled
class SearchBox(Ui_SearchInvoiceDialog):
    # def __init__(self):
    def initialise_params(self):
        # super(SearchBox, self).__init__()
        # self.setupUi(self)
        self.StartDateCal.clicked.connect(self.save_start)
        self.EndDateCal.clicked.connect(self.save_end)
        self.end_date, self.start_date = self.StartDateInvoiceInput.date(),self.EndDateInvoiveInput.date()
        self.resultTable = STable(self.ResultTableView)
        # seems to have no effect
        # self.resultTable.resizeRowsToContents()
        self.resultTable.init_table(cols=11, headers
        =['SNO', 'DATE', 'CLR', 'TO STATION', 'CONSIGNER', 'CONSIGNEE',
          'FREIGHT', 'TOTAL AMT', 'VEH NUMBER', 'INV NO', 'ITEMS'])
        self.InvoiceSearchButton.clicked.connect(self.on_search_clicked)
        self.DeleteInvoiceResults.clicked.connect(self.on_delete_results)
        # astectic purposes
        # for x in range(10):
        #     self.resultTable.insert_row(["333"] * 5)

    def save_start(self):
        print("clled in here")
        Diag = QtWidgets.QDialog()
        cal_window = Ui_CalenderInputDialog()
        cal_window.setupUi(Diag)
        Diag.exec_()
        val = cal_window.calendarWidget.selectedDate()
        self.StartDateInvoiceInput.setDate(val)
        self.start_date = val
        print("clled in here")


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
            #     "branch": "A", "date":datetime(year=2000,day=2,month=11), "CLR": "123", "inv_no": "34", "Totalamt": 1000, "Freight": 500,
            #     "Vehno":"TN89 A456"
            # }
            # write_to_invoice(data_dict)
            self.resultTable.setRowCount(0)
            if len(self.lineEdit.text())>0:
                station=self.lineEdit.text()
            else:
                station=None
            self.results = fetch_from_invoice(sdate=self.start_date.toPyDate(), edate=self.end_date.toPyDate(),
                                              station=station,
                                              branch=self.comboBox.currentText())
            print("fetched", self.results)
            # print("fetched", len(results))
            for sno, invoice in enumerate(self.results):
                sno += 1
                self.resultTable.insert_row([sno, invoice.date, invoice.CLR, invoice.ToStation, invoice.CNR,
                                             invoice.CNE, invoice.Freight, invoice.Totalamt, invoice.Vehno,
                                             invoice.inv_no, len(invoice.Items)], mode="no_fit")
        except(Exception) as e:
            print('ERR SEARCH DIAG ',e)

    def on_delete_results(self):
        # works fine
        # delete the selected rows in the results!
        # add code to delete the selected row from Db using inv_no
        for x in self.results:
            del_by_using_record(x)
        self.resultTable.clear()
        self.results = None
        # self.resultTable.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        # rows=self.resultTable.selectionModel().selectedRows()
        # print(rows)
        # print([x.data() for x in rows])
        # for x in rows:
        #     self.resultTable.removeRow(x.row())

# somthig error in the table out put check that bug -> fixed!
# everything besides that works cool
