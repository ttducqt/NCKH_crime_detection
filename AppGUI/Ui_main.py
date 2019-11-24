# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hello/Desktop/deep learnig/NCKH_Crime_Detector/AppGUI/main.ui',
# licensing of '/home/hello/Desktop/deep learnig/NCKH_Crime_Detector/AppGUI/main.ui' applies.
#
# Created: Sun Nov 24 12:08:42 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1358, 637)
        self.safeButton = QtWidgets.QPushButton(Form)
        self.safeButton.setGeometry(QtCore.QRect(860, 430, 89, 25))
        self.safeButton.setObjectName("safeButton")
        self.source_camLabel = QtWidgets.QLabel(Form)
        self.source_camLabel.setGeometry(QtCore.QRect(10, 500, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.source_camLabel.setFont(font)
        self.source_camLabel.setObjectName("source_camLabel")
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setGeometry(QtCore.QRect(10, 570, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.safeStatus = QtWidgets.QLabel(Form)
        self.safeStatus.setGeometry(QtCore.QRect(210, 550, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.safeStatus.setFont(font)
        self.safeStatus.setStyleSheet("border-image: url(/home/hello/Desktop/deep learnig/NCKH_Crime_Detector/AppGUI/resource/safe.png);")
        self.safeStatus.setText("")
        self.safeStatus.setObjectName("safeStatus")
        self.warningStatus = QtWidgets.QLabel(Form)
        self.warningStatus.setGeometry(QtCore.QRect(300, 550, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.warningStatus.setFont(font)
        self.warningStatus.setStyleSheet("border-image: url(/home/hello/Desktop/deep learnig/NCKH_Crime_Detector/AppGUI/resource/warning.png);")
        self.warningStatus.setText("")
        self.warningStatus.setObjectName("warningStatus")
        self.alertStatus = QtWidgets.QLabel(Form)
        self.alertStatus.setGeometry(QtCore.QRect(400, 550, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.alertStatus.setFont(font)
        self.alertStatus.setStyleSheet("border-image: url(/home/hello/Desktop/deep learnig/NCKH_Crime_Detector/AppGUI/resource/alert.png)")
        self.alertStatus.setText("")
        self.alertStatus.setObjectName("alertStatus")
        self.info_camLabel = QtWidgets.QLabel(Form)
        self.info_camLabel.setGeometry(QtCore.QRect(210, 500, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.info_camLabel.setFont(font)
        self.info_camLabel.setStyleSheet("")
        self.info_camLabel.setText("")
        self.info_camLabel.setObjectName("info_camLabel")
        self.warnButton = QtWidgets.QPushButton(Form)
        self.warnButton.setGeometry(QtCore.QRect(860, 470, 89, 25))
        self.warnButton.setObjectName("warnButton")
        self.alertButton = QtWidgets.QPushButton(Form)
        self.alertButton.setGeometry(QtCore.QRect(860, 500, 89, 25))
        self.alertButton.setObjectName("alertButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(790, 370, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.safeButton.setText(QtWidgets.QApplication.translate("Form", "safe", None, -1))
        self.source_camLabel.setText(QtWidgets.QApplication.translate("Form", "Source camera:", None, -1))
        self.statusLabel.setText(QtWidgets.QApplication.translate("Form", "Status:", None, -1))
        self.warnButton.setText(QtWidgets.QApplication.translate("Form", "warn", None, -1))
        self.alertButton.setText(QtWidgets.QApplication.translate("Form", "alert", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))

