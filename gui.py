# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sys


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(656, 411)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(270, 50, 351, 241))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 340, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 340, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 340, 121, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 340, 131, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 130, 76, 22))
        self.comboBox.setMouseTracking(True)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "시/도 입력", None))
        self.label_2.setText(_translate("Form", "시/군/구 입력", None))
        self.label_3.setText(_translate("Form", "영업 요일 입력", None))
        self.pushButton.setText(_translate("Form", "약국 저장", None))
        self.pushButton_2.setText(_translate("Form", "인근 약국 찾기", None))
        self.pushButton_3.setText(_translate("Form", "지도 연결", None))
        self.pushButton_4.setText(_translate("Form", "이메일로 내용 보내기", None))
        self.comboBox.setItemText(0, _translate("Form", "월", None))
        self.comboBox.setItemText(1, _translate("Form", "화", None))
        self.comboBox.setItemText(2, _translate("Form", "수", None))
        self.comboBox.setItemText(3, _translate("Form", "목", None))
        self.comboBox.setItemText(4, _translate("Form", "금", None))
        self.comboBox.setItemText(5, _translate("Form", "토", None))
        self.comboBox.setItemText(6, _translate("Form", "일", None))
        self.comboBox.setItemText(7, _translate("Form", "공휴일", None))


app = QApplication(sys.argv)
dlg = Ui_Form()
dlg.show()
app.exec_()