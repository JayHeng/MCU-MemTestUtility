# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_repo_jay\MCU-MemTestUtility\gui\PadCtrl-RT11yy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_padCtrlRT11yyDialog(object):
    def setupUi(self, padCtrlRT11yyDialog):
        padCtrlRT11yyDialog.setObjectName("padCtrlRT11yyDialog")
        padCtrlRT11yyDialog.resize(454, 348)
        self.label_pull = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_pull.setGeometry(QtCore.QRect(20, 90, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_pull.setFont(font)
        self.label_pull.setObjectName("label_pull")
        self.label_dse = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_dse.setGeometry(QtCore.QRect(20, 230, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dse.setFont(font)
        self.label_dse.setObjectName("label_dse")
        self.label_ode = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_ode.setGeometry(QtCore.QRect(20, 40, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ode.setFont(font)
        self.label_ode.setObjectName("label_ode")
        self.label_sre = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_sre.setGeometry(QtCore.QRect(20, 260, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_sre.setFont(font)
        self.label_sre.setObjectName("label_sre")
        self.comboBox_pull = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_pull.setGeometry(QtCore.QRect(140, 90, 291, 20))
        self.comboBox_pull.setObjectName("comboBox_pull")
        self.comboBox_pull.addItem("")
        self.comboBox_pull.addItem("")
        self.comboBox_pull.addItem("")
        self.comboBox_pull.addItem("")
        self.comboBox_dse = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_dse.setGeometry(QtCore.QRect(140, 230, 291, 20))
        self.comboBox_dse.setObjectName("comboBox_dse")
        self.comboBox_dse.addItem("")
        self.comboBox_dse.addItem("")
        self.comboBox_ode = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_ode.setGeometry(QtCore.QRect(140, 40, 291, 20))
        self.comboBox_ode.setObjectName("comboBox_ode")
        self.comboBox_ode.addItem("")
        self.comboBox_ode.addItem("")
        self.comboBox_sre = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_sre.setGeometry(QtCore.QRect(140, 260, 291, 20))
        self.comboBox_sre.setObjectName("comboBox_sre")
        self.comboBox_sre.addItem("")
        self.comboBox_sre.addItem("")
        self.pushButton_ok = QtWidgets.QPushButton(padCtrlRT11yyDialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(120, 300, 75, 31))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(padCtrlRT11yyDialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(270, 300, 75, 31))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_pdrv = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_pdrv.setGeometry(QtCore.QRect(20, 120, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_pdrv.setFont(font)
        self.label_pdrv.setObjectName("label_pdrv")
        self.comboBox_pdrv = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_pdrv.setGeometry(QtCore.QRect(140, 120, 291, 20))
        self.comboBox_pdrv.setObjectName("comboBox_pdrv")
        self.comboBox_pdrv.addItem("")
        self.comboBox_pdrv.addItem("")
        self.label_field = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_field.setGeometry(QtCore.QRect(20, 10, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_field.setFont(font)
        self.label_field.setAutoFillBackground(True)
        self.label_field.setAlignment(QtCore.Qt.AlignCenter)
        self.label_field.setWordWrap(False)
        self.label_field.setObjectName("label_field")
        self.label_description = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_description.setGeometry(QtCore.QRect(140, 10, 281, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_description.setFont(font)
        self.label_description.setAutoFillBackground(True)
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setWordWrap(False)
        self.label_description.setObjectName("label_description")
        self.comboBox_pue = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_pue.setGeometry(QtCore.QRect(140, 200, 291, 20))
        self.comboBox_pue.setObjectName("comboBox_pue")
        self.comboBox_pue.addItem("")
        self.comboBox_pue.addItem("")
        self.comboBox_pus = QtWidgets.QComboBox(padCtrlRT11yyDialog)
        self.comboBox_pus.setGeometry(QtCore.QRect(140, 170, 291, 20))
        self.comboBox_pus.setObjectName("comboBox_pus")
        self.comboBox_pus.addItem("")
        self.comboBox_pus.addItem("")
        self.label_pue = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_pue.setGeometry(QtCore.QRect(20, 200, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_pue.setFont(font)
        self.label_pue.setObjectName("label_pue")
        self.label_pus = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_pus.setGeometry(QtCore.QRect(20, 170, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_pus.setFont(font)
        self.label_pus.setObjectName("label_pus")
        self.label_fieldC = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_fieldC.setGeometry(QtCore.QRect(20, 70, 411, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_fieldC.setFont(font)
        self.label_fieldC.setAutoFillBackground(True)
        self.label_fieldC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fieldC.setWordWrap(False)
        self.label_fieldC.setObjectName("label_fieldC")
        self.label_fieldA = QtWidgets.QLabel(padCtrlRT11yyDialog)
        self.label_fieldA.setGeometry(QtCore.QRect(20, 150, 411, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_fieldA.setFont(font)
        self.label_fieldA.setAutoFillBackground(True)
        self.label_fieldA.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fieldA.setWordWrap(False)
        self.label_fieldA.setObjectName("label_fieldA")

        self.retranslateUi(padCtrlRT11yyDialog)
        QtCore.QMetaObject.connectSlotsByName(padCtrlRT11yyDialog)

    def retranslateUi(self, padCtrlRT11yyDialog):
        _translate = QtCore.QCoreApplication.translate
        padCtrlRT11yyDialog.setWindowTitle(_translate("padCtrlRT11yyDialog", "Dialog"))
        self.label_pull.setText(_translate("padCtrlRT11yyDialog", "[03-02] - PULL"))
        self.label_dse.setText(_translate("padCtrlRT11yyDialog", "[01-01] - DSE"))
        self.label_ode.setText(_translate("padCtrlRT11yyDialog", "[04-04] - ODE"))
        self.label_sre.setText(_translate("padCtrlRT11yyDialog", "[00-00] - SRE"))
        self.comboBox_pull.setItemText(0, _translate("padCtrlRT11yyDialog", "00b - Forbidden"))
        self.comboBox_pull.setItemText(1, _translate("padCtrlRT11yyDialog", "01b - Internal pullup resistor enabled"))
        self.comboBox_pull.setItemText(2, _translate("padCtrlRT11yyDialog", "10b - Internal pulldown resistor enabled"))
        self.comboBox_pull.setItemText(3, _translate("padCtrlRT11yyDialog", "11b - No Pull"))
        self.comboBox_dse.setItemText(0, _translate("padCtrlRT11yyDialog", "0b - normal drive strength"))
        self.comboBox_dse.setItemText(1, _translate("padCtrlRT11yyDialog", "1b - high drive strength"))
        self.comboBox_ode.setItemText(0, _translate("padCtrlRT11yyDialog", "0b - Disabled"))
        self.comboBox_ode.setItemText(1, _translate("padCtrlRT11yyDialog", "1b - Enabled"))
        self.comboBox_sre.setItemText(0, _translate("padCtrlRT11yyDialog", "0b - Slow Slew Rate"))
        self.comboBox_sre.setItemText(1, _translate("padCtrlRT11yyDialog", "1b - Fast Slew Rate"))
        self.pushButton_ok.setText(_translate("padCtrlRT11yyDialog", "Ok"))
        self.pushButton_cancel.setText(_translate("padCtrlRT11yyDialog", "Cancel"))
        self.label_pdrv.setText(_translate("padCtrlRT11yyDialog", "[01-01] - PDRV"))
        self.comboBox_pdrv.setItemText(0, _translate("padCtrlRT11yyDialog", "0b - high drive strength"))
        self.comboBox_pdrv.setItemText(1, _translate("padCtrlRT11yyDialog", "1b - normal drive strength"))
        self.label_field.setText(_translate("padCtrlRT11yyDialog", "Field"))
        self.label_description.setText(_translate("padCtrlRT11yyDialog", "Description"))
        self.comboBox_pue.setItemText(0, _translate("padCtrlRT11yyDialog", "0b - Pull Disable"))
        self.comboBox_pue.setItemText(1, _translate("padCtrlRT11yyDialog", "1b - Pull Enable"))
        self.comboBox_pus.setItemText(0, _translate("padCtrlRT11yyDialog", "0b - Weak pull down"))
        self.comboBox_pus.setItemText(1, _translate("padCtrlRT11yyDialog", "1b - Weak pull up"))
        self.label_pue.setText(_translate("padCtrlRT11yyDialog", "[02-02] - PUE"))
        self.label_pus.setText(_translate("padCtrlRT11yyDialog", "[03-03] - PUS"))
        self.label_fieldC.setText(_translate("padCtrlRT11yyDialog", "Below feilds apply to GPIO_EMC_B1/B2, GPIO_SD_B1/B2, GPIO_B1/B2"))
        self.label_fieldA.setText(_translate("padCtrlRT11yyDialog", "Below feilds apply to GPIO_AD, GPIO_AON"))