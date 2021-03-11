# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 81, 16))
        self.label.setObjectName("label")
        self.labelNomFichier = QtWidgets.QLabel(self.centralwidget)
        self.labelNomFichier.setGeometry(QtCore.QRect(380, 40, 301, 16))
        self.labelNomFichier.setText("")
        self.labelNomFichier.setObjectName("labelNomFichier")
        self.pushButtonAjouter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAjouter.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.pushButtonAjouter.setObjectName("pushButtonAjouter")
        self.pushButtonEnvoyer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEnvoyer.setEnabled(False)
        self.pushButtonEnvoyer.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButtonEnvoyer.setObjectName("pushButtonEnvoyer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choisi un fichier"))
        self.pushButtonAjouter.setText(_translate("MainWindow", "Ajouter"))
        self.pushButtonEnvoyer.setText(_translate("MainWindow", "Envoyer"))
