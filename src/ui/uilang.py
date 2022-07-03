#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys
import os

kMenuPosition_File     = 0x0
kMenuPosition_Edit     = 0x1
kMenuPosition_View     = 0x2
kMenuPosition_Tools    = 0x3
kMenuPosition_Window   = 0x4
kMenuPosition_Help     = 0x5

kRevision_0_1_0_en =  "【v0.1.0】 \n" + \
                      "  Feature: \n" + \
                      "     1. Support i.MXRT117x \n" + \
                      "     2. Support Quad SPI NOR Flash \n\n"

kMsgLanguageContentDict = {
        'homePage_title':                     ['Home Page'],
        'homePage_info':                      ['https://github.com/JayHeng/MCU-MemTestUtility.git \n'],
        'aboutAuthor_title':                  ['About Author'],
        'aboutAuthor_author':                 [u"Author: 痞子衡 \n"],
        'aboutAuthor_email1':                 ['Email: jie.heng@nxp.com \n'],
        'aboutAuthor_email2':                 ['Email: hengjie1989@foxmail.com \n'],
        'aboutAuthor_blog':                   [u"Blog: 痞子衡嵌入式 https://www.cnblogs.com/henjay724/ \n"],
        'revisionHistory_title':              ['Revision History'],
        'revisionHistory_v0_1_0':             [kRevision_0_1_0_en],

        'connectError_doubleCheckBmod':             ['Make sure that you have put MCU in UART SDP mode (BMOD[1:0] pins = 2\'b01)!'],
        'connectError_doubleCheckSerialMasterBoot': ['Make sure that you have put MCU in UART Master boot mode (ISP[2:0] pins = 3\'b111)!'],
}