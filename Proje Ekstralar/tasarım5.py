# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarım5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 417)
        Form.setStyleSheet("*{\n"
"    font-size:16px;\n"
"    font-family:sans-serif;\n"
"}\n"
"#Form{\n"
"    background:url(:/image/qtimage/r15.jpg);\n"
"}\n"
"QFrame{\n"
"    background:rgba(0,0,0,0.6);\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton{\n"
"    background:#03a9f4;\n"
"    color:#fff;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:rgba(0,0,0,0.6);\n"
"    border-radius:15px;\n"
"    color:#03a9f4;\n"
"}\n"
"QLineEdit{\n"
"    border-radius:15px;\n"
"    color:#03a9f4;    \n"
"}\n"
"QLabel{\n"
"    color:#fff;\n"
"    background:transparent;\n"
"    font-size:24px;\n"
"}\n"
"")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 160, 241, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 241, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 211, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.click)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Kullanıcı Adı"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Parola"))
        self.pushButton.setText(_translate("Form", "GİRİŞ"))

    def click(self):
        print("başarılı")

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

