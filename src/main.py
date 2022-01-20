#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
from PyQt5.Qt import *
from ui import uidef
from ui import uilang
from run import runcore

class memTesterMain(runcore.memTesterRun):

    def __init__(self, parent=None):
        super(memTesterMain, self).__init__(parent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = memTesterMain(None)
    mainWin.setWindowTitle(u"NXP MCU Mem Tester v1.0")
    mainWin.show()

    sys.exit(app.exec_())

