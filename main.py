from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from gui.main_window import Ui_Dialog
from gui.addUser_window import Ui_AddUser
from gui.exist_user_window import Ui_ExistUser
from sys import argv
from random import randint
import json
from include import get_digit, check_files, lang
from threading import Thread
from time import sleep


class ExistUserWindow(QWidget, Ui_ExistUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(lambda: self.close())
        self.language = languages[config['last_language']]
        self.messageLabel.setText(self.language['existUserText'])


class AddUserWindow(QWidget, Ui_AddUser):
    pushButton = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(lambda: self.close())
        self.addUser.clicked.connect(self.adduser_action)
        self.language = languages[config['last_language']]
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
        # self.easyRButton.toggled.connect(self.check_mode)
        self.answer_button_group = [self.answerButton1, self.answerButton2, self.answerButton3]
        self.addUserButton.clicked.connect(self.add_user_window)

        # Difficult mode select
        self.easyRButton.clicked.connect(self.change_difficult)
        self.mediumRButton.clicked.connect(self.change_difficult)
        self.hardRButton.clicked.connect(self.change_difficult)


        # CheckBox
        self.addCheckBox.click()


        #  ComboBox - Select Language
        self.comboBox.clear()
        for self.i in self.languages.keys():
            self.comboBox.addItem(self.i)
        self.comboBox.currentTextChanged.connect(self.change_language)

        #  Counter
        if len(users) > 0:
            self.right_count = config['users'][config['last_user']]['right']
            self.wrong_count = config['users'][config['last_user']]['wrong']
        else:
            self.right_count = 0
            self.wrong_count = 0

        self.stateCount = True
        self.counter = 0
        self.comboBox.setCurrentText(config['last_language'])
        self.change_language()
        self.home()

        #  ComboBox_2 - Select user
        for self.user in config['users']:
            self.comboBox_2.addItem(self.user)

        if len(config['users']) > 0:
            self.difficult = config['users'][config['last_user']]['last_difficult']
        else:
            self.difficult = 0

        if self.difficult == 0:
            self.easyRButton.click()
        elif self.difficult == 1:
            self.mediumRButton.click()
        elif self.difficult == 2:
            self.hardRButton.click()
        self.comboBox_2.setCurrentText(config['last_user'])
        self.comboBox_2.currentTextChanged.connect(self.change_user)
        self.selectUserLabel.hide()
        self.update_counter()

    def change_difficult(self):
        if self.easyRButton.isChecked():
            self.difficult = 0
        elif self.mediumRButton.isChecked():
            self.difficult = 1
        elif self.hardRButton.isChecked():
            self.difficult = 2

        if len(config['users']) > 0:
            config['users'][config['last_user']]['last_difficult'] = self.difficult


    def change_user(self):
        config['last_user'] = self.comboBox_2.currentText()
        if len(config['last_user']) > 0:
            self.right_count = config['users'][config['last_user']]['right']
            self.wrong_count = config['users'][config['last_user']]['wrong']
            self.difficult = config['users'][config['last_user']]['last_difficult']

            if self.difficult == 0:
                self.easyRButton.click()
            elif self.difficult == 1:
                self.mediumRButton.click()
            elif self.difficult == 2:
                self.hardRButton.click()

            self.selectUserLabel.setText(config['last_user'])
            self.update_counter()

    def update_counter(self):
        self.labelRightCount.setText(f"{self.languages[self.language]['labelRightCount']}: {self.right_count}")
        self.labelWrongCount.setText(f"{self.languages[self.language]['labelWrongCount']}: {self.wrong_count}")

    def home(self):
        #  Hide elements
        self.actionLabel.hide()
        self.answerLabel.hide()
        self.answerButton1.hide()
        self.answerButton2.hide()
        self.answerButton3.hide()
        self.homeButton.hide()
        self.statButton.hide()
        self.messageGroupBox.hide()
        self.selectUserLabel.hide()

        # Show elements
        # self.vline.show()
        self.actionGroup.show()
        self.comboBox.show()
        self.labelLanguage.show()
        self.lineLabel_2.show()
        self.modeGroup.show()
        self.startButton.show()
        self.statButton.hide()  # self.statButton.show()
        self.comboBox_2.show()
        self.addUserButton.show()
        # self.userGroupBox.show()

    def change_language(self):
        self.language = self.comboBox.currentText()
        config['last_language'] = self.language

        #  Title window
        self.setWindowTitle(self.languages[self.language]['titleWindow'])

        #  Main Label
        self.mainLabel.setText(self.languages[self.language]['mainLabel'])

        #  Buttons
        self.exitButton.setText(self.languages[self.language]['exitButton'])
        self.homeButton.setText(self.languages[self.language]['homeButton'])
        self.startButton.setText(self.languages[self.language]['startButton'])
        # self.mediumRButton.setText(self.languages[self.language]['mediumRButton'])
        # self.statButton.setText(self.languages[self.language]['statButton'])

        #  Action group box
        self.actionGroup.setTitle(self.languages[self.language]['actionGroup'])
        self.addCheckBox.setText(self.languages[self.language]['addCheckBox'])
        self.subCheckBox.setText(self.languages[self.language]['subCheckBox'])
        self.multCheckBox.setText(self.languages[self.language]['multCheckBox'])
        self.divCheckBox.setText(self.languages[self.language]['divCheckBox'])

        # Mode group box
        self.modeGroup.setTitle(self.languages[self.language]['modeGroup'])
        self.easyRButton.setText(self.languages[self.language]['easyRButton'])
        self.mediumRButton.setText(self.languages[self.language]['mediumRButton'])
        self.hardRButton.setText(self.languages[self.language]['hardRButton'])

        #  Result Group box
        self.resultGroupBox.setTitle(self.languages[self.language]['resultGroupBox'])
        self.labelRightCount.setText(f"{self.languages[self.language]['labelRightCount']}: {self.right_count}")
        self.labelWrongCount.setText(f"{self.languages[self.language]['labelWrongCount']}: {self.wrong_count}")

        # User group box
        self.userGroupBox.setTitle(self.languages[self.language]['userGroupBox'])

    def exit_action(self):
        self.close()

    def start(self):
        self.homeButton.show()
        self.modeGroup.hide()
        self.actionGroup.hide()
        self.startButton.hide()
        self.statButton.hide()
        # self.vline.hide()
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

        self.addUserButton.hide()
        self.comboBox_2.hide()
        self.selectUserLabel.setText(config['last_user'])
        self.selectUserLabel.show()

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

            self.digits = get_digit.get_digit_dictionary(self.difficult, self.action)


            self.actionLabel.setText(
                f"{self.digits['first_digit']} {self.action} {self.digits['sec_digit']}")  # Show Digit and action on actionLabel


                # Create list with wrong digits
            for self.i in 0, 1, 2:
                while True:
                    self.wrong_answer = self.digits['right_answer'] + randint(-2, 2)
                    # If answer in list or == right answer -> continue
                    if self.wrong_answer == self.digits['right_answer'] or self.wrong_answer in self.list_answer:
                        continue
                    elif self.wrong_answer <= 0:
                        continue
                    else:
                        self.list_answer[self.i] = int(self.wrong_answer)
                        break
            # Create correct
            self.correct_button_index = randint(0, 2)
            self.list_answer[self.correct_button_index] = int(self.digits['right_answer'])
        self.timer = timer_t

        self.create_answer_button()

    def create_answer_button(self):
        """Create text on answer button"""

        for i in range(0, 3):
            self.answer_button_group[i].setText(str(self.list_answer[i]))

    def check_answer(self):
        """Check answer when button clicked"""
        sender = self.sender()
        if timer_t <= self.timer + 3:
            if sender.objectName() == self.answer_button_group[self.correct_button_index].objectName():
                # print(f"self: {self.timer}, global:{timer_t}")
                if self.stateCount is not False:
                    self.right_count += 1
                    config['users'][config['last_user']]['right'] = self.right_count
                self.stateCount = True
                self.start_action()
            else:
                self.answerLabel.setText(f'{self.languages[self.language]["wrongAnswer"]} {self.digits["right_answer"]}')
                if self.stateCount is False:
                    pass
                else:
                    self.wrong_count += 1
                    config['users'][config['last_user']]['wrong'] = self.wrong_count
                self.stateCount = False
        else:
            self.timer = timer_t
            self.answerLabel.setText(f'{self.languages[self.language]["time_out"]} {self.digits["right_answer"]}')
            if self.stateCount is False:
                pass
            else:
                self.wrong_count += 1
                # config['users'][config['last_user']]['wrong'] = self.wrong_count
            self.stateCount = False

    def add_user_window(self):
        self.addUserWindow = AddUserWindow()
        self.addUserWindow.pushButton[str].connect(self.add_user)
        self.addUserWindow.show()

    def add_user(self, user):
        self.user = user

        if self.user not in users:
            users[self.user] = {'right': 0, 'wrong': 0, 'last_difficult': 0}
            config['users'][self.user] = {'right': 0, 'wrong': 0, 'last_difficult': 0}
            config['last_user'] = self.user
            self.comboBox_2.clear()
            for self.i in users:
                self.comboBox_2.addItem(self.i)
            config['users'] = users
        else:
            self.existUserWindow = ExistUserWindow()
            self.existUserWindow.show()

        self.comboBox_2.setCurrentText(self.user)

def timer():
    global timer_t
    while True:
        timer_t += 1
        sleep(1)
        # return timer_t

if __name__ == "__main__":
    languages = lang.languages

    #  Load config and db
    config_path, db_path = check_files.check_platform()

    with open(config_path) as f:
        config = json.load(f)

    if 'last_language' not in config.keys():
        config['last_language'] = list(languages.keys())[0]

    users = {}
    if 'users' not in config.keys():
        config['users'] = {}
    else:
        for user in config['users']:
            users[user] = config['users'][user]

    if 'last_user' not in config.keys():
        config['last_user'] = ''

    # Run timer
    timer_t = int(0)
    timer = Thread(target=timer, daemon=True)
    timer.start()


    app = QApplication(argv)
    window = MainWindow()
    window.show()  #
    app.exec_()

    #  Save config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
        f.close()
