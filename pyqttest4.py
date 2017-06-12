from PyQt4.QtGui import *
import sys
# MyDiag.py 모듈 import
import testDiag


# MyDiag 모듈 안의 Ui_MyDialog 클래스로부터 파생
class XDialog(QDialog, testDiag.Ui_MyDialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        # 버튼 이벤트 핸들러
        self.btnSave.clicked.connect(self.saveData)
        self.btnCancel.clicked.connect(self.clearData)

    def saveData(self):
        with open("data.csv", "a", encoding="utf-8") as f:
            s = "%s,%s,%s\n" % (self.editName.text(),
                                self.editCompany.text(),
                                self.editAddr.text())
            f.write(s)
        QMessageBox.information(self, "저장", "성공적으로 저장")

    # 취소 버튼 클릭시
    def clearData(self):
        self.editName.clear()
        self.editCompany.clear()
        self.editAddr.clear()


app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()
