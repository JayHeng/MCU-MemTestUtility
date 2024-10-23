
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os

kFlexspiConnSel_Instance = {'1':0x1,
                            '2':0x2,
                           }

kFlexspiConnSel_DataL4b = [
                              {'PortA_DATA[3:0] - GPIO_B2[13:10]':0x00,
                               'PortB_DATA[3:0] - GPIO_SD_B2[11:08]':0x10,
                               'PortB_DATA[3:0] - GPIO_B1[13:10]':0x12,
                              },
                              {'PortA_DATA[3:0] - GPIO_EMC_B1[38:35]':0x00,
                               'PortA_DATA[3:0] - GPIO_AON[27:24]':0x01,
                               'PortB_DATA[3:0] - GPIO_EMC_B1[33:30]':0x10,
                               'PortB_DATA[3:0] - GPIO_AON[18:15]':0x11,
                               'PortB_DATA[3:0] - GPIO_EMC_B1[25:22]':0x12,
                              }
                          ]

kFlexspiConnSel_DataH4b = [
                              {'None':0xFF,
                               'PortA_DATA[7:4] - GPIO_B2[06:03]':0x01,
                               'PortB_DATA[7:4] - GPIO_SD_B2[03:00]':0x11,
                               'PortB_DATA[7:4] - GPIO_B1[09:06]':0x13,
                              },
                              {'None':0xFF,
                               'PortB_DATA[3:0] - GPIO_EMC_B1[33:30]':0x10,
                               'PortB_DATA[3:0] - GPIO_AON[18:15]':0x11,
                               'PortB_DATA[3:0] - GPIO_EMC_B1[25:22]':0x12,
                              }
                          ]

kFlexspiConnSel_DataT8b    = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kFlexspiConnSel_ssb     = [
                              {'PortA_SS0_B        - GPIO_B2[09]':0x00,
                               'PortA_SS1_B        - GPIO_B2[01]':0x01,
                               'PortA_SS1_B        - GPIO_SD_B1[04]':0x02,
                               'PortA_SS1_B        - GPIO_SD_B1[02]':0x03,
                               'PortB_SS0_B        - GPIO_SD_B2[06]':0x10,
                               'PortB_SS0_B        - GPIO_SD_B1[05]':0x11,
                               'PortB_SS0_B        - GPIO_SD_B1[04]':0x12,
                               'PortB_SS0_B        - GPIO_B1[04]':0x13,
                               'PortB_SS1_B        - GPIO_SD_B2[04]':0x14,
                               'PortB_SS1_B        - GPIO_SD_B1[03]':0x15,
                               'PortB_SS1_B        - GPIO_B1[02]':0x16,
                              },
                              {'PortA_SS0_B        - GPIO_EMC_B1[39]':0x00,
                               'PortA_SS0_B        - GPIO_AON[22]':0x01,
                               'PortA_SS1_B        - GPIO_EMC_B1[26]':0x02,
                               'PortA_SS1_B        - GPIO_AON[20]':0x03,
                               'PortA_SS1_B        - GPIO_AON[19]':0x04,
                               'PortB_SS0_B        - GPIO_EMC_B1[28]':0x10,
                               'PortB_SS0_B        - GPIO_AON[21]':0x11,
                               'PortB_SS1_B        - GPIO_EMC_B1[27]':0x12,
                              }
                          ]

kFlexspiConnSel_sclk    = [
                              {'PortA_SCLK          - GPIO_B2[08]':0x00,
                               'PortB_SCLK          - GPIO_SD_B2[07]':0x10,
                               'PortB_SCLK          - GPIO_B1[05]':0x11,
                               'PortB_SCLK          - GPIO_B2[02]':0x12,
                              },
                              {'PortA_SCLK          - GPIO_EMC_B1[41]':0x00,
                               'PortA_SCLK          - GPIO_AON[23]':0x01,
                               'PortB_SCLK          - GPIO_EMC_B1[34]':0x10,
                               'PortB_SCLK          - GPIO_AON[19]':0x11,
                              }
                          ]

kFlexspiConnSel_sclkn   = [
                              {'None':0xFF,
                               'PortB_SCLKN        - GPIO_B2[02]':0x12,
                              },
                              {'None':0xFF,
                               'PortB_SCLKN        - GPIO_EMC_B1[34]':0x10,
                               'PortB_SCLKN        - GPIO_AON[19]':0x11,
                              }
                          ]

kFlexspiConnSel_dqs0     = [
                              {'None':0xFF,
                               'PortA_DQS           - GPIO_B2[07]':0x00,
                               'PortA_DQS           - GPIO_SD_B2[12]':0x01,
                               'PortB_DQS           - GPIO_SD_B2[05]':0x10,
                               'PortB_DQS           - GPIO_SD_B2[12]':0x11,
                               'PortB_DQS           - GPIO_B1[03]':0x12,
                              },
                              {'None':0xFF,
                               'PortA_DQS           - GPIO_EMC_B1[40]':0x00,
                               'PortA_DQS           - GPIO_AON[21]':0x01,
                               'PortA_DQS           - GPIO_AON[28]':0x02,
                               'PortB_DQS           - GPIO_EMC_B1[29]':0x10,
                               'PortB_DQS           - GPIO_AON[20]':0x11,
                               'PortB_DQS           - GPIO_AON[28]':0x12,
                               'PortB_DQS           - GPIO_EMC_B1[21]':0x13,
                              }
                          ]

kFlexspiConnSel_dqs1    = [
                              {'None':0xFF,
                               'PortA_DQS           - GPIO_SD_B2[12]':0x01,
                               'PortB_DQS           - GPIO_SD_B2[12]':0x11,
                              },
                              {'None':0xFF,
                               'PortB_DQS           - GPIO_EMC_B1[29]':0x10,
                               'PortB_DQS           - GPIO_AON[20]':0x11,
                               'PortB_DQS           - GPIO_AON[28]':0x12,
                               'PortB_DQS           - GPIO_EMC_B1[21]':0x13,
                               
                              }
                          ]

kFlexspiConnSel_rstb    = [
                              {'None':0xFF,
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
