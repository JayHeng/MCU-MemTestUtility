#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from . import uidef
from . import uilang
from . import uivar
sys.path.append(os.path.abspath(".."))
from win import padCtrlRTxxxWin

class memTesterUiPadCtrlRTxxx(QMainWindow, padCtrlRTxxxWin.Ui_padCtrlRTxxxDialog):

    def __init__(self, parent=None):
        super(memTesterUiPadCtrlRTxxx, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        self._recoverLastSettings()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        pass

    def callbackOk( self, event ):
        pass

    def callbackCancel( self, event ):
        self.close()

