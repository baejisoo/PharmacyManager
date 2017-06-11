import sys
from PyQt4 import QtGui, QtCore
#from gui import*
from urllib import request
import urllib.parse
from xml.dom.minidom import *
from xml.etree import ElementTree

app = QtGui.QApplication(sys.argv)
ServiceKey = 'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'

class MyForm(QtGui.QMainWindow, Ui_Form):
    global sidoName, sigunguName, day, order, pharmacyName

    def __init__(self, parent=None):

        self.ui = Ui_Form()
        self.ui.setupUi(self)


    def Qlinetext(self):

        sidoNameKor = self.ui.lineEdit.text()
        sidoName = urllib.parse.quote(sidoNameKor)

        sigunguNameKor = self.ui.lineEdit_2.text()
        sigunguName = urllib.parse.quote(sigunguNameKor)

        dayKor = self.ui.comboBox()
        day = urllib.parse.quote(dayKor)

        response_body = request.urlopen(
            'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
            + ServiceKey +
            '&Q0=' + sidoName + '&Q1=' + sigunguName + '&QT=' + day + '&pageNo=1&numOfRows=20').read()
        tree = ElementTree.fromstring(response_body)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            dutyName = item.find("dutyName")
            dutyAddr = item.find("dutyAddr")
            dutyTimeS = item.find("dutyTime" + day + "s")
            dutyTimeC = item.find("dutyTime" + day + "c")
            self.ui.listView.addItem("약국 이름: " + dutyName.text)
            self.ui.listView.addItem("약국 주소: " + dutyAddr.text)
            if (item.find("dutyTime" + day + "s") != None and item.find("dutyTime" + day + "c") != None):
                self.ui.listView.addItem("약국 영업 시간: " + dutyTimeS.text + "~" + dutyTimeC.text)


        return

myapp = MyForm()
myapp.show()
app.exec_()
