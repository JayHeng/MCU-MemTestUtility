#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys, os
sys.path.append(os.path.abspath(".."))
from ui import uidef
from ui import uilut
from ui.uilut import mixspiLutSequence

memPropertyDict = {
    'qe_cfg':     0x00,
    'qe_bytes':   0x00,
}

# LUT
mixspiLutDict = {
    'READ' :         mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0xEB, 
                                       uilut.kFLEXSPI_Command_RADDR_SDR, uilut.kFLEXSPI_4PAD, 0x18,
                                       uilut.kFLEXSPI_Command_DUMMY_SDR, uilut.kFLEXSPI_4PAD, 0x0A,
                                       uilut.kFLEXSPI_Command_READ_SDR,  uilut.kFLEXSPI_4PAD, 0x04),

    'READSTATUS' :   mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x05, 
                                       uilut.kFLEXSPI_Command_READ_SDR,  uilut.kFLEXSPI_1PAD, 0x01),

    'WRITEENABLE' :  mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x06),

    'ENABLEQE' :     mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x01,
                                       uilut.kFLEXSPI_Command_WRITE_SDR, uilut.kFLEXSPI_1PAD, 0x01),

    'READID' :       mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x9F,
                                       uilut.kFLEXSPI_Command_READ_SDR,  uilut.kFLEXSPI_1PAD, 0x04),

    # NON VOLATILE CONFIGURATION REGISTER
    'READREG1' :     mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0xB5, 
                                       uilut.kFLEXSPI_Command_READ_SDR,  uilut.kFLEXSPI_1PAD, 0x02),

    # FLAG STATUS REGISTER
    'READREG2' :     mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x70, 
                                       uilut.kFLEXSPI_Command_READ_SDR,  uilut.kFLEXSPI_1PAD, 0x01),

    'ERASESECTOR' :  mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x20,
                                       uilut.kFLEXSPI_Command_RADDR_SDR, uilut.kFLEXSPI_1PAD, 0x18),

    'PAGEPROGRAM' :  mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0x02,
                                       uilut.kFLEXSPI_Command_RADDR_SDR, uilut.kFLEXSPI_1PAD, 0x18,
                                       uilut.kFLEXSPI_Command_WRITE_SDR, uilut.kFLEXSPI_1PAD, 0x04,
                                       uilut.kFLEXSPI_Command_STOP,      uilut.kFLEXSPI_1PAD, 0x00),
}
