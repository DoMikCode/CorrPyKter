from methods import *
from window import *
import sys
import os

def corrupt(in_file, out_file, corruptionMethod, settings, start_byte=0, end_byte=100, interval=3,
            autoend=True, overwrite=False):
    temp_file = open(in_file, "rb")
    original = temp_file.read()
    temp_file.close()
    if autoend:
        end_byte = len(original)
    corr = corruptionMethod(start_byte, end_byte, interval)
    if overwrite or not os.path.exists(out_file):
        temp_file = open(out_file, "wb")
        out_file = temp_file.write(corr.corrupt(original, settings))
        temp_file.close()

corrupt("in.txt", "out.txt", ReplaceMethod, {"byte_a":int("0x61", 16), "byte_b":int("0x67", 16)})

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())
