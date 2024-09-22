#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json
from crc import CrcCalculator, Configuration
from . import uidef
from . import uivar

kPacketTag = "FTAG"

kCommandTag_PinUnittest    = 0x01
kCommandTag_ConfigSystem   = 0x02
kCommandTag_GetMemInfo     = 0x03
kCommandTag_RunRwTest      = 0x04
kCommandTag_RunPerfTest    = 0x05
kCommandTag_RunStressTest  = 0x06

def calculate_crc16( crcDataBytes ):
    #crc_calculator = CrcCalculator(Crc16.CCITT)
    #checksum = crc_calculator.calculate_checksum(crcDataBytes)
    width = 16
    poly = 0x1021
    init_value = 0x00
    final_xor_value = 0x00
    reverse_input = False
    reverse_output = False
    configuration = Configuration(width, poly, init_value, final_xor_value, reverse_input, reverse_output)
    use_table = True
    crc_calculator = CrcCalculator(configuration, use_table)
    checksum = crc_calculator.calculate_checksum(crcDataBytes)
    return checksum

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
                         self.rst_b
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
                         (self.option & 0xFF000000) >> 24
                        ])
        return mybytes

class pinTestPacket(object):

    def __init__( self, parent=None):
        #super(pinTestPacket, self).__init__(parent)
        self.memConnection = None
        self.unittestEn = None
        self.crcCheckSum = None
        self.reserved0 = [0x0, 0x0]

    def set_members( self ):
        self.memConnection = flexspiConnectionStruct()
        flexspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.memConnection.set_members(flexspiConnCfgDict)
        self.unittestEn = flexspiUnittestEnStruct()
        flexspiUnittestCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiPintest)
        self.unittestEn.set_members(flexspiUnittestCfgDict)
        self.crcCheckSum = 0x0000

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_PinUnittest])
        packetBytes = self.memConnection.out_bytes() + self.unittestEn.out_bytes()
        self.crcCheckSum = calculate_crc16(packetBytes)
        crcbytes = bytes([self.crcCheckSum & 0xFF,
                         (self.crcCheckSum & 0xFF00) >> 8,
                         self.reserved0[0],
                         self.reserved0[1]
                        ])
        return startbytes + packetBytes + crcbytes

class memoryPropertyStruct(object):

    def __init__( self, parent=None):
        #super(memoryPropertyStruct, self).__init__(parent)
        self.type = None
        self.chip = None
        self.speedMHz = None
        self.sizeInByte = 0x00000000
        self.ioMode = None
        self.interfaceMode = None
        self.dataRateMode = None
        self.dummyCycles = None

    def set_members( self, memoryPropertyCfgDict ):
        self.type = 0
        self.chip = 0
        self.speedMHz = 1
        self.sizeInByte = 0x00000000
        self.ioMode = 0
        self.interfaceMode = 0
        self.dataRateMode = 0
        self.dummyCycles = 0

    def out_bytes( self ):
        mybytes = bytes([self.type,
                         self.chip,
                         self.speedMHz & 0xFF,
                         (self.speedMHz & 0xFF00) >> 8,
                         self.sizeInByte & 0xFF,
                         (self.sizeInByte & 0xFF00) >> 8,
                         (self.sizeInByte & 0xFF0000) >> 16, 
                         (self.sizeInByte & 0xFF000000) >> 24,
                         self.ioMode,
                         self.interfaceMode,
                         self.dataRateMode,
                         self.dummyCycles
                        ])
        return mybytes

class configSystemPacket(object):

    def __init__( self, parent=None):
        #super(configSystemPacket, self).__init__(parent)
        self.cpuSpeedMHz = None
        self.enableL1Cache = None
        self.enablePrefetch = None
        self.prefetchBufSizeInByte = 4096
        self.reserved0 = [0x0, 0x0]
        self.memConnection = None
        self.memProperty = None
        self.crcCheckSum = None
        self.reserved1 = [0x0, 0x0]

    def set_members( self ):
        self.memConnection = flexspiConnectionStruct()
        flexspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_FlexspiConn)
        self.memConnection.set_members(flexspiConnCfgDict)
        self.memProperty = memoryPropertyStruct()
        self.memProperty.set_members(None)
        toolCommDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Tool)
        self.cpuSpeedMHz = toolCommDict['cpuSpeedMHz']
        self.enableL1Cache = toolCommDict['enableL1Cache']
        self.enablePrefetch = toolCommDict['enablePrefetch']
        self.crcCheckSum = 0x0000

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_ConfigSystem])
        mybytes = bytes([self.cpuSpeedMHz & 0xFF,
                          (self.cpuSpeedMHz & 0xFF00) >> 8,
                          self.enableL1Cache,
                          self.enablePrefetch,
                          self.prefetchBufSizeInByte & 0xFF,
                          (self.prefetchBufSizeInByte & 0xFF00) >> 8,
                          self.reserved0[0],
                          self.reserved0[1]
                         ])
        packetBytes = mybytes + self.memConnection.out_bytes() + self.memProperty.out_bytes()
        self.crcCheckSum = calculate_crc16(packetBytes)
        crcbytes = bytes([self.crcCheckSum & 0xFF,
                          (self.crcCheckSum & 0xFF00) >> 8,
                          self.reserved1[0],
                          self.reserved1[1]
                         ])
        return startbytes + packetBytes + crcbytes

class rwTestPacket(object):

    def __init__( self, parent=None):
        #super(rwTestPacket, self).__init__(parent)
        self.memStart = None
        self.memLen = None
        self.crcCheckSum = None
        self.reserved0 = [0x0, 0x0]

    def set_members( self ):
        self.memStart = 0x00000000
        self.memLen = 0x00000400
        self.crcCheckSum = 0x0000

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_RunRwTest])
        mybytes = bytes([self.memStart & 0xFF,
                         (self.memStart & 0xFF00) >> 8,
                         (self.memStart & 0xFF0000) >> 16, 
                         (self.memStart & 0xFF000000) >> 24,
                         self.memLen & 0xFF,
                         (self.memLen & 0xFF00) >> 8,
                         (self.memLen & 0xFF0000) >> 16, 
                         (self.memLen & 0xFF000000) >> 24
                        ])
        packetBytes = mybytes
        self.crcCheckSum = calculate_crc16(packetBytes)
        crcbytes = bytes([self.crcCheckSum & 0xFF,
                          (self.crcCheckSum & 0xFF00) >> 8,
                          self.reserved1[0],
                          self.reserved1[1]
                         ])
        return startbytes + packetBytes + crcbytes
