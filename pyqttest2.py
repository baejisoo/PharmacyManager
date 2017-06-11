from PyQt4.QtGui import *
import sys
# MyDiag.py 모듈 import
import MyDiag
from urllib import request
import urllib.parse
from xml.dom.minidom import *
from xml.etree import ElementTree

ServiceKey = 'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'
# MyDiag 모듈 안의 Ui_MyDialog 클래스로부터 파생

class XDialog(QDialog, MyDiag.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)

        self.pushButton_5.clicked.connect(self.editName)
        self.pushButton.clicked.connect(self.savePharmacy)

    def editName(self):
        global sidoName, sigunguName, day, order, pharmacyName
        sidoNameKor = self.lineEdit.text()
        sidoName = urllib.parse.quote(sidoNameKor)
        print(sidoNameKor)

        sigunguNameKor = self.lineEdit_2.text()
        sigunguName = urllib.parse.quote(sigunguNameKor)
        print(sigunguNameKor)

        dayKor = self.comboBox.currentText()
        if (dayKor == "월"):
            dayKor = "1"
        elif (dayKor == "화"):
            dayKor = "2"
        elif (dayKor == "수"):
            dayKor = "3"
        elif (dayKor == "목"):
            dayKor = "4"
        elif (dayKor == "금"):
            dayKor = "5"
        elif (dayKor == "토"):
            dayKor = "6"
        elif (dayKor == "일"):
            dayKor = "7"
        elif (dayKor == "공휴일"):
            dayKor = "8"
        day = urllib.parse.quote(dayKor)
        print(dayKor)

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
            self.listWidget.addItem("약국 이름: " + dutyName.text +'\n'+
                                        "약국 주소: " + dutyAddr.text)

    def savePharmacy(self):
        print(self.listWidget.currentRow().text)



app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()