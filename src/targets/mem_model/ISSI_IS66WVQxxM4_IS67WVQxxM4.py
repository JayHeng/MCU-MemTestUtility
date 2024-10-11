#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys, os
sys.path.append(os.path.abspath(".."))
from ui import uidef
from ui import uilut
from ui.uilut import mixspiLutSequence

memPropertyDict = {

}

# LUT
mixspiLutDict = {
    'READDATA' :     mixspiLutSequence(uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0xAA,
                                       uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0x00,
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_CADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_DUMMY_DDR,      uilut.kFLEXSPI_4PAD, 0x1c, 
                                       uilut.kFLEXSPI_Command_READ_DDR,       uilut.kFLEXSPI_4PAD, 0x01),

    'WRITEDATA' :    mixspiLutSequence(uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0x22,
                                       uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0x00, 
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_CADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_DUMMY_DDR,      uilut.kFLEXSPI_4PAD, 0x1c, 
                                       uilut.kFLEXSPI_Command_WRITE_DDR,      uilut.kFLEXSPI_4PAD, 0x01),

    'READREG' :      mixspiLutSequence(uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0xCC,
                                       uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0x00,
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_CADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_DUMMY_DDR,      uilut.kFLEXSPI_4PAD, 0x0C,
                                       uilut.kFLEXSPI_Command_READ_DDR,       uilut.kFLEXSPI_4PAD, 0x01),

    'WRITEREG' :     mixspiLutSequence(uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0x66,
                                       uilut.kFLEXSPI_Command_DDR,            uilut.kFLEXSPI_4PAD, 0x00, 
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_CADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_WRITE_DDR,      uilut.kFLEXSPI_4PAD, 0x01,
                                       uilut.kFLEXSPI_Command_STOP,           uilut.kFLEXSPI_1PAD, 0x00),

    'READID' :       mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,            uilut.kFLEXSPI_4PAD, 0xE0,
                                       uilut.kFLEXSPI_Command_RADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_CADDR_DDR,      uilut.kFLEXSPI_4PAD, 0x10,
                                       uilut.kFLEXSPI_Command_DUMMY_RWDS_DDR, uilut.kFLEXSPI_4PAD, 0x08,
                                       uilut.kFLEXSPI_Command_READ_DDR,       uilut.kFLEXSPI_4PAD, 0x01,
                                       uilut.kFLEXSPI_Command_STOP,           uilut.kFLEXSPI_1PAD, 0x00),
}

