#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from . import uidef
from . import uilang
from . import uivar
from . import ui_def_flexspi_conn_rt1170
sys.path.append(os.path.abspath(".."))
from win import flexspiConnectCfgWin

class memTesterUiCfgFlexspiConn(QMainWindow, flexspiConnectCfgWin.Ui_flexspiConnCfgDialog):

    def __init__(self, parent=None):
        super(memTesterUiCfgFlexspiConn, self).__init__(parent)
        self.setupUi(self)
        self._register_callbacks()
        self.mcuDevice = None
        self.textEdit_flexspiConnection = None
        flexspiConnCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.flexspiConnCfgDict = flexspiConnCfgDict.copy()

    def _register_callbacks(self):
        self.comboBox_instance.currentIndexChanged.connect(self.callbackSwitchInstance)
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)

    def setNecessaryInfo( self, mcuDevice, textEdit_flexspiConnection ):
        self.mcuDevice = mcuDevice
        self.textEdit_flexspiConnection = textEdit_flexspiConnection
        self._recoverLastSettings()

    def _switchInstance( self ,instance ):
        if self.mcuDevice == uidef.kMcuDevice_iMXRT117x:
            self.comboBox_dataL4b.clear()
            self.comboBox_dataL4b.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataL4b[instance].keys())
            self.comboBox_dataH4b.clear()
            self.comboBox_dataH4b.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataH4b[instance].keys())
            self.comboBox_ssb.clear()
            self.comboBox_ssb.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_ssb[instance].keys())
            self.comboBox_sclk.clear()
            self.comboBox_sclk.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclk[instance].keys())
            self.comboBox_dqs.clear()
            self.comboBox_dqs.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_dqs[instance].keys())
            self.comboBox_sclkn.clear()
            self.comboBox_sclkn.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclkn[instance].keys())
            self.comboBox_rstb.clear()
            self.comboBox_rstb.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_rstb[instance].keys())
        else:
            pass

    def callbackSwitchInstance( self ):
        instance = self.comboBox_instance.currentIndex()
        self._switchInstance(instance)

    def _recoverLastSettings ( self ):
        instance = self.flexspiConnCfgDict['instance'] - 1
        if self.mcuDevice == uidef.kMcuDevice_iMXRT117x:
            self.comboBox_instance.clear()
            self.comboBox_instance.addItems(ui_def_flexspi_conn_rt1170.kFlexspiConnSel_Instance.keys())
            self.comboBox_instance.setCurrentIndex(instance)
            self._switchInstance(instance)
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataL4b[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataL4b[instance][key] == self.flexspiConnCfgDict['dataL4b']:
                    self.comboBox_dataL4b.setCurrentIndex(self.comboBox_dataL4b.findText(key))
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataH4b[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataH4b[instance][key] == self.flexspiConnCfgDict['dataH4b']:
                    self.comboBox_dataH4b.setCurrentIndex(self.comboBox_dataH4b.findText(key))
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_ssb[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_ssb[instance][key] == self.flexspiConnCfgDict['ssb']:
                    self.comboBox_ssb.setCurrentIndex(self.comboBox_ssb.findText(key))
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclk[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclk[instance][key] == self.flexspiConnCfgDict['sclk']:
                    self.comboBox_sclk.setCurrentIndex(self.comboBox_sclk.findText(key))
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_dqs[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_dqs[instance][key] == self.flexspiConnCfgDict['dqs']:
                    self.comboBox_dqs.setCurrentIndex(self.comboBox_dqs.findText(key))
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclkn[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclkn[instance][key] == self.flexspiConnCfgDict['sclkn']:
                    self.comboBox_sclkn.setCurrentIndex(self.comboBox_sclkn.findText(key))
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_rstb[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_rstb[instance][key] == self.flexspiConnCfgDict['rstb']:
                    self.comboBox_rstb.setCurrentIndex(self.comboBox_rstb.findText(key))
                    break
        else:
            pass

    def callbackOk( self, event ):
        self.flexspiConnCfgDict['instance'] = int(self.comboBox_instance.currentText())
        instance = self.flexspiConnCfgDict['instance'] - 1

        self.textEdit_flexspiConnection.clear()

        pinStr = self.comboBox_dataL4b.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['dataL4b'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataL4b[instance][pinStr]

        pinStr = self.comboBox_dataH4b.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['dataH4b'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataH4b[instance][pinStr]

        pinStr = self.comboBox_ssb.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['ssb'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_ssb[instance][pinStr]

        pinStr = self.comboBox_sclk.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['sclk'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclk[instance][pinStr]

        pinStr = self.comboBox_dqs.currentText()
        self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['dqs'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_dqs[instance][pinStr]

        pinStr = self.comboBox_sclkn.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['sclkn'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclkn[instance][pinStr]

        pinStr = self.comboBox_rstb.currentText()
        if pinStr != 'None':
            self.textEdit_flexspiConnection.append(pinStr)
        self.flexspiConnCfgDict['rstb'] = ui_def_flexspi_conn_rt1170.kFlexspiConnSel_rstb[instance][pinStr]
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn, self.flexspiConnCfgDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()


