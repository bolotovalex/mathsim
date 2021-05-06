# import PyQt5
from PyQt5 import QtWidgets
from main_window import Ui_Dialog
import lang
from sys import argv
from random import randint
#import json


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.exit_action)
        #self.examRButton.toggled.connect(self.check_mode)
        self.startButton.clicked.connect(self.start)
        self.homeButton.clicked.connect(self.home)
        self.answerButton1.clicked.connect(self.check_answer)
        self.answerButton2.clicked.connect(self.check_answer)
        self.answerButton3.clicked.connect(self.check_answer)
        self.languages = lang.languages
        self.comboBox.clear()
        for self.i in self.languages.keys():
            self.comboBox.addItem(self.i)
        self.right_count = 0
        self.wrong_count = 0
        self.stateCount = True
        self.change_language()
        self.comboBox.currentTextChanged.connect(self.change_language)
        self.answer_button_group = [self.answerButton1, self.answerButton2, self.answerButton3]
        self.addCheckBox.click()
        self.counter = 0
        #print(json.dumps(self.languages, indent=4))
        #with open('lang.json', 'w', encoding='utf8') as f:
        #    f.write(json.dumps(self.languages, indent=4, sort_keys=True))
        #    f.close()
        self.home()


    def home(self):
        self.homeButton.hide()
        self.modeGroup.show()
        self.actionGroup.show()
        self.startButton.show()
        self.statButton.show()
        #self.vline.show()
        self.lineLabel_2.show()
        self.labelLanguage.show()
        self.comboBox.show()
        self.actionLabel.hide()
        self.answerButton1.hide()
        self.answerButton2.hide()
        self.answerButton3.hide()
        self.answerLabel.hide()
        self.messageGroupBox.hide()
        self.answerButton1.hide()
        self.answerButton2.hide()
        self.answerButton3.hide()
        self.answerLabel.hide()
        self.actionLabel.hide()
        self.homeButton.hide()
        self.techRButton.hide()
        self.messageGroupBox.hide()
        self.userGroupBox.show()
        self.statButton.hide()

    def change_language(self):
        self.language = self.comboBox.currentText()

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


def main():
    app = QtWidgets.QApplication(argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
