#import PyQt5
from PyQt5 import QtWidgets
from main_window import Ui_Dialog
import lang
from sys import argv

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.exit_action)
        self.languages = lang.languages
        self.comboBox.clear()
        for self.i in self.languages.keys():
            self.comboBox.addItem(self.i)
        self.change_language()
        self.comboBox.currentTextChanged.connect(self.change_language)
        self.actionLabel.hide()
        self.answerButton1.hide()
        self.answerButton2.hide()
        self.answerButton3.hide()
        self.answerLabel.hide()
        self.check_mode()
        self.main_menu()

    def check_mode(self):
        self.is_exam = self.examRButton.isChecked()
        #print(self.is_exam)

    def change_language(self):
        self.language = self.comboBox.currentText()
        self.exitButton.setText(self.languages[self.language]['exitButton'])
        self.mainLabel.setText(self.languages[self.language]['mainLabel'])
        self.homeButton.setText(self.languages[self.language]['homeButton'])
        self.examRButton.setText(self.languages[self.language]['examRButton'])
        self.techRButton.setText(self.languages[self.language]['teachRButton'])
        self.addCheckBox.setText(self.languages[self.language]['addCheckBox'])
        self.divCheckBox.setText(self.languages[self.language]['divCheckBox'])
        self.multCheckBox.setText(self.languages[self.language]['multCheckBox'])
        self.subCheckBox.setText(self.languages[self.language]['subCheckBox'])
        self.startButton.setText(self.languages[self.language]['startButton'])
        self.statButton.setText(self.languages[self.language]['statButton'])
        self.modeGroup.setTitle(self.languages[self.language]['modeGroup'])
        self.actionGroup.setTitle(self.languages[self.language]['actionGroup'])
        self.setWindowTitle(self.languages[self.language]['titleWindow'])

    def main_menu(self):
        self.homeButton.hide()
        self.examRButton.toggled.connect(self.check_mode)
        self.startButton.clicked.connect(self.start)
        self.homeButton.clicked.connect(self.home)


    def exit_action(self):
        self.close()


    def start(self):
        self.homeButton.show()
        self.modeGroup.hide()
        self.actionGroup.hide()
        self.startButton.hide()
        self.statButton.hide()
        self.vline.hide()
        self.lineLabel_2.hide()
        self.labelLanguage.hide()
        self.comboBox.hide()
        self.actionLabel.show()
        self.check_add = self.addCheckBox.isChecked()
        self.check_div = self.divCheckBox.isChecked()
        self.check_mult = self.multCheckBox.isChecked()
        self.check_sub = self.subCheckBox.isChecked()
        #self.start_action(self.check_add)
        self.actionLabel.show()
        self.answerButton1.show()
        self.answerButton2.show()
        self.answerButton3.show()
        self.answerLabel.show()
        self.answerLabel.setText('')

    def start_action(self):
        pass


    def addition_action(self):
        pass



    def home(self):
        self.homeButton.hide()
        self.modeGroup.show()
        self.actionGroup.show()
        self.startButton.show()
        self.statButton.show()
        self.vline.show()
        self.lineLabel_2.show()
        self.labelLanguage.show()
        self.comboBox.show()
        self.actionLabel.hide()
        self.answerButton1.hide()
        self.answerButton2.hide()
        self.answerButton3.hide()
        self.answerLabel.hide()



def main():
    app = QtWidgets.QApplication(argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == "__main__":
    main()