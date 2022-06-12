#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys
import os
import serial.tools.list_ports
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from . import uidef
from . import uilang
from . import uivar
from . import ui_def_flexspi_conn_rt1170
sys.path.append(os.path.abspath(".."))
from win import memTesterWin

s_serialPort = serial.Serial()
s_recvInterval = 1

class uartRecvWorker(QThread):
    sinOut = pyqtSignal()

    def __init__(self, parent=None):
        super(uartRecvWorker, self).__init__(parent)
        self.working = True

    def __del__(self):
        self.working = False

    def run(self):
        while self.working == True:
            self.sinOut.emit()
            self.sleep(s_recvInterval)

class memTesterUi(QMainWindow, memTesterWin.Ui_memTesterWin):

    def __init__(self, parent=None):
        super(memTesterUi, self).__init__(parent)
        self.setupUi(self)
        self.uartRecvThread = uartRecvWorker()
        self.uartRecvThread.sinOut.connect(self.receiveUartData)

        self.exeBinRoot = os.getcwd()
        self.exeTopRoot = os.path.dirname(self.exeBinRoot)
        exeMainFile = os.path.join(self.exeTopRoot, 'src', 'main.py')
        if not os.path.isfile(exeMainFile):
            self.exeTopRoot = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        uivar.setRuntimeSettings(None, self.exeTopRoot)
        uivar.initVar(os.path.join(self.exeTopRoot, 'bin', 'mtu_settings.json'))
        toolCommDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Tool)
        self.toolCommDict = toolCommDict.copy()
        self.flexspiConnCfgDict = None

        self.mcuDevice = None
        self._initTargetSetupValue()
        self.setTargetSetupValue()
        self.initUi()
        self._initFlexspiConn()
        self.memType = None
        self._initMemType()

    def initUi( self ):
        self.uartComPort = None
        self.uartBaudrate = None
        self.setPortSetupValue()

    def showAboutMessage( self, myTitle, myContent):
        QMessageBox.about(self, myTitle, myContent )

    def showInfoMessage( self, myTitle, myContent):
        QMessageBox.information(self, myTitle, myContent )

    def updateCpuSpeedInfo( self ):
        self.lineEdit_cpuSpeed.setText(str(self.tgt.maxCpuFreqInMHz))

    def adjustPortSetupValue( self ):
        # Auto detect available ports
        comports = list(serial.tools.list_ports.comports())
        ports = [None] * len(comports)
        for i in range(len(comports)):
            comport = list(comports[i])
            ports[i] = comport[0]
        lastPort = self.comboBox_comPort.currentText()
        lastBaud = self.comboBox_baudrate.currentText()
        self.comboBox_comPort.clear()
        self.comboBox_comPort.addItems(ports)
        if lastPort in ports:
            self.comboBox_comPort.setCurrentIndex(self.comboBox_comPort.findText(lastPort))
        else:
            self.comboBox_comPort.setCurrentIndex(0)
        baudItems = ['115200']
        self.comboBox_baudrate.clear()
        self.comboBox_baudrate.addItems(baudItems)
        if lastBaud in baudItems:
            self.comboBox_baudrate.setCurrentIndex(self.comboBox_baudrate.findText(lastBaud))
        else:
            self.comboBox_baudrate.setCurrentIndex(0)

    def _initTargetSetupValue( self ):
        self.comboBox_mcuDevice.clear()
        self.comboBox_mcuDevice.addItems(uidef.kMcuDevice_v1_0)
        self.comboBox_mcuDevice.setCurrentIndex(self.toolCommDict['mcuDevice'])

    def setTargetSetupValue( self ):
        self.mcuDevice = self.comboBox_mcuDevice.currentText()
        self.toolCommDict['mcuDevice'] = self.comboBox_mcuDevice.currentIndex()

    def _initFlexspiConn( self ):
        flexspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.flexspiConnCfgDict = flexspiConnCfgDict.copy()
        instance = self.flexspiConnCfgDict['instance'] - 1
        self.textEdit_flexspiConnection.clear()
        if self.mcuDevice == uidef.kMcuDevice_iMXRT117x:
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataL4b[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataL4b[instance][key] == self.flexspiConnCfgDict['dataL4b']:
                    self.textEdit_flexspiConnection.append(key)
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataH4b[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_DataH4b[instance][key] == self.flexspiConnCfgDict['dataH4b']:
                    if key != 'None':
                        self.textEdit_flexspiConnection.append(key)
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_ssb[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_ssb[instance][key] == self.flexspiConnCfgDict['ssb']:
                    self.textEdit_flexspiConnection.append(key)
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclk[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclk[instance][key] == self.flexspiConnCfgDict['sclk']:
                    self.textEdit_flexspiConnection.append(key)
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_dqs[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_dqs[instance][key] == self.flexspiConnCfgDict['dqs']:
                    self.textEdit_flexspiConnection.append(key)
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclkn[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_sclkn[instance][key] == self.flexspiConnCfgDict['sclkn']:
                    if key != 'None':
                        self.textEdit_flexspiConnection.append(key)
                    break
            for key in ui_def_flexspi_conn_rt1170.kFlexspiConnSel_rstb[instance].keys():
                if ui_def_flexspi_conn_rt1170.kFlexspiConnSel_rstb[instance][key] == self.flexspiConnCfgDict['rstb']:
                    if key != 'None':
                        self.textEdit_flexspiConnection.append(key)
                    break

    def updateUartPadInfo( self ):
        self.lineEdit_uartPad.setText(self.tgt.uartPeripheralPinStr)

    def updatePortSetupValue( self ):
        self.uartComPort = self.comboBox_comPort.currentText()
        self.uartBaudrate = self.comboBox_baudrate.currentText()

    def setPortSetupValue( self ):
        self.adjustPortSetupValue()
        self.updatePortSetupValue()

    def openUartPort ( self ):
        s_serialPort.port = self.uartComPort
        s_serialPort.baudrate = int(self.uartBaudrate)
        s_serialPort.bytesizes = serial.EIGHTBITS
        s_serialPort.stopbits = serial.STOPBITS_ONE
        s_serialPort.parity = serial.PARITY_NONE
        try:
            s_serialPort.open()
        except:
            QMessageBox.information(self, 'Port Error', 'Com Port cannot opened!')
            return
        s_serialPort.reset_input_buffer()
        s_serialPort.reset_output_buffer()
        self.uartRecvThread.start()
        self.pushButton_connect.setText('Reset')
        self.pushButton_connect.setStyleSheet("background-color: green")

    def closeUartPort ( self ):
        if s_serialPort.isOpen():
            s_serialPort.close()
            self.uartRecvThread.quit()
            self.pushButton_connect.setText('Connect')
            self.pushButton_connect.setStyleSheet("background-color: grey")

    def receiveUartData( self ):
        if s_serialPort.isOpen():
            num = s_serialPort.inWaiting()
            if num != 0:
                data = s_serialPort.read(num)
                self.showContentOnMainDisplayWin(data.decode())

    def _initMemType( self ):
        self.setMemType()

    def setMemType( self ):
        self.memType = self.comboBox_memType.currentText()
        self.comboBox_memChip.clear()
        if self.memType == uidef.kMemType_QuadSPI:
            self.comboBox_memChip.addItems(uidef.kFlexspiNorDevices_QuadSPI)
        elif self.memType == uidef.kMemType_OctalSPI:
            self.comboBox_memChip.addItems(uidef.kFlexspiNorDevices_OctalSPI)
        elif self.memType == uidef.kMemType_HyperFlash:
            self.comboBox_memChip.addItems(uidef.kFlexspiNorDevices_HyperFlash)
        elif self.memType == uidef.kMemType_PSRAM:
            self.comboBox_memChip.addItems(uidef.kFlexspiRamDevices_PSRAM)
        elif self.memType == uidef.kMemType_HyperRAM:
            self.comboBox_memChip.addItems(uidef.kFlexspiRamDevices_HyperRAM)
        else:
            pass

    def showContentOnMainDisplayWin( self, contentStr ):
        self.textEdit_displayWin.append(contentStr)

    def showContentOnSecPacketWin( self, contentStr ):
        self.textEdit_packetWin.append(contentStr)

    def clearContentOfScreens( self ):
        self.textEdit_displayWin.clear()
        self.textEdit_packetWin.clear()
