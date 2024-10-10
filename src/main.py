#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from ui import uidef
from ui import uilang
from ui import uivar
from ui import ui_cfg_conn
from ui import ui_cfg_pin_test
from ui import ui_cfg_rw_test
from ui import ui_cfg_perf_test
from ui import ui_cfg_stress_test
from run import runcore

kRetryPingTimes = 5
s_goAction = None

class memTesterMain(runcore.memTesterRun):

    def __init__(self, parent=None):
        super(memTesterMain, self).__init__(parent)
        self._register_callbacks()
        self.isDeviceConnected = False
        self._setupMcuTargets()
        self.isLoadFirmwareEnabled = True
        self.initToolMenu()

    def _register_callbacks(self):
        self.menuHelpAction_homePage.triggered.connect(self.callbackShowHomePage)
        self.menuHelpAction_aboutAuthor.triggered.connect(self.callbackShowAboutAuthor)
        self.menuHelpAction_revisionHistory.triggered.connect(self.callbackShowRevisionHistory)
        self.menuLoadFwAction_No.triggered.connect(self.callbackSetLoadFirmwareOpt)
        self.menuLoadFwAction_Yes.triggered.connect(self.callbackSetLoadFirmwareOpt)
        self.comboBox_mcuDevice.currentIndexChanged.connect(self.callbackSetMcuDevice)
        self.pushButton_mixspiConnectionConfiguration.clicked.connect(self.callbackMixspiConnectionConfiguration)
        self.pushButton_connect.clicked.connect(self.callbackConnectToDevice)
        self.comboBox_memVendor.currentIndexChanged.connect(self.callbackSetMemVendor)
        self.comboBox_memType.currentIndexChanged.connect(self.callbackSetMemType)
        self.pushButton_pinTest.clicked.connect(self.callbackPinTest)
        self.pushButton_configSystem.clicked.connect(self.callbackConfigSystem)
        self.pushButton_memRegs.clicked.connect(self.callbackMemRegs)
        self.pushButton_rwTest.clicked.connect(self.callbackRwTest)
        self.pushButton_perfTest.clicked.connect(self.callbackPerfTest)
        self.pushButton_stressTest.clicked.connect(self.callbackStressTest)
        self.pushButton_Go.clicked.connect(self.callbackGo)
        self.pushButton_clearScreen.clicked.connect(self.clearContentOfScreens)

    def _setupMcuTargets( self ):
        self.setTargetSetupValue()
        self.initFuncUi()
        self.initFuncRun()
        self.updateCpuSpeedInfo()
        self.updateUartPadInfo()

    def callbackSetMcuDevice( self ):
        self._setupMcuTargets()

    def callbackMixspiConnectionConfiguration( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <MixSPI Connnect Configuration> button.")
        mixspiConnCfgFrame.setNecessaryInfo(self.tgt.mixspiConnDict, self.textEdit_mixspiConnection)
        mixspiConnCfgFrame.show()

    def _retryToPingBootloader( self ):
        if not self.isLoadFirmwareEnabled:
            return True
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
            self.showContentOnSecPacketWin(u"【Action】: Click <Connect> button to load boot firmware.")
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
            self.showContentOnSecPacketWin(u"【Action】: Click <Reset> button to reboot system.")
            self.isDeviceConnected = False
            self.closeUartPort()

    def callbackSetMemVendor( self ):
        self.setMemVendor()

    def callbackSetMemType( self ):
        self.setMemType()

    def callbackPinTest( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <Pin Test> button.")
        global s_goAction
        s_goAction = uidef.kGoAction_PinTest
        pinTestFrame.show()
        self.resetAllActionButtonColor()
        self.setActionButtonColor(s_goAction)

    def callbackConfigSystem( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <Config System> button.")
        global s_goAction
        s_goAction = uidef.kGoAction_ConfigSystem
        self.resetAllActionButtonColor()
        self.setActionButtonColor(s_goAction)

    def callbackMemRegs( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <Mem REGs> button.")
        global s_goAction
        s_goAction = uidef.kGoAction_MemRegs
        self.resetAllActionButtonColor()
        self.setActionButtonColor(s_goAction)

    def callbackRwTest( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <R/W Test> button.")
        global s_goAction
        s_goAction = uidef.kGoAction_RwTest
        rwTestFrame.show()
        self.resetAllActionButtonColor()
        self.setActionButtonColor(s_goAction)

    def callbackPerfTest( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <Perf Test> button.")
        global s_goAction
        s_goAction = uidef.kGoAction_PerfTest
        perfTestFrame.show()
        self.resetAllActionButtonColor()
        self.setActionButtonColor(s_goAction)

    def callbackStressTest( self ):
        self.showContentOnSecPacketWin(u"【Action】: Click <Stress Test> button.")
        global s_goAction
        s_goAction = uidef.kGoAction_StressTest
        stressTestFrame.show()
        self.resetAllActionButtonColor()
        self.setActionButtonColor(s_goAction)

    def callbackGo( self ):
        global s_goAction
        if s_goAction == None:
            return
        if self.isGoActionWorking():
            self.showContentOnSecPacketWin(u"【Action】: Click <Stop> button.")
            self.sendTestStopPacket()
            self.resetAllActionButtonColor()
            s_goAction = None
            self.recoverGoActionButton()
        else:
            self.showContentOnSecPacketWin(u"【Action】: Click <Go> button.")
        if s_goAction == uidef.kGoAction_PinTest:
            self.sendPinTestPacket()
        elif s_goAction == uidef.kGoAction_ConfigSystem:
            if self.updateTargetSetupValue():
                self.sendConfigSystemPacket()
            else:
                return
        elif s_goAction == uidef.kGoAction_MemRegs:
            self.sendMemRegsPacket()
        elif s_goAction == uidef.kGoAction_RwTest:
            self.sendRwTestPacket()
        elif s_goAction == uidef.kGoAction_PerfTest:
            self.sendPerfTestPacket()
        elif s_goAction == uidef.kGoAction_StressTest:
            self.sendStressTestPacket()
        else:
            return
        self.updateGoActionButton()

    def _deinitToolToExit( self ):
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Tool, self.toolCommDict)
        uivar.deinitVar()

    def closeEvent(self, event):
        self._deinitToolToExit()
        event.accept()

    def callbackSetLoadFirmwareOpt( self ):
        self.setLoadFwOpt()

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
    mixspiConnCfgFrame = ui_cfg_conn.memTesterUiConn(None)
    mixspiConnCfgFrame.setWindowTitle(u"MixSPI Connection Configuration")
    pinTestFrame = ui_cfg_pin_test.memTesterUiPinTest(None)
    pinTestFrame.setWindowTitle(u"Pin Test")
    rwTestFrame = ui_cfg_rw_test.memTesterUiRwTest(None)
    rwTestFrame.setWindowTitle(u"R/W Test")
    perfTestFrame = ui_cfg_perf_test.memTesterUiPerfTest(None)
    perfTestFrame.setWindowTitle(u"Perf Test")
    stressTestFrame = ui_cfg_stress_test.memTesterUiStressTest(None)
    stressTestFrame.setWindowTitle(u"Stress Test")

    sys.exit(app.exec_())

