# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\COZMET\Desktop\todoPyQt\FournisseurImprimerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FournisseurImprimerWidget(object):
    def setupUi(self, FournisseurImprimerWidget):
        FournisseurImprimerWidget.setObjectName("FournisseurImprimerWidget")
        FournisseurImprimerWidget.resize(716, 600)
        self.label = QtWidgets.QLabel(FournisseurImprimerWidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 441, 16))
        self.label.setObjectName("label")

        self.retranslateUi(FournisseurImprimerWidget)
        QtCore.QMetaObject.connectSlotsByName(FournisseurImprimerWidget)

    def retranslateUi(self, FournisseurImprimerWidget):
        _translate = QtCore.QCoreApplication.translate
        FournisseurImprimerWidget.setWindowTitle(_translate("FournisseurImprimerWidget", "FournisseurImprimetWidget"))
        self.label.setText(_translate("FournisseurImprimerWidget", "Les données de la base de donnée sont enregistrées dans la fieulle exel fournisseur.xlsx"))
