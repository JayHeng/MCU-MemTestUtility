
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os


kXspiConnSel_Instance   = { '1':0x1,
                            '2':0x2,
                            '3':0x3,
                           }

kXspiConnSel_DataL4b    = [
                              {'TargetGroup0_DATA[3:0] - PIO6[11:8]':0x00
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_DataH4b    = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_DataT8b    = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_ssb        = [
                              {'TargetGroup0_SS0_B        - PIO6[2]':0x00,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_sclk       = [
                              {'TargetGroup0_SCLK          - PIO6[1]':0x00,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_sclkn      = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_dqs0       = [
                              {'None':0xFF,
                               'TargetGroup0_DQS           - PIO6[7]':0x00,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_dqs1       = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              }
                          ]

kXspiConnSel_rstb       = [
                              {'None':0xFF,
                              },
                              {'None':0xFF,
                              },
                              {'None':0xFF
                              }
                          ]

kXspiConnSelDict    = {
                       'instance':kXspiConnSel_Instance,
                       'dataL4b' :kXspiConnSel_DataL4b,
                       'dataH4b' :kXspiConnSel_DataH4b,
                       'dataT8b' :kXspiConnSel_DataT8b,
                       'ssb'     :kXspiConnSel_ssb,
                       'sclk'    :kXspiConnSel_sclk,
                       'sclkn'   :kXspiConnSel_sclkn,
                       'dqs0'    :kXspiConnSel_dqs0,
                       'dqs1'    :kXspiConnSel_dqs1,
                       'rstb'    :kXspiConnSel_rstb,
                      }



