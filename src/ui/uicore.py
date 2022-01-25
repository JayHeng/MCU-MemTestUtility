#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys
import os
import threading
import serial.tools.list_ports
from PyQt5.Qt import *
from . import uidef
from . import uilang
sys.path.append(os.path.abspath(".."))
from win import memTesterWin

s_serialPort = serial.Serial()
s_recvInterval = 1

class memTesterUi(QMainWindow, memTesterWin.Ui_memTesterWin):

    def __init__(self, parent=None):
        super(memTesterUi, self).__init__(parent)
        self.setupUi(self)

        self.exeBinRoot = os.getcwd()
        self.exeTopRoot = os.path.dirname(self.exeBinRoot)
        exeMainFile = os.path.join(self.exeTopRoot, 'src', 'main.py')
        if not os.path.isfile(exeMainFile):
            self.exeTopRoot = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        self.mcuDevice = 'i.MXRT117x'
        self.uartComPort = None
        self.uartBaudrate = None
        self.setPortSetupValue()

    def showAboutMessage( self, myTitle, myContent):
        QMessageBox.about(self, myTitle, myContent )

    def showInfoMessage( self, myTitle, myContent):
        QMessageBox.information(self, myTitle, myContent )

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
        threading.Timer(s_recvInterval, self.receiveUartData).start()

    def receiveUartData( self ):
        if s_serialPort.isOpen():
            num = s_serialPort.inWaiting()
            if num != 0:
                data = s_serialPort.read(num)
                self.textEdit_displayWin.append(data.decode())
            threading.Timer(s_recvInterval, self.receiveUartData).start()
