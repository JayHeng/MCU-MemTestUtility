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
g_toolCommDict = {'mcuDevice':None,
                  'cpuSpeedMHz':None,
                  'enableL1Cache':None,
                  'enablePrefetch':None,
                  'prefetchBufSizeInByte':None
                 }

g_flexspiConnCfgDict = {'instance':1,
                        'dataL4b':None,
                        'dataH4b':None,
                        'dataT8b':None,
                        'ssb':None,
                        'sclk':None,
                        'dqs':None,
                        'sclkn':None,
                        'rstb':None,
                       }

g_flexspiPintestCfgDict = {'wavePulse':None,
                           'waveSample':None,
                           'dataL4b_en':None,
                           'dataH4b_en':None,
                           'dataT8b_en':None,
                           'ssb_en':None,
                           'sclk_en':None,
                           'dqs_en':None,
                           'sclkn_en':None,
                           'rstb_en':None,
                            }

def initVar(cfgFilename):
    global g_hasSubWinBeenOpened
    global g_cfgFilename
    global g_toolCommDict
    global g_flexspiConnCfgDict
    global g_flexspiPintestCfgDict

    g_hasSubWinBeenOpened = False
    g_cfgFilename = cfgFilename
    if os.path.isfile(cfgFilename):
        cfgDict = None
        with open(cfgFilename, 'r') as fileObj:
            cfgDict = json.load(fileObj)
            fileObj.close()

        g_toolCommDict = cfgDict["cfgToolCommon"][0]
        g_flexspiConnCfgDict = cfgDict["cfgFlexspiConn"][0]
        g_flexspiPintestCfgDict = cfgDict["cfgFlexspiPintest"][0]
    else:
        g_toolCommDict = {'mcuDevice':0,
                          'cpuSpeedMHz':996,
                          'enableL1Cache':0,
                          'enablePrefetch':0,
                          'prefetchBufSizeInByte':4096
                         }
        g_flexspiConnCfgDict = {'instance':0x1,
                                'dataL4b':0x0,
                                'dataH4b':0xFF,
                                'dataT8b':0xFF,
                                'ssb':0x0,
                                'sclk':0x0,
                                'dqs':0x0,
                                'sclkn':0xFF,
                                'rstb':0xFF,
                               }
        g_flexspiPintestCfgDict = {'wavePulse':10,
                                   'waveSample':1,
                                   'dataL4b_dis':0,
                                   'dataH4b_dis':1,
                                   'dataT8b_dis':1,
                                   'ssb_dis':0,
                                   'sclk_dis':0,
                                   'dqs_dis':1,
                                   'sclkn_dis':1,
                                   'rstb_dis':1,
                                   }

def deinitVar(cfgFilename=None):
    global g_cfgFilename
    if cfgFilename == None and g_cfgFilename != None:
        cfgFilename = g_cfgFilename
    with open(cfgFilename, 'w') as fileObj:
        global g_toolCommDict
        global g_flexspiConnCfgDict
        global g_flexspiPintestCfgDict
        cfgDict = {
            "cfgToolCommon": [g_toolCommDict],
            "cfgFlexspiConn": [g_flexspiConnCfgDict],
            "cfgFlexspiPintest": [g_flexspiPintestCfgDict]
        }
        json.dump(cfgDict, fileObj, indent=1)
        fileObj.close()

def getAdvancedSettings( group ):
    if group == uidef.kAdvancedSettings_Tool:
        global g_toolCommDict
        return g_toolCommDict
    elif group == uidef.kAdvancedSettings_FlexspiConn:
        global g_flexspiConnCfgDict
        return g_flexspiConnCfgDict
    elif group == uidef.kAdvancedSettings_FlexspiPintest:
        global g_flexspiPintestCfgDict
        return g_flexspiPintestCfgDict
    else:
        pass

def setAdvancedSettings( group, *args ):
    if group == uidef.kAdvancedSettings_Tool:
        global g_toolCommDict
        g_toolCommDict = args[0]
    elif group == uidef.kAdvancedSettings_FlexspiConn:
        global g_flexspiConnCfgDict
        g_flexspiConnCfgDict = args[0]
    elif group == uidef.kAdvancedSettings_FlexspiPintest:
        global g_flexspiPintestCfgDict
        g_flexspiPintestCfgDict = args[0]
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

