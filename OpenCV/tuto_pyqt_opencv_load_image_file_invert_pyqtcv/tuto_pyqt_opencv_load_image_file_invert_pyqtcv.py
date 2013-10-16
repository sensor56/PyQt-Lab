# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
#
# Created: Tue Oct 15 16:11:17 2013
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
        Form.resize(655, 276)
        self.labelImageSrc = QtGui.QLabel(Form)
        self.labelImageSrc.setGeometry(QtCore.QRect(2, 2, 320, 240))
        self.labelImageSrc.setFrameShape(QtGui.QFrame.Box)
        self.labelImageSrc.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelImageSrc.setText(_fromUtf8(""))
        self.labelImageSrc.setObjectName(_fromUtf8("labelImageSrc"))
        self.pushButtonOuvrir = QtGui.QPushButton(Form)
        self.pushButtonOuvrir.setGeometry(QtCore.QRect(595, 250, 51, 21))
        self.pushButtonOuvrir.setObjectName(_fromUtf8("pushButtonOuvrir"))
        self.lineEditChemin = QtGui.QLineEdit(Form)
        self.lineEditChemin.setGeometry(QtCore.QRect(0, 250, 591, 23))
        self.lineEditChemin.setObjectName(_fromUtf8("lineEditChemin"))
        self.labelImageOut = QtGui.QLabel(Form)
        self.labelImageOut.setGeometry(QtCore.QRect(330, 2, 320, 240))
        self.labelImageOut.setFrameShape(QtGui.QFrame.Box)
        self.labelImageOut.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelImageOut.setText(_fromUtf8(""))
        self.labelImageOut.setObjectName(_fromUtf8("labelImageOut"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "load Image File- Image Source et Sortie", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOuvrir.setText(QtGui.QApplication.translate("Form", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

