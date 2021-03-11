# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\COZMET\Desktop\todoPyQt\FournisseurWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FounisseurValideWidget(object):
    def setupUi(self, FounisseurValideWidget):
        FounisseurValideWidget.setObjectName("FounisseurValideWidget")
        FounisseurValideWidget.resize(816, 665)
        self.layoutWidget = QtWidgets.QWidget(FounisseurValideWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 91, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonNouveau = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\COZMET\\Desktop\\todoPyQt\\Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNouveau.setIcon(icon)
        self.pushButtonNouveau.setObjectName("pushButtonNouveau")
        self.verticalLayout.addWidget(self.pushButtonNouveau)
        self.pushButtonValider = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonValider.setObjectName("pushButtonValider")
        self.verticalLayout.addWidget(self.pushButtonValider)
        self.pushButtonRechercher = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonRechercher.setObjectName("pushButtonRechercher")
        self.verticalLayout.addWidget(self.pushButtonRechercher)
        self.pushButtonDernier = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonDernier.setObjectName("pushButtonDernier")
        self.verticalLayout.addWidget(self.pushButtonDernier)
        self.pushButtonPremier = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonPremier.setObjectName("pushButtonPremier")
        self.verticalLayout.addWidget(self.pushButtonPremier)
        self.pushButtonDefilerArrier = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonDefilerArrier.setObjectName("pushButtonDefilerArrier")
        self.verticalLayout.addWidget(self.pushButtonDefilerArrier)
        self.pushButtonDefilerAvant = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonDefilerAvant.setObjectName("pushButtonDefilerAvant")
        self.verticalLayout.addWidget(self.pushButtonDefilerAvant)
        self.pushButtonAfficher = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonAfficher.setObjectName("pushButtonAfficher")
        self.verticalLayout.addWidget(self.pushButtonAfficher)
        self.pushButtonImprimer = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonImprimer.setObjectName("pushButtonImprimer")
        self.verticalLayout.addWidget(self.pushButtonImprimer)
        self.pushButtonSortir = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSortir.setObjectName("pushButtonSortir")
        self.verticalLayout.addWidget(self.pushButtonSortir)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widgetCentredFournisseur = QtWidgets.QWidget(FounisseurValideWidget)
        self.widgetCentredFournisseur.setGeometry(QtCore.QRect(110, 10, 681, 631))
        self.widgetCentredFournisseur.setObjectName("widgetCentredFournisseur")

        self.retranslateUi(FounisseurValideWidget)
        QtCore.QMetaObject.connectSlotsByName(FounisseurValideWidget)

    def retranslateUi(self, FounisseurValideWidget):
        _translate = QtCore.QCoreApplication.translate
        FounisseurValideWidget.setWindowTitle(_translate("FounisseurValideWidget", "Fournisseur"))
        self.pushButtonNouveau.setText(_translate("FounisseurValideWidget", "Nouveau"))
        self.pushButtonValider.setText(_translate("FounisseurValideWidget", "Valider"))
        self.pushButtonRechercher.setText(_translate("FounisseurValideWidget", "Rechercher"))
        self.pushButtonDernier.setText(_translate("FounisseurValideWidget", "Dernier"))
        self.pushButtonPremier.setText(_translate("FounisseurValideWidget", "Premier"))
        self.pushButtonDefilerArrier.setText(_translate("FounisseurValideWidget", "Défiler en arrière"))
        self.pushButtonDefilerAvant.setText(_translate("FounisseurValideWidget", "Défiler en avant"))
        self.pushButtonAfficher.setText(_translate("FounisseurValideWidget", "Afficher"))
        self.pushButtonImprimer.setText(_translate("FounisseurValideWidget", "Imprimer"))
        self.pushButtonSortir.setText(_translate("FounisseurValideWidget", "Sortir"))
