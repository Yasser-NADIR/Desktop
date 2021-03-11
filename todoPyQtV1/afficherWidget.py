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

	def setData(self):
		rows = self.getData()
		self.tableWidget.setRowCount(len(rows))
		i = 0
		for data in rows:
			print(data)
			self.setRow(i, data)
			i += 1

	def cellClicked(self, a, b):
		print("a cell clicked !",a,b)