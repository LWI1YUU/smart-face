# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 470)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color : rgb(85, 85, 127);\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 10, 581, 441))
        self.widget.setStyleSheet("background-color: rgb(233, 233, 233);\n"
"")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 140, 271, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(230, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 255, 228);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 210, 271, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(233, 233, 233);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(233, 233, 233);\n"
"")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(200, 30, 181, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(233, 233, 233);\n"
"color: rgb(85, 170, 0);\n"
"")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label.setText(_translate("Form", "Email"))
        self.label_3.setText(_translate("Form", "LOGIN PAGE !"))

import sys
from PyQt5.QtWidgets import QApplication, QWidget
# Import the Ui_Form class from the generated Python file

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Create an instance of the Ui_Form class
        self.ui.setupUi(self)  # Setup the user interface

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()  # Show the main application window
    sys.exit(app.exec_())