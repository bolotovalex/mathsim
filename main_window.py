# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(640, 480))
        self.homeButton = QtWidgets.QPushButton(Dialog)
        self.homeButton.setGeometry(QtCore.QRect(10, 440, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.mainLabel = QtWidgets.QLabel(Dialog)
        self.mainLabel.setGeometry(QtCore.QRect(130, 10, 380, 35))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mainLabel.setFont(font)
        self.mainLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainLabel.setAutoFillBackground(False)
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(530, 440, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(390, 441, 130, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "lang1")
        self.comboBox.addItem("")
        self.comboBox.setItemText(1, "lang2")
        self.labelLanguage = QtWidgets.QLabel(Dialog)
        self.labelLanguage.setGeometry(QtCore.QRect(270, 439, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelLanguage.setFont(font)
        self.labelLanguage.setObjectName("labelLanguage")
        self.lineLabel = QtWidgets.QFrame(Dialog)
        self.lineLabel.setGeometry(QtCore.QRect(10, 50, 621, 20))
        self.lineLabel.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLabel.setObjectName("lineLabel")
        self.lineLabel_2 = QtWidgets.QFrame(Dialog)
        self.lineLabel_2.setGeometry(QtCore.QRect(10, 220, 621, 20))
        self.lineLabel_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLabel_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLabel_2.setObjectName("lineLabel_2")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(240, 240, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.actionGroup = QtWidgets.QGroupBox(Dialog)
        self.actionGroup.setGeometry(QtCore.QRect(330, 70, 291, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionGroup.setFont(font)
        self.actionGroup.setObjectName("actionGroup")
        self.layoutWidget = QtWidgets.QWidget(self.actionGroup)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 251, 112))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addCheckBox.setFont(font)
        self.addCheckBox.setObjectName("addCheckBox")
        self.verticalLayout_3.addWidget(self.addCheckBox)
        self.subCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subCheckBox.setFont(font)
        self.subCheckBox.setObjectName("subCheckBox")
        self.verticalLayout_3.addWidget(self.subCheckBox)
        self.multCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.multCheckBox.setFont(font)
        self.multCheckBox.setObjectName("multCheckBox")
        self.verticalLayout_3.addWidget(self.multCheckBox)
        self.divCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.divCheckBox.setFont(font)
        self.divCheckBox.setObjectName("divCheckBox")
        self.verticalLayout_3.addWidget(self.divCheckBox)
        self.modeGroup = QtWidgets.QGroupBox(Dialog)
        self.modeGroup.setGeometry(QtCore.QRect(20, 70, 291, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.modeGroup.setFont(font)
        self.modeGroup.setObjectName("modeGroup")
        self.mediumRButton = QtWidgets.QRadioButton(self.modeGroup)
        self.mediumRButton.setGeometry(QtCore.QRect(10, 60, 259, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mediumRButton.setFont(font)
        self.mediumRButton.setObjectName("mediumRButton")
        self.easyRButton = QtWidgets.QRadioButton(self.modeGroup)
        self.easyRButton.setGeometry(QtCore.QRect(10, 30, 259, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.easyRButton.setFont(font)
        self.easyRButton.setCheckable(True)
        self.easyRButton.setChecked(True)
        self.easyRButton.setObjectName("easyRButton")
        self.hardRButton = QtWidgets.QRadioButton(self.modeGroup)
        self.hardRButton.setGeometry(QtCore.QRect(10, 90, 259, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hardRButton.setFont(font)
        self.hardRButton.setObjectName("hardRButton")
        self.statButton = QtWidgets.QPushButton(Dialog)
        self.statButton.setGeometry(QtCore.QRect(240, 290, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.statButton.setFont(font)
        self.statButton.setObjectName("statButton")
        self.lineLabel_3 = QtWidgets.QFrame(Dialog)
        self.lineLabel_3.setGeometry(QtCore.QRect(0, 420, 641, 20))
        self.lineLabel_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLabel_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLabel_3.setObjectName("lineLabel_3")
        self.actionLabel = QtWidgets.QLabel(Dialog)
        self.actionLabel.setGeometry(QtCore.QRect(90, 60, 461, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.actionLabel.setFont(font)
        self.actionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actionLabel.setObjectName("actionLabel")
        self.answerButton1 = QtWidgets.QPushButton(Dialog)
        self.answerButton1.setGeometry(QtCore.QRect(90, 150, 141, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.answerButton1.setFont(font)
        self.answerButton1.setObjectName("answerButton1")
        self.answerButton2 = QtWidgets.QPushButton(Dialog)
        self.answerButton2.setGeometry(QtCore.QRect(250, 150, 141, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.answerButton2.setFont(font)
        self.answerButton2.setObjectName("answerButton2")
        self.answerButton3 = QtWidgets.QPushButton(Dialog)
        self.answerButton3.setGeometry(QtCore.QRect(410, 150, 141, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.answerButton3.setFont(font)
        self.answerButton3.setObjectName("answerButton3")
        self.answerLabel = QtWidgets.QLabel(Dialog)
        self.answerLabel.setGeometry(QtCore.QRect(30, 250, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answerLabel.setFont(font)
        self.answerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel.setObjectName("answerLabel")
        self.labelRightCount = QtWidgets.QLabel(Dialog)
        self.labelRightCount.setGeometry(QtCore.QRect(20, 360, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRightCount.setFont(font)
        self.labelRightCount.setObjectName("labelRightCount")
        self.labelWrongCount = QtWidgets.QLabel(Dialog)
        self.labelWrongCount.setGeometry(QtCore.QRect(20, 390, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelWrongCount.setFont(font)
        self.labelWrongCount.setObjectName("labelWrongCount")
        self.resultGroupBox = QtWidgets.QGroupBox(Dialog)
        self.resultGroupBox.setGeometry(QtCore.QRect(10, 330, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultGroupBox.setFont(font)
        self.resultGroupBox.setObjectName("resultGroupBox")
        self.messageGroupBox = QtWidgets.QGroupBox(Dialog)
        self.messageGroupBox.setGeometry(QtCore.QRect(9, 250, 621, 41))
        self.messageGroupBox.setTitle("")
        self.messageGroupBox.setObjectName("messageGroupBox")
        self.userGroupBox = QtWidgets.QGroupBox(Dialog)
        self.userGroupBox.setGeometry(QtCore.QRect(420, 330, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userGroupBox.setFont(font)
        self.userGroupBox.setObjectName("userGroupBox")
        self.addUserButton = QtWidgets.QPushButton(self.userGroupBox)
        self.addUserButton.setGeometry(QtCore.QRect(10, 60, 41, 21))
        self.addUserButton.setObjectName("addUserButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.userGroupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 30, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.selectUserLabel = QtWidgets.QLabel(Dialog)
        self.selectUserLabel.setGeometry(QtCore.QRect(430, 360, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectUserLabel.setFont(font)
        self.selectUserLabel.setObjectName("selectUserLabel")
        self.resultGroupBox.raise_()
        self.homeButton.raise_()
        self.mainLabel.raise_()
        self.exitButton.raise_()
        self.comboBox.raise_()
        self.labelLanguage.raise_()
        self.lineLabel.raise_()
        self.lineLabel_2.raise_()
        self.startButton.raise_()
        self.actionGroup.raise_()
        self.modeGroup.raise_()
        self.statButton.raise_()
        self.lineLabel_3.raise_()
        self.actionLabel.raise_()
        self.answerButton1.raise_()
        self.answerButton2.raise_()
        self.answerButton3.raise_()
        self.answerLabel.raise_()
        self.labelWrongCount.raise_()
        self.labelRightCount.raise_()
        self.messageGroupBox.raise_()
        self.userGroupBox.raise_()
        self.selectUserLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.homeButton.setText(_translate("Dialog", "homeButton"))
        self.mainLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">mainLabel</p></body></html>"))
        self.exitButton.setText(_translate("Dialog", "exitButton"))
        self.labelLanguage.setText(_translate("Dialog", "Язык/Language:"))
        self.startButton.setText(_translate("Dialog", "startButton"))
        self.actionGroup.setTitle(_translate("Dialog", "actionGroup"))
        self.addCheckBox.setText(_translate("Dialog", "addCheckBox"))
        self.subCheckBox.setText(_translate("Dialog", "subCheckBox"))
        self.multCheckBox.setText(_translate("Dialog", "multCheckBox"))
        self.divCheckBox.setText(_translate("Dialog", "divCheckBox"))
        self.modeGroup.setTitle(_translate("Dialog", "modeGroup"))
        self.mediumRButton.setText(_translate("Dialog", "mediumRButton"))
        self.easyRButton.setText(_translate("Dialog", "easyRadioButton"))
        self.hardRButton.setText(_translate("Dialog", "hardRButton"))
        self.statButton.setText(_translate("Dialog", "statButton"))
        self.actionLabel.setText(_translate("Dialog", "81 / 9"))
        self.answerButton1.setText(_translate("Dialog", "B1"))
        self.answerButton2.setText(_translate("Dialog", "B2"))
        self.answerButton3.setText(_translate("Dialog", "B3"))
        self.answerLabel.setText(_translate("Dialog", "TextLabel"))
        self.labelRightCount.setText(_translate("Dialog", "labelRightCount"))
        self.labelWrongCount.setText(_translate("Dialog", "labelWrongCount"))
        self.resultGroupBox.setTitle(_translate("Dialog", "resultGroupBox"))
        self.userGroupBox.setTitle(_translate("Dialog", "userGroupBox"))
        self.addUserButton.setText(_translate("Dialog", "+"))
        self.selectUserLabel.setText(_translate("Dialog", "selectUserLabel"))
