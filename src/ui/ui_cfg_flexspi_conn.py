#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from . import uidef
from . import uilang
sys.path.append(os.path.abspath(".."))
from win import flexspiConnectCfgWin

class memTesterUiCfgFlexspi(QMainWindow, flexspiConnectCfgWin.Ui_flexspiConnCfgDialog):

    def __init__(self, parent=None):
        super(memTesterUiCfgFlexspi, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def callbackOk( self, event ):
        self.close()

    def callbackCancel( self, event ):
        self.close()

    def callbackClose( self, event ):
        self.close()


