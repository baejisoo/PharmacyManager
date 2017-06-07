from PyQt4.QtGui import *
from urllib import request
import urllib.parse
from xml.dom.minidom import *
from xml.etree import ElementTree

ServiceKey = 'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        global sidoName, sigunguName, day, order, pharmacyName

        sidoNameKor = QLabel("시/도 입력: ")
        sidoName = QLineEdit()

        sigunguNameKor = QLabel("시/군/구 입력: ")
        sigunguName = QLineEdit()

        dayKor = QLabel("영업 요일 입력(월/화/수/목/금/토/일/공휴일): ")
        day = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(sidoNameKor) , layout.addWidget(sidoName)
        layout.addWidget(sigunguNameKor) , layout.addWidget(sigunguName)
        layout.addWidget(dayKor) , layout.addWidget(day)

        self.setLayout(layout)


app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()


