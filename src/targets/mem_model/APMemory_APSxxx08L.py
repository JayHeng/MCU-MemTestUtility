#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys, os
sys.path.append(os.path.abspath(".."))
from ui import uidef
from ui import uilut
from ui.uilut import mixspiLutSequence

flashPropertyDict = {
    'qe_cfg':     0x02,
    'qe_bytes':   0x01,
}

# LUT
mixspiLutDict = {
    'READDATA' :     mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,            uilut.kFLEXSPI_8PAD, 0x20, 
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_8PAD, 0x20,
                                       uilut.kFLEXSPI_Command_DUMMY_RWDS_DDR, uilut.kFLEXSPI_8PAD, 0x07, 
                                       uilut.kFLEXSPI_Command_READ_DDR,       uilut.kFLEXSPI_8PAD, 0x04),

    'WRITEDATA' :    mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,            uilut.kFLEXSPI_8PAD, 0xA0, 
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_8PAD, 0x20,
                                       uilut.kFLEXSPI_Command_DUMMY_RWDS_DDR, uilut.kFLEXSPI_8PAD, 0x07, 
                                       uilut.kFLEXSPI_Command_WRITE_DDR,      uilut.kFLEXSPI_8PAD, 0x04),

    'READREG' :      mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,            uilut.kFLEXSPI_8PAD, 0x40,
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_8PAD, 0x20,
                                       uilut.kFLEXSPI_Command_DUMMY_RWDS_DDR, uilut.kFLEXSPI_8PAD, 0x07,
                                       uilut.kFLEXSPI_Command_READ_DDR,       uilut.kFLEXSPI_8PAD, 0x04),

    'WRITEREG' :     mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,            uilut.kFLEXSPI_8PAD, 0xC0,
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_8PAD, 0x20,
                                       uilut.kFLEXSPI_Command_WRITE_DDR,      uilut.kFLEXSPI_8PAD, 0x08,
                                       uilut.kFLEXSPI_Command_STOP,           uilut.kFLEXSPI_1PAD, 0x00),

    'RESET' :        mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,            uilut.kFLEXSPI_8PAD, 0xFF,
                                       uilut.kFLEXSPI_Command_DUMMY_SDR,      uilut.kFLEXSPI_8PAD, 0x03),
}


