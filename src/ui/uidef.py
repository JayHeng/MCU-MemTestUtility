
# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys, os

kMcuSeries_iMXRT10yy = 'RT10yy'
kMcuSeries_iMXRT11yy = 'RT11yy'

kMcuSeries_iMXRTyyyy = [kMcuSeries_iMXRT10yy, kMcuSeries_iMXRT11yy]
kMcuSeries_iMXRTxxx  = 'RTxxx'

kMcuDevice_iMXRT500  = 'i.MXRT5xx'
kMcuDevice_iMXRT500S = 'i.MXRT5xxS'
kMcuDevice_iMXRT600  = 'i.MXRT6xx'
kMcuDevice_iMXRT600S = 'i.MXRT6xxS'
kMcuDevice_iMXRT700  = 'i.MXRT7xx'
kMcuDevice_iMXRTxxx = [kMcuDevice_iMXRT500, kMcuDevice_iMXRT600, kMcuDevice_iMXRT700]

kMcuDevice_iMXRT1011 = 'i.MXRT1011'
kMcuDevice_iMXRT1015 = 'i.MXRT1015'
kMcuDevice_iMXRT102x = 'i.MXRT1021'
kMcuDevice_iMXRT1024 = 'i.MXRT1024 SIP'
kMcuDevice_iMXRT105x = 'i.MXRT105x'
kMcuDevice_iMXRT106x = 'i.MXRT106x'
kMcuDevice_iMXRT1064 = 'i.MXRT1064 SIP'
kMcuDevice_iMXRT10yy = [kMcuDevice_iMXRT1011, kMcuDevice_iMXRT1015, kMcuDevice_iMXRT102x, kMcuDevice_iMXRT1024, kMcuDevice_iMXRT105x, kMcuDevice_iMXRT106x, kMcuDevice_iMXRT1064]

kMcuDevice_iMXRT116x = 'i.MXRT116x'
kMcuDevice_iMXRT117x = 'i.MXRT117x'
kMcuDevice_iMXRT118x = 'i.MXRT118x'
kMcuDevice_iMXRT11yy = [kMcuDevice_iMXRT116x, kMcuDevice_iMXRT117x, kMcuDevice_iMXRT118x]

kMcuDevice_v1_0       = [kMcuDevice_iMXRT500, kMcuDevice_iMXRT600, kMcuDevice_iMXRT700, kMcuDevice_iMXRT106x, kMcuDevice_iMXRT117x, kMcuDevice_iMXRT118x]
kMcuDevice_Latest     = kMcuDevice_iMXRTxxx + kMcuDevice_iMXRT10yy + kMcuDevice_iMXRT11yy

kFlexspiNorDevice_ISSI_IS25LP064A       = 'ISSI_IS25LPxxxA_IS25WPxxxA'
kFlexspiNorDevice_ISSI_IS26KS512S       = 'ISSI_IS26KSxxxS_IS26KLxxxS'
kFlexspiNorDevice_ISSI_IS25WX256        = 'ISSI_IS25WX256'
kFlexspiNorDevice_MXIC_MX25L12845G      = 'Macronix_MX25Uxxx32F_MX25Lxxx45G'
kFlexspiNorDevice_MXIC_MX25UM51245G     = 'Macronix_MX25UMxxx45G_MX66UMxxx45G_MX25LMxxx45G'
kFlexspiNorDevice_MXIC_MX25UM51345G     = 'Macronix_MX25UM51345G'
kFlexspiNorDevice_MXIC_MX25UM51345G_2nd = 'Macronix_MX25UM51345G_2nd'
kFlexspiNorDevice_Micron_MT25QL128A     = 'Micron_MT25QLxxxA'
kFlexspiNorDevice_Micron_MT35X          = 'Micron_MT35XLxxxA_MT35XUxxxA'
kFlexspiNorDevice_Adesto_AT25SF128A     = 'Adesto_AT25SFxxxA'
kFlexspiNorDevice_Adesto_ATXP032        = 'Adesto_ATXPxxx'
kFlexspiNorDevice_Cypress_S25FL128S     = 'Cypress_S25FSxxxS_S25FLxxxS'
kFlexspiNorDevice_Cypress_S28HS512T     = 'Cypress_S28HSxxxT_S28HLxxxT'
kFlexspiNorDevice_Cypress_S26KS512S     = 'Cypress_S26KSxxxS_S26KLxxxS'
kFlexspiNorDevice_GigaDevice_GD25Q64C   = 'GigaDevice_GD25QxxxC'
kFlexspiNorDevice_GigaDevice_GD25LB256E = 'GigaDevice_GD25LBxxxE'
kFlexspiNorDevice_GigaDevice_GD25LT256E = 'GigaDevice_GD25LTxxxE'
kFlexspiNorDevice_GigaDevice_GD25LX256E = 'GigaDevice_GD25LXxxxE'
kFlexspiNorDevice_Winbond_W25Q128JV     = 'Winbond_W25QxxxJV'
kFlexspiNorDevice_Winbond_W35T51NW      = 'Winbond_W35T51NW'
kFlexspiNorDevice_Microchip_SST26VF064B = 'Microchip_SST26VFxxxB'
kFlexspiNorDevice_FudanMicro_FM25Q64    = 'FudanMicro_FM25Qxxx'
kFlexspiNorDevice_BoyaMicro_BY25Q16BS   = 'BoyaMicro_BY25QxxxBS'
kFlexspiNorDevice_XMC_XM25QH64B         = 'XMC_XM25QHxxxB_XM25QUxxxB'
kFlexspiNorDevice_XTXtech_X25Q64D       = 'XTXtech_X25FxxxB_X25QxxxD'
kFlexspiNorDevice_Puya_P25Q64LE         = 'Puya_P25QxxxLE_P25QxxxH_P25QxxxU'
kFlexspiNorDevice_AMIC_A25LQ64          = 'AMIC_A25LQxxx'

