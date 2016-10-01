from methods import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import os

def corrupt(in_file, out_file, corruptionMethod, start_byte=0, end_byte=100, interval=3,
            autoend=True, overwrite=False, **kwargs):
    temp_file = open(in_file, "rb")
    original = temp_file.read()
    temp_file.close()
    if autoend:
        end_byte = len(original)
    corr = corruptionMethod(start_byte, end_byte, interval)
    if overwrite or not os.path.exists(out_file):
        temp_file = open(out_file, "wb")
        out_file = temp_file.write(corr.corrupt(original, byte_a=int("0x61", 16), byte_b=int("0x67", 16)))
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