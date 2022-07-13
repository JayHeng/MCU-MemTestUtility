
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os

kFlexspiConnSel_Instance = {'1':0x1,
                            '2':0x2
                           }

kFlexspiConnSel_DataL4b = [
                              {'PortA_DATA[3:0] - GPIO_B2[13:10]':0x00,
                               'PortB_DATA[3:0] - GPIO_SD_B2[11:8]':0x10
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_DataH4b = [
                              {'None':0xFF
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_ssb     = [
                              {'PortA_SS0_B - GPIO_B2[9]':0x00,
                               'PortB_SS0_B - GPIO_SD_B2[6]':0x10
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_sclk    = [
                              {'PortA_SCLK - GPIO_B2[8]':0x00,
                               'PortB_SCLK - GPIO_SD_B2[7]':0x10
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_dqs     = [
                              {'PortA_DQS - GPIO_B2[7]':0x00,
                               'PortB_DQS - GPIO_SD_B2[5]':0x10
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_sclkn   = [
                              {'None':0xFF
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_rstb    = [
                              {'None':0xFF
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSelDict = {
                       'instance':kFlexspiConnSel_Instance,
                       'dataL4b' :kFlexspiConnSel_DataL4b,
                       'dataH4b' :kFlexspiConnSel_DataH4b,
                       'ssb'     :kFlexspiConnSel_ssb,
                       'sclk'    :kFlexspiConnSel_sclk,
                       'dqs'     :kFlexspiConnSel_dqs,
                       'sclkn'   :kFlexspiConnSel_sclkn,
                       'rstb'    :kFlexspiConnSel_rstb,
                      }
