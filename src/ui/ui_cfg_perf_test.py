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
from win import perfTestWin

kPerfTestSet_Coremark        = 0xA0
kPerfTestSet_Dhrystone       = 0xB0
kPerfTestSet_Mbw             = 0xC0
kPerfTestSet_Sysbench        = 0xD0

perfTestSetList = ['coremark', 'dhrystone', 'mbw', 'sysbench']

kPerfTestSubSet_Memcpy       = 0xC1
kPerfTestSubSet_Dumb         = 0xC2
kPerfTestSubSet_MemcpyFixBlk = 0xC3

perfTestSubSetList = ['1 - memcpy test', '2 - dumb (b[i]=a[i] style) test', '3 - memcpy test with fixed block size']

class memTesterUiPerfTest(QMainWindow, perfTestWin.Ui_perfTestDialog):

    def __init__(self, parent=None):
        super(memTesterUiPerfTest, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        perftestCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_PerfTest)
        self.mixspiPerftestCfgDict = perftestCfgDict.copy()
        self._recoverLastSettings()

    def _showInfoMessage( self, myTitle, myContent):
        QMessageBox.information( self, myTitle, myContent )

    def _getVal32FromHexText( self, hexText ):
        status = False
        val32 = None
        if len(hexText) > 2 and hexText[0:2] == '0x':
            try:
                val32 = int(hexText[2:len(hexText)], 16)
                status = True
            except:
                pass
        if not status:
            self._showInfoMessage('Illegal Input', 'You should input like this format: 0x5000 for mem start and size fields')
        return status, val32

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def _recoverLastSettings ( self ):
        if self.mixspiPerftestCfgDict['testSet'] == kPerfTestSet_Coremark:
            self.comboBox_testSet.setCurrentIndex(0)
        elif self.mixspiPerftestCfgDict['testSet'] == kPerfTestSet_Dhrystone:
            self.comboBox_testSet.setCurrentIndex(1)
        elif self.mixspiPerftestCfgDict['testSet'] == kPerfTestSet_Mbw:
            self.comboBox_testSet.setCurrentIndex(2)
            self.comboBox_subTestSet.setCurrentIndex(self.mixspiPerftestCfgDict['subTestSet'] - kPerfTestSet_Mbw - 1)
            if self.mixspiPerftestCfgDict['enableAverageShow']:
                self.comboBox_showAvg.setCurrentIndex(0)
            else:
                self.comboBox_showAvg.setCurrentIndex(1)
        elif self.mixspiPerftestCfgDict['testSet'] == kPerfTestSet_Sysbench:
            self.comboBox_testSet.setCurrentIndex(3)
        else:
            pass
        self.lineEdit_numOfRuns.setText(str(self.mixspiPerftestCfgDict['iterations']))
        self.lineEdit_testMemStart.setText(str(hex(self.mixspiPerftestCfgDict['testMemStart'])))
        self.lineEdit_testMemSize.setText(str(hex(self.mixspiPerftestCfgDict['testMemSize'])))
        self.lineEdit_testBlockSize.setText(str(hex(self.mixspiPerftestCfgDict['testBlockSize'])))

    def callbackOk( self, event ):
        testSetIdx = self.comboBox_testSet.currentIndex()
        if testSetIdx == 0:
            self.mixspiPerftestCfgDict['testSet'] = kPerfTestSet_Coremark
        elif  testSetIdx == 1:
            self.mixspiPerftestCfgDict['testSet'] = kPerfTestSet_Dhrystone
        elif  testSetIdx == 2:
            self.mixspiPerftestCfgDict['testSet'] = kPerfTestSet_Mbw
            self.mixspiPerftestCfgDict['subTestSet'] = kPerfTestSet_Mbw + self.comboBox_subTestSet.currentIndex() + 1
            if self.comboBox_showAvg.currentText() == 'Yes':
                self.mixspiPerftestCfgDict['enableAverageShow'] = 1
            else:
                self.mixspiPerftestCfgDict['enableAverageShow'] = 0
        elif  testSetIdx == 3:
            self.mixspiPerftestCfgDict['testSet'] = kPerfTestSet_Sysbench
        else:
            pass
        self.mixspiPerftestCfgDict['iterations'] = int(self.lineEdit_numOfRuns.text())
        status, memStart = self._getVal32FromHexText(self.lineEdit_testMemStart.text())
        if status:
            self.mixspiPerftestCfgDict['testMemStart'] = memStart
        else:
            return
        status, memSize = self._getVal32FromHexText(self.lineEdit_testMemSize.text())
        if status:
            self.mixspiPerftestCfgDict['testMemSize'] = memSize
        else:
            return
        status, blockSize = self._getVal32FromHexText(self.lineEdit_testBlockSize.text())
        if status:
            self.mixspiPerftestCfgDict['testBlockSize'] = blockSize
        else:
            return
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_PerfTest, self.mixspiPerftestCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