kFlexspiNorDevices_QuadSPI = [kFlexspiNorDevice_ISSI_IS25LP064A,
                              kFlexspiNorDevice_MXIC_MX25L12845G,
                              kFlexspiNorDevice_Micron_MT25QL128A,
                              kFlexspiNorDevice_Adesto_AT25SF128A,
                              kFlexspiNorDevice_Cypress_S25FL128S,
                              kFlexspiNorDevice_GigaDevice_GD25LB256E,
                              kFlexspiNorDevice_GigaDevice_GD25LT256E,
                              kFlexspiNorDevice_Winbond_W25Q128JV,
                              kFlexspiNorDevice_Microchip_SST26VF064B,
                              kFlexspiNorDevice_FudanMicro_FM25Q64,
                              kFlexspiNorDevice_BoyaMicro_BY25Q16BS,
                              kFlexspiNorDevice_XMC_XM25QH64B,
                              kFlexspiNorDevice_XTXtech_X25Q64D,
                              kFlexspiNorDevice_Puya_P25Q64LE,
                              kFlexspiNorDevice_AMIC_A25LQ64
                             ]

kFlexspiNorDevices_OctalSPI = [kFlexspiNorDevice_MXIC_MX25UM51245G,
                               kFlexspiNorDevice_MXIC_MX25UM51345G,
                               kFlexspiNorDevice_Micron_MT35X,
                               kFlexspiNorDevice_Adesto_ATXP032,
                               kFlexspiNorDevice_ISSI_IS25WX256,
                               kFlexspiNorDevice_Winbond_W35T51NW,
                               kFlexspiNorDevice_GigaDevice_GD25LX256E,
                              ]

kFlexspiNorDevices_HyperFlash = [kFlexspiNorDevice_ISSI_IS26KS512S,
                                 kFlexspiNorDevice_Cypress_S26KS512S
                                ]

kFlexspiRamDevice_APMemory_APS12808L       = 'APMemory_APSxxx08L'
kFlexspiRamDevice_Cypress_S27KL0641        = 'Cypress_S27KLxxx1_S27KSxxx1'
kFlexspiRamDevice_ISSI_IS66WVH8M8          = 'ISSI_IS66WVHxxM8_IS67WVHxxM8'
kFlexspiRamDevice_ISSI_IS66WVO8M8          = 'ISSI_IS66WVOxxM8_IS67WVOxxM8'
kFlexspiRamDevice_ISSI_IS66WVQ8M4          = 'ISSI_IS66WVQxxM4_IS67WVQxxM4'
kFlexspiRamDevice_Winbond_W957D8           = 'Winbond_W957D8_W957A8'

kFlexspiRamDevices_PSRAM    = [kFlexspiRamDevice_APMemory_APS12808L,
                               kFlexspiRamDevice_ISSI_IS66WVO8M8,
                               kFlexspiRamDevice_ISSI_IS66WVQ8M4
                              ]

kFlexspiRamDevices_HyperRAM = [kFlexspiRamDevice_Cypress_S27KL0641,
                               kFlexspiRamDevice_ISSI_IS66WVH8M8,
                               kFlexspiRamDevice_Winbond_W957D8
                              ]

kMemVendor_Winbond    = 'Winbond'
kMemVendor_Macronix   = 'Macronix'
kMemVendor_GigaDevice = 'GigaDevice'
kMemVendor_Infineon   = 'Infineon_Cypress_Spansion'
kMemVendor_Micron     = 'Micron'
kMemVendor_ISSI       = 'ISSI'
kMemVendor_Renesas    = 'Renesas_Dialog__Adesto'
kMemVendor_APMemory   = 'APMemory'
kMemVendor_Misc       = 'Misc'
kMemVendor_NXP        = 'NXP'

