import sys
from PyQt4 import QtGui, QtCore
from gui import*

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
app.exec_()
