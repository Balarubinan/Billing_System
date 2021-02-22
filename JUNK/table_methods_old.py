# self.billing_table.setStyleSheet("alternate-background-color: yellow;background-color: grey;")

# def create_table(self, parent, row=0, cols=0):
#     table = QTableWidget(parent)
#     table.setAlternatingRowColors(True)
#     table.setColumnCount(cols)
#     table.setRowCount(row)
#     table.setFixedWidth(parent.width())
#     table.setFixedHeight(parent.height())
#     return table
#
#
#
# # rdata -> 2D array
# # use this function only when loading data directly from DB as a 2D array
# def LoadTable(self,table,rdata=None):
#     # debugging purpose! remove after debugs!
#     if rdata is None:
#         rdata = [["asd"] * 6]
#     print(rdata[0])
#     if len(rdata[0])>table.columnCount():
#         raise Exception("Invalid data shape for row")
#     table.setColumnCount(len(rdata[0]))
#     width=table.parent().width()//len(rdata[0])
#     print("width is",width,"paren",table.parent().width)
#     table.setRowCount(0)
#     rowpos=table.rowCount()
#     # rowCount returns the number of rows currently in table
#     # add the title code here
#     # self.table.insertRow(rowpos)
#     rows,cols=table.rowCount(),self.table.columnCount()
#     for x in range(len(rdata)):
#         table.insertRow(rowpos)
#         for y in range(cols):
#             table.setColumnWidth(y,width)
#             table.setItem(rowpos,y,QTableWidgetItem(f'{rdata[x][y]}'))
#         rowpos+=1
#
#
# def clear_table(self,table):
#     table.clear()
#
# # rdata -> An 1D array
# def insert_row(self,table:QTableWidget,rdata:list):
#     if len(rdata)>table.columnCount():
#         raise Exception("Invalid data shape for row")
#     cnt=table.rowCount()
#     table.insertRow(cnt)
#     width=floor(table.parent().width()/table.columnCount())
#     for x in range(len(rdata)):
#         table.setColumnWidth(x,width)
#         table.setItem(cnt,x,QTableWidgetItem(str(rdata[x])))
#
# # use int to get a row full of numbers
# def get_row_contents(self,table:QTableWidget,rowid:int,mode="str"):
#     try:
#         lis=[]
#         for x in range(table.columnCount()):
#             lis.append(int(table.itemAt(rowid,x).text()) if mode is "int" else table.itemAt(rowid,x).text())
#         return lis
#     except(Exception) as e:
#         print("Exception while fecthing rowcontents",e)
#
# def get_column_contents(self,table:QTableWidget,colid:int,mode="str"):
#     try:
#         lis=[]
#         for x in range(table.rowCount()):
#             lis.append(int(table.itemAt(x,colid).text()) if mode is "int" else table.itemAt(x,colid).text())
#         return lis
#     except(Exception) as e:
#         print("Exception while fetching Colcontents ",e)
