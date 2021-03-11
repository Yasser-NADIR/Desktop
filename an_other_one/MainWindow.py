# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.widgetCentral = QtWidgets.QWidget(mainWindow)
        self.widgetCentral.setStyleSheet("")
        self.widgetCentral.setObjectName("widgetCentral")
        mainWindow.setCentralWidget(self.widgetCentral)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu1 = QtWidgets.QMenu(self.menubar)
        self.menuMenu1.setObjectName("menuMenu1")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionFournisseur = QtWidgets.QAction(mainWindow)
        self.actionFournisseur.setObjectName("actionFournisseur")
        self.actionClose = QtWidgets.QAction(mainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actiontest = QtWidgets.QAction(mainWindow)
        self.actiontest.setObjectName("actiontest")
        self.actionFamilleProduit = QtWidgets.QAction(mainWindow)
        self.actionFamilleProduit.setObjectName("actionFamilleProduit")
        self.actionProduit = QtWidgets.QAction(mainWindow)
        self.actionProduit.setObjectName("actionProduit")
        self.actionEntete_Detail = QtWidgets.QAction(mainWindow)
        self.actionEntete_Detail.setObjectName("actionEntete_Detail")
        self.menuMenu1.addAction(self.actionFournisseur)
        self.menuMenu1.addAction(self.actionFamilleProduit)
        self.menuMenu1.addAction(self.actionProduit)
        self.menuMenu1.addAction(self.actionEntete_Detail)
        self.menuMenu1.addAction(self.actionClose)
        self.menubar.addAction(self.menuMenu1.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "App"))
        self.menuMenu1.setTitle(_translate("mainWindow", "Menu1"))
        self.actionFournisseur.setText(_translate("mainWindow", "Fournisseur"))
        self.actionClose.setText(_translate("mainWindow", "Close"))
        self.actiontest.setText(_translate("mainWindow", "test"))
        self.actionFamilleProduit.setText(_translate("mainWindow", "FamilleProduit"))
        self.actionProduit.setText(_translate("mainWindow", "Produit"))
        self.actionEntete_Detail.setText(_translate("mainWindow", "EnteteDetail"))
