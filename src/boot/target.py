#! /usr/bin/env python

# Copyright (c) 2013 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys, os
from . import commands, memoryrange, peripherals
sys.path.append(os.path.abspath(".."))
from utils import misc

##
# Bootloader target definition.
class Target(object):

    def __init__(self, cpu, board='', build='', **kwargs):
                #baseDir='.', elfFile=None, memory={}, availableCommands=0,
                #availablePeripherals=0, deviceMemoryAccessable=False, systemDeviceId=0, isBootROM=False, isCrcCheckSupported=False):
        self.cpu = cpu
        self.board = board
        self.build = build

        self.baseDir = misc.get_dict_default(kwargs, 'baseDir', '.')
        self.mcuSeries = misc.get_dict_default(kwargs, 'mcuSeries', '.')
        self.maxCpuFreqInMHz = misc.get_dict_default(kwargs, 'maxCpuFreqInMHz', 0)
        self.memoryRange = misc.get_dict_default(kwargs, 'memoryRange', {})
        self.reservedRegionDict = misc.get_dict_default(kwargs, 'reservedRegionDict', {})
        self.availableCommands = misc.get_dict_default(kwargs, 'availableCommands', 0)
        self.availablePeripherals = misc.get_dict_default(kwargs, 'availablePeripherals', 0)
        self.uartPeripheralPinStr = misc.get_dict_default(kwargs, 'uartPeripheralPinStr', '.')
        self.firmwareLoadAddr = misc.get_dict_default(kwargs, 'firmwareLoadAddr', None)
        self.firmwareJumpAddr = misc.get_dict_default(kwargs, 'firmwareJumpAddr', None)
        self.firmwareInitialSp = misc.get_dict_default(kwargs, 'firmwareInitialSp', None)
        self.supportedPeripheralSpeed_uart = misc.get_dict_default(kwargs, 'supportedPeripheralSpeed_uart', None)
        self.flexspiNorDevice = misc.get_dict_default(kwargs, 'flexspiNorDevice', None)
        self.flexspiNorMemBase = misc.get_dict_default(kwargs, 'flexspiNorMemBase0', None)
        self.flexspiNorMemBase0 = misc.get_dict_default(kwargs, 'flexspiNorMemBase0', None)
        self.flexspiNorMemBase1 = misc.get_dict_default(kwargs, 'flexspiNorMemBase1', None)
        self.isSipFlexspiNorDevice = misc.get_dict_default(kwargs, 'isSipFlexspiNorDevice', None)
        self.mixspiConnDict = misc.get_dict_default(kwargs, 'mixspiConnDict', None)

    ##
    # @brief Check if a command is supported by the target.
    #
    # @return True if the command is supported. False if not.
    def isCommandSupported(self, tag):
        return bool(commands.Commands[tag].propertyMask & self.availableCommands)

    ##
    # @brief Check if a peripheral is supported by the target.
    #
    # @return True if the peripheral is supported. False if not.
    def isPeripheralSupported(self, name):
        return bool(peripherals.PeripheralMasks[name].propertyMask & self.availablePeripherals)



