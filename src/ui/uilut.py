#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import json
from . import uidef

############################################################################
NOR_CMD_LUT_SEQ_IDX_READ            = 0
NOR_CMD_LUT_SEQ_IDX_ERASESECTOR     = 1
NOR_CMD_LUT_SEQ_IDX_ENABLEQE        = 2
NOR_CMD_LUT_SEQ_IDX_ENTERQPI        = 3
NOR_CMD_LUT_SEQ_IDX_ENTEROPI        = 3
NOR_CMD_LUT_SEQ_IDX_READSTATUS      = 4
NOR_CMD_LUT_SEQ_IDX_SETDUMMY        = 5
NOR_CMD_LUT_SEQ_IDX_SETDRIVE        = 6
NOR_CMD_LUT_SEQ_IDX_UNIQUECFG       = 6
NOR_CMD_LUT_SEQ_IDX_WRITEENABLE     = 7
NOR_CMD_LUT_SEQ_IDX_READREG1        = 8
NOR_CMD_LUT_SEQ_IDX_PAGEPROGRAM     = 10
NOR_CMD_LUT_SEQ_IDX_READREG2        = 11
# FlexSPI LUT seq defn (1bit spi)
NOR_CMD_LUT_SEQ_IDX_READID          = 12
NOR_CMD_LUT_SEQ_IDX_READID_QPI_1    = 13
NOR_CMD_LUT_SEQ_IDX_READID_QPI_2    = 14
NOR_CMD_LUT_SEQ_IDX_READID_OPI      = 15
# FlexSPI LUT seq defn (quad lut)
NOR_CMD_LUT_SEQ_IDX_READSTATUS_QPI  = 12
NOR_CMD_LUT_SEQ_IDX_WRITEENABLE_QPI = 13
NOR_CMD_LUT_SEQ_IDX_ERASESECTOR_QPI = 14
NOR_CMD_LUT_SEQ_IDX_PAGEPROGRAM_QPI = 15
# FlexSPI LUT seq defn (octal lut)
NOR_CMD_LUT_SEQ_IDX_READSTATUS_OPI  = 12
NOR_CMD_LUT_SEQ_IDX_WRITEENABLE_OPI = 13
NOR_CMD_LUT_SEQ_IDX_ERASESECTOR_OPI = 14
NOR_CMD_LUT_SEQ_IDX_PAGEPROGRAM_OPI = 15
############################################################################

kFLEXSPI_Command_STOP           = 0x00
kFLEXSPI_Command_SDR            = 0x01
kFLEXSPI_Command_RADDR_SDR      = 0x02
kFLEXSPI_Command_CADDR_SDR      = 0x03
kFLEXSPI_Command_MODE1_SDR      = 0x04
kFLEXSPI_Command_MODE2_SDR      = 0x05
kFLEXSPI_Command_MODE4_SDR      = 0x06
kFLEXSPI_Command_MODE8_SDR      = 0x07
kFLEXSPI_Command_WRITE_SDR      = 0x08
kFLEXSPI_Command_READ_SDR       = 0x09
kFLEXSPI_Command_LEARN_SDR      = 0x0A
kFLEXSPI_Command_DATSZ_SDR      = 0x0B
kFLEXSPI_Command_DUMMY_SDR      = 0x0C
kFLEXSPI_Command_DUMMY_RWDS_SDR = 0x0D
kFLEXSPI_Command_DDR            = 0x21
kFLEXSPI_Command_RADDR_DDR      = 0x22
kFLEXSPI_Command_CADDR_DDR      = 0x23
kFLEXSPI_Command_MODE1_DDR      = 0x24
kFLEXSPI_Command_MODE2_DDR      = 0x25
kFLEXSPI_Command_MODE4_DDR      = 0x26
kFLEXSPI_Command_MODE8_DDR      = 0x27
kFLEXSPI_Command_WRITE_DDR      = 0x28
kFLEXSPI_Command_READ_DDR       = 0x29
kFLEXSPI_Command_LEARN_DDR      = 0x2A
kFLEXSPI_Command_DATSZ_DDR      = 0x2B
kFLEXSPI_Command_DUMMY_DDR      = 0x2C
kFLEXSPI_Command_DUMMY_RWDS_DDR = 0x2D
kFLEXSPI_Command_JUMP_ON_CS     = 0x1F

