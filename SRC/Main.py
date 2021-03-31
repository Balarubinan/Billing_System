from PyQt5.QtGui import QFont, QKeySequence

from UI_files.Billing7 import Ui_MainWindow
from SRC.DatabaseFiles.DatabaseFunctions import *
from PyQt5.QtWidgets import *
import sys
from UI_files.STable import STable
from UI_files.searchDiagDerived import SearchBox
from UI_files.ButtonCalender import ButtonCalender
from datetime import datetime
from SRC.miscfunctions import *


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
        self.billing_table.init_table(cols=4, headers=['QTY', 'ITEM', 'RATE', 'SUBTOTAL'], row=1)
        self.invoicetoptable = STable(self.TableAreaTop)
        self.invoicetoptable.init_table(cols=11, headers=['SNO', 'DATE', 'CLR', 'TO STATION', 'CONSIGNER', 'CONSIGNEE',
                                                          'FREIGHT', 'TOTAL AMT', 'VEH NUMBER', 'INV NO', 'ITEMS'])
        # self.ItemNameInput.returnPressed.connect(self.LoadOrAddItem)
        # self.AddItemButton.clicked.connect(self.ItemAdd)
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
        self.InvoiceDate = ButtonCalender(self.InvoiceTopFrame)
        # Tab_2
        self.InvoiceTable = STable(self.InvoiceMainTableView)
        self.InvoiceTable.init_table(cols=11, headers=['SNO', 'DATE', 'CLR', 'TO STATION', 'CONSIGNER', 'CONSIGNEE',
                                                       'FREIGHT', 'TOTAL AMT', 'VEH NUMBER', 'INV NO', 'ITEMS'])

        # self.MainTabWidget.tabBarClicked.connect(self.init_tab_2)
        self.PrintInvoiceNumInput.textChanged.connect(self.add_search_results)

        # data_dict = {
        #     "CNE": "Bala", "CNR": "BAla e", "ToStation": "madurai", "LRType": "PAID", "Items":[],
        #     "branch": "A", "date":datetime(year=2000,day=2,month=11), "CLR": "123", "inv_no": "37", "Totalamt": 1000, "Freight": 500,
        #     "Vehno":"TN89 A456"
        # }
        # write_to_invoice(data_dict)
        #

        # self.comboBox is the Invoice station box
        # self.tab_2.isActiveWindow.connect(self.InvoiceSectionOpen)
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
        self.invoicetoptable.itemClicked.connect(self.load_prev_LR)
        self.billing_table.cellChanged.connect(self.check_end_LR)

    def check_end_LR(self, row, column):
        # checks if the current cell is last cell if so insert a blank row
        # else is the current cell is the first cell then check if the cell is blank
        # if yes then proceed to create new LR
        try:
            currow = self.billing_table.currentRow()
            print(row, column, "gdg", currow)
            # FIX :
            # a always returns the first cell's id -> Why?? the hell??
            if column == 3:
                r = self.billing_table.rowCount()
                self.billing_table.setRowCount(r + 1)
                # self.billing_table.item(currow,column).setFocus()
                self.billing_table.setCurrentCell(currow + 1, 0)
                a = self.billing_table.item(currow, column)
                a.setFocus()
            if self.billing_table.currentItem().text() == "":
                self.HChargeInput.setFocus()

            # self.billing_table.insertRow(r+1)

        except(Exception) as e:
            print("ERROR ", e)

    def define_shorcuts(self):
        """create al shorcuts here and display all of them in the display window"""
        # shorcut examples
        # define new shortcuts here
        self.quitSc = QShortcut(QKeySequence('Ctrl+Y'), self)
        self.quitSc.activated.connect(self.quit_application)
        pass

    def quit_application(self, q: QAction):
        # add a confirmation dialog and save current progress hhere

        print("quit app called")
        self.close()

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
        # implementing QMessage box
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
        if not validate_decimal(rate) or not validate_decimal(qty):
            self.show_message('Enter only digits for rate and qty!')
            return
        try:
            rate, qty = float(rate), float(qty)
            if self.itemmode is "new":
                # self.newitemflag="update"
                write_to_item_list(name, rate)
            elif name in self.ItemRateDict and self.ItemRateDict[name] != str(rate):
                update_item_list(name, rate)
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

    def finaliseCurrentLR(self, mode=None):
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
            # sno_next = sno_get_next()
            sno_next = self.invoicetoptable.rowCount() + 1
            # inv_no is not needed here
            # inv_no = get_next_invno()
            inv_no = ""
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
            # the above line shows the number of unique items ie item1 -> 20 ,item2 -> 10 will
            # be shown as 2 items in the items column in the invoice top table
            branch = self.BranchComboBox.currentText()
            data_dict = {
                "CNE": CNE, "CNR": CNR, "ToStation": station, "LRType": lrtype, "Items": self.current_invoice_items,
                "branch": branch, "date": date, "CLR": CLR, "inv_no": "", "Totalamt": totalamt, "Freight": freight,
                "Vehno": vechno, "Hcharge": hcharge, "Crossing": crossing
            }
            # mdoe always falls to else part check it
            if mode is None:
                write_to_invoice(data_dict)
            else:
                update_by_CLR(CLR, data_dict)
            # clearing all the textfields
            for x in self.BotFrame.children():
                if type(x) == QLineEdit:
                    x.setText("")
            # clearing the table
            # self.billing_table.clear()
            self.billing_table.setRowCount(0)
            # self.billing_table.clear_table()
            # update CLR
            inc_CLR()
            self.last_CLR += 1
            self.CLRNumber.setText(str(self.last_CLR))
        except(Exception) as e:
            print("ERROR ", e)

    def add_search_results(self):
        try:
            self.InvoiceTable.setRowCount(0)
            station, branch = self.InvoiceStationInput.text(), self.InvoiceBranchCode.currentText()
            date = self.InvoiceDate.getDate()
            if None in (station, branch, date):
                return
            else:
                print(station, date, branch)
                res = fetch_from_invoice(station=station, sdate=date, edate=date, branch=branch)
                print("res arraay is", [x for x in res])
                for sno, x in enumerate(res):
                    self.InvoiceTable.insert_row(
                        [sno + 1, date, x.CLR, x.ToStation, x.CNR, x.CNE, x.Freight, x.Totalamt, x.Vehno, x.inv_no,
                         len(x.Items)])
        except(Exception) as e:
            print("Error init_tab2", e)

    def load_prev_LR(self):
        # rowind returns a set of index objects each having the attrib .row()
        # works us the item CLR to fetch the LR and show it to the corresponding texts
        # in the LR form below....
        # on Click New LR just save the current LR
        try:
            # to stop use from accidentally modifying the LR
            self.CLRNumber.setReadOnly(True)
            rowind = self.invoicetoptable.selectedIndexes()
            res = self.invoicetoptable.get_row_contents(rowind[0].row())
            # in the InvoicetopTable the CLR number is in the 3rd column
            # so use 22 as the index
            print(res[2], "Is the CLR number", type(res[2]))
            results = fecth_by_CLR(int(res[2]))
            # print(len(results))
            # an array returned but only one Object is expected
            print([x for x in results])
            result: Invoice = [x for x in results][0]
            self.CNRInput.setText(result.CNR)
            self.CNEInput.setText(result.CNE)
            self.CrossingInput.setText(str(result.Crossing))
            self.HChargeInput.setText(str(result.Hcharge))
            self.TotalAmountLabel.setText(str(result.Totalamt))
            self.ToStationInput.setText(result.ToStation)
            self.DateInput.setDate(result.date)
            self.VechicleNumInput.setText(result.Vehno)

            for x in result.Items:  # type:InvoiceItems
                # x:InvoiceItems
                self.billing_table.insert_row([x.qty, x.name, x.rate, str(float(x.qty) * float(x.rate))])

            self.CLRNumber.setReadOnly(False)
        except(Exception) as e:
            print("ERROR LOAD ", e)


try:
    app = QApplication(sys.argv)
    w = AppClass()
    w.show()
    sys.exit(app.exec_())
except(Exception) as e:
    print("Exception in base code ", e)

# Create a new Design
# change Tab policy
# Re-model Layout for auto resizing
# Add Qwidget space in the main UI
