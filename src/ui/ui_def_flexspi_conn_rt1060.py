
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os


kFlexspiConnSel_Instance = {'1':0x1,
                            '2':0x2,
                           }

kFlexspiConnSel_DataL4b = [
                              {'PortA_DATA[3:0] - GPIO_SD_B1[11:8]':0x00,
                               'PortB_DATA[3:0] - GPIO_SD_B1[3:0]':0x10,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_DataH4b = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_DataT8b    = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_ssb     = [
                              {'PortA_SS0_B        - GPIO_SD_B1[6]':0x00,
                               'PortA_SS1_B        - GPIO_SD_B0[0]':0x01,
                               'PortB_SS0_B        - GPIO_SD_B0[4]':0x10,
                               'PortB_SS1_B        - GPIO_SD_B0[1]':0x11,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_sclk    = [
                              {'PortA_SCLK          - GPIO_SD_B1[7]':0x00,
                               'PortB_SCLK          - GPIO_SD_B1[4]':0x10,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_sclkn   = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_dqs0    = [
                              {'None':0xFF,
                               'PortA_DQS           - GPIO_SD_B1[5]':0x00,
                               'PortB_DQS           - GPIO_SD_B0[5]':0x10,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_dqs1    = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_rstb    = [
                              {'None':0xFF,
                               'RST_B                  - GPIO_AD_B0[9]':0x00,
                              },
                              {'None':0xFF
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

