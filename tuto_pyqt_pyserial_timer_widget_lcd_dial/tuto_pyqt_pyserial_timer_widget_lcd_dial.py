# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
#
# Created: Sun Mar  3 11:23:16 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(570, 335)
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(340, 15, 221, 91))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 127);\n"
"color: rgb(85, 170, 0);"))
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.dial = QtGui.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(190, 10, 141, 121))
        self.dial.setMaximum(250)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.pushButtonGO = QtGui.QPushButton(Form)
        self.pushButtonGO.setGeometry(QtCore.QRect(340, 115, 110, 51))
        self.pushButtonGO.setObjectName(_fromUtf8("pushButtonGO"))
        self.pushButtonSTOP = QtGui.QPushButton(Form)
        self.pushButtonSTOP.setGeometry(QtCore.QRect(450, 115, 110, 51))
        self.pushButtonSTOP.setObjectName(_fromUtf8("pushButtonSTOP"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 135, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.labelPort = QtGui.QLabel(Form)
        self.labelPort.setGeometry(QtCore.QRect(5, 10, 101, 16))
        self.labelPort.setObjectName(_fromUtf8("labelPort"))
        self.labelReception = QtGui.QLabel(Form)
        self.labelReception.setGeometry(QtCore.QRect(5, 200, 191, 16))
        self.labelReception.setObjectName(_fromUtf8("labelReception"))
        self.labelFinLigne = QtGui.QLabel(Form)
        self.labelFinLigne.setGeometry(QtCore.QRect(5, 150, 71, 16))
        self.labelFinLigne.setObjectName(_fromUtf8("labelFinLigne"))
        self.comboBoxDebit = QtGui.QComboBox(Form)
        self.comboBoxDebit.setGeometry(QtCore.QRect(5, 70, 121, 24))
        self.comboBoxDebit.setObjectName(_fromUtf8("comboBoxDebit"))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.comboBoxDebit.addItem(_fromUtf8(""))
        self.pushButtonInitSerial = QtGui.QPushButton(Form)
        self.pushButtonInitSerial.setGeometry(QtCore.QRect(130, 10, 41, 51))
        self.pushButtonInitSerial.setObjectName(_fromUtf8("pushButtonInitSerial"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(5, 190, 556, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.textEditReception = QtGui.QTextEdit(Form)
        self.textEditReception.setGeometry(QtCore.QRect(5, 220, 266, 106))
        self.textEditReception.setStyleSheet(_fromUtf8("background-color: rgb(244, 255, 190);"))
        self.textEditReception.setObjectName(_fromUtf8("textEditReception"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(5, 95, 166, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButtonEnvoi = QtGui.QPushButton(Form)
        self.pushButtonEnvoi.setGeometry(QtCore.QRect(130, 150, 41, 41))
        self.pushButtonEnvoi.setObjectName(_fromUtf8("pushButtonEnvoi"))
        self.lineEditChaineEnvoi = QtGui.QLineEdit(Form)
        self.lineEditChaineEnvoi.setGeometry(QtCore.QRect(5, 125, 166, 23))
        self.lineEditChaineEnvoi.setText(_fromUtf8(""))
        self.lineEditChaineEnvoi.setObjectName(_fromUtf8("lineEditChaineEnvoi"))
        self.comboBoxFinLigne = QtGui.QComboBox(Form)
        self.comboBoxFinLigne.setGeometry(QtCore.QRect(5, 165, 121, 24))
        self.comboBoxFinLigne.setObjectName(_fromUtf8("comboBoxFinLigne"))
        self.comboBoxFinLigne.addItem(_fromUtf8(""))
        self.comboBoxFinLigne.addItem(_fromUtf8(""))
        self.comboBoxFinLigne.addItem(_fromUtf8(""))
        self.comboBoxFinLigne.addItem(_fromUtf8(""))
        self.labelDebit = QtGui.QLabel(Form)
        self.labelDebit.setGeometry(QtCore.QRect(5, 55, 111, 16))
        self.labelDebit.setObjectName(_fromUtf8("labelDebit"))
        self.pushButtonStop = QtGui.QPushButton(Form)
        self.pushButtonStop.setGeometry(QtCore.QRect(130, 65, 41, 31))
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.labelChaineEnvoi = QtGui.QLabel(Form)
        self.labelChaineEnvoi.setGeometry(QtCore.QRect(5, 110, 121, 16))
        self.labelChaineEnvoi.setObjectName(_fromUtf8("labelChaineEnvoi"))
        self.comboBoxPort = QtGui.QComboBox(Form)
        self.comboBoxPort.setGeometry(QtCore.QRect(5, 25, 121, 24))
        self.comboBoxPort.setEditable(True)
        self.comboBoxPort.setObjectName(_fromUtf8("comboBoxPort"))
        self.comboBoxPort.addItem(_fromUtf8(""))
        self.comboBoxPort.addItem(_fromUtf8(""))
        self.comboBoxPort.addItem(_fromUtf8(""))
        self.comboBoxPort.addItem(_fromUtf8(""))
        self.textEditTraceEnvoiSerie = QtGui.QTextEdit(Form)
        self.textEditTraceEnvoiSerie.setGeometry(QtCore.QRect(285, 220, 276, 106))
        self.textEditTraceEnvoiSerie.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"background-color: rgb(170, 255, 255);"))
        self.textEditTraceEnvoiSerie.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEditTraceEnvoiSerie.setObjectName(_fromUtf8("textEditTraceEnvoiSerie"))
        self.labelTraceEnvoiSerie = QtGui.QLabel(Form)
        self.labelTraceEnvoiSerie.setGeometry(QtCore.QRect(285, 200, 191, 16))
        self.labelTraceEnvoiSerie.setObjectName(_fromUtf8("labelTraceEnvoiSerie"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(175, 10, 16, 186))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(270, 205, 16, 121))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.lineEditChaineEnvoiGO = QtGui.QLineEdit(Form)
        self.lineEditChaineEnvoiGO.setGeometry(QtCore.QRect(225, 170, 146, 23))
        self.lineEditChaineEnvoiGO.setObjectName(_fromUtf8("lineEditChaineEnvoiGO"))
        self.labelChaineEnvoiGO = QtGui.QLabel(Form)
        self.labelChaineEnvoiGO.setGeometry(QtCore.QRect(195, 175, 36, 16))
        self.labelChaineEnvoiGO.setObjectName(_fromUtf8("labelChaineEnvoiGO"))
        self.labelChaineEnvoiSTOP = QtGui.QLabel(Form)
        self.labelChaineEnvoiSTOP.setGeometry(QtCore.QRect(380, 175, 36, 16))
        self.labelChaineEnvoiSTOP.setObjectName(_fromUtf8("labelChaineEnvoiSTOP"))
        self.lineEditChaineEnvoiSTOP = QtGui.QLineEdit(Form)
        self.lineEditChaineEnvoiSTOP.setGeometry(QtCore.QRect(415, 170, 146, 23))
        self.lineEditChaineEnvoiSTOP.setObjectName(_fromUtf8("lineEditChaineEnvoiSTOP"))

        self.retranslateUi(Form)
        self.comboBoxFinLigne.setCurrentIndex(1)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "PyQt + PySerial : Timer + widget LCD + Dial : Minuterie", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGO.setText(QtGui.QApplication.translate("Form", "GO !", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSTOP.setText(QtGui.QApplication.translate("Form", "STOP", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Durée (secondes)", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPort.setText(QtGui.QApplication.translate("Form", "Port Série :", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReception.setText(QtGui.QApplication.translate("Form", "Réception sur le port série : ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFinLigne.setText(QtGui.QApplication.translate("Form", "Fin de ligne :", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(0, QtGui.QApplication.translate("Form", "115200", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(1, QtGui.QApplication.translate("Form", "57600", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(2, QtGui.QApplication.translate("Form", "38400", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(3, QtGui.QApplication.translate("Form", "28800", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(4, QtGui.QApplication.translate("Form", "19200", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(5, QtGui.QApplication.translate("Form", "14400", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(6, QtGui.QApplication.translate("Form", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDebit.setItemText(7, QtGui.QApplication.translate("Form", "4800", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonInitSerial.setText(QtGui.QApplication.translate("Form", "Init", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnvoi.setText(QtGui.QApplication.translate("Form", "Envoi", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFinLigne.setItemText(0, QtGui.QApplication.translate("Form", "Rien", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFinLigne.setItemText(1, QtGui.QApplication.translate("Form", "Saut de ligne (\\n = LF)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFinLigne.setItemText(2, QtGui.QApplication.translate("Form", "Retour Chariot (\\r = CR)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFinLigne.setItemText(3, QtGui.QApplication.translate("Form", "Les 2 (LF + CR)", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDebit.setText(QtGui.QApplication.translate("Form", "Débit Série (bauds) :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStop.setText(QtGui.QApplication.translate("Form", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChaineEnvoi.setText(QtGui.QApplication.translate("Form", "Chaîne à envoyer :", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPort.setItemText(0, QtGui.QApplication.translate("Form", "/dev/ttyACM0", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPort.setItemText(1, QtGui.QApplication.translate("Form", "/dev/ttyACM1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPort.setItemText(2, QtGui.QApplication.translate("Form", "/dev/ttyUSB0", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxPort.setItemText(3, QtGui.QApplication.translate("Form", "/dev/ttyUSB1", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTraceEnvoiSerie.setText(QtGui.QApplication.translate("Form", "Envoi sur le port série : ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditChaineEnvoiGO.setText(QtGui.QApplication.translate("Form", "LED=ON", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChaineEnvoiGO.setText(QtGui.QApplication.translate("Form", "GO :", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChaineEnvoiSTOP.setText(QtGui.QApplication.translate("Form", "STOP:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditChaineEnvoiSTOP.setText(QtGui.QApplication.translate("Form", "LED=OFF", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

