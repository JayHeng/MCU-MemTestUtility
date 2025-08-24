#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json
from . import uidef
from . import uivar

g_exeTopRoot = None
g_hasSubWinBeenOpened = False
g_cfgFilename = None
g_toolCommDict = {'loadFwEn':None,
                  'cmdPacketShowEn':None,
                  'mcuDevice':None,
                  'cpuSpeedMHz':None,
                  'enableL1Cache':None,
                  'enablePrefetch':None,
                  'prefetchBufSizeInByte':None,
                  'memVendor':None,
                  'memType':None,
                  'memTypeDef':None,
                  'memChip':None,
                  'memSpeed':None,
                  'memMode0IoPads':None,
                  'memMode1Interface':None,
                  'memMode2SampleRate':None
                 }

g_mixspiConnCfgDict  = {'instance':1,
                        'dataL4b':None,
                        'dataH4b':None,
                        'dataT8b':None,
                        'ssb':None,
                        'sclk':None,
                        'sclkn':None,
                        'dqs0':None,
                        'dqs1':None,
                        'rstb':None,
                       }

g_mixspiPadCtrlDict  = {'useDefault':True,
                        'rt11yyValC':None,
                        'rt11yyValA':None,
                        'rt10yyVal':None,
                        'rtxxxVal':None,
                        ################
                        'dataL4b_u32':None,
                        'dataH4b_u32':None,
                        'dataT8b_u32':None,
                        'ssb_u32':None,
                        'sclk_u32':None,
                        'sclkn_u32':None,
                        'dqs0_u32':None,
                        'dqs1_u32':None,
                        'rstb_u32':None,
                       }

g_mixspiPintestCfgDict  = {'wavePulse':None,
                           'waveSample':None,
                           'dataL4b_dis':None,
                           'dataH4b_dis':None,
                           'dataT8b_dis':None,
                           'ssb_dis':None,
                           'sclk_dis':None,
                           'sclkn_dis':None,
                           'dqs0_dis':None,
                           'dqs1_dis':None,
                           'rstb_dis':None,
                            }

g_mixspiRwTestCfgDict = {'testSet':None,
                         'testMemStart':None,
                         'testMemSize':None,
                         'fillPatternWord':None,
                          }

g_mixspiPerfTestCfgDict = {'testSet':None,
                           'iterations':None,
                           'subTestSet':None,
                           'enableAverageShow':None,
                           'testMemStart':None,
                           'testMemSize':None,
                           'testBlockSize':None,
                            }

g_mixspiStressTestCfgDict = {'testSet':None,
                             'iterations':None,
                             'enableStopWhenFail':None,
                             'testMemStart':None,
                             'testMemSize':None,
                             'testPageSize':None,
                            }

g_mixspiMemRegsCfgDict = {'isTypeRead':None,
                          'regIdx':None,
                          'regsVal':[uidef.kInvalidMemRegVal] * 9,
                          }

def initVar(cfgFilename):
    global g_hasSubWinBeenOpened
    global g_cfgFilename
    global g_toolCommDict
    global g_mixspiConnCfgDict
    global g_mixspiPadCtrlDict
    global g_mixspiPintestCfgDict
    global g_mixspiRwTestCfgDict
    global g_mixspiPerfTestCfgDict
    global g_mixspiStressTestCfgDict
    global g_mixspiMemRegsCfgDict

    g_hasSubWinBeenOpened = False
    g_cfgFilename = cfgFilename
    if os.path.isfile(cfgFilename):
        cfgDict = None
        with open(cfgFilename, 'r') as fileObj:
            cfgDict = json.load(fileObj)
            fileObj.close()

        g_toolCommDict = cfgDict["cfgToolCommon"][0]
        g_mixspiConnCfgDict = cfgDict["cfgConn"][0]
        g_mixspiPadCtrlDict = cfgDict["cfgPadCtrl"][0]
        g_mixspiPintestCfgDict = cfgDict["cfgPintest"][0]
        g_mixspiRwTestCfgDict = cfgDict["cfgRwTest"][0]
        g_mixspiPerfTestCfgDict = cfgDict["cfgPerfTest"][0]
        g_mixspiStressTestCfgDict = cfgDict["cfgStressTest"][0]
        g_mixspiMemRegsCfgDict = cfgDict["cfgMemRegs"][0]
    else:
        g_toolCommDict = {'loadFwEn':True,
                          'cmdPacketShowEn':False,
                          'mcuDevice':0,
                          'cpuSpeedMHz':996,
                          'enableL1Cache':0,
                          'enablePrefetch':0,
                          'prefetchBufSizeInByte':4096,
                          'memVendor':0,
                          'memType':0,
                          'memTypeDef':0,
                          'memChip':0,
                          'memSpeed':30,
                          'memMode0IoPads':0,
                          'memMode1Interface':0,
                          'memMode2SampleRate':0
                         }
        g_mixspiConnCfgDict  = {'instance':0x1,
                                'dataL4b':0x00,
                                'dataH4b':0xFF,
                                'dataT8b':0xFF,
                                'ssb':0x00,
                                'sclk':0x00,
                                'sclkn':0xFF,
                                'dqs0':0x00,
                                'dqs1':0xFF,
                                'rstb':0xFF,
                               }
        g_mixspiPadCtrlDict  = {'useDefault':True,
                                'rt11yyValC':0x0,
                                'rt11yyValA':0x0,
                                'rt10yyVal':0x0,
                                'rtxxxVal':0x0,
                                ################
                                'dataL4b_u32':0x0,
                                'dataH4b_u32':0x0,
                                'dataT8b_u32':0x0,
                                'ssb_u32':0x0,
                                'sclk_u32':0x0,
                                'sclkn_u32':0x0,
                                'dqs0_u32':0x0,
                                'dqs1_u32':0x0,
                                'rstb_u32':0x0,
                               }
        g_mixspiPintestCfgDict  = {'wavePulse':10,
                                   'waveSample':1,
                                   'dataL4b_dis':0,
                                   'dataH4b_dis':1,
                                   'dataT8b_dis':1,
                                   'ssb_dis':0,
                                   'sclk_dis':0,
                                   'sclkn_dis':1,
                                   'dqs0_dis':0,
                                   'dqs1_dis':1,
                                   'rstb_dis':1,
                                   }

        g_mixspiRwTestCfgDict = {'testSet':0x90,
                                 'testMemStart':0x20500000,
                                 'testMemSize':0x20000,
                                 'fillPatternWord':0x5AA5FF00,
                                  }

        g_mixspiPerfTestCfgDict = {'testSet':0xC0,
                                   'iterations':10,
                                   'subTestSet':0xC1,
                                   'enableAverageShow':1,
                                   'testMemStart':0x20500000,
                                   'testMemSize':0x20000,
                                   'testBlockSize':0x400,
                                    }

        g_mixspiStressTestCfgDict = {'testSet':0xE0,
                                     'iterations':1,
                                     'enableStopWhenFail':1,
                                     'testMemStart':0x20500000,
                                     'testMemSize':0x10000,
                                     'testPageSize':0x400,
                                    }

        g_mixspiMemRegsCfgDict = {'isTypeRead':True,
                                  'regIdx':0,
                                  'regsVal':[uidef.kInvalidMemRegVal] * 9,
                                 }

