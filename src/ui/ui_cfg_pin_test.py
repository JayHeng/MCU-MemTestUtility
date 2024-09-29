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
from win import pinTestWin

class memTesterUiPinTest(QMainWindow, pinTestWin.Ui_pinTestDialog):

    def __init__(self, parent=None):
        super(memTesterUiPinTest, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        pintestCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_Pintest)
        self.mixspiPintestCfgDict = pintestCfgDict.copy()
        self._recoverLastSettings()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        self.lineEdit_wavePulse.setText(str(self.mixspiPintestCfgDict['wavePulse']))
        self.comboBox_waveSample.setCurrentIndex(self.mixspiPintestCfgDict['waveSample'])
        self.comboBox_dataL4b.setCurrentIndex(self.mixspiPintestCfgDict['dataL4b_dis'])
        self.comboBox_dataH4b.setCurrentIndex(self.mixspiPintestCfgDict['dataH4b_dis'])
        self.comboBox_dataT8b.setCurrentIndex(self.mixspiPintestCfgDict['dataT8b_dis'])
        self.comboBox_ssb.setCurrentIndex(self.mixspiPintestCfgDict['ssb_dis'])
        self.comboBox_sclk.setCurrentIndex(self.mixspiPintestCfgDict['sclk_dis'])
        self.comboBox_sclkn.setCurrentIndex(self.mixspiPintestCfgDict['sclkn_dis'])
        self.comboBox_dqs0.setCurrentIndex(self.mixspiPintestCfgDict['dqs0_dis'])
        self.comboBox_dqs1.setCurrentIndex(self.mixspiPintestCfgDict['dqs1_dis'])
        self.comboBox_rstb.setCurrentIndex(self.mixspiPintestCfgDict['rstb_dis'])

    def callbackOk( self, event ):
        self.mixspiPintestCfgDict['wavePulse'] = int(self.lineEdit_wavePulse.text())
        self.mixspiPintestCfgDict['waveSample'] = self.comboBox_waveSample.currentIndex()
        self.mixspiPintestCfgDict['dataL4b_dis'] = self.comboBox_dataL4b.currentIndex()
        self.mixspiPintestCfgDict['dataH4b_dis'] = self.comboBox_dataH4b.currentIndex()
        self.mixspiPintestCfgDict['dataT8b_dis'] = self.comboBox_dataT8b.currentIndex()
        self.mixspiPintestCfgDict['ssb_dis'] = self.comboBox_ssb.currentIndex()
        self.mixspiPintestCfgDict['sclk_dis'] = self.comboBox_sclk.currentIndex()
        self.mixspiPintestCfgDict['sclkn_dis'] = self.comboBox_sclkn.currentIndex()
        self.mixspiPintestCfgDict['dqs0_dis'] = self.comboBox_dqs0.currentIndex()
        self.mixspiPintestCfgDict['dqs1_dis'] = self.comboBox_dqs1.currentIndex()
        self.mixspiPintestCfgDict['rstb_dis'] = self.comboBox_rstb.currentIndex()
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Pintest, self.mixspiPintestCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()
