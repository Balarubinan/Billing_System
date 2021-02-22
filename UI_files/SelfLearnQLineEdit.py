from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import *
import sys
import os
import atexit
# creates error sometimes look to it!!er
import pickle


class SLQLineEdit(QLineEdit):
    def __init__(self, parent, Name, shortCutEnabled=False):
        self.Name = Name
        super(SLQLineEdit, self).__init__(parent)
        self.learn_list = self.load()
        self.autoCompleter = QCompleter(self.learn_list)
        self.setCompleter(self.autoCompleter)
        self.returnPressed.connect(self.OnreturnPressed)
        atexit.register(self.update_learn_list)
        self.textChanged.connect(self.OnTextChange)
        if shortCutEnabled:
            self.shortCutMap = self.load_shortcuts()
        else:
            self.shortCutMap=False

    def load(self):
        try:
            cur_path = os.getcwd()
            with open(f"{cur_path}/list_learner_files/{self.Name}.txt", 'rb') as f:
                data = pickle.load(f)
                print(data)
                return (data)
        except(Exception) as e:
            print("Occuered exception is ", e)
            return ['Null List']

    def load_shortcuts(self):
        # debugging purposes
        # create a file and store the shorcuts and create a window to get all the shortcuts

        return {str(x): f"shortcut{x}" for x in range(16)}

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
        if self.shortCutMap:
            self.setText(self.remove_shortcut_text())
        if self.text() not in self.learn_list:
            # self.learn_list.append(self.text())
            self.learn_list.append(self.text().strip(" "))
            newCompleter = QCompleter(self.learn_list)
            self.setCompleter(newCompleter)
            print("Current learn lis", self.learn_list)
            # self.setText("")
            # self.update_learn_list()

    def OnTextChange(self, text: str) -> None:
        try:
            if text in self.shortCutMap:
                print("Shortcut detected!!")
                self.setText(self.text() + self.shortCutMap[text])
                self.setSelection(1, len(self.text()))
            else:
                print("Plain text change!")
        except(Exception) as e:
            print("Fucked up excpetion", e)


# from SRC.Main import AppClass
import sys


class demoAppClass(QMainWindow):
    def __init__(self):
        super(demoAppClass, self).__init__()
        # self.new_item=SLQLineEdit("vechicleNOOO")
        # self.setLayout(QLayout())
        self.CLRSearchInput = SLQLineEdit(self, Name="CLR learn",shortCutEnabled=True)
        self.CLRSearchInput.setText("Fuekf you")
        print("Ehi from demo class")
        self.show()


app = QApplication(sys.argv)
w = demoAppClass()
w.show()
sys.exit(app.exec_())
