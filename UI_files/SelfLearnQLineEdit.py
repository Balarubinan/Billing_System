import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont,QStandardItem,QStandardItemModel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import *
import sys
import os
import atexit
# creates error sometimes look to it!!er
import pickle
import codecs
from tamil import utf8
# suggestion for tamil are not working properly




class SLQLineEdit(QLineEdit):
    def __init__(self, parent, Name, shortCutEnabled=False):
        self.Name = Name
        # setting readonly to avoid entering characters
        super(SLQLineEdit, self).__init__(parent)
        # self.setReadOnly(True)
        if shortCutEnabled:
            self.shortCutMap = self.load_shortcuts()
        else:
            self.shortCutMap={}

        self.learn_list = self.load()
        # self.model = QStandardItemModel()
        # self.model.appendRow([QStandardItem(str(text)) for text in self.learn_list])
        # self.model.appendRow([QStandardItem(str(text)) for text in self.learn_list])
        self.autoCompleter = QCompleter(self.learn_list)
        # self.autoCompleter = QCompleter(self.model,self)
        # self.autoCompleter.setFilterMode()
        # self.autoCompleter.setCaseSensitivity()
        # self.autoCompleter.setCompletionMode(QCompleter.InlineCompletion)
        self.setCompleter(self.autoCompleter)
        self.returnPressed.connect(self.OnreturnPressed)
        atexit.register(self.update_learn_list)
        # self.textChanged.connect(self.OnTextChange)
        # these don't work!
        self.textEdited.connect(self.OnTextChange)
        # self.editingFinished.connect(self.onEdit)

    def load(self):
        try:
            cur_path = os.getcwd()
            with open(f"{cur_path}/list_learner_files/{self.Name}.txt", 'rb') as f:
                data = pickle.load(f)
                print(data)
                return (data)
        except(Exception) as e:
            print("Occuered exception is ", e)
            return ['Null']

    def load_shortcuts(self):
        # debugging purposes
        # create a file and store the shorcuts and create a window to get all the shortcuts
        # YAY works for tamil text too
        with open("C:\\Users\\Balarubinan\\PycharmProjects\\Billing_system\\UI_files\\list_learner_files\\station_list.txt",'r',encoding="utf-8") as f:
            return {str(x+1):y for x,y in enumerate(f.readlines())}

    def get_tamil_str(self,string):
        l=utf8.get_letters(string)
        print(l)
        return ''.join(l)

    def update_learn_list(self):
        cur_path = os.getcwd()
        try:
            print("Update learn list Calleed!")
            with open(f"{cur_path}/list_learner_files/{self.Name}.txt", 'wb') as f:
                # lis=filter(lambda x:x not in old_lis,self.learn_list)
                # for x in self.learn_list:
                #     f.write(x+"\n")
                pickle.dump(self.learn_list, f)
        except(Exception) as e:
            print("Filel not found!!", e)

    def remove_shortcut_text(self):
        return ''.join([x for x in self.text() if x not in self.shortCutMap])

    def OnreturnPressed(self):
        try:
            if self.shortCutMap:
                self.setText(self.remove_shortcut_text())
            # if not self.model.findItems(self.text()):
            #     print("Aded to list")
            #     self.model.appendRow(QStandardItem(self.text().strip(" ")))
            #     self.learn_list.append(self.text().strip(" "))
            if self.text() not in self.learn_list:
                self.learn_list.append(self.text().strip(" "))
                # self.learn_list.append(self.get_tamil_str(self.text().strip(" ")))
                # newCompleter = QCompleter(self.learn_list)
                self.autoCompleter = QCompleter(self.learn_list)
                self.setCompleter(self.autoCompleter)
                # self.autoCompleter.setCompletionMode(QCompleter.InlineCompletion)
                self.autoCompleter.setCompletionMode(QCompleter.PopupCompletion)
                print("Current learn lis", self.learn_list)
                self.setText(")")
                # self.update_learn_list()
        except(Exception) as e:
            print("Excpetion ",e)

    def onEdit(self):
        print("Edditign fucn")

    def OnTextChange(self, text: str) -> None:
        print("Caaledn")
        try:
            if text in self.shortCutMap:
                print("Shortcut detected!!",text)
                self.setText(self.text() + self.shortCutMap[text])
                self.setSelection(1, len(self.text()))
            else:
                print("Plain text change!",text)
        except(Exception) as e:
            print("Fucked up excpetion", e)

    # def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
    #     try:
    #
    #         # print(chr(event.key()))
    #         if event.key() in (QtCore.Qt.Key_Backspace,QtCore.Qt.Key_Enter,QtCore.Qt.Key_Return):
    #             pass
    #         else:
    #             self.setText(self.text()+chr(event.key()))
    #             self.OnTextChange(self.text())
    #
    #         if event.key() in (QtCore.Qt.Key_Return,QtCore.Qt.Key_Enter):
    #             print("Killing")
    #             self.OnreturnPressed()
    #             # self.deleteLater()
    #         if event.key()==QtCore.Qt.Key_Backspace:
    #             self.setText(self.text()[:len(self.text())-1])
    #         event.accept()
    #     except(Exception) as e:
    #         print("Error is ",e)



# from SRC.Main import AppClass
import sys


class demoAppClass(QMainWindow):
    def __init__(self):
        super(demoAppClass, self).__init__()
        # self.new_item=SLQLineEdit("vechicleNOOO")
        # self.setLayout(QLayout())
        self.CLRSearchInput = SLQLineEdit(self, Name="CLR learn",shortCutEnabled=True)
        # self.CLRSearchInput.setText("Fuekf you")
        self.CLRSearchInput.setFixedHeight(50)
        self.CLRSearchInput.setFixedWidth(400)
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        print("Ehi from demo class")
        self.show()


app = QApplication(sys.argv)
w = demoAppClass()
w.show()
sys.exit(app.exec_())
