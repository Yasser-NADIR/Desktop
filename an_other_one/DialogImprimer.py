# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogImprimer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogImprimer(object):
    def setupUi(self, DialogImprimer):
        DialogImprimer.setObjectName("DialogImprimer")
        DialogImprimer.resize(177, 81)
        DialogImprimer.setMinimumSize(QtCore.QSize(177, 81))
        DialogImprimer.setMaximumSize(QtCore.QSize(177, 81))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogImprimer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonPDF = QtWidgets.QRadioButton(DialogImprimer)
        self.radioButtonPDF.setObjectName("radioButtonPDF")
        self.horizontalLayout.addWidget(self.radioButtonPDF)
        self.radioButtonWord = QtWidgets.QRadioButton(DialogImprimer)
        self.radioButtonWord.setObjectName("radioButtonWord")
        self.horizontalLayout.addWidget(self.radioButtonWord)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonImprimer = QtWidgets.QPushButton(DialogImprimer)
        self.pushButtonImprimer.setObjectName("pushButtonImprimer")
        self.verticalLayout.addWidget(self.pushButtonImprimer)

        self.retranslateUi(DialogImprimer)
        QtCore.QMetaObject.connectSlotsByName(DialogImprimer)

    def retranslateUi(self, DialogImprimer):
        _translate = QtCore.QCoreApplication.translate
        DialogImprimer.setWindowTitle(_translate("DialogImprimer", "Impression"))
        self.radioButtonPDF.setText(_translate("DialogImprimer", "pdf"))
        self.radioButtonWord.setText(_translate("DialogImprimer", "word"))
        self.pushButtonImprimer.setText(_translate("DialogImprimer", "Imprimer"))
