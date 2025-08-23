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
from win import memRegsWin

class memTesterUiMemRegs(QMainWindow, memRegsWin.Ui_memRegsDialog):

    def __init__(self, parent=None):
        super(memTesterUiMemRegs, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        memRegsCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_MemRegs)
        self.mixspiMemRegsCfgDict = memRegsCfgDict.copy()

    def _register_callbacks(self):
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)
        self.comboBox_accessType.currentIndexChanged.connect(self.callbackChangeAccessType)
        self.comboBox_registerIdx.currentIndexChanged.connect(self.callbackChangeRegisterIdx)

    def setNecessaryInfo( self, memPropertyDict ):
        self.memPropertyDict = memPropertyDict.copy()
        self._recoverLastSettings()

    def _refreshRegsProperty( self ):
        try:
            self.pushButton_reg0.setText(self.memPropertyDict['statRegName'])
            self.pushButton_reg1.setText(self.memPropertyDict['reg1Name'])
            self.pushButton_reg2.setText(self.memPropertyDict['reg2Name'])
            self.pushButton_reg3.setText('N/A')
            self.pushButton_reg4.setText('N/A')
            self.pushButton_reg5.setText('N/A')
            self.pushButton_reg6.setText('N/A')
            self.pushButton_reg7.setText('N/A')
            self.pushButton_reg8.setText('N/A')
        except:
            pass
        self.lineEdit_reg0.setReadOnly(True)
        self.lineEdit_reg1.setReadOnly(True)
        self.lineEdit_reg2.setReadOnly(True)
        self.lineEdit_reg3.setReadOnly(True)
        self.lineEdit_reg4.setReadOnly(True)
        self.lineEdit_reg5.setReadOnly(True)
        self.lineEdit_reg6.setReadOnly(True)
        self.lineEdit_reg7.setReadOnly(True)
        self.lineEdit_reg8.setReadOnly(True)
        if not self.mixspiMemRegsCfgDict['isTypeRead']:
            if self.mixspiMemRegsCfgDict['regIdx'] == 1:
                self.lineEdit_reg0.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 2:
                self.lineEdit_reg1.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 3:
                self.lineEdit_reg2.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 4:
                self.lineEdit_reg3.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 5:
                self.lineEdit_reg4.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 6:
                self.lineEdit_reg5.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 7:
                self.lineEdit_reg6.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 8:
                self.lineEdit_reg7.setReadOnly(False)
            elif self.mixspiMemRegsCfgDict['regIdx'] == 9:
                self.lineEdit_reg8.setReadOnly(False)
            else:
                self.lineEdit_reg0.setReadOnly(False)
                self.lineEdit_reg1.setReadOnly(False)
                self.lineEdit_reg2.setReadOnly(False)
                self.lineEdit_reg3.setReadOnly(False)
                self.lineEdit_reg4.setReadOnly(False)
                self.lineEdit_reg5.setReadOnly(False)
                self.lineEdit_reg6.setReadOnly(False)
                self.lineEdit_reg7.setReadOnly(False)
                self.lineEdit_reg8.setReadOnly(False)
        else:
            if self.mixspiMemRegsCfgDict['regsVal'][0] != None:
                self.lineEdit_reg0.setText(str(hex(self.mixspiMemRegsCfgDict['regsVal'][0])))
            if self.mixspiMemRegsCfgDict['regsVal'][1] != None:
                self.lineEdit_reg1.setText(str(hex(self.mixspiMemRegsCfgDict['regsVal'][1])))
            if self.mixspiMemRegsCfgDict['regsVal'][2] != None:
                self.lineEdit_reg2.setText(str(hex(self.mixspiMemRegsCfgDict['regsVal'][2])))

    def _recoverLastSettings ( self ): 
        if self.mixspiMemRegsCfgDict['isTypeRead']:
            self.comboBox_accessType.setCurrentIndex(0)
        else:
            self.comboBox_accessType.setCurrentIndex(1)
        self.comboBox_registerIdx.setCurrentIndex(self.mixspiMemRegsCfgDict['regIdx'])
        self._refreshRegsProperty()

    def callbackChangeAccessType( self ):
        if self.comboBox_accessType.currentIndex() == 0:
            self.mixspiMemRegsCfgDict['isTypeRead'] = True
        else:
            self.mixspiMemRegsCfgDict['isTypeRead'] = False
        self._refreshRegsProperty()

    def callbackChangeRegisterIdx( self ):
        self.mixspiMemRegsCfgDict['regIdx'] = self.comboBox_registerIdx.currentIndex()
        self._refreshRegsProperty()

    def callbackOk( self, event ):
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_MemRegs, self.mixspiMemRegsCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()

