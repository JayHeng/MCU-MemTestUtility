# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_repo_jay\MCU-MemTestUtility\gui\Connection-Configuration.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_connCfgDialog(object):
    def setupUi(self, connCfgDialog):
        connCfgDialog.setObjectName("connCfgDialog")
        connCfgDialog.resize(419, 388)
        self.label_instance = QtWidgets.QLabel(connCfgDialog)
        self.label_instance.setGeometry(QtCore.QRect(20, 20, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_instance.setFont(font)
        self.label_instance.setObjectName("label_instance")
        self.comboBox_instance = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_instance.setGeometry(QtCore.QRect(110, 20, 291, 20))
        self.comboBox_instance.setObjectName("comboBox_instance")
        self.comboBox_instance.addItem("")
        self.comboBox_instance.addItem("")
        self.label_dataL4b = QtWidgets.QLabel(connCfgDialog)
        self.label_dataL4b.setGeometry(QtCore.QRect(20, 50, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dataL4b.setFont(font)
        self.label_dataL4b.setObjectName("label_dataL4b")
        self.label_dataH4b = QtWidgets.QLabel(connCfgDialog)
        self.label_dataH4b.setGeometry(QtCore.QRect(20, 80, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dataH4b.setFont(font)
        self.label_dataH4b.setObjectName("label_dataH4b")
        self.label_ssb = QtWidgets.QLabel(connCfgDialog)
        self.label_ssb.setGeometry(QtCore.QRect(20, 140, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ssb.setFont(font)
        self.label_ssb.setObjectName("label_ssb")
        self.label_sclk = QtWidgets.QLabel(connCfgDialog)
        self.label_sclk.setGeometry(QtCore.QRect(20, 170, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_sclk.setFont(font)
        self.label_sclk.setObjectName("label_sclk")
        self.label_dqs0 = QtWidgets.QLabel(connCfgDialog)
        self.label_dqs0.setGeometry(QtCore.QRect(20, 230, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dqs0.setFont(font)
        self.label_dqs0.setObjectName("label_dqs0")
        self.label_sclkn = QtWidgets.QLabel(connCfgDialog)
        self.label_sclkn.setGeometry(QtCore.QRect(20, 200, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_sclkn.setFont(font)
        self.label_sclkn.setObjectName("label_sclkn")
        self.label_rstb = QtWidgets.QLabel(connCfgDialog)
        self.label_rstb.setGeometry(QtCore.QRect(20, 290, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rstb.setFont(font)
        self.label_rstb.setObjectName("label_rstb")
        self.comboBox_dataL4b = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_dataL4b.setGeometry(QtCore.QRect(110, 50, 291, 20))
        self.comboBox_dataL4b.setObjectName("comboBox_dataL4b")
        self.comboBox_dataL4b.addItem("")
        self.comboBox_dataL4b.addItem("")
        self.comboBox_dataL4b.addItem("")
        self.comboBox_dataL4b.addItem("")
        self.comboBox_dataH4b = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_dataH4b.setGeometry(QtCore.QRect(110, 80, 291, 20))
        self.comboBox_dataH4b.setObjectName("comboBox_dataH4b")
        self.comboBox_dataH4b.addItem("")
        self.comboBox_dataH4b.addItem("")
        self.comboBox_dataH4b.addItem("")
        self.comboBox_ssb = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_ssb.setGeometry(QtCore.QRect(110, 140, 291, 20))
        self.comboBox_ssb.setObjectName("comboBox_ssb")
        self.comboBox_ssb.addItem("")
        self.comboBox_ssb.addItem("")
        self.comboBox_ssb.addItem("")
        self.comboBox_ssb.addItem("")
        self.comboBox_ssb.addItem("")
        self.comboBox_ssb.addItem("")
        self.comboBox_sclk = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_sclk.setGeometry(QtCore.QRect(110, 170, 291, 20))
        self.comboBox_sclk.setObjectName("comboBox_sclk")
        self.comboBox_sclk.addItem("")
        self.comboBox_sclk.addItem("")
        self.comboBox_sclk.addItem("")
        self.comboBox_sclk.addItem("")
        self.comboBox_dqs0 = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_dqs0.setGeometry(QtCore.QRect(110, 230, 291, 20))
        self.comboBox_dqs0.setObjectName("comboBox_dqs0")
        self.comboBox_dqs0.addItem("")
        self.comboBox_dqs0.addItem("")
        self.comboBox_dqs0.addItem("")
        self.comboBox_dqs0.addItem("")
        self.comboBox_sclkn = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_sclkn.setGeometry(QtCore.QRect(110, 200, 291, 20))
        self.comboBox_sclkn.setObjectName("comboBox_sclkn")
        self.comboBox_sclkn.addItem("")
        self.comboBox_sclkn.addItem("")
        self.comboBox_sclkn.addItem("")
        self.comboBox_rstb = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_rstb.setGeometry(QtCore.QRect(110, 290, 291, 20))
        self.comboBox_rstb.setObjectName("comboBox_rstb")
        self.comboBox_rstb.addItem("")
        self.comboBox_rstb.addItem("")
        self.comboBox_rstb.addItem("")
        self.pushButton_ok = QtWidgets.QPushButton(connCfgDialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(90, 330, 75, 31))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(connCfgDialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 330, 75, 31))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.comboBox_dataT8b = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_dataT8b.setGeometry(QtCore.QRect(110, 110, 291, 20))
        self.comboBox_dataT8b.setObjectName("comboBox_dataT8b")
        self.comboBox_dataT8b.addItem("")
        self.label_dataT8b = QtWidgets.QLabel(connCfgDialog)
        self.label_dataT8b.setGeometry(QtCore.QRect(20, 110, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dataT8b.setFont(font)
        self.label_dataT8b.setObjectName("label_dataT8b")
        self.label_dqs1 = QtWidgets.QLabel(connCfgDialog)
        self.label_dqs1.setGeometry(QtCore.QRect(20, 260, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dqs1.setFont(font)
        self.label_dqs1.setObjectName("label_dqs1")
        self.comboBox_dqs1 = QtWidgets.QComboBox(connCfgDialog)
        self.comboBox_dqs1.setGeometry(QtCore.QRect(110, 260, 291, 20))
        self.comboBox_dqs1.setObjectName("comboBox_dqs1")
        self.comboBox_dqs1.addItem("")

        self.retranslateUi(connCfgDialog)
        QtCore.QMetaObject.connectSlotsByName(connCfgDialog)

    def retranslateUi(self, connCfgDialog):
        _translate = QtCore.QCoreApplication.translate
        connCfgDialog.setWindowTitle(_translate("connCfgDialog", "Dialog"))
        self.label_instance.setText(_translate("connCfgDialog", "Instance:"))
        self.comboBox_instance.setItemText(0, _translate("connCfgDialog", "1"))
        self.comboBox_instance.setItemText(1, _translate("connCfgDialog", "2"))
        self.label_dataL4b.setText(_translate("connCfgDialog", "DATA_L4B:"))
        self.label_dataH4b.setText(_translate("connCfgDialog", "DATA_H4B:"))
        self.label_ssb.setText(_translate("connCfgDialog", "SS_B:"))
        self.label_sclk.setText(_translate("connCfgDialog", "SCLK:"))
        self.label_dqs0.setText(_translate("connCfgDialog", "DQS/RWDS0:"))
        self.label_sclkn.setText(_translate("connCfgDialog", "SCLK_N:"))
        self.label_rstb.setText(_translate("connCfgDialog", "RST_B:"))
        self.comboBox_dataL4b.setItemText(0, _translate("connCfgDialog", "PortA_DATA[3:0] - GPIO_SD_B2[11:8]"))
        self.comboBox_dataL4b.setItemText(1, _translate("connCfgDialog", "PortA_DATA[3:0] - GPIO_AD[23:20]"))
        self.comboBox_dataL4b.setItemText(2, _translate("connCfgDialog", "PortB_DATA[3:0] - GPIO_SD_B2[3:0]"))
        self.comboBox_dataL4b.setItemText(3, _translate("connCfgDialog", "PortB_DATA[3:0] - GPIO_AD[15:12]"))
        self.comboBox_dataH4b.setItemText(0, _translate("connCfgDialog", "None"))
        self.comboBox_dataH4b.setItemText(1, _translate("connCfgDialog", "PortB_DATA[3:0] - GPIO_SD_B2[3:0]"))
        self.comboBox_dataH4b.setItemText(2, _translate("connCfgDialog", "PortB_DATA[3:0] - GPIO_AD[15:12]"))
        self.comboBox_ssb.setItemText(0, _translate("connCfgDialog", "PortA_SS0_B - GPIO_SD_B2[6]"))
        self.comboBox_ssb.setItemText(1, _translate("connCfgDialog", "PortA_SS0_B - GPIO_AD[18]"))
        self.comboBox_ssb.setItemText(2, _translate("connCfgDialog", "PortA_SS1_B - GPIO_SD_B1[2]"))
        self.comboBox_ssb.setItemText(3, _translate("connCfgDialog", "PortB_SS0_B - GPIO_SD_B1[4]"))
        self.comboBox_ssb.setItemText(4, _translate("connCfgDialog", "PortB_SS1_B - GPIO_AD[35]"))
        self.comboBox_ssb.setItemText(5, _translate("connCfgDialog", "PortB_SS1_B - GPIO_SD_B1[3]"))
        self.comboBox_sclk.setItemText(0, _translate("connCfgDialog", "PortA_SCLK - GPIO_SD_B2[7]"))
        self.comboBox_sclk.setItemText(1, _translate("connCfgDialog", "PortA_SCLK - GPIO_AD[19]"))
        self.comboBox_sclk.setItemText(2, _translate("connCfgDialog", "PortB_SCLK - GPIO_SD_B2[4]"))
        self.comboBox_sclk.setItemText(3, _translate("connCfgDialog", "PortB_SCLK - GPIO_AD[16]"))
        self.comboBox_dqs0.setItemText(0, _translate("connCfgDialog", "PortA_DQS - GPIO_SD_B2[5]"))
        self.comboBox_dqs0.setItemText(1, _translate("connCfgDialog", "PortA_DQS - GPIO_AD[17]"))
        self.comboBox_dqs0.setItemText(2, _translate("connCfgDialog", "PortA_DQS - GPIO_EMC_B2[18]"))
        self.comboBox_dqs0.setItemText(3, _translate("connCfgDialog", "PortB_DQS - GPIO_SD_B1[5]"))
        self.comboBox_sclkn.setItemText(0, _translate("connCfgDialog", "None"))
        self.comboBox_sclkn.setItemText(1, _translate("connCfgDialog", "PortB_SCLKN - GPIO_SD_B2[4]"))
        self.comboBox_sclkn.setItemText(2, _translate("connCfgDialog", "PortB_SCLKN - GPIO_AD[16]"))
        self.comboBox_rstb.setItemText(0, _translate("connCfgDialog", "None"))
        self.comboBox_rstb.setItemText(1, _translate("connCfgDialog", "RST_B - GPIO_SD_B1[0]"))
        self.comboBox_rstb.setItemText(2, _translate("connCfgDialog", "RST_B - GPIO_EMC_B1[40]"))
        self.pushButton_ok.setText(_translate("connCfgDialog", "Ok"))
        self.pushButton_cancel.setText(_translate("connCfgDialog", "Cancel"))
        self.comboBox_dataT8b.setItemText(0, _translate("connCfgDialog", "None"))
        self.label_dataT8b.setText(_translate("connCfgDialog", "DATA_T8B:"))
        self.label_dqs1.setText(_translate("connCfgDialog", "DQS/RWDS1:"))
        self.comboBox_dqs1.setItemText(0, _translate("connCfgDialog", "None"))
