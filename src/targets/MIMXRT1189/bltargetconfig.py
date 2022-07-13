#!/usr/bin/env python

# Copyright (c) 2014 Freescale Semiconductor, Inc.
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
sys.path.append(os.path.abspath(".."))
from boot.memoryrange import MemoryRange
from ui import uidef
from ui import ui_def_flexspi_conn_rt1180

cpu = 'MIMXRT1189'
board = 'EVK'
compiler = 'iar'
build = 'Release'
mcuSeries = uidef.kMcuSeries_iMXRT11yy
maxCpuFreqInMHz = 240

availablePeripherals = 0x11
uartPeripheralPinStr = 'LPUART1 - GPIO_AON[9:8]'
firmwareLoadAddr = None
firmwareJumpAddr = None
firmwareInitialSp = None
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify

flexspiNorDevice = uidef.kFlexspiNorDevice_ISSI_IS25LP064A
flexspiNorMemBase0 = 0x38000000
flexspiNorMemBase1 = 0x32000000
isSipFlexspiNorDevice = False

flexspiConnDict = ui_def_flexspi_conn_rt1180.kFlexspiConnSelDict

# memory map
memoryRange = {
    # ITCM_CM33, 512KByte
    'itcm' : MemoryRange(0x1FFC0000, 0x40000, 'state_mem0.dat'),
    # DTCM, 512KByte
    'dtcm' : MemoryRange(0x20000000, 0x80000, 'state_mem1.dat'),
    # OCRAM, 2MByte
    'ocram' : MemoryRange(0x20200000, 0x200000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {   # new
    # OCRAM, 2MB
    'ram' : [0x20203800, 0x20207F58]
}

