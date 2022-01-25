#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from ui import uidef
from ui import uilang
from run import runcore

kRetryPingTimes = 5

class memTesterMain(runcore.memTesterRun):

    def __init__(self, parent=None):
        super(memTesterMain, self).__init__(parent)
        self._register_callbacks()

    def _register_callbacks(self):
        self.menuHelpAction_homePage.triggered.connect(self.callbackShowHomePage)
        self.menuHelpAction_aboutAuthor.triggered.connect(self.callbackShowAboutAuthor)
        self.menuHelpAction_revisionHistory.triggered.connect(self.callbackShowRevisionHistory)
        self.pushButton_connect.clicked.connect(self.callbackConnectToDevice)

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

    def callbackConnectToDevice( self, event ):
        self.updatePortSetupValue()
        self.connectToDevice()
        if self._retryToPingBootloader():
            #self.jumpToFirmware()
            pass
        else:
            if (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT10yy) or \
               (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT11yy):
                QMessageBox.information(self, 'Connection Error', uilang.kMsgLanguageContentDict['connectError_doubleCheckBmod'][0])
            elif (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRTxxx):
                QMessageBox.information(self, 'Connection Error', uilang.kMsgLanguageContentDict['connectError_doubleCheckIsp'][0])
            else:
                pass

    def callbackShowHomePage(self):
        QMessageBox.about(self, uilang.kMsgLanguageContentDict['homePage_title'][0], uilang.kMsgLanguageContentDict['homePage_info'][0] )

    def callbackShowAboutAuthor(self):
        msgText = ((uilang.kMsgLanguageContentDict['aboutAuthor_author'][0]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email1'][0]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_email2'][0]) +
                   (uilang.kMsgLanguageContentDict['aboutAuthor_blog'][0]))
        QMessageBox.about(self, uilang.kMsgLanguageContentDict['aboutAuthor_title'][0], msgText )

    def callbackShowRevisionHistory(self):
        QMessageBox.about(self, uilang.kMsgLanguageContentDict['revisionHistory_title'][0], uilang.kMsgLanguageContentDict['revisionHistory_v1_0_0'][0] )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = memTesterMain(None)
    mainWin.setWindowTitle(u"NXP MCU Mem Tester v1.0")
    mainWin.show()

    sys.exit(app.exec_())

