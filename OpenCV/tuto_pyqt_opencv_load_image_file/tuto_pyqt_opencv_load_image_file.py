# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
#
# Created: Wed Dec 12 08:30:14 2012
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
        Form.resize(337, 295)
        self.labelImage = QtGui.QLabel(Form)
        self.labelImage.setGeometry(QtCore.QRect(10, 10, 320, 240))
        self.labelImage.setFrameShape(QtGui.QFrame.Box)
        self.labelImage.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelImage.setText(_fromUtf8(""))
        self.labelImage.setObjectName(_fromUtf8("labelImage"))
        self.pushButtonOuvrir = QtGui.QPushButton(Form)
        self.pushButtonOuvrir.setGeometry(QtCore.QRect(280, 260, 51, 27))
        self.pushButtonOuvrir.setObjectName(_fromUtf8("pushButtonOuvrir"))
        self.lineEditChemin = QtGui.QLineEdit(Form)
        self.lineEditChemin.setGeometry(QtCore.QRect(10, 260, 261, 23))
        self.lineEditChemin.setObjectName(_fromUtf8("lineEditChemin"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "load Image File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOuvrir.setText(QtGui.QApplication.translate("Form", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

