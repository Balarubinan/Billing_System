import sys

from UI_files.calenderpopup import Ui_CalenderInputDialog
from UI_files.searchDiagDerived import SearchBox
from UI_files.ButtonCalender import ButtonCalender
from UI_files.SelfLearnQLineEdit import SLQLineEdit
from PyQt5.QtWidgets import QCalendarWidget, QApplication,QDialog

TEST_WIDGET = SLQLineEdit

class WW(TEST_WIDGET,QDialog):
    def __init__(self):
        super(WW, self).__init__()
        # self.setupUi(self)
        self.show()
        # self.pushButton.clicked.connect()
        # self.wid=self.calendarWidget

app = QApplication(sys.argv)
w = WW()
# QCalendarWidget().selectedDate()
# w.show()
app.exec_()
# # the date attribute persists in the Calender widget....
# # replace this widget in the Main Billing section date selection!
# print("selected date was ",w.end_date,w.start_date)
