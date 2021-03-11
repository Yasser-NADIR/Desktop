from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from FournisseurAfficherWidget import Ui_FounisseurAfficherWidget

class AfficherWidget(Ui_FounisseurAfficherWidget):
	def __init__(self, widget, cursor):
		super(AfficherWidget, self).__init__()
		self.widget = QWidget(widget)
		self.cursor = cursor

		self.setupUi(self.widget)
		self.widget.close()

		self.tableWidget.cellClicked.connect(self.cellClicked)

	def getData(self):
		self.cursor.execute("SELECT * FROM dbFournisseur")
		return self.cursor.fetchall()

	def setRow(self, row, data):
		i = 0
		for d in data:
			self.tableWidget.setItem(row, i, QTableWidgetItem(str(d)))
			i += 1

	def getRow(self, row):
		data = []
		for i in range(18):
			data.append(self.tableWidget.item(row, i).text())
		return data

	def setData(self):
		rows = self.getData()
		self.tableWidget.setRowCount(len(rows))
		i = 0
		for data in rows:
			self.setRow(i, data)
			i += 1

	def cellClicked(self):
		if len(self.tableWidget.selectedItems()):
			for i in range(len(self.tableWidget.selectedItems())):
				print(i+1,"cordonnée", self.tableWidget.selectedItems()[i].row(), self.tableWidget.selectedItems()[i].column())
			if len(self.tableWidget.selectedItems()) == 1:
				self.pushButtonModifier.setEnabled(True)
				self.pushButtonSupprimer.setEnabled(True)
				return self.tableWidget.selectedItems()[0].row()

		if len(self.tableWidget.selectedItems()) != 1 : 
			self.pushButtonModifier.setEnabled(False)
			self.pushButtonSupprimer.setEnabled(False)