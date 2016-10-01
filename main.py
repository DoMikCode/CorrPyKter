from methods import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys

def corrupt(in_file, out_file, corruptionMethod, overwrite=True):
    temp_file = open(in_file, "rb")
    original = temp_file.read()
    temp_file.close()
    print(original)
    corr =  corruptionMethod(1, 100, 3)
    print(corr.corrupt(original, byte_a=bytes('a', 'utf-8'), byte_b=b'c'))
    if overwrite:
        temp_file = open(out_file, "wb")
        #out_file = temp_file.write()
        temp_file.close()

corrupt("in.txt", "out.txt", ReplaceMethod)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(640, 480)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()
#
#     sys.exit(app.exec_())
