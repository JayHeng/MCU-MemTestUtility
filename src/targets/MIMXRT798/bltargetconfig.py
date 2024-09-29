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
from ui import ui_def_xspi_conn_rt700

cpu = 'MIMXRT798'
board = 'EVK'
compiler = 'iar'
build = 'Release'
mcuSeries = uidef.kMcuSeries_iMXRTxxx
maxCpuFreqInMHz = 320

availablePeripherals = 0x11
uartPeripheralPinStr = 'LP-Flexcomm0 UART - PIO0[31,0]'
firmwareLoadAddr = 0x00080000
firmwareJumpAddr = 0x00083175
firmwareInitialSp = 0x20300000
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify

flexspiNorDevice = uidef.kFlexspiNorDevice_MXIC_MX25UM51345G
flexspiNorMemBase0 = 0x28000000
flexspiNorMemBase1 = 0x08000000
isSipFlexspiNorDevice = False

mixspiConnDict = ui_def_xspi_conn_rt700.kXspiConnSelDict

# memory map
memoryRange = {
    # SRAM, 3MByte
    'sram' : MemoryRange(0x00000000, 0x780000, 'state_mem0.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {
    # SRAM, 80KB
    'sram' : [0x00000000, 0x00013FFF]
}
