from FournisseurRechercherWidget import Ui_FournisseurRechercherWidget
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

class Rechercher(Ui_FournisseurRechercherWidget):
	def __init__(self, widget, cursor):
		super(Rechercher, self).__init__()
		self.widget = QWidget(widget)
		self.cursor = cursor
		self.setupUi(self.widget)
		self.widget.close()

		self.pushButtonRechercher.clicked.connect(self.onRechercher)

	def onRechercher(self):
		cle = self.lineEditCle.text()
		self.lineEditCle.setText("")
		self.cursor.execute("SELECT * FROM dbfournisseur WHERE code_fournisseuri = %s", cle)
		resultat = self.cursor.fetchone()
		if resultat:
			i = 0
			for ele in resultat:
				self.tableWidget.setItem(0, i, QTableWidgetItem(str(ele)))
				i += 1

	def cleanTable(self):
		for i in range(self.tableWidget.columnCount()) :
			self.tableWidget.setItem(0, i, QTableWidgetItem(""))