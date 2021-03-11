from DialogImprimer import Ui_DialogImprimer
from PyQt5.QtWidgets import QDialog, QMessageBox
from PrintFunction import printPDFFournisseur, printWordFournisseur, printPDFFamilleProduit, printPDFProduit

class DialogImprimer(QDialog, Ui_DialogImprimer):
	def __init__(self, data, filename=None, widgetName=None, parent=None):
		super(DialogImprimer, self).__init__(parent)
		self.setupUi(self)
		self.data = data
		self.pushButtonImprimer.clicked.connect(self.Imprimer)
		self.filename = filename
		self.widgetName = widgetName

	def Imprimer(self):
		if self.widgetName == "fournisseur":
			if self.radioButtonPDF.isChecked():
				printPDFFournisseur.render(self.data, self.filename)
				QMessageBox.information(self, "Impression", "Impression en format pdf")
			else:
				pass
		elif self.widgetName == "familleproduit":
			if self.radioButtonPDF.isChecked():
				printPDFFamilleProduit.render(self.data, self.filename)
				QMessageBox.information(self, "Impression", "Impression en format pdf")
			else:
				pass
		elif self.widgetName == "produit":
			if self.radioButtonPDF.isChecked():
				printPDFProduit.render(self.data, self.filename)
				QMessageBox.information(self, "Impression", "Impression en format pdf")
			else:
				pass

		self.close()
