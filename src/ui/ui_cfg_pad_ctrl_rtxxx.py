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
from win import padCtrlRTxxxWin

class memTesterUiPadCtrlRTxxx(QMainWindow, padCtrlRTxxxWin.Ui_padCtrlRTxxxDialog):

    def __init__(self, parent=None):
        super(memTesterUiPadCtrlRTxxx, self).__init__(parent)
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
        self.comboBox_drive.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 12) & 0x3)
        self.comboBox_iiena.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 11) & 0x1)
        self.comboBox_odena.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 10) & 0x1)
        self.comboBox_amena.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 9) & 0x1)
        self.comboBox_fulldrv.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 8) & 0x1)
        self.comboBox_slewrate.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 7) & 0x1)
        self.comboBox_ibena.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 6) & 0x1)
        self.comboBox_pupdsel.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 5) & 0x1)
        self.comboBox_pupdena.setCurrentIndex((self.mixspiPadCtrlDict['rtxxxVal'] >> 4) & 0x1)

    def callbackOk( self, event ):
        rtxxxVal = 0x0
        drive = self.comboBox_drive.currentIndex()
        iiena = self.comboBox_iiena.currentIndex()
        odena = self.comboBox_odena.currentIndex()
        amena = self.comboBox_amena.currentIndex()
        fulldrv = self.comboBox_fulldrv.currentIndex()
        slewrate = self.comboBox_slewrate.currentIndex()
        ibena = self.comboBox_ibena.currentIndex()
        pupdsel = self.comboBox_pupdsel.currentIndex()
        pupdena = self.comboBox_pupdena.currentIndex()
        rtxxxVal = rtxxxVal | (drive << 12) | (iiena << 11) | (odena << 10)   | (amena << 9) | (fulldrv << 8)  | (slewrate << 7) | (ibena << 6) | (pupdsel << 5) | (pupdena << 4);
        self.mixspiPadCtrlDict['rtxxxVal'] = rtxxxVal
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_PadCtrl, self.mixspiPadCtrlDict)
        self.sendExitSignal()
        self.close()

    def callbackCancel( self, event ):
        self.close()

