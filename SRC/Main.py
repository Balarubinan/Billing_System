from math import floor

from PyQt5 import QtCore

from UI_files.Billing3 import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import sys
from UI_files.STable import STable
from UI_files.SelfLearnQLineEdit import SLQLineEdit


# for some reason adding QDialog in the AppClass Creates error !

class AppClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppClass, self).__init__()
        self.setupUi(self)
        self.billing_table=STable(self.TableAreaBottom)
        self.billing_table.init_table(cols=6)

        self.billing_table.insert_row(["this"]*6)
        for x in "Balarubinan":
            self.billing_table.insert_row([x]*6)

        # both work super_fine!!
        # print(self.billing_table.get_row_contents(2))
        # print(self.billing_table.get_column_contents(0))
        # comment and replace all
        # self.CLRNumber = SLQLineEdit(self.BotFrame,Name="CLR learn")
        # self.CLRNumber.setGeometry(QtCore.QRect(1193, 55, 151, 31))
        # self.CLRNumber.setText("")
        # self.CLRNumber.setReadOnly(False)
        # self.CLRNumber.setObjectName("CLRNumber")


try:
    app = QApplication(sys.argv)
    w = AppClass()
    w.show()
    sys.exit(app.exec_())
except(Exception) as e:
    print("Exception in base code ",e)

