#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from . import uidef
from . import uilang
from . import uivar
from . import ui_cfg_pad_ctrl_rtxxx
from . import ui_cfg_pad_ctrl_rt10yy
from . import ui_cfg_pad_ctrl_rt11yy
sys.path.append(os.path.abspath(".."))
from win import connCfgWin

kRT1xxxGpioGroupList_COMM = ["GPIO_EMC_B", "GPIO_SD_B", "GPIO_B"]
kRT1xxxGpioGroupList_AD   = ["GPIO_AD", "GPIO_AON"]

kDefaultPadCtrlVal = 0xFFFFFFFF

class memTesterUiConn(QMainWindow, connCfgWin.Ui_connCfgDialog):

    def __init__(self, parent=None):
        super(memTesterUiConn, self).__init__(parent)
        self.setupUi(self)
        self.mixspiConnDict = None
        self.textEdit_mixspiConnection = None
        connCfgDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_Conn)
        self.mixspiConnCfgDict = connCfgDict.copy()
        padCtrlDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_PadCtrl)
        self.mixspiPadCtrlDict = padCtrlDict.copy()
        self.padCtrlRTxxxFrame = ui_cfg_pad_ctrl_rtxxx.memTesterUiPadCtrlRTxxx()
        self.padCtrlRTxxxFrame.setWindowTitle(u"i.MXRTxxx IOPCTL configuration")
        self.padCtrlRT10yyFrame = ui_cfg_pad_ctrl_rt10yy.memTesterUiPadCtrlRT10yy()
        self.padCtrlRT10yyFrame.setWindowTitle(u"i.MXRT1xxx IOMUXC SW PAD Control Register")
        self.padCtrlRT11yyFrame = ui_cfg_pad_ctrl_rt11yy.memTesterUiPadCtrlRT11yy()
        self.padCtrlRT11yyFrame.setWindowTitle(u"i.MXRT1xxx IOMUXC SW PAD Control Register")
        self._register_callbacks()

    def _showInfoMessage( self, myTitle, myContent):
        QMessageBox.information( self, myTitle, myContent )

    def _getVal32FromHexText( self, hexText ):
        status = False
        val32 = None
        if hexText == 'N/A':
            return True, kDefaultPadCtrlVal
        if len(hexText) > 2 and hexText[0:2] == '0x':
            try:
                val32 = int(hexText[2:len(hexText)], 16)
                status = True
            except:
                pass
        if not status:
            self._showInfoMessage('Illegal Input', 'You should input like this format: 0x1f or keep N/A for pad ctrl fields')
        return status, val32

    def _register_callbacks(self):
        self.comboBox_instance.currentIndexChanged.connect(self.callbackSwitchInstance)
        self.pushButton_padCtrl.clicked.connect(self.callbackPadCtrl)
        self.pushButton_ok.clicked.connect(self.callbackOk)
        self.pushButton_cancel.clicked.connect(self.callbackCancel)
        self.padCtrlRT11yyFrame.exitSignal.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_dataL4b.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_dataH4b.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_dataT8b.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_ssb.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_sclk.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_sclkn.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_dqs0.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_dqs1.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)
        self.comboBox_rstb.currentIndexChanged.connect(self.callbackRefreshUserPadCtrlSettings)

    def setNecessaryInfo( self, mcuDevice, mixspiConnDict, textEdit_mixspiConnection ):
        self.mcuDevice = mcuDevice
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
        self.callbackRefreshUserPadCtrlSettings()

    def _isGpioGroupMatched( self, gpioName, gpioGroupList):
        isMatched = False
        for group in gpioGroupList:
            if gpioName.find(group) != -1:
                isMatched = True
                break
        return isMatched

    def callbackRefreshUserPadCtrlSettings( self ):
        padCtrlDict= uivar.getAdvancedSettings(uidef.kAdvancedSettings_PadCtrl)
        self.mixspiPadCtrlDict = padCtrlDict.copy()
        padCtrl = 0
        if self.mcuDevice in uidef.kMcuDevice_iMXRT11yy:
            pinStr = self.comboBox_dataL4b.currentText()
            if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
            elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
            self.lineEdit_padCtrlDataL4b.setText(str(hex(padCtrl)))

            pinStr = self.comboBox_ssb.currentText()
            if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
            elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
            self.lineEdit_padCtrlSsb.setText(str(hex(padCtrl)))

            pinStr = self.comboBox_sclk.currentText()
            if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
            elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
            self.lineEdit_padCtrlSclk.setText(str(hex(padCtrl)))

            pinStr = self.comboBox_dataH4b.currentText()
            if pinStr != 'None':
                if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
                elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
                self.lineEdit_padCtrlDataH4b.setText(str(hex(padCtrl)))
            else:
                self.lineEdit_padCtrlDataH4b.setText('N/A')

            pinStr = self.comboBox_dataT8b.currentText()
            if pinStr != 'None':
                if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
                elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
                self.lineEdit_padCtrlDataT8b.setText(str(hex(padCtrl)))
            else:
                self.lineEdit_padCtrlDataT8b.setText('N/A')

            pinStr = self.comboBox_sclkn.currentText()
            if pinStr != 'None':
                if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
                elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
                self.lineEdit_padCtrlSclkn.setText(str(hex(padCtrl)))
            else:
                self.lineEdit_padCtrlSclkn.setText('N/A')

            pinStr = self.comboBox_dqs0.currentText()
            if pinStr != 'None':
                if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
                elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
                self.lineEdit_padCtrlDqs0.setText(str(hex(padCtrl)))
            else:
                self.lineEdit_padCtrlDqs0.setText('N/A')

            pinStr = self.comboBox_dqs1.currentText()
            if pinStr != 'None':
                if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
                elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
                self.lineEdit_padCtrlDqs1.setText(str(hex(padCtrl)))
            else:
                self.lineEdit_padCtrlDqs1.setText('N/A')

            pinStr = self.comboBox_rstb.currentText()
            if pinStr != 'None':
                if self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_COMM):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValC']
                elif self._isGpioGroupMatched(pinStr, kRT1xxxGpioGroupList_AD):
                    padCtrl = self.mixspiPadCtrlDict['rt11yyValA']
                self.lineEdit_padCtrlRstb.setText(str(hex(padCtrl)))
            else:
                self.lineEdit_padCtrlRstb.setText('N/A')

    def callbackPadCtrl( self ):
        if self.mcuDevice in uidef.kMcuDevice_iMXRTxxx:
            self.padCtrlRTxxxFrame.show()
        elif self.mcuDevice in uidef.kMcuDevice_iMXRT10yy:
            self.padCtrlRT10yyFrame.show()
        elif self.mcuDevice in uidef.kMcuDevice_iMXRT11yy:
            self.padCtrlRT11yyFrame.show()
        else:
            pass

    def _getUserPadCtrlSettings( self ):
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlDataL4b.text())
        if status:
            self.mixspiPadCtrlDict['dataL4b_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlSsb.text())
        if status:
            self.mixspiPadCtrlDict['ssb_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlSclk.text())
        if status:
            self.mixspiPadCtrlDict['sclk_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlDataH4b.text())
        if status:
            self.mixspiPadCtrlDict['dataH4b_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlDataT8b.text())
        if status:
            self.mixspiPadCtrlDict['dataT8b_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlSclkn.text())
        if status:
            self.mixspiPadCtrlDict['sclkn_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlDqs0.text())
        if status:
            self.mixspiPadCtrlDict['dqs0_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlDqs1.text())
        if status:
            self.mixspiPadCtrlDict['dqs1_u32'] = padCtrl
        else:
            return False
        status, padCtrl = self._getVal32FromHexText(self.lineEdit_padCtrlRstb.text())
        if status:
            self.mixspiPadCtrlDict['rstb_u32'] = padCtrl
        else:
            return False
        return True

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

        if not self._getUserPadCtrlSettings():
            return
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Conn, self.mixspiConnCfgDict)
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_PadCtrl, self.mixspiPadCtrlDict)
        self.close()

    def callbackCancel( self, event ):
        self.close()


