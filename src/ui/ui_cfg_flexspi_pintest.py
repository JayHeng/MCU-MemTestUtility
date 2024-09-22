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
        flexspiPintestCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiPintest)
        self.flexspiPintestCfgDict = flexspiPintestCfgDict.copy()
        self._recoverLastSettings()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        self.lineEdit_wavePulse.setText(str(self.flexspiPintestCfgDict['wavePulse']))
        self.comboBox_dataL4b.setCurrentIndex(self.flexspiPintestCfgDict['dataL4b_dis'])
        self.comboBox_dataH4b.setCurrentIndex(self.flexspiPintestCfgDict['dataH4b_dis'])
        self.comboBox_ssb.setCurrentIndex(self.flexspiPintestCfgDict['ssb_dis'])
        self.comboBox_sclk.setCurrentIndex(self.flexspiPintestCfgDict['sclk_dis'])
        self.comboBox_dqs.setCurrentIndex(self.flexspiPintestCfgDict['dqs_dis'])
        self.comboBox_sclkn.setCurrentIndex(self.flexspiPintestCfgDict['sclkn_dis'])
        self.comboBox_rstb.setCurrentIndex(self.flexspiPintestCfgDict['rstb_dis'])

    def callbackOk( self, event ):
        self.flexspiPintestCfgDict['wavePulse'] = int(self.lineEdit_wavePulse.text())
        self.flexspiPintestCfgDict['dataL4b_dis'] = self.comboBox_dataL4b.currentIndex()
        self.flexspiPintestCfgDict['dataH4b_dis'] = self.comboBox_dataH4b.currentIndex()
        self.flexspiPintestCfgDict['ssb_dis'] = self.comboBox_ssb.currentIndex()
        self.flexspiPintestCfgDict['sclk_dis'] = self.comboBox_sclk.currentIndex()
        self.flexspiPintestCfgDict['dqs_dis'] = self.comboBox_dqs.currentIndex()
        self.flexspiPintestCfgDict['sclkn_dis'] = self.comboBox_sclkn.currentIndex()
        self.flexspiPintestCfgDict['rstb_dis'] = self.comboBox_rstb.currentIndex()
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_FlexspiPintest, self.flexspiPintestCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

