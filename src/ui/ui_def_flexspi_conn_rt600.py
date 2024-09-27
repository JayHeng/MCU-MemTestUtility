
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os


kFlexspiConnSel_Instance = {'1':0x1,
                           }

kFlexspiConnSel_DataL4b = [
                              {'PortA_DATA[3:0] - PIO1[23:20]':0x00,
                               'PortB_DATA[3:0] - PIO1[14:11]':0x10,
                              }
                          ]

kFlexspiConnSel_DataH4b = [
                              {'None':0xFF,
                               'PortA_DATA[7:4] - PIO1[27:24]':0x01,
                               'PortB_DATA[7:4] - PIO2[23,22,18,17]':0x11,
                              }
                          ]

kFlexspiConnSel_DataT8b    = [
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_ssb     = [
                              {'PortA_SS0_B - PIO1[19]':0x00,
                               'PortB_SS0_B - PIO2[19]':0x10,
                              }
                          ]

kFlexspiConnSel_sclk    = [
                              {'PortA_SCLK - PIO1[18]':0x00,
                               'PortB_SCLK - PIO1[29]':0x10,
                              }
                          ]

kFlexspiConnSel_sclkn   = [
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_dqs0    = [
                              {'None':0xFF,
                               'PortA_DQS - PIO1[28]':0x00,
                              }
                          ]

kFlexspiConnSel_dqs1    = [
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_rstb    = [
                              {'None':0xFF,
                               'RST_B - PIO0[26]':0x00,
                              }
                          ]

kFlexspiConnSelDict = {
                       'instance':kFlexspiConnSel_Instance,
                       'dataL4b' :kFlexspiConnSel_DataL4b,
                       'dataH4b' :kFlexspiConnSel_DataH4b,
                       'dataT8b' :kFlexspiConnSel_DataT8b,
                       'ssb'     :kFlexspiConnSel_ssb,
                       'sclk'    :kFlexspiConnSel_sclk,
                       'sclkn'   :kFlexspiConnSel_sclkn,
                       'dqs0'     :kFlexspiConnSel_dqs0,
                       'dqs1'     :kFlexspiConnSel_dqs1,
                       'rstb'    :kFlexspiConnSel_rstb,
                      }



