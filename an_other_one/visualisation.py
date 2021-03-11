from VisualisationWidget import Ui_VisualisationWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PrintFunction import printXML, printHTML, printPDF, printCSV

class VisualisationWidget(Ui_VisualisationWidget):
	def __init__(self, widgetCentral, nameWidget, parent):
		super(VisualisationWidget, self).__init__()
		self.setupUi(widgetCentral)
		self.widgetCentral.close()
		self.parent = parent
		self.nameWidget = nameWidget

		self.pushButtonFermer.clicked.connect(self.close)
		self.tableWidgetViewData.cellClicked.connect(self.Orienter)
		self.pushButtonSubmitRequest.clicked.connect(self.SubmitRequest)
		self.radioButtonXML.clicked.connect(self.printXml)
		self.radioButtonHTML.clicked.connect(self.printHtml)
		self.radioButtonPDF.clicked.connect(self.printPdf)
		self.radioButtonCSV.clicked.connect(self.printCsv)
		#la redefinition de la fonction show de widgetCentral
		self.show = self.widgetCentral.show
		self.widgetCentral.show = self.onShow

		
		self.initComboBoxRequests(["premier", "deuxieme", "troisieme"])

	def initComboBoxRequests(self, requests):
		for _ in range(self.comboBoxRequests.count()):
			self.comboBoxRequests.removeItem(0)
		for request in requests:
			self.comboBoxRequests.addItem(str(request))

	#cette fonction va prendre le nom de la table cible
	#par la suite elle va recuperer les nom des colonnes
	#et enfin recupere les enregistrement pour les affichés
	def displayAll(self, nameTable):
		self.parent.cursor.execute("SELECT column_name FROM information_schema.columns where table_name = %s", (nameTable, ))
		colonnes = self.parent.cursor.fetchall()
		self.tableWidgetViewData.setColumnCount(len(colonnes))
		for i in range(len(colonnes)):
			self.tableWidgetViewData.setHorizontalHeaderItem(i, QTableWidgetItem(colonnes[i][0]))

		query = "SELECT * FROM {} ".format(nameTable)
		self.parent.cursor.execute(query)
		rows = self.parent.cursor.fetchall()
		self.tableWidgetViewData.setRowCount(len(rows))
		for i in range(len(rows)):
			for j in range(len(rows[i])):
				self.tableWidgetViewData.setItem(i, j, QTableWidgetItem(str(rows[i][j])))

	def Orienter(self, row, column):
		text = []
		for i in range(self.tableWidgetViewData.columnCount()):
			text.append(self.tableWidgetViewData.item(row, i).text())
		self.parent.setText(text)
		self.parent.pushButtonValider.setEnabled(False)
		self.parent.pushButtonModifier.setEnabled(True)
		self.parent.pushButtonSupprimer.setEnabled(True)
		self.close()

	#pour appliquer les requettes
	def SubmitRequest(self):
		pass

	def printXml(self):
		self.parent.cursor.execute("SELECT column_name FROM information_schema.columns where table_name = %s", (self.nameWidget, ))
		columns = self.parent.cursor.fetchall()
		columns = [c[0] for c in columns]
		query = "SELECT * FROM {}".format(self.nameWidget)
		self.parent.cursor.execute(query)
		rows = self.parent.cursor.fetchall()

		printXML.render(self.nameWidget, columns, rows, self.nameWidget)#tableName columns rows filename

	def printHtml(self):
		self.parent.cursor.execute("SELECT column_name FROM information_schema.columns where table_name = %s", (self.nameWidget, ))
		columns = self.parent.cursor.fetchall()
		columns = [c[0] for c in columns]
		query = "SELECT * FROM {}".format(self.nameWidget)
		self.parent.cursor.execute(query)
		rows = self.parent.cursor.fetchall()

		printHTML.render(columns, rows, self.nameWidget)

	def printPdf(self):

		self.parent.cursor.execute("SELECT column_name FROM information_schema.columns where table_name = %s", (self.nameWidget, ))
		columns = self.parent.cursor.fetchall()
		columns = [c[0] for c in columns]
		query = "SELECT * FROM {}".format(self.nameWidget)
		self.parent.cursor.execute(query)
		rows = self.parent.cursor.fetchall()

		printPDF.render(columns, rows, self.nameWidget)

	def printCsv(self):

		self.parent.cursor.execute("SELECT column_name FROM information_schema.columns where table_name = %s", (self.nameWidget, ))
		columns = self.parent.cursor.fetchall()
		columns = [c[0] for c in columns]
		query = "SELECT * FROM {}".format(self.nameWidget)
		self.parent.cursor.execute(query)
		rows = self.parent.cursor.fetchall()

		printCSV.render(columns, rows, self.nameWidget)


	def close(self):
		self.widgetCentral.close()
		self.parent.widgetCentral.show()

	def onShow(self):
		self.show()
		self.displayAll(self.nameWidget)

