from PyQt4.QtGui import *


class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # 레이블,Edit,버튼 컨트롤
        lblName = QLabel("Name")
        editName = QLineEdit()
        btnOk = QPushButton("OK")
        edit = QTextEdit("Edit")

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(editName)
        layout.addWidget(btnOk)
        layout.addWidget(edit)

        # 다이얼로그에 레이아웃 지정
        self.setLayout(layout)


# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()