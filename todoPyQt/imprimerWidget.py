from PyQt5.QtWidgets import QWidget
from FournisseurImprimerWidget import Ui_FournisseurImprimerWidget
import xlsxwriter

class ImprimerWidget(Ui_FournisseurImprimerWidget):
	def __init__(self, widget, cursor):
		super(ImprimerWidget, self).__init__()
		self.widget = QWidget(widget)
		self.cursor = cursor

		self.setupUi(self.widget)
		self.widget.close()

	def writeOnExel(self):
		workbook = xlsxwriter.Workbook("Founisseur.xlsx")
		worksheet = workbook.add_worksheet()
		header = ["code Fournisseur","nom fournisseur","code Fournisseur",
					"registre de commerce","telephone","fax","c correspondance",
					"site web","email","fichier","adresse banque","compte b",
					"adresse Fournisseur","adresse","adresse1","Remarque1",
					"Remarque2","flag"]

		for i in range(len(header)):
			worksheet.write(0, i, header[i])

		data = self.getData()
		i = 1
		for row in data:
			for j in range(len(row)):
				worksheet.write(i, j, row[j])
			i += 1

			

		workbook.close()

	def getData(self):
		self.cursor.execute("SELECT * FROM dbfournisseur")
		return self.cursor.fetchall()

