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
from win import flexspiPinUnittestWin

class memTesterUiCfgFlexspiPin(QMainWindow, flexspiPinUnittestWin.Ui_flexspiPinUnittestDialog):

    def __init__(self, parent=None):
        super(memTesterUiCfgFlexspiPin, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        flexspiUnittestCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiUnittest)
        self.flexspiUnittestCfgDict = flexspiUnittestCfgDict.copy()
        self._recoverLastSettings()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        self.lineEdit_wavePulse.setText(str(self.flexspiUnittestCfgDict['wavePulse']))
        self.comboBox_dataL4b.setCurrentIndex(self.flexspiUnittestCfgDict['dataL4b_dis'])
        self.comboBox_dataH4b.setCurrentIndex(self.flexspiUnittestCfgDict['dataH4b_dis'])
        self.comboBox_ssb.setCurrentIndex(self.flexspiUnittestCfgDict['ssb_dis'])
        self.comboBox_sclk.setCurrentIndex(self.flexspiUnittestCfgDict['sclk_dis'])
        self.comboBox_dqs.setCurrentIndex(self.flexspiUnittestCfgDict['dqs_dis'])
        self.comboBox_sclkn.setCurrentIndex(self.flexspiUnittestCfgDict['sclkn_dis'])
        self.comboBox_rstb.setCurrentIndex(self.flexspiUnittestCfgDict['rstb_dis'])

    def callbackOk( self, event ):
        self.flexspiUnittestCfgDict['wavePulse'] = int(self.lineEdit_wavePulse.text())
        self.flexspiUnittestCfgDict['dataL4b_dis'] = self.comboBox_dataL4b.currentIndex()
        self.flexspiUnittestCfgDict['dataH4b_dis'] = self.comboBox_dataH4b.currentIndex()
        self.flexspiUnittestCfgDict['ssb_dis'] = self.comboBox_ssb.currentIndex()
        self.flexspiUnittestCfgDict['sclk_dis'] = self.comboBox_sclk.currentIndex()
        self.flexspiUnittestCfgDict['dqs_dis'] = self.comboBox_dqs.currentIndex()
        self.flexspiUnittestCfgDict['sclkn_dis'] = self.comboBox_sclkn.currentIndex()
        self.flexspiUnittestCfgDict['rstb_dis'] = self.comboBox_rstb.currentIndex()
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_FlexspiUnittest, self.flexspiUnittestCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