def deinitVar(cfgFilename=None):
    global g_cfgFilename
    if cfgFilename == None and g_cfgFilename != None:
        cfgFilename = g_cfgFilename
    with open(cfgFilename, 'w') as fileObj:
        global g_toolCommDict
        global g_mixspiConnCfgDict
        global g_mixspiPadCtrlDict
        global g_mixspiPintestCfgDict
        global g_mixspiRwTestCfgDict
        global g_mixspiPerfTestCfgDict
        global g_mixspiStressTestCfgDict
        global g_mixspiMemRegsCfgDict
        cfgDict = {
            "cfgToolCommon": [g_toolCommDict],
            "cfgConn": [g_mixspiConnCfgDict],
            "cfgPadCtrl": [g_mixspiPadCtrlDict],
            "cfgPintest": [g_mixspiPintestCfgDict],
            "cfgRwTest": [g_mixspiRwTestCfgDict],
            "cfgPerfTest": [g_mixspiPerfTestCfgDict],
            "cfgStressTest": [g_mixspiStressTestCfgDict],
            "cfgMemRegs": [g_mixspiMemRegsCfgDict],
        }
        json.dump(cfgDict, fileObj, indent=1)
        fileObj.close()

def getAdvancedSettings( group ):
    if group == uidef.kAdvancedSettings_Tool:
        global g_toolCommDict
        return g_toolCommDict
    elif group == uidef.kAdvancedSettings_Conn:
        global g_mixspiConnCfgDict
        return g_mixspiConnCfgDict
    elif group == uidef.kAdvancedSettings_PadCtrl:
        global g_mixspiPadCtrlDict
        return g_mixspiPadCtrlDict
    elif group == uidef.kAdvancedSettings_Pintest:
        global g_mixspiPintestCfgDict
        return g_mixspiPintestCfgDict
    elif group == uidef.kAdvancedSettings_RwTest:
        global g_mixspiRwTestCfgDict
        return g_mixspiRwTestCfgDict
    elif group == uidef.kAdvancedSettings_PerfTest:
        global g_mixspiPerfTestCfgDict
        return g_mixspiPerfTestCfgDict
    elif group == uidef.kAdvancedSettings_StressTest:
        global g_mixspiStressTestCfgDict
        return g_mixspiStressTestCfgDict
    elif group == uidef.kAdvancedSettings_MemRegs:
        global g_mixspiMemRegsCfgDict
        return g_mixspiMemRegsCfgDict
    else:
        pass

def setAdvancedSettings( group, *args ):
    if group == uidef.kAdvancedSettings_Tool:
        global g_toolCommDict
        g_toolCommDict = args[0]
    elif group == uidef.kAdvancedSettings_Conn:
        global g_mixspiConnCfgDict
        g_mixspiConnCfgDict = args[0]
    elif group == uidef.kAdvancedSettings_PadCtrl:
        global g_mixspiPadCtrlDict
        g_mixspiPadCtrlDict = args[0]
    elif group == uidef.kAdvancedSettings_Pintest:
        global g_mixspiPintestCfgDict
        g_mixspiPintestCfgDict = args[0]
    elif group == uidef.kAdvancedSettings_RwTest:
        global g_mixspiRwTestCfgDict
        g_mixspiRwTestCfgDict = args[0]
    elif group == uidef.kAdvancedSettings_PerfTest:
        global g_mixspiPerfTestCfgDict
        g_mixspiPerfTestCfgDict = args[0]
    elif group == uidef.kAdvancedSettings_StressTest:
        global g_mixspiStressTestCfgDict
        g_mixspiStressTestCfgDict = args[0]
    elif group == uidef.kAdvancedSettings_MemRegs:
        global g_mixspiMemRegsCfgDict
        g_mixspiMemRegsCfgDict = args[0]
    else:
        pass

def getRuntimeSettings( ):
    global g_hasSubWinBeenOpened
    global g_exeTopRoot
    return g_hasSubWinBeenOpened, g_exeTopRoot

def setRuntimeSettings( *args ):
    global g_hasSubWinBeenOpened
    if args[0] != None:
        g_hasSubWinBeenOpened = args[0]
    try:
        global g_exeTopRoot
        if args[1] != None:
            g_exeTopRoot = args[1]
    except:
        pass

