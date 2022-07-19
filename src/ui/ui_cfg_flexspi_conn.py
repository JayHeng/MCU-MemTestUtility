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
from win import flexspiConnectCfgWin

class memTesterUiCfgFlexspiConn(QMainWindow, flexspiConnectCfgWin.Ui_flexspiConnCfgDialog):

    def __init__(self, parent=None):
        super(memTesterUiCfgFlexspiConn, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        self.flexspiConnDict = None
        self.textEdit_flexspiConnection = None
        flexspiConnCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.flexspiConnCfgDict = flexspiConnCfgDict.copy()

    def _register_callbacks(self):
        self.comboBox_instance.currentIndexChanged.connect(self.callbackSwitchInstance)
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def setNecessaryInfo( self, flexspiConnDict, textEdit_flexspiConnection ):
        self.flexspiConnDict = flexspiConnDict
        self.textEdit_flexspiConnection = textEdit_flexspiConnection
        self._recoverLastSettings()

    def _switchInstance( self ,instance ):
        self.comboBox_dataL4b.clear()
        self.comboBox_dataL4b.addItems(self.flexspiConnDict['dataL4b'][instance].keys())
        self.comboBox_dataH4b.clear()
        self.comboBox_dataH4b.addItems(self.flexspiConnDict['dataH4b'][instance].keys())
        self.comboBox_ssb.clear()
        self.comboBox_ssb.addItems(self.flexspiConnDict['ssb'][instance].keys())
        self.comboBox_sclk.clear()
        self.comboBox_sclk.addItems(self.flexspiConnDict['sclk'][instance].keys())
        self.comboBox_dqs.clear()
        self.comboBox_dqs.addItems(self.flexspiConnDict['dqs'][instance].keys())
        self.comboBox_sclkn.clear()
        self.comboBox_sclkn.addItems(self.flexspiConnDict['sclkn'][instance].keys())
        self.comboBox_rstb.clear()
        self.comboBox_rstb.addItems(self.flexspiConnDict['rstb'][instance].keys())

    def callbackSwitchInstance( self ):
        instance = self.comboBox_instance.currentIndex()
        self._switchInstance(instance)

    def _recoverLastSettings ( self ):
        instance = self.flexspiConnCfgDict['instance'] - 1
        self.comboBox_instance.clear()
        self.comboBox_instance.addItems(self.flexspiConnDict['instance'].keys())
        self.comboBox_instance.setCurrentIndex(instance)
        self._switchInstance(instance)
        for key in self.flexspiConnDict['dataL4b'][instance].keys():
            if self.flexspiConnDict['dataL4b'][instance][key] == self.flexspiConnCfgDict['dataL4b']:
                self.comboBox_dataL4b.setCurrentIndex(self.comboBox_dataL4b.findText(key))
                break
        for key in self.flexspiConnDict['dataH4b'][instance].keys():
            if self.flexspiConnDict['dataH4b'][instance][key] == self.flexspiConnCfgDict['dataH4b']:
                self.comboBox_dataH4b.setCurrentIndex(self.comboBox_dataH4b.findText(key))
                break
        for key in self.flexspiConnDict['ssb'][instance].keys():
            if self.flexspiConnDict['ssb'][instance][key] == self.flexspiConnCfgDict['ssb']:
                self.comboBox_ssb.setCurrentIndex(self.comboBox_ssb.findText(key))
                break
        for key in self.flexspiConnDict['sclk'][instance].keys():
            if self.flexspiConnDict['sclk'][instance][key] == self.flexspiConnCfgDict['sclk']:
                self.comboBox_sclk.setCurrentIndex(self.comboBox_sclk.findText(key))
                break
        for key in self.flexspiConnDict['dqs'][instance].keys():
            if self.flexspiConnDict['dqs'][instance][key] == self.flexspiConnCfgDict['dqs']:
                self.comboBox_dqs.setCurrentIndex(self.comboBox_dqs.findText(key))
                break
        for key in self.flexspiConnDict['sclkn'][instance].keys():
            if self.flexspiConnDict['sclkn'][instance][key] == self.flexspiConnCfgDict['sclkn']:
                self.comboBox_sclkn.setCurrentIndex(self.comboBox_sclkn.findText(key))
                break
        for key in self.flexspiConnDict['rstb'][instance].keys():
            if self.flexspiConnDict['rstb'][instance][key] == self.flexspiConnCfgDict['rstb']:
                self.comboBox_rstb.setCurrentIndex(self.comboBox_rstb.findText(key))
                break


    def callbackOk( self, event ):
        self.flexspiConnCfgDict['instance'] = int(self.comboBox_instance.currentText())
        instance = self.flexspiConnCfgDict['instance'] - 1

        self.textEdit_flexspiConnection.clear()

        pinStr = self.comboBox_dataL4b.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['dataL4b'] = self.flexspiConnDict['dataL4b'][instance][pinStr]

        pinStr = self.comboBox_dataH4b.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['dataH4b'] = self.flexspiConnDict['dataH4b'][instance][pinStr]

        pinStr = self.comboBox_ssb.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['ssb'] = self.flexspiConnDict['ssb'][instance][pinStr]

        pinStr = self.comboBox_sclk.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['sclk'] = self.flexspiConnDict['sclk'][instance][pinStr]

        pinStr = self.comboBox_dqs.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['dqs'] = self.flexspiConnDict['dqs'][instance][pinStr]

        pinStr = self.comboBox_sclkn.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['sclkn'] = self.flexspiConnDict['sclkn'][instance][pinStr]

        pinStr = self.comboBox_rstb.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['rstb'] = self.flexspiConnDict['rstb'][instance][pinStr]
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn, self.flexspiConnCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()


