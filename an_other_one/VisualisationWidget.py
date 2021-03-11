# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualisationWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VisualisationWidget(object):
    def setupUi(self, VisualisationWidget):
        VisualisationWidget.setObjectName("VisualisationWidget")
        VisualisationWidget.resize(707, 632)
        self.widgetCentral = QtWidgets.QWidget(VisualisationWidget)
        self.widgetCentral.setGeometry(QtCore.QRect(9, 9, 689, 614))
        self.widgetCentral.setObjectName("widgetCentral")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetCentral)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxRequest = QtWidgets.QGroupBox(self.widgetCentral)
        self.groupBoxRequest.setObjectName("groupBoxRequest")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxRequest)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBoxRequests = QtWidgets.QComboBox(self.groupBoxRequest)
        self.comboBoxRequests.setMinimumSize(QtCore.QSize(131, 22))
        self.comboBoxRequests.setObjectName("comboBoxRequests")
        self.horizontalLayout.addWidget(self.comboBoxRequests)
        self.pushButtonSubmitRequest = QtWidgets.QPushButton(self.groupBoxRequest)
        self.pushButtonSubmitRequest.setObjectName("pushButtonSubmitRequest")
        self.horizontalLayout.addWidget(self.pushButtonSubmitRequest)
        self.gridLayout_2.addWidget(self.groupBoxRequest, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(299, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.groupBoxImpression = QtWidgets.QGroupBox(self.widgetCentral)
        self.groupBoxImpression.setObjectName("groupBoxImpression")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxImpression)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonHTML = QtWidgets.QRadioButton(self.groupBoxImpression)
        self.radioButtonHTML.setObjectName("radioButtonHTML")
        self.gridLayout.addWidget(self.radioButtonHTML, 0, 0, 1, 1)
        self.radioButtonPDF = QtWidgets.QRadioButton(self.groupBoxImpression)
        self.radioButtonPDF.setObjectName("radioButtonPDF")
        self.gridLayout.addWidget(self.radioButtonPDF, 0, 1, 1, 1)
        self.radioButtonCSV = QtWidgets.QRadioButton(self.groupBoxImpression)
        self.radioButtonCSV.setObjectName("radioButtonCSV")
        self.gridLayout.addWidget(self.radioButtonCSV, 1, 0, 1, 1)
        self.radioButtonXML = QtWidgets.QRadioButton(self.groupBoxImpression)
        self.radioButtonXML.setObjectName("radioButtonXML")
        self.gridLayout.addWidget(self.radioButtonXML, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxImpression, 0, 0, 1, 1)
        self.tableWidgetViewData = QtWidgets.QTableWidget(self.widgetCentral)
        self.tableWidgetViewData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetViewData.setRowCount(0)
        self.tableWidgetViewData.setColumnCount(0)
        self.tableWidgetViewData.setObjectName("tableWidgetViewData")
        self.tableWidgetViewData.verticalHeader().setVisible(False)
        self.tableWidgetViewData.verticalHeader().setHighlightSections(False)
        self.gridLayout_2.addWidget(self.tableWidgetViewData, 1, 0, 1, 5)
        self.pushButtonFermer = QtWidgets.QPushButton(self.widgetCentral)
        self.pushButtonFermer.setObjectName("pushButtonFermer")
        self.gridLayout_2.addWidget(self.pushButtonFermer, 0, 4, 1, 1)

        self.retranslateUi(VisualisationWidget)
        QtCore.QMetaObject.connectSlotsByName(VisualisationWidget)

    def retranslateUi(self, VisualisationWidget):
        _translate = QtCore.QCoreApplication.translate
        VisualisationWidget.setWindowTitle(_translate("VisualisationWidget", "VisualisationWidget"))
        self.groupBoxRequest.setTitle(_translate("VisualisationWidget", "Requatte"))
        self.pushButtonSubmitRequest.setText(_translate("VisualisationWidget", "Envoyer"))
        self.groupBoxImpression.setTitle(_translate("VisualisationWidget", "Impression"))
        self.radioButtonHTML.setText(_translate("VisualisationWidget", "HTML"))
        self.radioButtonPDF.setText(_translate("VisualisationWidget", "PDF"))
        self.radioButtonCSV.setText(_translate("VisualisationWidget", "CSV"))
        self.radioButtonXML.setText(_translate("VisualisationWidget", "XML"))
        self.pushButtonFermer.setText(_translate("VisualisationWidget", "Fermer"))
