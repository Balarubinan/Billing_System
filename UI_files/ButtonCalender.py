from PyQt5.QtWidgets import QPushButton,QCalendarWidget,QDialog
from UI_files.calenderpopup import Ui_CalenderInputDialog

class ButtonCalender(QPushButton):
    def __init__(self):
        super(ButtonCalender, self).__init__()
        self.setText("--select date--")
        self.clicked.connect(self.OnClick)
        self.selected_date=None
        # self.resize(500,500)

    def OnClick(self):
        self.w=QDialog()
        self.cal=Ui_CalenderInputDialog()
        self.cal.setupUi(self.w)
        self.w.exec_()
        self.selected_date=self.cal.calendarWidget.selectedDate()
        self.setText(str(self.selected_date.toPyDate()))

    def getDate(self):
        if self.selected_date is not None:
            return self.selected_date.toPyDate()
        else:
             return None