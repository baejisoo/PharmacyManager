from PyQt4.QtGui import *
#버튼 클릭하여 입력(이벤트 핸들러 추가)
class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        lblName = QLabel("Name")
        self.editName = QLineEdit()
        btnOk = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(self.editName)
        layout.addWidget(btnOk)
        self.setLayout(layout)

        btnOk.clicked.connect(self.btnOkClicked)

    def btnOkClicked(self):
        name = self.editName.text()
        QMessageBox.information(self, "Info", name)

# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()
