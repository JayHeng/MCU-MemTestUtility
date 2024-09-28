# MCU-MemTestUtility
A powerful memory validation tool based on Python3.7.9+PyQt5.15.1, it can do Flash/HyperRAM/PSRAM functional/performance tests on NXP MCU (i.MXRT...) | 恩智浦MCU外部存储器性能测试一站式工具

### 1. 使用步骤
```text
1. 打开 MCU-MemTestUtility 软件
2. 下拉菜单选择 'MCU Device'
3. 将 PC 与目标 MCU 板卡通过指定的串口（ROM ISP UART）连接，MCU 应处于 ISP 模式
4. 点击 'Connect' 按钮（加载 \src\targets\xxxDevice\boot_firmware.bin 到 MCU 内部 RAM 执行）
  - 菜单栏 Tools/Load Firmware 选项默认为 Yes，即自动加载 boot_firmware.bin；设为 No 则需手动在线调试运行 mtu_fw 工程
5. 点击 'FlexSPI Connection Configuration' 按钮选择当前连接外存的引脚组合

SubTest 1 - 引脚连通性测试：
  1.1 点击 'Pin Unittest' 按钮在弹出的界面里选择要测试的 GPIO 引脚
  1.2 点击 'Go' 按钮启动测试
```

### 附录、制作 boot_firmware.bin 步骤
```text
1. 打开 imxrt-flexspi-mem-fw 项目工程
2. 编译 \boards\mimxrt\mtu_fw 工程得到 boot_firmware.srec
3. 打开 NXP-MCUBootUtility 软件
  - 对于 RT10xx 系列，Boot Device 选择 EEPROM，Image File 输入 boot_firmware.srec，点击 'Generate Unsigned Bootable Image' 按钮得到 \gen\bootable_image\ivt_boot_firmware_unsigned_xxx.bin 即为 boot_firmware.bin（需要设置 writeFile, jumpAddress 命令地址）
  - 对于 RT1170 系列，Boot Device 选择 EEPROM，Image File 输入 boot_firmware.srec，点击 'Generate Unsigned Bootable Image' 按钮得到 \gen\bootable_image\ivt_boot_firmware_unsigned_nopadding.bin 即为 boot_firmware.bin（loadImage 命令直接解析开头 ivt，无需 Padding）
  - 对于 RT1180 系列，Boot Device 选择 FLEXSPI NOR，Image File 输入 boot_firmware.srec，点击 'Generate Unsigned Bootable Image' 按钮得到 \gen\bootable_image\container_boot_firmware_unsigned.bin 即为 boot_firmware.bin（loadImage 命令解析 container，开头需要 1KB Padding）
```
