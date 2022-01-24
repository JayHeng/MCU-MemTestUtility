#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys
import os
import array
from . import rundef
sys.path.append(os.path.abspath(".."))
from ui import uicore
from ui import uidef
from ui import uilang
from boot import bltest
from boot import target

def createTarget(device, exeBinRoot):
    cpu = "MIMXRT1052"
    if device == uidef.kMcuDevice_iMXRT500:
        cpu = "MIMXRT595"
    elif device == uidef.kMcuDevice_iMXRT600:
        cpu = "MIMXRT685"
    elif device == uidef.kMcuDevice_iMXRT1011:
        cpu = "MIMXRT1011"
    elif device == uidef.kMcuDevice_iMXRT1015:
        cpu = "MIMXRT1015"
    elif device == uidef.kMcuDevice_iMXRT102x:
        cpu = "MIMXRT1021"
    elif device == uidef.kMcuDevice_iMXRT1024:
        cpu = "MIMXRT1024"
    elif device == uidef.kMcuDevice_iMXRT105x:
        cpu = "MIMXRT1052"
    elif device == uidef.kMcuDevice_iMXRT106x:
        cpu = "MIMXRT1062"
    elif device == uidef.kMcuDevice_iMXRT1064:
        cpu = "MIMXRT1064"
    elif device == uidef.kMcuDevice_iMXRT116x:
        cpu = "MIMXRT1166"
    elif device == uidef.kMcuDevice_iMXRT117x:
        cpu = "MIMXRT1176"
    else:
        pass
    targetBaseDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets', cpu)

    # Check for existing target directory.
    if not os.path.isdir(targetBaseDir):
        targetBaseDir = os.path.join(os.path.dirname(exeBinRoot), 'src', 'targets', cpu)
        if not os.path.isdir(targetBaseDir):
            raise ValueError("Missing target directory at path %s" % targetBaseDir)

    targetConfigFile = os.path.join(targetBaseDir, 'bltargetconfig.py')

    # Check for config file existence.
    if not os.path.isfile(targetConfigFile):
        raise RuntimeError("Missing target config file at path %s" % targetConfigFile)

    # Build locals dict by copying our locals and adjusting file path and name.
    targetConfig = locals().copy()
    targetConfig['__file__'] = targetConfigFile
    targetConfig['__name__'] = 'bltargetconfig'

    # Execute the target config script.
    execfile(targetConfigFile, globals(), targetConfig)

    # Create the target object.
    tgt = target.Target(**targetConfig)

    return tgt, targetBaseDir

class memTesterRun(uicore.memTesterUi):

    def __init__(self, parent=None):
        super(memTesterRun, self).__init__(parent)
        self.blhost = None
        self.sdphost = None
        self.tgt = None
        self.cpuDir = None
        self.sdphostVectorsDir = os.path.join(self.exeTopRoot, 'tools', 'sdphost', 'win', 'vectors')
        self.blhostVectorsDir = os.path.join(self.exeTopRoot, 'tools', 'blhost2_6', 'win', 'vectors')
        self.createMcuTarget()

    def createMcuTarget( self ):
        self.tgt, self.cpuDir = createTarget(self.mcuDevice, self.exeBinRoot)

    def connectToDevice( self ):
        # Create the target object.
        self.createMcuTarget()
        xhost = None
        if self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            xhost = 'sdp_'
        elif (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT11yy) or \
             (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRTxxx):
            xhost = ''
        else:
            pass

        xPeripheral = xhost + 'uart'
        uartComPort = self.uartComPort
        uartBaudrate = int(self.uartBaudrate)
        usbVid = ''
        usbPid = ''

        if self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            self.sdphost = bltest.createBootloader(self.tgt,
                                                   self.sdphostVectorsDir,
                                                   xPeripheral,
                                                   uartBaudrate, uartComPort,
                                                   usbVid, usbPid)
        elif (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT11yy) or \
             (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRTxxx):
            self.blhost = bltest.createBootloader(self.tgt,
                                                  self.blhostVectorsDir,
                                                  xPeripheral,
                                                  uartBaudrate, uartComPort,
                                                  usbVid, usbPid,
                                                  True)
        else:
            pass

    def pingRom( self ):
        if self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT10yy:
            status, results, cmdStr = self.sdphost.errorStatus()
            return (status == boot.status.kSDP_Status_HabEnabled or status == boot.status.kSDP_Status_HabDisabled)
        elif (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRT11yy) or \
             (self.tgt.mcuSeries == uidef.kMcuSeries_iMXRTxxx):
            status, results, cmdStr = self.blhost.getProperty(boot.properties.kPropertyTag_CurrentVersion)
            return (status == boot.status.kStatus_Success)
        else:
            pass
