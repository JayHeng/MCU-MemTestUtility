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
from win import padCtrlRT11yyWin

class memTesterUiPadCtrlRT11yy(QMainWindow, padCtrlRT11yyWin.Ui_padCtrlRT11yyDialog):

    def __init__(self, parent=None):
        super(memTesterUiPadCtrlRT11yy, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        padCtrlDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_PadCtrl)
        self.mixspiPadCtrlDict = padCtrlDict.copy()
        self._recoverLastSettings()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        self.comboBox_ode.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValC'] >> 4) & 0x1)
        self.comboBox_pull.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValC'] >> 2) & 0x3)
        self.comboBox_pdrv.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValC'] >> 1) & 0x1)
        self.comboBox_pus.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValA'] >> 3) & 0x1)
        self.comboBox_pue.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValA'] >> 2) & 0x1)
        self.comboBox_dse.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValA'] >> 1) & 0x1)
        self.comboBox_pus.setCurrentIndex((self.mixspiPadCtrlDict['rt11yyValA'] >> 0) & 0x1)

    def callbackOk( self, event ):
        rt11yyValC = 0x0
        rt11yyValA = 0x0
        ode = self.comboBox_ode.currentIndex()
        pull = self.comboBox_pull.currentIndex()
        pdrv = self.comboBox_pdrv.currentIndex()
        pus = self.comboBox_pus.currentIndex()
        pue = self.comboBox_pue.currentIndex()
        dse = self.comboBox_dse.currentIndex()
        sre = self.comboBox_sre.currentIndex()
        rt11yyValC = rt11yyValC | (ode << 4) | (pull << 2) | (pdrv << 1);
        rt11yyValA = rt11yyValA | (ode << 4) | (pus << 3) | (pue << 2) | (dse << 1) | (sre << 0);
        self.mixspiPadCtrlDict['rt11yyValC'] = rt11yyValC
        self.mixspiPadCtrlDict['rt11yyValA'] = rt11yyValA
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_PadCtrl, self.mixspiPadCtrlDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

