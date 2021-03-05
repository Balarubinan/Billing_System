from UI_files.LoginForm import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class LoginBox(Ui_Dialog, QDialog):
    def __init__(self):
        super(LoginBox, self).__init__()
        self.setupUi(self)
        self.show()
        self.LoginButton.clicked.connect(self.check_pass)
        self.LoginForgotButton.clicked.connect(self.forgot_pass)
        self.approved = False

    def check_pass(self):
        if (self.LoginUserNameInput.text(), self.LoginPassInput.text()) == ("admin", "SYSadmin"):
            print("Login Success!")
            self.approved = True
            self.close()
        else:
            self.LoginPassInput.setText("")
            print("Wrong pass")

    def forgot_pass(self):
        print("Forgot pass invoked!!")
