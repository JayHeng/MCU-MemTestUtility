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
from win import rwTestWin

kRwTestSet_WriteReadVerify      = 0x90

rwTestSetList = ['write-read-verify']

class memTesterUiRwTest(QMainWindow, rwTestWin.Ui_rwTestDialog):

    def __init__(self, parent=None):
        super(memTesterUiRwTest, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        rwtestCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_RwTest)
        self.mixspiRwtestCfgDict = rwtestCfgDict.copy()
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
        if self.mixspiRwtestCfgDict['testSet'] == kRwTestSet_WriteReadVerify:
            self.comboBox_testSet.setCurrentIndex(0)
        else:
            pass
        self.lineEdit_testMemStart.setText(str(hex(self.mixspiRwtestCfgDict['testMemStart'])))
        self.lineEdit_testMemSize.setText(str(hex(self.mixspiRwtestCfgDict['testMemSize'])))
        self.lineEdit_fillPatternWord.setText(str(hex(self.mixspiRwtestCfgDict['fillPatternWord'])))

    def callbackOk( self, event ):
        testSetIdx = self.comboBox_testSet.currentIndex()
        if testSetIdx == 0:
            self.mixspiRwtestCfgDict['testSet'] = kRwTestSet_WriteReadVerify
        else:
            pass
        status, memStart = self._getVal32FromHexText(self.lineEdit_testMemStart.text())
        if status:
            self.mixspiRwtestCfgDict['testMemStart'] = memStart
        else:
            return
        status, memSize = self._getVal32FromHexText(self.lineEdit_testMemSize.text())
        if status:
            self.mixspiRwtestCfgDict['testMemSize'] = memSize
        else:
            return
        status, patternWord = self._getVal32FromHexText(self.lineEdit_fillPatternWord.text())
        if status:
            self.mixspiRwtestCfgDict['fillPatternWord'] = patternWord
        else:
            return
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_RwTest, self.mixspiRwtestCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

