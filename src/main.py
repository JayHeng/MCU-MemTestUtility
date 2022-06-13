#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from ui import uidef
from ui import uilang
from ui import uivar
from ui import ui_cfg_flexspi_conn
from ui import ui_cfg_flexspi_pintest
from run import runcore

kRetryPingTimes = 5

class memTesterMain(runcore.memTesterRun):

    def __init__(self, parent=None):
        super(memTesterMain, self).__init__(parent)
        self._register_callbacks()
        self.isDeviceConnected = False
        self._setupMcuTargets()

    def _register_callbacks(self):
        self.menuHelpAction_homePage.triggered.connect(self.callbackShowHomePage)
        self.menuHelpAction_aboutAuthor.triggered.connect(self.callbackShowAboutAuthor)
        self.menuHelpAction_revisionHistory.triggered.connect(self.callbackShowRevisionHistory)
        self.comboBox_mcuDevice.currentIndexChanged.connect(self.callbackSetMcuDevice)
        self.pushButton_flexspiConnectionConfiguration.clicked.connect(self.callbackFlexspiConnectionConfiguration)
        self.pushButton_connect.clicked.connect(self.callbackConnectToDevice)
        self.comboBox_memType.currentIndexChanged.connect(self.callbackSetMemType)
        self.pushButton_pinUnittest.clicked.connect(self.callbackFlexspiPinUnittest)
        self.pushButton_clearScreen.clicked.connect(self.clearContentOfScreens)

    def _setupMcuTargets( self ):
        self.setTargetSetupValue()
        self.initUi()
        self.initRun()
        self.updateCpuSpeedInfo()
        self.updateUartPadInfo()

    def callbackSetMcuDevice( self ):
        self._setupMcuTargets()

    def callbackFlexspiConnectionConfiguration( self ):
        flexspiConnCfgFrame.setNecessaryInfo(self.mcuDevice, self.textEdit_flexspiConnection)
        flexspiConnCfgFrame.show()

    def _retryToPingBootloader( self ):
        pingStatus = False
        pingCnt = kRetryPingTimes
        while (not pingStatus) and pingCnt > 0:
            pingStatus = self.pingRom()
            if pingStatus:
                break
            pingCnt = pingCnt - 1
            time.sleep(2)
        return pingStatus

    def callbackConnectToDevice( self ):
        if not self.isDeviceConnected:
            self.showContentOnSecPacketWin(u"【Action】: Click connect button to load boot firmware.")
            self.updatePortSetupValue()
            self.connectToDevice()
            if self._retryToPingBootloader():
                if self.jumpToFirmware():
                    self.showContentOnSecPacketWin(u"【  Info 】: boot firmware is loaded.")
                    self.openUartPort()
                    self.isDeviceConnected = True
                else:
                    pass
            else:
                if (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT10yy) or \
                   (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT11yy):
                    self.showInfoMessage('Connection Error', uilang.kMsgLanguageContentDict['connectError_doubleCheckBmod'][0])
                elif (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRTxxx):
                    self.showInfoMessage('Connection Error', uilang.kMsgLanguageContentDict['connectError_doubleCheckSerialMasterBoot'][0])
                else:
                    pass
        else:
            self.showContentOnSecPacketWin(u"【Action】: Click reset button to reboot system.")
            self.isDeviceConnected = False
            self.closeUartPort()

    def callbackSetMemType( self ):
        self.setMemType()

    def callbackFlexspiPinUnittest( self ):
        flexspiPinUnittestFrame.show()

    def _deinitToolToExit( self ):
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Tool, self.toolCommDict)
        uivar.deinitVar()

    def closeEvent(self, event):
        self._deinitToolToExit()
        event.accept()

    def callbackShowHomePage(self):
        self.showAboutMessage(uilang.kMsgLanguageContentDict['homePage_title'][0], uilang.kMsgLanguageContentDict['homePage_info'][0] )

    def callbackShowAboutAuthor(self):
        msgText = ((uilang.kMsgLanguageContentDict['aboutAuthor_author'][0]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email1'][0]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email2'][0]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_blog'][0]))
        self.showAboutMessage(uilang.kMsgLanguageContentDict['aboutAuthor_title'][0], msgText )

    def callbackShowRevisionHistory(self):
        self.showAboutMessage(uilang.kMsgLanguageContentDict['revisionHistory_title'][0], uilang.kMsgLanguageContentDict['revisionHistory_v1_0_0'][0] )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = memTesterMain(None)
    mainWin.setWindowTitle(u"MCU Mem Test Utility v1.0")
    mainWin.show()
    flexspiConnCfgFrame = ui_cfg_flexspi_conn.memTesterUiCfgFlexspiConn(None)
    flexspiConnCfgFrame.setWindowTitle(u"FlexSPI Connection Configuration")
    flexspiPinUnittestFrame = ui_cfg_flexspi_pintest.memTesterUiCfgFlexspiPin(None)
    flexspiPinUnittestFrame.setWindowTitle(u"FlexSPI Pin Unit Test")

    sys.exit(app.exec_())

