from math import floor

from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

class STable(QTableWidget):
    def __init__(self,parent):
        super(STable, self).__init__(parent)
        # self.init_table(self.parent())

    def init_table(self, row=0, cols=0, headers=None):
        if headers is None:
            headers = []
        self.setAlternatingRowColors(True)
        self.setColumnCount(cols)
        self.setRowCount(row)
        self.setFixedWidth(self.parent().width())
        self.setFixedHeight(self.parent().height())
        self.setHorizontalHeaderLabels(headers)

    def LoadTable(self,rdata=None):
        # debugging purpose! remove after debugs!
        if rdata is None:
            rdata = [["asd"] * 6]
        print(rdata[0])
        if len(rdata[0])>self.columnCount():
            raise Exception("Invalid data shape for row")
        self.setColumnCount(len(rdata[0]))
        width=self.parent().width()//len(rdata[0])
        print("width is",width,"paren",self.parent().width)
        self.setRowCount(0)
        rowpos=self.rowCount()
        # rowCount returns the number of rows currently in table
        # add the title code here
        # self.table.insertRow(rowpos)
        rows,cols=self.rowCount(),self.columnCount()
        for x in range(len(rdata)):
            self.insertRow(rowpos)
            for y in range(cols):
                self.setColumnWidth(y,width)
                self.setItem(rowpos,y,QTableWidgetItem(f'{rdata[x][y]}'))
            rowpos+=1


    def clear_table(self,table):
        self.clear()

    # rdata -> An 1D array
    def insert_row(self,rdata:list):
        if len(rdata)>self.columnCount():
            raise Exception("Invalid data shape for row")
        cnt=self.rowCount()
        self.insertRow(cnt)
        width=floor(self.parent().width() / self.columnCount())
        for x in range(len(rdata)):
            self.setColumnWidth(x, width)
            self.setItem(cnt, x, QTableWidgetItem(str(rdata[x])))

    # use int to get a row full of numbers
    def get_row_contents(self, rowid:int, mode="str"):
        try:
            lis=[]
            print("*"*100)
            for x in range(self.columnCount()):
                lis.append(int(self.item(rowid, x).text()) if mode is "int" else self.item(rowid, x).text())
                print("Item fetched ",(self.itemAt(rowid, x).text()))
            print("*" * 100)
            return lis
        except(Exception) as e:
            print("Exception while fecthing rowcontents",e)

    def get_column_contents(self, colid:int, mode="str"):
        try:
            lis=[]
            for x in range(self.rowCount()):
                lis.append(int(self.item(x, colid).text()) if mode is "int" else self.item(x, colid).text())
            return lis
        except(Exception) as e:
            print("Exception while fetching Colcontents ",e)

