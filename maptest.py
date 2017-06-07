import webbrowser
from PyQt4.QtGui import *



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