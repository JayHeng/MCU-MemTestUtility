
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os


kFlexspiConnSel_Instance = {'1':0x1,
                            '2':0x2
                           }

kFlexspiConnSel_DataL4b = [
                              {'PortA_DATA[3:0] - PIO1[23:20]':0x00
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

kFlexspiConnSel_DataT8b    = [
                              {'None':0xFF
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_ssb     = [
                              {'PortA_SS0_B - PIO1[19]':0x00
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_sclk    = [
                              {'PortA_SCLK - PIO1[18]':0x00
                              },
                              {'None':0xFF
                              }
                          ]

kFlexspiConnSel_dqs     = [
                              {'PortA_DQS - PIO1[28]':0x00
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
                              {'None':0xFF,
                               'RST_B - PIO0[14]':0x00
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
                       'dqs'     :kFlexspiConnSel_dqs,
                       'sclkn'   :kFlexspiConnSel_sclkn,
                       'rstb'    :kFlexspiConnSel_rstb,
                      }



