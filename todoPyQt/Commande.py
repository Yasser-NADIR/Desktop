from commandeWidget import Ui_CommandeWidget
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QDate
import psycopg2
import xlsxwriter

class commandeWidget(Ui_CommandeWidget):
	def __init__(self, centralwidget):
		super(commandeWidget, self).__init__()
		self.setupUi(centralwidget)
		self.widgetCentral.close()

		self.db = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="dbapp")
		self.cursor = self.db.cursor()
		for widget in (self.lineEditIdCommande,self.lineEditFKCommande,self.lineEditQuantite,self.lineEditPrixUnite,self.lineEditPrixGlobal,self.lineEditRemarqueDetail):
			widget.textChanged.connect(self.verifierText)
		
		self.initComboBox()
		self.initIdCommande()
		self.initChamps()

		self.lineEditIdCommande.textChanged.connect(lambda text: self.verifierNumber(self.lineEditIdCommande, text))
		self.lineEditFKCommande.textChanged.connect(lambda text: self.verifierNumber(self.lineEditFKCommande, text))
		self.lineEditQuantite.textChanged.connect(lambda text: self.verifierNumber(self.lineEditQuantite, text))
		self.lineEditPrixUnite.textChanged.connect(lambda text: self.verifierNumber(self.lineEditPrixUnite, text))
		self.lineEditCodeCmd.textChanged.connect(lambda text: self.verifierNumber(self.lineEditCodeCmd ,text))
		self.lineEditCodeSociete.textChanged.connect(lambda text: self.verifierNumber(self.lineEditCodeSociete ,text))

		self.lineEditQuantite.textChanged.connect(lambda nombre: self.calculePrixGlobal(self.lineEditPrixGlobal, self.lineEditPrixUnite.text(), nombre))
		self.lineEditPrixUnite.textChanged.connect(lambda prixUnite: self.calculePrixGlobal(self.lineEditPrixGlobal, prixUnite, self.lineEditQuantite.text()))



		self.pushButtonAjouter.clicked.connect(self.ajouter)
		self.tableWidgetEntete.cellClicked.connect(self.clickedItemEntete)
		self.pushButtonModifier.clicked.connect(self.modifier)
		self.pushButtonSupprimer.clicked.connect(self.supprimer)
		self.pushButtonNouveau.clicked.connect(self.Nouveau)
		self.pushButtonValider.clicked.connect(self.Valider)
		self.pushButtonRechercher.clicked.connect(self.Rechercher)
		self.tableWidgetRechercher.cellClicked.connect(self.clickedItemRechercher)
		self.pushButtonModifierRechercher.clicked.connect(self.ModifierRechercher)
		self.pushButtonSupprimerRechercher.clicked.connect(self.SupprimerRechercher)
		self.pushButtonImprimer.clicked.connect(self.Imprimer)

	def initNomFournisseur(self):
		self.cursor.execute("SELECT nom_fournisseur FROM dbfournisseur")
		data = self.cursor.fetchall()
		for nom in data:
			self.comboBoxCodeFournisseur.addItem(nom[0])

	def initRefProduit(self):
		self.cursor.execute("SELECT produit FROM produit")
		data = self.cursor.fetchall()
		for ref in data:
			self.comboBoxRefProduit.addItem(ref[0])

	def initCodeUnite(self):
		self.cursor.execute("SELECT code FROM unite")
		data = self.cursor.fetchall()
		for code in data:
			self.comboBoxCodeUnite.addItem(code[0])

	def initComboBox(self):
		self.initNomFournisseur()
		self.initRefProduit()
		self.initCodeUnite()

	def initIdCommande(self):
		self.cursor.execute("SELECT COUNT(*) FROM dbentetecommande")
		id_ = str(self.cursor.fetchone()[0]+1)
		self.lineEditCodeCmd.setText(id_)
		self.lineEditFKCommande.setText(id_)
		self.lineEditIdCommande.setText(str(1))

	def getTextDetail(self):
		return (self.lineEditIdCommande.text(),
				self.lineEditFKCommande.text(),
				self.comboBoxRefProduit.currentText(),
				self.lineEditQuantite.text(),
				self.lineEditPrixUnite.text(),
				f"{self.dateEditDateLivraison.date().year()}-{self.dateEditDateLivraison.date().month()}-{self.dateEditDateLivraison.date().day()}",
				self.comboBoxCodeUnite.currentText(),
				self.lineEditPrixGlobal.text(),
				self.lineEditRemarqueDetail.text())

	def getTextEntete(self):
		return (self.lineEditCodeCmd.text(),
				self.lineEditRefMarche.text(),
				self.comboBoxCodeFournisseur.currentText(),
				self.lineEditCodeSociete.text(),
				f"{self.dateEditDateCommande.date().year()}-{self.dateEditDateCommande.date().month()}-{self.dateEditDateCommande.date().day()}",
				self.lineEditFlag.text(),
				self.lineEditRemarqueEntet.text())

	def getDataTableDetail(self):
		data = []

		for line in range(self.tableWidgetEntete.rowCount()):
			row = []
			for column in range(self.tableWidgetEntete.columnCount()):
				row.append(self.tableWidgetEntete.item(line, column).text())
			data.append(row)
		return data

	def cleanTextDetail(self):
		self.lineEditQuantite.setText("")
		self.lineEditPrixUnite.setText("")
		self.lineEditPrixGlobal.setText("")
		self.lineEditRemarqueDetail.setText("")

	def cleanTextEntete(self):
		self.lineEditRefMarche.setText("")
		self.lineEditCodeSociete.setText("")
		self.lineEditFlag.setText("")
		self.lineEditRemarqueEntet.setText("")

		
	def setTextDetail(self, data):
		self.lineEditIdCommande.setText(data[0])
		self.lineEditFKCommande.setText(data[1])
		self.comboBoxRefProduit.setCurrentText(data[2])
		self.lineEditQuantite.setText(data[3])
		self.lineEditPrixUnite.setText(data[4])
		self.dateEditDateLivraison.setDate(QDate(int(data[5].split("-")[0]), int(data[5].split("-")[1]), int(data[5].split("-")[2])))
		self.comboBoxCodeUnite.setCurrentText(data[6])
		self.lineEditPrixGlobal.setText(data[7])
		self.lineEditRemarqueDetail.setText(data[8])

	def setTextEntete(self, data):
		self.lineEditCodeCmd.setText(str(data[0]))
		self.lineEditRefMarche.setText(str(data[1]))
		self.comboBoxCodeFournisseur.setCurrentText(str(data[2]))
		self.lineEditCodeSociete.setText(str(data[3]))
		self.dateEditDateCommande.setDate(QDate(data[4].year,data[4].month,data[4].day ))
		self.lineEditFlag.setText(str(data[5]))
		self.lineEditRemarqueEntet.setText(str(data[6]))

	def initChamps(self):
		self.lineEditRefMarche.setText("xxx")
		self.lineEditCodeSociete.setText("xxx")
		self.lineEditFlag.setText("xxx")
		self.lineEditRemarqueEntet.setText("xxx")

		self.lineEditQuantite.setText("xxx")
		self.lineEditPrixUnite.setText("xxx")
		self.lineEditPrixGlobal.setText("xxx")
		self.lineEditRemarqueDetail.setText("xxx")

	def isfloat(self, value):
		try:
		    float(value)
		    return True
		except ValueError:
		    return False

	def verifierText(self):
		text = self.getTextDetail()
		for t in text:
			if t == "":
				self.pushButtonAjouter.setEnabled(False)
				return
		self.pushButtonAjouter.setEnabled(True)

	def verifierNumber(self, lineEdit, text):
		if self.isfloat(text):
			return
		if len(text) and text[-1].isdigit() == False:
			lineEdit.setText(text[:-1])

	def calculePrixGlobal(self, lineEdit, prixUnite, nombre):
		if prixUnite and nombre:
			lineEdit.setText(f"{float(prixUnite)* float(nombre)}")
		else:
			lineEdit.setText("")


	def ajouter(self):
		text = self.getTextDetail()
		self.tableWidgetEntete.setRowCount(self.tableWidgetEntete.rowCount()+1)
		for i in range(self.tableWidgetEntete.columnCount()):
			item = QTableWidgetItem(text[i])
			self.tableWidgetEntete.setItem(self.tableWidgetEntete.rowCount()-1, i, item)
		self.cleanTextDetail()
		self.pushButtonAjouter.setEnabled(False)
		id_ = int(self.lineEditIdCommande.text())+1
		self.lineEditIdCommande.setText(str(id_))

	def clickedItemEntete(self, row, column):
		if len(self.tableWidgetEntete.selectedItems()) == 0:
			rowSelectedItem = None
			self.pushButtonModifier.setEnabled(False)
			self.pushButtonSupprimer.setEnabled(False)
			return

		self.pushButtonModifier.setEnabled(True)
		self.pushButtonSupprimer.setEnabled(True)

	def clickedItemRechercher(self, row, column):
		if len(self.tableWidgetRechercher.selectedItems()) == 0:
			rowSelectedItem = None
			self.pushButtonModifierRechercher.setEnabled(False)
			self.pushButtonSupprimerRechercher.setEnabled(False)
			return

		self.pushButtonModifierRechercher.setEnabled(True)
		self.pushButtonSupprimerRechercher.setEnabled(True)

	def modifier(self):
		row = self.tableWidgetEntete.selectedItems()[0].row()
		data = []
		for i in range(self.tableWidgetEntete.columnCount()):
			data.append(self.tableWidgetEntete.item(row, i).text())
		self.supprimer()
		self.setTextDetail(data)

	def supprimer(self):
		row = self.tableWidgetEntete.selectedItems()[0].row()
		if self.tableWidgetEntete.rowCount()-1 == row:
			self.tableWidgetEntete.setRowCount(self.tableWidgetEntete.rowCount()-1)
		else:
			for i in range(row, self.tableWidgetEntete.rowCount()-1):
				for j in range(self.tableWidgetEntete.columnCount()):
					item = QTableWidgetItem(self.tableWidgetEntete.item(i+1, j).text())
					self.tableWidgetEntete.setItem(i, j, item)
			self.tableWidgetEntete.setRowCount(self.tableWidgetEntete.rowCount()-1)

		self.pushButtonModifier.setEnabled(False)
		self.pushButtonSupprimer.setEnabled(False)

	def Nouveau(self):
		self.cleanTextDetail()
		self.cleanTextEntete()
		self.tableWidgetEntete.setRowCount(0)
		self.initIdCommande()
		self.initChamps()

	def Valider(self):
		dataEntete = self.getTextEntete()
		dataDetail = self.getDataTableDetail()
		self.Nouveau()
		self.cursor.execute("INSERT INTO dbentetecommande VALUES (%s, %s, %s, %s, %s, %s, %s)", dataEntete)
		self.db.commit()
		for d in dataDetail:
			self.cursor.execute("INSERT INTO dbdetailcommande VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", d)
			self.db.commit()

	def Rechercher(self):
		choix = self.comboBoxChoixRecherche.currentText()
		if choix == "Entete":
			entete = ["code cmd", "ref marche", "code fournisseur", "code societe", "date commande", "flag", "remarque"]
			self.cursor.execute("SELECT * FROM dbentetecommande")
			data = self.cursor.fetchall()
			self.tableWidgetRechercher.setColumnCount(7)
			self.tableWidgetRechercher.setRowCount(len(data))
			for i in range(7):
				item = QTableWidgetItem()
				item.setText(entete[i])
				self.tableWidgetRechercher.setHorizontalHeaderItem(i, item)
			for i in range(len(data)):
				row = data[i]
				for j in range(7):
					item = QTableWidgetItem()
					item.setText(str(row[j]))
					self.tableWidgetRechercher.setItem(i, j, item)
		elif choix == "Detail":
			entete = ["id commande","fk commande","ref produit","quantite","prix unite","date livraison","code unité","Prix global","remarque"]
			self.cursor.execute("SELECT * FROM dbdetailcommande")
			data = self.cursor.fetchall()
			self.tableWidgetRechercher.setColumnCount(9)
			self.tableWidgetRechercher.setRowCount(len(data))
			for i in range(9):
				item = QTableWidgetItem()
				item.setText(entete[i])
				self.tableWidgetRechercher.setHorizontalHeaderItem(i, item)
			for i in range(len(data)):
				row = data[i]
				for j in range(9):
					item = QTableWidgetItem()
					item.setText(str(row[j]))
					self.tableWidgetRechercher.setItem(i, j, item)

	def ModifierRechercher(self):
		row = self.tableWidgetRechercher.selectedItems()[0].row()
		data = []
		for i in range(self.tableWidgetRechercher.columnCount()):
			data.append(self.tableWidgetRechercher.item(row, i).text()) 

		if self.comboBoxChoixRecherche.currentText() == "Entete":
			self.tabWidget.setCurrentIndex(0)
			index = data[0]
		else:
			self.tabWidget.setCurrentIndex(1)
			index = data[1]

		self.cursor.execute("SELECT * FROM dbentetecommande WHERE code_cmd = %s", index)
		entete = self.cursor.fetchone()
		self.cursor.execute("SELECT * FROM dbdetailcommande WHERE fk_commande = %s", index)
		detail = self.cursor.fetchall()
		self.setTextEntete(entete)
		self.tableWidgetEntete.setRowCount(len(detail))
		for row in range(len(detail)) :
			for i in range(self.tableWidgetEntete.columnCount()):
				item = QTableWidgetItem(str(detail[row][i]))
				self.tableWidgetEntete.setItem(row, i, item)

		self.lineEditIdCommande.setText(str(len(detail)+1))


	def SupprimerRechercher(self):
		row = self.tableWidgetRechercher.selectedItems()[0].row()
		if self.comboBoxChoixRecherche.currentText() == "Entete":
			index = self.tableWidgetRechercher.item(row, 0).text()
			self.cursor.execute("DELETE FROM dbentetecommande WHERE code_cmd = %s", index)
		else:
			index = self.tableWidgetRechercher.item(row, 1).text()
			self.cursor.execute("DELETE FROM dbentetecommandedbdetailcommande WHERE fk_commande = %s", index)

		self.db.commit()

		if self.tableWidgetRechercher.rowCount()-1 == row:
			self.tableWidgetRechercher.setRowCount(self.tableWidgetRechercher.rowCount()-1)
		else:
			for i in range(row, self.tableWidgetRechercher.rowCount()-1):
				for j in range(self.tableWidgetRechercher.columnCount()):
					item = QTableWidgetItem(self.tableWidgetRechercher.item(i+1, j).text())
					self.tableWidgetRechercher.setItem(i, j, item)
			self.tableWidgetRechercher.setRowCount(self.tableWidgetRechercher.rowCount()-1)

		self.pushButtonModifierRechercher.setEnabled(False)
		self.pushButtonSupprimerRechercher.setEnabled(False)

		self.cleanTextDetail()
		self.cleanTextEntete()

	def Imprimer(self):

		book = xlsxwriter.Workbook("commande.xlsx")
		sheet = book.add_worksheet()


		self.cursor.execute("""SELECT *
							FROM dbentetecommande, dbdetailcommande
							WHERE fk_commande = code_cmd AND code_cmd = %s
							""", (elf.getTextEntete()[0], ))
		data = self.cursor.fetchall()

		"""for i in range(2, len(data)):
									for j in range(len(dataDetail[0])):
										sheet.write(i, j, dataDetail[i-2][j])"""

		QMessageBox.information(self.widget, "Impression", "les information sont imprimer dans le fichier commande.xlsx")

		book.close()

		