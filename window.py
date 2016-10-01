from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.resize(640, 480)
        self.move(300, 300)
        self.setWindowTitle('PyCorrupter')
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())