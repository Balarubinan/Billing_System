from PyQt5.QtGui import QFont

from UI_files.Billing6 import Ui_MainWindow
from SRC.DatabaseFiles.DatabaseFunctions import *
from PyQt5.QtWidgets import *
import sys
from UI_files.STable import STable
from UI_files.searchDiagDerived import SearchBox
from datetime import datetime


# for some reason adding QDialog in the AppClass Creates error !

class AppClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppClass, self).__init__()
        self.setupUi(self)
        font = QFont()
        font.setPointSize(15)
        self.TableAreaTop.setFont(font)
        self.TableAreaTop.update()
        self.billing_table=STable(self.TableAreaBottom)
        self.billing_table.init_table(cols=4, headers=['QTY', 'ITEM', 'RATE', 'SUBTOTAL'])
        self.invoicetoptable = STable(self.TableAreaTop)
        self.invoicetoptable.init_table(cols=11, headers=['SNO', 'DATE', 'CLR', 'TO STATION', 'CONSIGNER', 'CONSIGNEE',
                                                          'FREIGHT', 'TOTAL AMT', 'VEH NUMBER', 'INV NO', 'ITEMS'])
        self.ItemNameInput.returnPressed.connect(self.LoadOrAddItem)
        self.AddItemButton.clicked.connect(self.ItemAdd)
        self.NewLrButton.clicked.connect(self.finaliseCurrentLR)
        self.ItemRateDict = fetch_all_ItemsList()
        self.newitemflag = False
        self.current_total = 0
        self.current_invoice_items = []
        self.QM = QMessageBox()
        self.DateLabel.setText(str(datetime.today()))
        self.last_CLR = get_last_CLR()
        self.CLRNumber.setText(str(self.last_CLR))
        self.itemmode = "new"
        # self.menufile.triggered[QAction].connect(self.fileaction)
        self.actionExit.triggered.connect(self.quit_application)
        self.actionFile_search.triggered.connect(self.search_dialog)

        #
        # self.billing_table.insert_row(["this"]*6)
        # for x in "Balarubinan":
        #     self.billing_table.insert_row([x]*6)

        # both work super_fine!!
        # print(self.billing_table.get_row_contents(2))
        # print(self.billing_table.get_column_contents(0))
        # comment and replace all
        # self.CLRNumber = SLQLineEdit(self.BotFrame,Name="CLR learn")
        # self.CLRNumber.setGeometry(QtCore.QRect(1193, 55, 151, 31))
        # self.CLRNumber.setText("")
        # self.CLRNumber.setReadOnly(False)
        # self.CLRNumber.setObjectName("CLRNumber")

    def quit_application(self, q: QAction):
        # add a confirmation dialog and save current progress hhere
        print("quit app called")

    def search_dialog(self):
        # self.popup=QDialog()
        try:
            # self.popup=QDialog()
            self.searchDiag = SearchBox()
            self.searchDiag.setupUi(self.searchDiag)
            self.searchDiag.initialise_params()
            self.searchDiag.exec_()
            # self.searchDiag.exec_()
        except(Exception) as e:
            print("Error is ", e)

    def show_message(self, msg, title="message"):
        # implement QMessage box call here
        self.QM.setWindowTitle(title)
        self.QM.setText(msg)
        self.QM.exec_()
        print(msg)

    def LoadOrAddItem(self):
        item_name = self.ItemNameInput.text().strip('')
        if item_name in self.ItemRateDict:
            self.RateInput.setText(str(self.ItemRateDict[item_name]))
            self.itemmode = "update"
        else:
            self.itemmode = "new"

    def ItemAdd(self):
        print("Add Item called!")
        name, rate, qty = self.ItemNameInput.text(), self.RateInput.text(), self.QtyInput.text()
        if not rate.replace('.', '', 1).isdecimal() or not qty.replace('.', '', 1).isdecimal():
            self.show_message('Enter only digits for rate and qty!')
            return
        try:
            rate, qty = float(rate), float(qty)
            if self.itemmode is "new":
                # self.newitemflag="update"
                # write_to_item_list(name,rate)
                pass
            elif self.ItemRateDict[name] != str(rate):
                # update_item_list(name,rate)
                pass
                # check if it is okay to do this

            self.ItemRateDict[name] = rate
            subtotal_amt = rate * qty
            self.billing_table.insert_row([qty, name, rate, subtotal_amt])
            self.TotalAmountLabel.setText(str(float(self.TotalAmountLabel.text()) + subtotal_amt))
            self.current_invoice_items.append([qty, name, rate, subtotal_amt])
            print(self.current_invoice_items, "are the current the items")
            print("Add ItemENd")
        except(Exception) as e:
            print("Erorr is ", e)

    def finaliseCurrentLR(self):
        # calculate GST if needed
        try:
            if self.HChargeInput.text().replace('.', '', 1).isdecimal():
                hcharge = float(self.HChargeInput.text())
            else:
                hcharge = 0
            if self.CrossingInput.text().replace('.', '', 1).isdecimal():
                crossing = float(self.CrossingInput.text())
            else:
                crossing = 0

            totalamt = float(self.TotalAmountLabel.text())
            freight = crossing + hcharge
            sno_next = sno_get_next()
            inv_no = get_next_invno()
            # check if CLR nummber is the actuall name of the input widget!!
            CLR, CNE, CNR = self.CLRNumber.text(), self.CNEInput.text(), self.CNRInput.text()
            station = self.ToStationInput.text()
            vechno = self.VechicleNumInput.text()
            lrtype = self.LRTypeInput.currentText()
            # gives a QDate Object
            date = self.DateInput.dateTime()
            # returns a datetime native python object
            date = date.toPyDateTime()
            self.invoicetoptable.insert_row([sno_next, date, CLR, station, CNR, CNE, freight, totalamt, vechno, inv_no,
                                             len(self.current_invoice_items)])
            branch = self.BranchComboBox.currentText()
            data_dict = {
                "CNE": CNE, "CNR": CNR, "ToStation": station, "LRType": lrtype, "Items": self.current_invoice_items,
                "branch": branch, "date": date, "CLR": CLR, "inv_no": inv_no, "Totalamt": totalamt, "Freight": freight,
                "Vehno": vechno
            }
            write_to_invoice(data_dict)
            # clearing all the textfields
            for x in self.BotFrame.children():
                if type(x) == QLineEdit:
                    x.setText("")
            # clearing the table
            # rows are empty but still are there -> remove them too
            # self.billing_table.clear()
            self.billing_table.setRowCount(0)
            # self.billing_table.clear_table()
            # update CLR
            inc_CLR()
            self.last_CLR += 1
            self.CLRNumber.setText(str(self.last_CLR))
        except(Exception) as e:
            print("ERROR ", e)


try:
    app = QApplication(sys.argv)
    w = AppClass()
    w.show()
    sys.exit(app.exec_())
except(Exception) as e:
    print("Exception in base code ",e)

