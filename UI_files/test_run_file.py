import sys

from UI_files.calenderpopup import Ui_CalenderInputDialog
from UI_files.searchDiagDerived import SearchBox
from UI_files.ButtonCalender import ButtonCalender
from UI_files.SelfLearnQLineEdit import SLQLineEdit
from UI_files.LoginForm import Ui_Dialog
from UI_files.LoginDerived import LoginBox
from PyQt5.QtWidgets import QCalendarWidget, QApplication,QDialog
from UI_files.Billing6 import Ui_MainWindow
from SRC.Main import AppClass

TEST_WIDGET = QCalendarWidget


class WW(TEST_WIDGET,QDialog):
    def __init__(self):
        super(WW, self).__init__()
        # self.setupUi(self)
        self.show()
        # self.pushButton.clicked.connect()
        # self.wid=self.calendarWidget

app = QApplication(sys.argv)
x = LoginBox()
# QCalendarWidget().selectedDate()
# w.show()
app.exec_()

# BELOW => Login Template
# $CHECK => if it's okay to innvoke a application.exec_() instance right after
# some other MainWindow used it
# if x.approved:
#     x.destroy()
#     w = AppClass()
#     w.show()
#     app.exec_()
# # the date attribute persists in the Calender widget....
# # replace this widget in the Main Billing section date selection!
# print("selected date was ",w.end_date,w.start_date)
