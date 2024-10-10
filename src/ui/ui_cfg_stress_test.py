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
from win import stressTestWin

kStressTestSet_Memtester     = 0xE0

stressTestSetList = ['memtester']

class memTesterUiStressTest(QMainWindow, stressTestWin.Ui_stressTestDialog):

    def __init__(self, parent=None):
        super(memTesterUiStressTest, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        stresstestCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_StressTest)
        self.mixspiStresstestCfgDict = stresstestCfgDict.copy()
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
        if self.mixspiStresstestCfgDict['testSet'] == kStressTestSet_Memtester:
            self.comboBox_testSet.setCurrentIndex(0)
            if self.mixspiStresstestCfgDict['enableStopWhenFail']:
                self.comboBox_stopWhenFail.setCurrentIndex(0)
            else:
                self.comboBox_stopWhenFail.setCurrentIndex(1)
        self.lineEdit_numOfRuns.setText(str(self.mixspiStresstestCfgDict['iterations']))
        self.lineEdit_testMemStart.setText(str(hex(self.mixspiStresstestCfgDict['testMemStart'])))
        self.lineEdit_testMemSize.setText(str(hex(self.mixspiStresstestCfgDict['testMemSize'])))
        self.lineEdit_testPageSize.setText(str(hex(self.mixspiStresstestCfgDict['testPageSize'])))

    def callbackOk( self, event ):
        testSetIdx = self.comboBox_testSet.currentIndex()
        if testSetIdx == 0:
            self.mixspiStresstestCfgDict['testSet'] = kStressTestSet_Memtester
            if self.comboBox_stopWhenFail.currentText() == 'Yes':
                self.mixspiStresstestCfgDict['enableStopWhenFail'] = 1
            else:
                self.mixspiStresstestCfgDict['enableStopWhenFail'] = 0
        else:
            pass
        self.mixspiStresstestCfgDict['iterations'] = int(self.lineEdit_numOfRuns.text())
        status, memStart = self._getVal32FromHexText(self.lineEdit_testMemStart.text())
        if status:
            self.mixspiStresstestCfgDict['testMemStart'] = memStart
        else:
            return
        status, memSize = self._getVal32FromHexText(self.lineEdit_testMemSize.text())
        if status:
            self.mixspiStresstestCfgDict['testMemSize'] = memSize
        else:
            return
        status, pageSize = self._getVal32FromHexText(self.lineEdit_testPageSize.text())
        if status:
            self.mixspiStresstestCfgDict['testPageSize'] = pageSize
        else:
            return
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_StressTest, self.mixspiStresstestCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

