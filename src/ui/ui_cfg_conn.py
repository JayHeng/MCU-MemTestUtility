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
from win import connCfgWin

class memTesterUiConn(QMainWindow, connCfgWin.Ui_connCfgDialog):

    def __init__(self, parent=None):
        super(memTesterUiConn, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        self.mixspiConnDict = None
        self.textEdit_mixspiConnection = None
        connCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_Conn)
        self.mixspiConnCfgDict = connCfgDict.copy()

    def _register_callbacks(self):
        self.comboBox_instance.currentIndexChanged.connect(self.callbackSwitchInstance)
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def setNecessaryInfo( self, mixspiConnDict, textEdit_mixspiConnection ):
        self.mixspiConnDict = mixspiConnDict
        self.textEdit_mixspiConnection = textEdit_mixspiConnection
        self._recoverLastSettings()

    def _switchInstance( self ,instance ):
        self.comboBox_dataL4b.clear()
        self.comboBox_dataL4b.addItems(self.mixspiConnDict['dataL4b'][instance].keys())
        self.comboBox_dataH4b.clear()
        self.comboBox_dataH4b.addItems(self.mixspiConnDict['dataH4b'][instance].keys())
        self.comboBox_dataT8b.clear()
        self.comboBox_dataT8b.addItems(self.mixspiConnDict['dataT8b'][instance].keys())
        self.comboBox_ssb.clear()
        self.comboBox_ssb.addItems(self.mixspiConnDict['ssb'][instance].keys())
        self.comboBox_sclk.clear()
        self.comboBox_sclk.addItems(self.mixspiConnDict['sclk'][instance].keys())
        self.comboBox_sclkn.clear()
        self.comboBox_sclkn.addItems(self.mixspiConnDict['sclkn'][instance].keys())
        self.comboBox_dqs0.clear()
        self.comboBox_dqs0.addItems(self.mixspiConnDict['dqs0'][instance].keys())
        self.comboBox_dqs1.clear()
        self.comboBox_dqs1.addItems(self.mixspiConnDict['dqs1'][instance].keys())
        self.comboBox_rstb.clear()
        self.comboBox_rstb.addItems(self.mixspiConnDict['rstb'][instance].keys())

    def callbackSwitchInstance( self ):
        instance = self.comboBox_instance.currentIndex()
        self.mixspiConnCfgDict['instance'] = instance + 1
        self._recoverLastSettings(False)

    def _recoverLastSettings ( self , needToUpdateInst = True):
        instance = self.mixspiConnCfgDict['instance'] - 1
        if needToUpdateInst:
            self.comboBox_instance.clear()
            self.comboBox_instance.addItems(self.mixspiConnDict['instance'].keys())
            self.comboBox_instance.setCurrentIndex(instance)
        self._switchInstance(instance)
        for key in self.mixspiConnDict['dataL4b'][instance].keys():
            if self.mixspiConnDict['dataL4b'][instance][key] == self.mixspiConnCfgDict['dataL4b']:
                self.comboBox_dataL4b.setCurrentIndex(self.comboBox_dataL4b.findText(key))
                break
        for key in self.mixspiConnDict['dataH4b'][instance].keys():
            if self.mixspiConnDict['dataH4b'][instance][key] == self.mixspiConnCfgDict['dataH4b']:
                self.comboBox_dataH4b.setCurrentIndex(self.comboBox_dataH4b.findText(key))
                break
        for key in self.mixspiConnDict['dataT8b'][instance].keys():
            if self.mixspiConnDict['dataT8b'][instance][key] == self.mixspiConnCfgDict['dataT8b']:
                self.comboBox_dataT8b.setCurrentIndex(self.comboBox_dataT8b.findText(key))
                break
        for key in self.mixspiConnDict['ssb'][instance].keys():
            if self.mixspiConnDict['ssb'][instance][key] == self.mixspiConnCfgDict['ssb']:
                self.comboBox_ssb.setCurrentIndex(self.comboBox_ssb.findText(key))
                break
        for key in self.mixspiConnDict['sclk'][instance].keys():
            if self.mixspiConnDict['sclk'][instance][key] == self.mixspiConnCfgDict['sclk']:
                self.comboBox_sclk.setCurrentIndex(self.comboBox_sclk.findText(key))
                break
        for key in self.mixspiConnDict['sclkn'][instance].keys():
            if self.mixspiConnDict['sclkn'][instance][key] == self.mixspiConnCfgDict['sclkn']:
                self.comboBox_sclkn.setCurrentIndex(self.comboBox_sclkn.findText(key))
                break
        for key in self.mixspiConnDict['dqs0'][instance].keys():
            if self.mixspiConnDict['dqs0'][instance][key] == self.mixspiConnCfgDict['dqs0']:
                self.comboBox_dqs0.setCurrentIndex(self.comboBox_dqs0.findText(key))
                break
        for key in self.mixspiConnDict['dqs1'][instance].keys():
            if self.mixspiConnDict['dqs1'][instance][key] == self.mixspiConnCfgDict['dqs1']:
                self.comboBox_dqs1.setCurrentIndex(self.comboBox_dqs1.findText(key))
                break
        for key in self.mixspiConnDict['rstb'][instance].keys():
            if self.mixspiConnDict['rstb'][instance][key] == self.mixspiConnCfgDict['rstb']:
                self.comboBox_rstb.setCurrentIndex(self.comboBox_rstb.findText(key))
                break


    def callbackOk( self, event ):
        self.mixspiConnCfgDict['instance'] = int(self.comboBox_instance.currentText())
        instance = self.mixspiConnCfgDict['instance'] - 1

        self.textEdit_mixspiConnection.clear()

        pinStr = self.comboBox_dataL4b.currentText()
        self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['dataL4b'] = self.mixspiConnDict['dataL4b'][instance][pinStr]

        pinStr = self.comboBox_dataH4b.currentText()
        if pinStr != 'None':
            self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['dataH4b'] = self.mixspiConnDict['dataH4b'][instance][pinStr]

        pinStr = self.comboBox_dataT8b.currentText()
        if pinStr != 'None':
            self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['dataT8b'] = self.mixspiConnDict['dataT8b'][instance][pinStr]

        pinStr = self.comboBox_ssb.currentText()
        self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['ssb'] = self.mixspiConnDict['ssb'][instance][pinStr]

        pinStr = self.comboBox_sclk.currentText()
        self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['sclk'] = self.mixspiConnDict['sclk'][instance][pinStr]

        pinStr = self.comboBox_sclkn.currentText()
        if pinStr != 'None':
            self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['sclkn'] = self.mixspiConnDict['sclkn'][instance][pinStr]

        pinStr = self.comboBox_dqs0.currentText()
        if pinStr != 'None':
            self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['dqs0'] = self.mixspiConnDict['dqs0'][instance][pinStr]

        pinStr = self.comboBox_dqs1.currentText()
        if pinStr != 'None':
            self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['dqs1'] = self.mixspiConnDict['dqs1'][instance][pinStr]

        pinStr = self.comboBox_rstb.currentText()
        if pinStr != 'None':
            self.textEdit_mixspiConnection.append(pinStr)
        self.mixspiConnCfgDict['rstb'] = self.mixspiConnDict['rstb'][instance][pinStr]
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Conn, self.mixspiConnCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()