kFLEXSPI_1PAD = 0x00
kFLEXSPI_2PAD = 0x01
kFLEXSPI_4PAD = 0x02
kFLEXSPI_8PAD = 0x03

CUSTOM_LUT_LENGTH = 64

class mixspiLutSequence(object):
    def __init__( self, cmd0, pad0, op0,
                        cmd1=0x0, pad1=0x0, op1=0x0,
                        cmd2=0x0, pad2=0x0, op2=0x0,
                        cmd3=0x0, pad3=0x0, op3=0x0,
                        cmd4=0x0, pad4=0x0, op4=0x0,
                        cmd5=0x0, pad5=0x0, op5=0x0,
                        cmd6=0x0, pad6=0x0, op6=0x0,
                        cmd7=0x0, pad7=0x0, op7=0x0):

        self.sequence = [0x0, 0x0, 0x0, 0x0]
        self.sequence[0] |= (op0 & 0xFF) | ((pad0 << 8) & 0x300) | ((cmd0 << 10) & 0xFC00)
        self.sequence[0] |= ((op1 & 0xFF) | ((pad1 << 8) & 0x300) | ((cmd1 << 10) & 0xFC00)) << 16

        self.sequence[1] |= (op2 & 0xFF) | ((pad2 << 8) & 0x300) | ((cmd2 << 10) & 0xFC00)
        self.sequence[1] |= ((op3 & 0xFF) | ((pad3 << 8) & 0x300) | ((cmd3 << 10) & 0xFC00)) << 16

        self.sequence[2] |= (op4 & 0xFF) | ((pad4 << 8) & 0x300) | ((cmd4 << 10) & 0xFC00)
        self.sequence[2] |= ((op5 & 0xFF) | ((pad5 << 8) & 0x300) | ((cmd5 << 10) & 0xFC00)) << 16

        self.sequence[3] |= (op6 & 0xFF) | ((pad6 << 8) & 0x300) | ((cmd6 << 10) & 0xFC00)
        self.sequence[3] |= ((op7 & 0xFF) | ((pad7 << 8) & 0x300) | ((cmd7 << 10) & 0xFC00)) << 16

def generateCompleteMemLut( mixspiLutDict ):
    memLut = [0x0] * CUSTOM_LUT_LENGTH
    for key in mixspiLutDict.keys():
        if key == 'READ':
            memLut[(NOR_CMD_LUT_SEQ_IDX_READ * 4):((NOR_CMD_LUT_SEQ_IDX_READ + 1) * 4)] = mixspiLutDict[key].sequence
        if key == 'READSTATUS':
            memLut[(NOR_CMD_LUT_SEQ_IDX_READSTATUS * 4):((NOR_CMD_LUT_SEQ_IDX_READSTATUS + 1) * 4)] = mixspiLutDict[key].sequence
        if key == 'WRITEENABLE':
            memLut[(NOR_CMD_LUT_SEQ_IDX_WRITEENABLE * 4):((NOR_CMD_LUT_SEQ_IDX_WRITEENABLE + 1) * 4)] = mixspiLutDict[key].sequence
        if key == 'ENABLEQE':
            memLut[(NOR_CMD_LUT_SEQ_IDX_ENABLEQE * 4):((NOR_CMD_LUT_SEQ_IDX_ENABLEQE + 1) * 4)] = mixspiLutDict[key].sequence
        if key == 'READID':
            memLut[(NOR_CMD_LUT_SEQ_IDX_READID * 4):((NOR_CMD_LUT_SEQ_IDX_READID + 1) * 4)] = mixspiLutDict[key].sequence
        if key == 'READREG1':
            memLut[(NOR_CMD_LUT_SEQ_IDX_READREG1 * 4):((NOR_CMD_LUT_SEQ_IDX_READREG1 + 1) * 4)] = mixspiLutDict[key].sequence
        if key == 'READREG2':
            memLut[(NOR_CMD_LUT_SEQ_IDX_READREG2 * 4):((NOR_CMD_LUT_SEQ_IDX_READREG2 + 1) * 4)] = mixspiLutDict[key].sequence
    return memLut
