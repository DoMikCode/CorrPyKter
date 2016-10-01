from PyQt5 import uic
from PyQt5.QtWidgets import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        self.show()



def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())