from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from main_window import Ui_Dialog
from addUser_window import Ui_AddUser
from exist_user_window import Ui_ExistUser
#import lang
from sys import argv
from random import randint
import sqlite3
import check_files
import json

class ExistUserWindow(QWidget, Ui_ExistUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(lambda: self.close())
        self.change_language()


    def change_language(self):
        self.language = languages[config['language']]
        self.messageLabel.setText(self.language['existUserText'])

class AddUserWindow(QWidget, Ui_AddUser):
    pushButton = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(lambda: self.close())
        self.addUser.clicked.connect(self.adduser_action)
        self.change_language()

    def change_language(self):
        self.language = languages[config['language']]
        self.addUserBox.setTitle(self.language['addUserGroup'])
        self.cancel.setText(self.language['cancel'])
        self.addUser.setText(self.language['addUser'])

    def adduser_action(self):
        self.pushButton.emit(self.addUserEdit.text())
        self.close()




class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.languages = languages

        #  Buttons
        self.exitButton.clicked.connect(self.exit_action)
        self.startButton.clicked.connect(self.start)
        self.homeButton.clicked.connect(self.home)
        self.answerButton1.clicked.connect(self.check_answer)
        self.answerButton2.clicked.connect(self.check_answer)
        self.answerButton3.clicked.connect(self.check_answer)
        #self.examRButton.toggled.connect(self.check_mode)
        self.answer_button_group = [self.answerButton1, self.answerButton2, self.answerButton3]
        self.addUserButton.clicked.connect(self.add_user_window)

        #CheckBox
        self.addCheckBox.click()

        #  ComboBox
        self.comboBox.clear()
        for self.i in self.languages.keys():
            self.comboBox.addItem(self.i)
        self.comboBox.currentTextChanged.connect(self.change_language)

        #  Counter
        self.right_count = 0
        self.wrong_count = 0
        self.stateCount = True
        self.counter = 0
        self.comboBox.setCurrentText(config['language'])
        self.change_language()
        self.home()


    def home(self):
        #  Hide elements
        self.actionLabel.hide()
        self.answerLabel.hide()
        self.answerButton1.hide()
        self.answerButton2.hide()
        self.answerButton3.hide()
        self.homeButton.hide()
        self.statButton.hide()
        self.techRButton.hide()
        self.messageGroupBox.hide()

        # Show elements
        #self.vline.show()
        self.actionGroup.show()
        self.comboBox.show()
        self.labelLanguage.show()
        self.lineLabel_2.show()
        self.modeGroup.show()
        self.startButton.show()
        self.statButton.show()
        self.userGroupBox.show()
        self.rebase_user_box()

    def rebase_user_box(self):
        self.comboBox_2.clear()
        for i in users:
            self.comboBox_2.addItem(i)
        #self.comboBox_2.setCurrentText(self.user)



    def change_language(self):
        self.language = self.comboBox.currentText()
        config['language'] = self.language

        #  Title window
        self.setWindowTitle(self.languages[self.language]['titleWindow'])

        #  Main Lbael
        self.mainLabel.setText(self.languages[self.language]['mainLabel'])

        #  Buttons
        self.exitButton.setText(self.languages[self.language]['exitButton'])
        self.homeButton.setText(self.languages[self.language]['homeButton'])
        self.startButton.setText(self.languages[self.language]['startButton'])
        self.techRButton.setText(self.languages[self.language]['teachRButton'])
        self.statButton.setText(self.languages[self.language]['statButton'])

        #  Action group box
        self.actionGroup.setTitle(self.languages[self.language]['actionGroup'])
        self.addCheckBox.setText(self.languages[self.language]['addCheckBox'])
        self.subCheckBox.setText(self.languages[self.language]['subCheckBox'])
        self.multCheckBox.setText(self.languages[self.language]['multCheckBox'])
        self.divCheckBox.setText(self.languages[self.language]['divCheckBox'])

        # Mode group box
        self.modeGroup.setTitle(self.languages[self.language]['modeGroup'])
        self.examRButton.setText(self.languages[self.language]['examRButton'])

        #  Result Group box
        self.resultGroupBox.setTitle(self.languages[self.language]['resultGroupBox'])
        self.labelRightCount.setText(f"{self.languages[self.language]['labelRightCount']}: {self.right_count}")
        self.labelWrongCount.setText(f"{self.languages[self.language]['labelWrongCount']}: {self.wrong_count}")

        # User group box
        self.userGroupBox.setTitle(self.languages[self.language]['userGroupBox'])

    def exit_action(self):
        con.commit()
        self.close()

    def start(self):
        self.homeButton.show()
        self.modeGroup.hide()
        self.actionGroup.hide()
        self.startButton.hide()
        self.statButton.hide()
        #self.vline.hide()
        self.lineLabel_2.hide()
        self.labelLanguage.hide()
        self.comboBox.hide()
        self.actionLabel.show()
        self.addCheckBox.isChecked()
        self.subCheckBox.isChecked()
        self.multCheckBox.isChecked()
        self.divCheckBox.isChecked()
        self.actionLabel.show()
        self.answerButton1.show()
        self.answerButton2.show()
        self.answerButton3.show()
        self.answerLabel.show()
        self.answerLabel.setText('')
        self.userGroupBox.hide()
        self.messageGroupBox.show()
        self.start_action()

    def start_action(self):
        """Main function."""

        self.answerLabel.setText('')  # Clear wrong answer message
        self.labelRightCount.setText(f"{self.languages[self.language]['labelRightCount']}: {self.right_count}")
        self.labelWrongCount.setText(f"{self.languages[self.language]['labelWrongCount']}: {self.wrong_count}")

        # Check checkboxes. If not checked - hide button and show no action text
        if (self.addCheckBox.isChecked() is False and self.divCheckBox.isChecked() is False and
                self.multCheckBox.isChecked() is False and self.subCheckBox.isChecked() is False):
            self.actionLabel.hide()
            self.answerButton1.hide()
            self.answerButton2.hide()
            self.answerButton3.hide()
            self.answerLabel.setText(self.languages[self.language]['noAction'])

        else:
            self.list_action = []
            if self.addCheckBox.isChecked() is True:
                self.list_action.append('+')
            if self.subCheckBox.isChecked() is True:
                self.list_action.append('-')
            if self.multCheckBox.isChecked() is True:
                self.list_action.append('*')
            if self.divCheckBox.isChecked() is True:
                self.list_action.append('/')


            self.action = self.list_action[randint(0, len(self.list_action) - 1)]  # Check number of actions
            self.list_answer = [0 for self.i in
                                range(3)]  # Create answer list for right and wrong answer for button

            #If checked addition and/or multiplication checkbox
            if self.action == '+' or self.action == '*':
                self.first_digit = randint(2, 10)
                self.sec_digit = randint(2, 10)
                self.actionLabel.setText(
                    f"{self.first_digit} {self.action} {self.sec_digit}")  # Show Digit and action on actionLabel

                #If check addition
                if self.action == '+':
                    self.answer = int(self.first_digit) + int(self.sec_digit)

                #if check multilplication
                else:
                    self.answer = int(self.first_digit) * int(self.sec_digit)

            elif self.action == '-':
                self.first_digit = randint(3,20)
                while True:
                    if self.first_digit == 3:
                        self.sec_digit = randint(1,self.first_digit)
                    else:
                        self.sec_digit = randint(2, self.first_digit)
                    if self.sec_digit >= self.first_digit - 1:
                        continue
                    else:
                        break

                self.actionLabel.setText(
                    f"{self.first_digit} {self.action} {self.sec_digit}")  # Show Digit and action on actionLabel
                self.answer = int(self.first_digit) - int(self.sec_digit)

            elif self.action == '/':
                self.sec_digit = randint(2, 10)
                self.first_digit = randint(2, 10) * self.sec_digit
                self.actionLabel.setText(
                    f"{self.first_digit} {self.action} {self.sec_digit}")  # Show Digit and action on actionLabel
                self.answer = int(self.first_digit) / int(self.sec_digit)

            #Create list with wrong digits
            for self.i in 0, 1, 2:
                while True:
                    self.wrong_answer = int(self.answer) + randint(-2, 2)
                    # If answer in list or == right answer -> continue
                    if self.wrong_answer == self.answer or self.wrong_answer in self.list_answer:
                        continue
                    elif self.wrong_answer <= 0:
                        continue
                    else:
                        self.list_answer[self.i] = int(self.wrong_answer)
                        break
            #Create coorect
            self.correct_button_index = randint(0, 2)
            self.list_answer[self.correct_button_index] = int(self.answer)

        self.create_answer_button()

    def create_answer_button(self):
        """Create text on answer button"""

        for i in range(0, 3):
            self.answer_button_group[i].setText(str(self.list_answer[i]))

    def check_answer(self):
        """Check answer when button clicked"""
        sender = self.sender()
        if sender.objectName() == self.answer_button_group[self.correct_button_index].objectName():
            if self.stateCount is not False:
                self.right_count += 1
            self.stateCount = True
            self.start_action()
        else:
            self.answerLabel.setText(f'{self.languages[self.language]["wrongAnswer"]} {int(self.answer)}')
            if self.stateCount is False:
                pass
            else:
                self.wrong_count += 1
            self.stateCount = False

    def add_user_window(self):
        self.addUserWindow = AddUserWindow()
        self.addUserWindow.pushButton[str].connect(self.add_user)
        self.addUserWindow.show()

    def add_user(self, user):
        self.user = user
        if self.user not in users:
            users[self.user] = {}
            self.comboBox_2.clear()
            for i in users:
                self.comboBox_2.addItem(i)
            self.comboBox_2.setCurrentText(self.user)
            cursor.execute(f"INSERT INTO mathsim('username','right','wrong') VALUES('{self.user}','0','0')")
            con.commit()
            self.rebase_user_box()
        else:
            self.existUserWindow = ExistUserWindow()
            self.existUserWindow.show()

if __name__ == "__main__":
    #  Load languages
    with open('lang.json') as f:
         languages = json.load(f)

    #  Load config and db
    config_path, db_path = check_files.check_platform()
    db_path = 'db.db'
    with open(config_path) as f:
        config = json.load(f)
    if 'language' not in config.keys():
        config['language'] = list(languages.keys())[0]
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS mathsim (
        No INTEGER PRIMARY KEY,
        username data_type NOT NULL,
        right data_type DEFAULT 0,
        wrong data_type DEFAULT 0)''')
    cursor.execute('''SELECT * FROM mathsim''')
    list_users = cursor.fetchall()

    users = {}
    for i in  list_users:
        users[i[1]] = {'right': i[2], 'wrong': i[3]}

    app = QApplication(argv)
    window = MainWindow()
    window.show()  #
    app.exec_()

    #  Save config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
        f.close()
