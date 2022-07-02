#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json
from . import uidef
from . import uivar

kPacketTag = "FTAG"

kCommandTag_PinUnittest    = 0x01
kCommandTag_ConfigSystem   = 0x02
kCommandTag_GetMemInfo     = 0x03
kCommandTag_RunPerfTest    = 0x04
kCommandTag_RunStressTest  = 0x05

class flexspiConnectionStruct(object):

    def __init__( self, parent=None):
        #super(flexspiConnectionStruct, self).__init__(parent)
        self.instance = None
        self.dataLow4bit = None
        self.dataHigh4bit = None
        self.ss_b = None
        self.sclk = None
        self.dqs = None
        self.sclk_n = None
        self.rst_b = None

    def set_members( self, flexspiConnCfgDict ):
        self.instance = flexspiConnCfgDict['instance']
        self.dataLow4bit = flexspiConnCfgDict['dataL4b']
        self.dataHigh4bit = flexspiConnCfgDict['dataH4b']
        self.ss_b = flexspiConnCfgDict['ssb']
        self.sclk = flexspiConnCfgDict['sclk']
        self.dqs = flexspiConnCfgDict['dqs']
        self.sclk_n = flexspiConnCfgDict['sclkn']
        self.rst_b = flexspiConnCfgDict['rstb']

    def out_bytes( self ):
        mybytes = bytes([self.instance,
                         self.dataLow4bit,
                         self.dataHigh4bit, 
                         self.ss_b,
                         self.sclk,
                         self.dqs,
                         self.sclk_n,
                         self.rst_b,
                        ])
        return mybytes

class flexspiUnittestEnStruct(object):

    def __init__( self, parent=None):
        #super(flexspiUnittestEnStruct, self).__init__(parent)
        self.pulseInMs = None
        self.option = None

    def set_members( self, flexspiUnittestCfgDict ):
        self.pulseInMs = flexspiUnittestCfgDict['wavePulse']
        self.option = 0x00000000
        if flexspiUnittestCfgDict['dataL4b_dis'] == 0:
            self.option = self.option | (1 << 0)
        if flexspiUnittestCfgDict['dataH4b_dis'] == 0:
            self.option = self.option | (1 << 1)
        if flexspiUnittestCfgDict['ssb_dis'] == 0:
            self.option = self.option | (1 << 2)
        if flexspiUnittestCfgDict['sclk_dis'] == 0:
            self.option = self.option | (1 << 3)
        if flexspiUnittestCfgDict['dqs_dis'] == 0:
            self.option = self.option | (1 << 4)
        if flexspiUnittestCfgDict['sclkn_dis'] == 0:
            self.option = self.option | (1 << 5)
        if flexspiUnittestCfgDict['rstb_dis'] == 0:
            self.option = self.option | (1 << 6)

    def out_bytes( self ):
        mybytes = bytes([self.pulseInMs & 0xFF,
                         (self.pulseInMs & 0xFF00) >> 8,
                         (self.pulseInMs & 0xFF0000) >> 16, 
                         (self.pulseInMs & 0xFF000000) >> 24,
                         self.option & 0xFF,
                         (self.option & 0xFF00) >> 8,
                         (self.option & 0xFF0000) >> 16, 
                         (self.option & 0xFF000000) >> 24,
                        ])
        return mybytes

class pinTestPacket(object):

    def __init__( self, parent=None):
        #super(pinTestPacket, self).__init__(parent)
        self.memConnection = None
        self.unittestEn = None
        self.reserved0 = [0x0, 0x0, 0x0]
        self.crcCheckSum = None
        self.reserved1 = [0x0, 0x0]

    def set_members( self ):
        self.memConnection = flexspiConnectionStruct()
        flexspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.memConnection.set_members(flexspiConnCfgDict)
        self.unittestEn = flexspiUnittestEnStruct()
        flexspiUnittestCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiUnittest)
        self.unittestEn.set_members(flexspiUnittestCfgDict)
        self.crcCheckSum = 0x0000

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_PinUnittest])
        mybytes = bytes([self.reserved0[0],
                         self.reserved0[1],
                         self.reserved0[2], 
                         self.crcCheckSum & 0xFF,
                         (self.crcCheckSum & 0xFF00) >> 8,
                         self.reserved1[0],
                         self.reserved1[1]
                        ])
        return startbytes + self.memConnection.out_bytes() + self.unittestEn.out_bytes() + mybytes

