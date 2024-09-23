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

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from . import uidef
from . import uilang
from . import uivar
from . import uipacket
from . import ui_def_flexspi_conn_rt500
from . import ui_def_flexspi_conn_rt600
from . import ui_def_flexspi_conn_rt1060
from . import ui_def_flexspi_conn_rt1170
from . import ui_def_flexspi_conn_rt1180
sys.path.append(os.path.abspath(".."))
from win import memTesterWin

s_serialPort = serial.Serial()
s_recvInterval = 1
s_recvPinWave = [0] * 100
s_isRecvAsciiMode = True
s_recvUartMagic = ""

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

class pinWaveformFigure(FigureCanvas):

    def __init__(self,width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(pinWaveformFigure,self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlabel('Time(ms)')
        self.axes.set_ylabel('Volt(3.3V)')
        self.axes.set_ylim(0,1.1)
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=1000, blit=True, save_count=50)

    def plotwave(self):
        self.line, = self.axes.plot(s_recvPinWave)

    def animate(self, i):
        #global s_recvPinWave
        #for i in range(len(s_recvPinWave)):
        #    s_recvPinWave[i] = (int(i/10) % 2)
        self.line.set_ydata(s_recvPinWave)
        return self.line,

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
        self.initFuncUi()
        self._initFlexspiConn()
        self.memType = None
        self._initMemType()

        self.pinWaveFig = pinWaveformFigure(width=2, height=4, dpi=50)
        self.pinWaveFig.plotwave()
        self.pinWaveGridlayout = QGridLayout(self.groupBox_pinWaveform)
        self.pinWaveGridlayout.addWidget(self.pinWaveFig,0,0)

    def initToolMenu( self ):
        loadFwActionGroup = QActionGroup(self)
        loadFwActionGroup.addAction(self.menuLoadFwAction_No)
        loadFwActionGroup.addAction(self.menuLoadFwAction_Yes)
        loadFwActionGroup.setExclusive(True)

    def setLoadFwOpt( self ):
        self.isLoadFirmwareEnabled = self.menuLoadFwAction_Yes.isChecked()

    def initFuncUi( self ):
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
        self.lineEdit_cpuSpeed.setText(str(self.toolCommDict['cpuSpeedMHz']))
        if self.toolCommDict['enableL1Cache']:
            self.checkBox_enableL1Cache.setChecked(True)
        else:
            self.checkBox_enableL1Cache.setChecked(False)
        if self.toolCommDict['enablePrefetch']:
            self.checkBox_enablePrefetch.setChecked(True)
        else:
            self.checkBox_enablePrefetch.setChecked(False)

    def setTargetSetupValue( self ):
        self.mcuDevice = self.comboBox_mcuDevice.currentText()
        self.toolCommDict['mcuDevice'] = self.comboBox_mcuDevice.currentIndex()

    def _initFlexspiConn( self ):
        flexspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.flexspiConnCfgDict = flexspiConnCfgDict.copy()
        instance = self.flexspiConnCfgDict['instance'] - 1
        self.textEdit_flexspiConnection.clear()
        flexspiConnSelDict = None
        if self.mcuDevice == uidef.kMcuDevice_iMXRT500:
            flexspiConnSelDict = ui_def_flexspi_conn_rt500.kFlexspiConnSelDict.copy()
        elif self.mcuDevice == uidef.kMcuDevice_iMXRT600:
            flexspiConnSelDict = ui_def_flexspi_conn_rt600.kFlexspiConnSelDict.copy()
        elif self.mcuDevice == uidef.kMcuDevice_iMXRT106x:
            flexspiConnSelDict = ui_def_flexspi_conn_rt1060.kFlexspiConnSelDict.copy()
        elif self.mcuDevice == uidef.kMcuDevice_iMXRT117x:
            flexspiConnSelDict = ui_def_flexspi_conn_rt1170.kFlexspiConnSelDict.copy()
        elif self.mcuDevice == uidef.kMcuDevice_iMXRT118x:
            flexspiConnSelDict = ui_def_flexspi_conn_rt1180.kFlexspiConnSelDict.copy()
        else:
            pass

        for key in flexspiConnSelDict['dataL4b'][instance].keys():
            if flexspiConnSelDict['dataL4b'][instance][key] == self.flexspiConnCfgDict['dataL4b']:
                self.textEdit_flexspiConnection.append(key)
                break
        for key in flexspiConnSelDict['dataH4b'][instance].keys():
            if flexspiConnSelDict['dataH4b'][instance][key] == self.flexspiConnCfgDict['dataH4b']:
                if key != 'None':
                    self.textEdit_flexspiConnection.append(key)
                break
        for key in flexspiConnSelDict['ssb'][instance].keys():
            if flexspiConnSelDict['ssb'][instance][key] == self.flexspiConnCfgDict['ssb']:
                self.textEdit_flexspiConnection.append(key)
                break
        for key in flexspiConnSelDict['sclk'][instance].keys():
            if flexspiConnSelDict['sclk'][instance][key] == self.flexspiConnCfgDict['sclk']:
                self.textEdit_flexspiConnection.append(key)
                break
        for key in flexspiConnSelDict['dqs'][instance].keys():
            if flexspiConnSelDict['dqs'][instance][key] == self.flexspiConnCfgDict['dqs']:
                if key != 'None':
                    self.textEdit_flexspiConnection.append(key)
                break
        for key in flexspiConnSelDict['sclkn'][instance].keys():
            if flexspiConnSelDict['sclkn'][instance][key] == self.flexspiConnCfgDict['sclkn']:
                if key != 'None':
                    self.textEdit_flexspiConnection.append(key)
                break
        for key in flexspiConnSelDict['rstb'][instance].keys():
            if flexspiConnSelDict['rstb'][instance][key] == self.flexspiConnCfgDict['rstb']:
                if key != 'None':
                    self.textEdit_flexspiConnection.append(key)
                break

    def updateTargetSetupValue( self ):
        try:
            cpuSpeed = int(self.lineEdit_cpuSpeed.text())
            if cpuSpeed > self.tgt.maxCpuFreqInMHz:
                self.showInfoMessage('Range Error', 'cpu speed should not be more than max freq ' + str(self.tgt.maxCpuFreqInMHz) + ' MHz!')
                return False
            self.toolCommDict['cpuSpeedMHz'] = cpuSpeed
        except:
            self.showInfoMessage('Input Error', 'cpu speed should be an integer!')
            return False
        if self.checkBox_enableL1Cache.isChecked():
            self.toolCommDict['enableL1Cache'] = 1
        else:
            self.toolCommDict['enableL1Cache'] = 0
        if self.checkBox_enablePrefetch.isChecked():
            self.toolCommDict['enablePrefetch'] = 1
        else:
            self.toolCommDict['enablePrefetch'] = 0
        uivar.setAdvancedSettings(uidef.kAdvancedSettings_Tool, self.toolCommDict)
        return True

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
        s_serialPort.set_buffer_size(rx_size=1024 * 16)
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

    def _findUartPrintSwitchMagic( self, uartData, magic ):
        global s_recvUartMagic
        status = None
        string = ""
        try:
            string += data.decode('utf-8')
            if len(string) > len(magic):
                status = False
            elif string in magic:
                status = True
                s_recvUartMagic += string
            else:
                status = False
        except:
            pass
        return status, string

    def receiveUartData( self ):
        global s_isRecvAsciiMode
        global s_recvUartMagic
        if s_serialPort.isOpen():
            num = s_serialPort.inWaiting()
            if num != 0:
                data = s_serialPort.read(num)
                if not s_isRecvAsciiMode:
                    status, string = self._findUartPrintSwitchMagic(data, "Switch_To_ASCII_Mode")
                    if status:
                        if s_recvUartMagic == "Switch_To_ASCII_Mode":
                            s_isRecvAsciiMode = True
                            s_recvUartMagic = ""
                            #self.showContentOnMainDisplayWin("  __it is ascii mode")
                    else:
                        global s_recvPinWave
                        # We just use first 20 conv result each time
                        if num >= 20:
                            # To show square, every conv reslur will repeat 5 times in s_recvPinWave
                            for i in range(len(s_recvPinWave)):
                                s_recvPinWave[i] = data[int(i/5)]
                        #self.showContentOnMainDisplayWin("  __it is in hex mode output")
                    return
                else:
                    status, string = self._findUartPrintSwitchMagic(data, "Switch_To_HEX8B_Mode")
                    if status:
                        if s_recvUartMagic == "Switch_To_HEX8B_Mode":
                            s_isRecvAsciiMode = False
                            s_recvUartMagic = ""
                            #self.showContentOnMainDisplayWin("  __it is hex mode")
                    else:
                         self.showContentOnMainDisplayWin(string)

    def sendUartData( self , byteList ):
        if s_serialPort.isOpen():
            #num = s_serialPort.out_waiting()
            #while num != 0:
            #    num = s_serialPort.out_waiting()
            s_serialPort.write(byteList)
            packetStr = ''
            for i in range(len(byteList)):
                packetStr = packetStr + hex(byteList[i])
                if i != len(byteList) - 1:
                    packetStr = packetStr + ', '
            self.showContentOnSecPacketWin(u"Cmd Packet ->: " + packetStr)

    def sendPinTestPacket( self ):
        mypacket = uipacket.pinTestPacket()
        mypacket.set_members()
        self.sendUartData(mypacket.out_bytes())

    def sendConfigSystemPacket( self ):
        mypacket = uipacket.configSystemPacket()
        mypacket.set_members()
        self.sendUartData(mypacket.out_bytes())

    def sendRwTestPacket( self ):
        mypacket = uipacket.rwTestPacket()
        mypacket.set_members()
        self.sendUartData(mypacket.out_bytes())

    def sendTestStopPacket( self ):
        mypacket = uipacket.testStopPacket()
        mypacket.set_members()
        self.sendUartData(mypacket.out_bytes())

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

    def resetAllActionButtonColor( self ):
        self.pushButton_pinUnittest.setStyleSheet("background-color: " + uidef.kButtonColor_Disable)
        self.pushButton_configSystem.setStyleSheet("background-color: " + uidef.kButtonColor_Disable)
        self.pushButton_memInfo.setStyleSheet("background-color: " + uidef.kButtonColor_Disable)
        self.pushButton_rwTest.setStyleSheet("background-color: " + uidef.kButtonColor_Disable)
        self.pushButton_perfTest.setStyleSheet("background-color: " + uidef.kButtonColor_Disable)
        self.pushButton_stressTest.setStyleSheet("background-color: " + uidef.kButtonColor_Disable)

    def setActionButtonColor( self, goAction ):
        if goAction == uidef.kGoAction_PinUnittest:
            self.pushButton_pinUnittest.setStyleSheet("background-color: " + uidef.kButtonColor_Enable)
        elif goAction == uidef.kGoAction_ConfigSystem:
            self.pushButton_configSystem.setStyleSheet("background-color: " + uidef.kButtonColor_Enable)
        elif goAction == uidef.kGoAction_MemInfo:
            self.pushButton_memInfo.setStyleSheet("background-color: " + uidef.kButtonColor_Enable)
        elif goAction == uidef.kGoAction_RwTest:
            self.pushButton_rwTest.setStyleSheet("background-color: " + uidef.kButtonColor_Enable)
        elif goAction == uidef.kGoAction_PerfTest:
            self.pushButton_perfTest.setStyleSheet("background-color: " + uidef.kButtonColor_Enable)
        elif goAction == uidef.kGoAction_StressTest:
            self.pushButton_stressTest.setStyleSheet("background-color: " + uidef.kButtonColor_Enable)
        else:
            pass

    def isGoActionWorking( self ):
        return (self.pushButton_Go.text() == "Stop")

    def updateGoActionButton( self ):
        self.pushButton_Go.setText("Stop")

    def recoverGoActionButton( self ):
        self.pushButton_Go.setText("Go")
