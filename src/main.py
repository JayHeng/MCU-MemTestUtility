#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
from PyQt5.Qt import *
from win import memTesterWin

class memTesterMain(QMainWindow, memTesterWin.Ui_memTesterWin):

    def __init__(self, parent=None):
        super(memTesterMain, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = memTesterMain()
    mainWin.setWindowTitle(u"NXP MCU Mem Tester v1.0")
    mainWin.show()

    sys.exit(app.exec_())

