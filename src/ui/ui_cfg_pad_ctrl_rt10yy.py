#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from PyQt5 import QtCore
from PyQt5.Qt import *
from . import uidef
from . import uilang
from . import uivar
sys.path.append(os.path.abspath(".."))
from win import padCtrlRT10yyWin

class memTesterUiPadCtrlRT10yy(QMainWindow, padCtrlRT10yyWin.Ui_padCtrlRT10yyDialog):

    def __init__(self, parent=None):
        super(memTesterUiPadCtrlRT10yy, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        padCtrlDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_PadCtrl)
        self.mixspiPadCtrlDict = padCtrlDict.copy()
        self._recoverLastSettings()

    exitSignal = QtCore.pyqtSignal(str)

    def sendExitSignal( self ):
        content = '1'
        self.exitSignal.emit(content)

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        self.comboBox_hys.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 16) & 0x1)
        self.comboBox_pus.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 14) & 0x3)
        self.comboBox_pue.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 13) & 0x1)
        self.comboBox_pke.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 12) & 0x1)
        self.comboBox_ode.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 11) & 0x1)
        self.comboBox_speed.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 6) & 0x3)
        self.comboBox_dse.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 3) & 0x7)
        self.comboBox_sre.setCurrentIndex((self.mixspiPadCtrlDict['rt10yyVal'] >> 0) & 0x1)

    def callbackOk( self, event ):
        rt10yyVal = 0x0
        hys = self.comboBox_hys.currentIndex()
        pus = self.comboBox_pus.currentIndex()
        pue = self.comboBox_pue.currentIndex()
        pke = self.comboBox_pke.currentIndex()
        ode = self.comboBox_ode.currentIndex()
        speed = self.comboBox_speed.currentIndex()
        dse = self.comboBox_dse.currentIndex()
        sre = self.comboBox_sre.currentIndex()
        rt10yyVal = rt10yyVal | (hys << 16) | (pus << 14) | (pue << 13)   | (pke << 12) | (ode << 11)  | (speed << 6) | (dse << 3) | (sre << 0);
        self.mixspiPadCtrlDict['rt10yyVal'] = rt10yyVal
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_PadCtrl, self.mixspiPadCtrlDict)
        self.sendExitSignal()
        self.close()

    def callbackCancel( self, event ):
        self.close()

