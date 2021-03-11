# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\COZMET\Desktop\todoPyQt\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCreation = QtWidgets.QMenu(self.menubar)
        self.menuCreation.setObjectName("menuCreation")
        self.menuR_Achat = QtWidgets.QMenu(self.menubar)
        self.menuR_Achat.setObjectName("menuR_Achat")
        self.menuR_Vente = QtWidgets.QMenu(self.menubar)
        self.menuR_Vente.setObjectName("menuR_Vente")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFournisseur = QtWidgets.QAction(MainWindow)
        self.actionFournisseur.setObjectName("actionFournisseur")
        self.actionUnite = QtWidgets.QAction(MainWindow)
        self.actionUnite.setObjectName("actionUnite")
        self.actionStatus = QtWidgets.QAction(MainWindow)
        self.actionStatus.setObjectName("actionStatus")
        self.actionFamille_Produit = QtWidgets.QAction(MainWindow)
        self.actionFamille_Produit.setObjectName("actionFamille_Produit")
        self.actionProduit = QtWidgets.QAction(MainWindow)
        self.actionProduit.setObjectName("actionProduit")
        self.actionCatalogue = QtWidgets.QAction(MainWindow)
        self.actionCatalogue.setObjectName("actionCatalogue")
        self.actionClient = QtWidgets.QAction(MainWindow)
        self.actionClient.setObjectName("actionClient")
        self.actionFamille = QtWidgets.QAction(MainWindow)
        self.actionFamille.setObjectName("actionFamille")
        self.menuR_Achat.addAction(self.actionFournisseur)
        self.menuR_Achat.addAction(self.actionUnite)
        self.menuR_Achat.addAction(self.actionStatus)
        self.menuR_Achat.addAction(self.actionFamille_Produit)
        self.menuR_Achat.addAction(self.actionProduit)
        self.menuR_Achat.addAction(self.actionCatalogue)
        self.menuR_Vente.addAction(self.actionClient)
        self.menuR_Vente.addAction(self.actionFamille)
        self.menubar.addAction(self.menuCreation.menuAction())
        self.menubar.addAction(self.menuR_Achat.menuAction())
        self.menubar.addAction(self.menuR_Vente.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuCreation.setTitle(_translate("MainWindow", "Creation"))
        self.menuR_Achat.setTitle(_translate("MainWindow", "R_Achat"))
        self.menuR_Vente.setTitle(_translate("MainWindow", "R_Vente"))
        self.actionFournisseur.setText(_translate("MainWindow", "Fournisseur"))
        self.actionUnite.setText(_translate("MainWindow", "Unite"))
        self.actionStatus.setText(_translate("MainWindow", "Status"))
        self.actionFamille_Produit.setText(_translate("MainWindow", "Famille Produit"))
        self.actionProduit.setText(_translate("MainWindow", "Produit"))
        self.actionCatalogue.setText(_translate("MainWindow", "Catalogue"))
        self.actionClient.setText(_translate("MainWindow", "Client"))
        self.actionFamille.setText(_translate("MainWindow", "Famille"))