kMemVendorList = [kMemVendor_Winbond,
                  kMemVendor_Macronix,
                  kMemVendor_GigaDevice,
                  kMemVendor_Infineon,
                  kMemVendor_Micron,
                  kMemVendor_ISSI,
                  kMemVendor_Renesas,
                  kMemVendor_APMemory,
                  kMemVendor_Misc,
                  kMemVendor_NXP]

kMemType_QuadSPI        = 'QuadSPI_NOR'
kMemType_OctalSPI       = 'OctalSPI_NOR'
kMemType_HyperFlash     = 'HyperFlash'
kMemType_PSRAM          = 'PSRAM'
kMemType_HyperRAM       = 'HyperRAM'
kMemType_InternalMem    = 'Internal_Memory'

kMemTypeList = [kMemType_QuadSPI, kMemType_OctalSPI, kMemType_HyperFlash, 'none', kMemType_PSRAM, kMemType_HyperRAM, kMemType_InternalMem]

kMemDeviceDict = {
    kMemVendor_Winbond:{
         kMemType_QuadSPI:[kFlexspiNorDevice_Winbond_W25Q128JV],
         kMemType_OctalSPI:[kFlexspiNorDevice_Winbond_W35T51NW],
         kMemType_HyperRAM:[kFlexspiRamDevice_Winbond_W957D8],
    },
    kMemVendor_Macronix:{
         kMemType_QuadSPI:[kFlexspiNorDevice_MXIC_MX25L12845G],
         kMemType_OctalSPI:[kFlexspiNorDevice_MXIC_MX25UM51245G, kFlexspiNorDevice_MXIC_MX25UM51345G],
    },
    kMemVendor_GigaDevice:{
         kMemType_QuadSPI:[kFlexspiNorDevice_GigaDevice_GD25LB256E, kFlexspiNorDevice_GigaDevice_GD25LT256E],
         kMemType_OctalSPI:[kFlexspiNorDevice_GigaDevice_GD25LX256E],
    },
    kMemVendor_Infineon:{
         kMemType_QuadSPI:[kFlexspiNorDevice_Cypress_S25FL128S],
         kMemType_OctalSPI:[kFlexspiNorDevice_Cypress_S28HS512T],
         kMemType_HyperFlash:[kFlexspiNorDevice_Cypress_S26KS512S],
         kMemType_HyperRAM:[kFlexspiRamDevice_Cypress_S27KL0641],
    },
    kMemVendor_Micron:{
         kMemType_QuadSPI:[kFlexspiNorDevice_Micron_MT25QL128A],
         kMemType_OctalSPI:[kFlexspiNorDevice_Micron_MT35X],
    },
    kMemVendor_ISSI:{
         kMemType_QuadSPI:[kFlexspiNorDevice_ISSI_IS25LP064A],
         kMemType_OctalSPI:[kFlexspiNorDevice_ISSI_IS25WX256],
         kMemType_HyperFlash:[kFlexspiNorDevice_ISSI_IS26KS512S],
         kMemType_PSRAM:[kFlexspiRamDevice_ISSI_IS66WVQ8M4, kFlexspiRamDevice_ISSI_IS66WVO8M8],
         kMemType_HyperRAM:[kFlexspiRamDevice_ISSI_IS66WVH8M8],
    },
    kMemVendor_Renesas:{
         kMemType_QuadSPI:[kFlexspiNorDevice_Adesto_AT25SF128A],
         kMemType_OctalSPI:[kFlexspiNorDevice_Adesto_ATXP032],
    },
    kMemVendor_APMemory:{
         kMemType_PSRAM:[kFlexspiRamDevice_APMemory_APS12808L],
    },
    kMemVendor_Misc:{
         kMemType_QuadSPI:[kFlexspiNorDevice_Microchip_SST26VF064B,
                           kFlexspiNorDevice_FudanMicro_FM25Q64,
                           kFlexspiNorDevice_BoyaMicro_BY25Q16BS,
                           kFlexspiNorDevice_XMC_XM25QH64B,
                           kFlexspiNorDevice_XTXtech_X25Q64D,
                           kFlexspiNorDevice_Puya_P25Q64LE,
                           kFlexspiNorDevice_AMIC_A25LQ64],
    },
    kMemVendor_NXP:{
         kMemType_InternalMem:['SRAM'],
    },
}

kAdvancedSettings_Tool             = 0
kAdvancedSettings_Conn             = 1
kAdvancedSettings_Pintest          = 2
kAdvancedSettings_RwTest           = 3
kAdvancedSettings_PerfTest         = 4
kAdvancedSettings_StressTest       = 5

kAdvancedSettings_PadCtrl          = 6

kGoAction_PinTest                = 0
kGoAction_ConfigSystem           = 1
kGoAction_MemRegs                = 2
kGoAction_RwTest                 = 3
kGoAction_PerfTest               = 4
kGoAction_StressTest             = 5

kButtonColor_Enable  = "rgb(142,229,238)"
kButtonColor_Disable = "rgb(248,248,255)"
