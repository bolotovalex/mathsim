# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exist_user_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExistUser(object):
    def setupUi(self, ExistUser):
        ExistUser.setObjectName("ExistUser")
        ExistUser.resize(256, 90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExistUser.sizePolicy().hasHeightForWidth())
        ExistUser.setSizePolicy(sizePolicy)
        self.messageLabel = QtWidgets.QLabel(ExistUser)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        self.okButton = QtWidgets.QPushButton(ExistUser)
        self.okButton.setGeometry(QtCore.QRect(90, 60, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(ExistUser)
        QtCore.QMetaObject.connectSlotsByName(ExistUser)

    def retranslateUi(self, ExistUser):
        _translate = QtCore.QCoreApplication.translate
        ExistUser.setWindowTitle(_translate("ExistUser", "Dialog"))
        self.messageLabel.setText(_translate("ExistUser", "TextLabel"))
        self.okButton.setText(_translate("ExistUser", "Ok"))
