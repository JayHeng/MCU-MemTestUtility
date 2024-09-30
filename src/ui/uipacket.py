#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json
from crc import CrcCalculator, Configuration
from . import uidef
from . import uivar
from . import uilut

kPacketTag = "FTAG"

kCommandTag_PinTest        = 0x01
kCommandTag_ConfigSystem   = 0x02
kCommandTag_GetMemInfo     = 0x03
kCommandTag_RunRwTest      = 0x04
kCommandTag_RunPerfTest    = 0x05
kCommandTag_RunStressTest  = 0x06

kCommandTag_TestStop       = 0xF0

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

class mixspiConnectionStruct(object):

    def __init__( self, parent=None):
        #super(mixspiConnectionStruct, self).__init__(parent)
        self.instance = None
        self.dataLow4bit = None
        self.dataHigh4bit = None
        self.dataTop8bit = None
        self.ss_b = None
        self.sclk = None
        self.sclk_n = None
        self.dqs0 = None
        self.dqs1 = None
        self.rst_b = None
        self.reserved0 = [0x0, 0x0]

    def set_members( self, mixspiConnCfgDict ):
        self.instance = mixspiConnCfgDict['instance']
        self.dataLow4bit = mixspiConnCfgDict['dataL4b']
        self.dataHigh4bit = mixspiConnCfgDict['dataH4b']
        self.dataTop8bit = mixspiConnCfgDict['dataT8b']
        self.ss_b = mixspiConnCfgDict['ssb']
        self.sclk = mixspiConnCfgDict['sclk']
        self.sclk_n = mixspiConnCfgDict['sclkn']
        self.dqs0 = mixspiConnCfgDict['dqs0']
        self.dqs1 = mixspiConnCfgDict['dqs1']
        self.rst_b = mixspiConnCfgDict['rstb']

    def out_bytes( self ):
        mybytes = bytes([self.instance,
                         self.dataLow4bit,
                         self.dataHigh4bit, 
                         self.dataTop8bit, 
                         self.ss_b,
                         self.sclk,
                         self.sclk_n,
                         self.dqs0,
                         self.dqs1,
                         self.rst_b,
                         self.reserved0[0],
                         self.reserved0[1],
                        ])
        return mybytes

class mixspiPintestEnStruct(object):

    def __init__( self, parent=None):
        #super(mixspiPintestEnStruct, self).__init__(parent)
        self.pulseInMs = None
        self.enableAdcSample = None
        self.reserved0 = [0x0, 0x0, 0x0]
        self.option = None

    def set_members( self, mixspiPintestCfgDict ):
        self.pulseInMs = mixspiPintestCfgDict['wavePulse']
        self.enableAdcSample = mixspiPintestCfgDict['waveSample']
        self.option = 0x00000000
        if mixspiPintestCfgDict['dataL4b_dis'] == 0:
            self.option = self.option | (1 << 0)
        if mixspiPintestCfgDict['dataH4b_dis'] == 0:
            self.option = self.option | (1 << 1)
        if mixspiPintestCfgDict['dataT8b_dis'] == 0:
            self.option = self.option | (1 << 2)
        if mixspiPintestCfgDict['ssb_dis'] == 0:
            self.option = self.option | (1 << 3)
        if mixspiPintestCfgDict['sclk_dis'] == 0:
            self.option = self.option | (1 << 4)
        if mixspiPintestCfgDict['sclkn_dis'] == 0:
            self.option = self.option | (1 << 5)
        if mixspiPintestCfgDict['dqs0_dis'] == 0:
            self.option = self.option | (1 << 6)
        if mixspiPintestCfgDict['dqs1_dis'] == 0:
            self.option = self.option | (1 << 7)
        if mixspiPintestCfgDict['rstb_dis'] == 0:
            self.option = self.option | (1 << 8)

    def out_bytes( self ):
        mybytes = bytes([self.pulseInMs & 0xFF,
                         (self.pulseInMs & 0xFF00) >> 8,
                         (self.pulseInMs & 0xFF0000) >> 16, 
                         (self.pulseInMs & 0xFF000000) >> 24,
                         self.enableAdcSample,
                         self.reserved0[0],
                         self.reserved0[1],
                         self.reserved0[2],
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
        self.memConnection = mixspiConnectionStruct()
        mixspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Conn)
        self.memConnection.set_members(mixspiConnCfgDict)
        self.unittestEn = mixspiPintestEnStruct()
        mixspiPintestCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Pintest)
        self.unittestEn.set_members(mixspiPintestCfgDict)
        self.crcCheckSum = 0x0000

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_PinTest])
        packetBytes = self.memConnection.out_bytes() + self.unittestEn.out_bytes()
        self.crcCheckSum = calculate_crc16(packetBytes)
        crcbytes = bytes([self.crcCheckSum & 0xFF,
                         (self.crcCheckSum & 0xFF00) >> 8,
                         self.reserved0[0],
                         self.reserved0[1]
                        ])
        return startbytes + packetBytes + crcbytes

class memoryPropertyStruct(object):

    def __init__( self, memLut, flashPropertyDict):
        #super(memoryPropertyStruct, self).__init__(parent)
        self.type = None
        self.chip = None
        self.speedMHz = None
        self.sizeInByte = 0x00000000
        self.ioMode = None
        self.interfaceMode = None
        self.dataRateMode = None
        self.dummyCycles = None
        self.flashQuadEnableCfg = flashPropertyDict['qe_cfg']
        self.flashQuadEnableBytes = flashPropertyDict['qe_bytes']
        self.reserved0 = 0x0
        self.memLut = memLut

    def set_members( self, memUserSettingDict ):
        self.type = 0
        self.chip = 0
        self.speedMHz = memUserSettingDict['memSpeed']
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
                         self.dummyCycles,
                         self.flashQuadEnableCfg & 0xFF,
                         (self.flashQuadEnableCfg & 0xFF00) >> 8,
                         self.flashQuadEnableBytes,
                         self.reserved0
                        ])
        for i in range(uilut.CUSTOM_LUT_LENGTH):
            mybytes += bytes([self.memLut[i] & 0xFF,
                             (self.memLut[i] & 0xFF00) >> 8,
                             (self.memLut[i] & 0xFF0000) >> 16,
                             (self.memLut[i] & 0xFF000000) >> 24
                             ])
        return mybytes

class configSystemPacket(object):

    def __init__( self, memLut, flashPropertyDict):
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

        self.memLut = memLut
        self.flashPropertyDict = flashPropertyDict

    def set_members( self, memUserSettingDict ):
        self.memConnection = mixspiConnectionStruct()
        mixspiConnCfgDict = uivar.getAdvancedSettings(uidef.kAdvancedSettings_Conn)
        self.memConnection.set_members(mixspiConnCfgDict)
        self.memProperty = memoryPropertyStruct(self.memLut, self.flashPropertyDict)
        self.memProperty.set_members(memUserSettingDict)
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

class memInfoPacket(object):

    def __init__( self, parent=None):
        pass

    def set_members( self ):
        pass

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_GetMemInfo])
        return startbytes

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

class testStopPacket(object):

    def __init__( self, parent=None):
        pass

    def set_members( self ):
        pass

    def out_bytes( self ):
        startbytes = bytes(kPacketTag, 'ascii') + bytes([kCommandTag_TestStop])
        return startbytes
