# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github_repo_jay\MCU-MemTestUtility\gui\Stress-Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stressTestDialog(object):
    def setupUi(self, stressTestDialog):
        stressTestDialog.setObjectName("stressTestDialog")
        stressTestDialog.resize(353, 267)
        self.label_testSet = QtWidgets.QLabel(stressTestDialog)
        self.label_testSet.setGeometry(QtCore.QRect(20, 20, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_testSet.setFont(font)
        self.label_testSet.setObjectName("label_testSet")
        self.label_numOfRuns = QtWidgets.QLabel(stressTestDialog)
        self.label_numOfRuns.setGeometry(QtCore.QRect(20, 50, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_numOfRuns.setFont(font)
        self.label_numOfRuns.setObjectName("label_numOfRuns")
        self.comboBox_testSet = QtWidgets.QComboBox(stressTestDialog)
        self.comboBox_testSet.setGeometry(QtCore.QRect(140, 20, 191, 20))
        self.comboBox_testSet.setObjectName("comboBox_testSet")
        self.comboBox_testSet.addItem("")
        self.pushButton_ok = QtWidgets.QPushButton(stressTestDialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(80, 210, 75, 31))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(stressTestDialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(210, 210, 75, 31))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.lineEdit_numOfRuns = QtWidgets.QLineEdit(stressTestDialog)
        self.lineEdit_numOfRuns.setGeometry(QtCore.QRect(140, 50, 191, 20))
        self.lineEdit_numOfRuns.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_numOfRuns.setObjectName("lineEdit_numOfRuns")
        self.label_stopWhenFail = QtWidgets.QLabel(stressTestDialog)
        self.label_stopWhenFail.setGeometry(QtCore.QRect(20, 80, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_stopWhenFail.setFont(font)
        self.label_stopWhenFail.setObjectName("label_stopWhenFail")
        self.label_testMemStart = QtWidgets.QLabel(stressTestDialog)
        self.label_testMemStart.setGeometry(QtCore.QRect(20, 110, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_testMemStart.setFont(font)
        self.label_testMemStart.setObjectName("label_testMemStart")
        self.label_testMemSize = QtWidgets.QLabel(stressTestDialog)
        self.label_testMemSize.setGeometry(QtCore.QRect(20, 140, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_testMemSize.setFont(font)
        self.label_testMemSize.setObjectName("label_testMemSize")
        self.label_testPageSize = QtWidgets.QLabel(stressTestDialog)
        self.label_testPageSize.setGeometry(QtCore.QRect(20, 170, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_testPageSize.setFont(font)
        self.label_testPageSize.setObjectName("label_testPageSize")
        self.lineEdit_testMemSize = QtWidgets.QLineEdit(stressTestDialog)
        self.lineEdit_testMemSize.setGeometry(QtCore.QRect(140, 140, 191, 20))
        self.lineEdit_testMemSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_testMemSize.setObjectName("lineEdit_testMemSize")
        self.lineEdit_testPageSize = QtWidgets.QLineEdit(stressTestDialog)
        self.lineEdit_testPageSize.setGeometry(QtCore.QRect(140, 170, 191, 20))
        self.lineEdit_testPageSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_testPageSize.setObjectName("lineEdit_testPageSize")
        self.lineEdit_testMemStart = QtWidgets.QLineEdit(stressTestDialog)
        self.lineEdit_testMemStart.setGeometry(QtCore.QRect(140, 110, 191, 20))
        self.lineEdit_testMemStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_testMemStart.setObjectName("lineEdit_testMemStart")
        self.comboBox_stopWhenFail = QtWidgets.QComboBox(stressTestDialog)
        self.comboBox_stopWhenFail.setGeometry(QtCore.QRect(140, 80, 191, 20))
        self.comboBox_stopWhenFail.setObjectName("comboBox_stopWhenFail")
        self.comboBox_stopWhenFail.addItem("")
        self.comboBox_stopWhenFail.addItem("")

        self.retranslateUi(stressTestDialog)
        QtCore.QMetaObject.connectSlotsByName(stressTestDialog)

    def retranslateUi(self, stressTestDialog):
        _translate = QtCore.QCoreApplication.translate
        stressTestDialog.setWindowTitle(_translate("stressTestDialog", "Dialog"))
        self.label_testSet.setText(_translate("stressTestDialog", "Test Set:"))
        self.label_numOfRuns.setText(_translate("stressTestDialog", "Iterations:"))
        self.comboBox_testSet.setItemText(0, _translate("stressTestDialog", "memtester"))
        self.pushButton_ok.setText(_translate("stressTestDialog", "Ok"))
        self.pushButton_cancel.setText(_translate("stressTestDialog", "Cancel"))
        self.lineEdit_numOfRuns.setText(_translate("stressTestDialog", "1"))
        self.label_stopWhenFail.setText(_translate("stressTestDialog", "Stop When Fail:"))
        self.label_testMemStart.setText(_translate("stressTestDialog", "Test MEM start:"))
        self.label_testMemSize.setText(_translate("stressTestDialog", "Test MEM size:"))
        self.label_testPageSize.setText(_translate("stressTestDialog", "Test Page size:"))
        self.lineEdit_testMemSize.setText(_translate("stressTestDialog", "0x80000"))
        self.lineEdit_testPageSize.setText(_translate("stressTestDialog", "0x400"))
        self.lineEdit_testMemStart.setText(_translate("stressTestDialog", "0x60000000"))
        self.comboBox_stopWhenFail.setItemText(0, _translate("stressTestDialog", "Yes"))
        self.comboBox_stopWhenFail.setItemText(1, _translate("stressTestDialog", "No"))
