#import PyQt5
from PyQt5 import QtWidgets
import main_window
import lang
from sys import argv

class MainWindow(QtWidgets.QMainWindow, main_window.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.exit_action)
        self.languages = lang.languages
        self.comboBox.clear()
        self.homeButton.hide()
        self.examRButton.toggled.connect(self.check_mode)
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
        self.modeLabel.setText(self.languages[self.language]['modeLabel'])
        self.homeButton.setText(self.languages[self.language]['homeButton'])
        self.homeButton.setText(self.languages[self.language]['homeButton'])
        self.examRButton.setText(self.languages[self.language]['examRButton'])
        self.techRButton.setText(self.languages[self.language]['teachRButton'])

    def main_menu(self):
        pass

    def exit_action(self):
        self.close()


def main():
    app = QtWidgets.QApplication(argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == "__main__":
    main()