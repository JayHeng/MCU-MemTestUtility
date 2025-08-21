
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os

kFlexspiConnSel_Instance = {'1':0x1,
                            '2':0x2,
                           }

kFlexspiConnSel_DataL4b = [
                              {'PortA_DATA[3:0] - GPIO_SD_B2[11:08]':0x00,
                               'PortA_DATA[3:0] - GPIO_AD[23:20]':0x01,
                               'PortB_DATA[3:0] - GPIO_SD_B2[03:00]':0x10,
                               'PortB_DATA[3:0] - GPIO_AD[15:12]':0x11,
                              },
                              {'PortA_DATA[3:0] - GPIO_EMC_B2[16:13]':0x00,
                               'PortA_DATA[3:0] - GPIO_SD_B1[05:02]':0x01,
                               'PortB_DATA[3:0] - GPIO_EMC_B2[06:03]':0x10,
                              }
                          ]

kFlexspiConnSel_DataH4b = [
                              {'None':0xFF,
                               'PortB_DATA[3:0] - GPIO_SD_B2[03:00]':0x10,
                               'PortB_DATA[3:0] - GPIO_AD[15:12]':0x11,
                              },
                              {'None':0xFF,
                               'PortA_DATA[7:4] - GPIO_EMC_B2[20:17]':0x02,
                               'PortB_DATA[7:4] - GPIO_EMC_B1[41]_EMC_B2[02:00]':0x11,
                              }
                          ]

kFlexspiConnSel_DataT8b    = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_ssb     = [
                              {'PortA_SS0_B        - GPIO_SD_B2[06]':0x00,
                               'PortA_SS0_B        - GPIO_AD[18]':0x01,
                               'PortA_SS1_B        - GPIO_SD_B1[02]':0x02,
                               'PortB_SS0_B        - GPIO_SD_B1[04]':0x10,
                               'PortB_SS1_B        - GPIO_AD[35]':0x11,
                               'PortB_SS1_B        - GPIO_SD_B1[03]':0x12,
                              },
                              {'PortA_SS0_B        - GPIO_EMC_B2[11]':0x00,
                               'PortA_SS0_B        - GPIO_SD_B1[00]':0x01,
                               'PortA_SS1_B        - GPIO_AD[01]':0x02,
                               'PortB_SS0_B        - GPIO_EMC_B2[08]':0x10,
                               'PortB_SS1_B        - GPIO_AD[00]':0x11,
                              }
                          ]

kFlexspiConnSel_sclk    = [
                              {'PortA_SCLK          - GPIO_SD_B2[07]':0x00,
                               'PortA_SCLK          - GPIO_AD[19]':0x01,
                               'PortB_SCLK          - GPIO_SD_B2[04]':0x10,
                               'PortB_SCLK          - GPIO_AD[16]':0x11,
                              },
                              {'PortA_SCLK          - GPIO_EMC_B2[10]':0x00,
                               'PortA_SCLK          - GPIO_SD_B1[01]':0x01,
                               'PortB_SCLK          - GPIO_EMC_B2[09]':0x10,
                              }
                          ]

kFlexspiConnSel_sclkn   = [
                              {'None':0xFF,
                               'PortB_SCLKN        - GPIO_SD_B2[04]':0x10,
                               'PortB_SCLKN        - GPIO_AD[16]':0x11,
                              },
                              {'None':0xFF,
                               'PortB_SCLKN        - GPIO_EMC_B2[09]':0x10,
                              }
                          ]

kFlexspiConnSel_dqs0    = [
                              {'None':0xFF,
                               'PortA_DQS           - GPIO_SD_B2[05]':0x00,
                               'PortA_DQS           - GPIO_AD[17]':0x01,
                               'PortA_DQS           - GPIO_EMC_B2[18]':0x02,
                               'PortB_DQS           - GPIO_SD_B1[05]':0x10,
                              },
                              {'None':0xFF,
                               'PortA_DQS           - GPIO_EMC_B2[12]':0x00,
                               'PortB_DQS           - GPIO_EMC_B1[07]':0x10,
                              }
                          ]

kFlexspiConnSel_dqs1    = [
                              {'None':0xFF,
                               'PortB_DQS           - GPIO_SD_B1[05]':0x10,
                              },
                              {'None':0xFF,
                               'PortB_DQS           - GPIO_EMC_B1[07]':0x10,
                              }
                          ]

kFlexspiConnSel_rstb    = [
                              {'None':0xFF,
                               'RST_B                  - GPIO_SD_B1[00]':0x00,
                               'RST_B                  - GPIO_EMC_B1[40]':0x01,
                              },
                              {'None':0xFF,
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

