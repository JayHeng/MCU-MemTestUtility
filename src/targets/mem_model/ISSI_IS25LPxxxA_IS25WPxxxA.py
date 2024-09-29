#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys, os
sys.path.append(os.path.abspath(".."))
from ui import uidef
from ui import uilut
from ui.uilut import mixspiLutSequence

# LUT
mixspiLutDict = {
    'READ' :         mixspiLutSequence(uilut.kFLEXSPI_Command_SDR,       uilut.kFLEXSPI_1PAD, 0xEB, 
                                       uilut.kFLEXSPI_Command_RADDR_SDR, uilut.kFLEXSPI_4PAD, 0x18,
                                       uilut.kFLEXSPI_Command_MODE8_SDR, uilut.kFLEXSPI_4PAD, 0x00, 
                                       uilut.kFLEXSPI_Command_DUMMY_SDR, uilut.kFLEXSPI_4PAD, 0x04,
                                       uilut.kFLEXSPI_Command_READ_SDR,  uilut.kFLEXSPI_4PAD, 0x04,
                                       uilut.kFLEXSPI_Command_STOP,     uilut. kFLEXSPI_1PAD, 0x00),
}


