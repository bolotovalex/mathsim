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
        self.clearButton.clicked.connect(self.clear)

    def exit_action(self):
        self.close()

    def clear(self):
        pass
        #self.


def main():
    app = QtWidgets.QApplication(argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == "__main__":
    main()