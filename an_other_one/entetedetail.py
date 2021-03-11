from EnteteDetailWidget import Ui_EnteteDetailWidget
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDate
#boite de dialogue d'impression
from boxDialogImprimer import DialogImprimer
#pour l'impression
from PrintFunction.printPDFEnteteDetail import printPDFEnteteDetail
from function.magicFunction import *
import os


class EnteteDetailWidget(Ui_EnteteDetailWidget):
	def __init__(self, widgetCentral, db):
		super(EnteteDetailWidget, self).__init__()
		self.setupUi(widgetCentral)
		self.widgetCentral.close

		self.db = db
		self.cursor = db.cursor()

		#cet attribut donne l'information sur label qui est cliqué, None si aucune label cliqué
		self.labelClicked = None

		#index est la positionnement de enregistrement quand on utilise avant ou arriere
		#-l donne le dernier enregistrement
		self.index = -1

		#la line selectionné
		self.selectedRow = None

		#initialisation les champs
		self.Nouveau()

		self.labelCodeCmd.mousePressEvent = lambda a: self.ClickedWidget(self.labelCodeCmd, "int")

		#liaison des evenements
		self.pushButtonNouveau.clicked.connect(self.Nouveau)
		self.pushButtonValider.clicked.connect(self.Valider)
		self.pushButtonRechercher.clicked.connect(self.Rechercher)
		self.pushButtonModifier.clicked.connect(self.Modifier)
		self.pushButtonSupprimer.clicked.connect(self.Supprimer)
		self.pushButtonPremier.clicked.connect(self.Premier)
		self.pushButtonDernier.clicked.connect(self.Dernier)
		self.pushButtonAvant.clicked.connect(self.Avant)
		self.pushButtonArriere.clicked.connect(self.Arriere)
		self.pushButtonImprimer.clicked.connect(self.Imprimer)
		self.pushButtonImprimerTout.clicked.connect(self.ImprimerTout)
		self.pushButtonVisualiser.clicked.connect(self.Visualiser)

		#calcule prix global quand on modifie le prix unitaire ou la quantité
		self.lineEdit_float_PrixUnitaire.textChanged.connect(self.calculTotalPrix)
		self.lineEdit_float_Quantite.textChanged.connect(self.calculTotalPrix)

		#les bottons qui manipulent la partie detail
		self.pushButtonAjouterDetail.clicked.connect(self.AjouterDetail)
		self.pushButtonModifierDetail.clicked.connect(self.ModiferDetail)
		self.pushButtonSupprimerDetail.clicked.connect(self.SupprimerDetail)
		self.pushButtonInsererDetail.clicked.connect(self.InsererDetail)
		self.pushButtonEffacerDetail.clicked.connect(self.EffacerDetail)

		#quand il faut activer modifier et supprimer detail
		#quand un item de tableau est selectionné
		self.tableWidgetDetailDisplay.cellClicked.connect(self.CellClicked)

	#les fonctions intermidiaire
	#getText donne le contenue de tout les champ de l'entete
	def getTextEntete(self):
		self.cursor.execute("SELECT codefournisseuri FROM fournisseur WHERE nomfournisseur=%s", (self.comboBoxCodeFournisseur.currentText(), ))
		code = self.cursor.fetchone()[0]
		return (self.lineEdit_int_CodeCmd.text(),
				code,
				"{}-{}-{}".format(self.dateEditDateCmd.date().year(), self.dateEditDateCmd.date().month(), self.dateEditDateCmd.date().day()))

	#setText remplie tous les champs de l'entete par des valeur passé par argument
	def setTextEntete(self, text):
		self.lineEdit_int_CodeCmd.setText(str(text[0]))
		self.comboBoxCodeFournisseur.setCurrentText(str(text[1]))
		self.dateEditDateCmd.setDate(QDate(text[2].year, text[2].month, text[2].day))

	def getTextDetailTable(self):
		rows = []
		nbrRow = self.tableWidgetDetailDisplay.rowCount()
		for i in range(nbrRow):
			row = []
			for j in range(6):
				row.append(self.tableWidgetDetailDisplay.item(i, j).text())
			rows.append(row)
		return rows

	def setTextDetailTable(self, row, text):
		for i in range(len(text)):
			self.tableWidgetDetailDisplay.setItem(row-1, i, QTableWidgetItem(str(text[i])))

	def getTextDetail(self):
		self.cursor.execute("SELECT codeproduit FROM produit WHERE nomproduit = %s", (self.comboBoxRefProduit.currentText(), ))
		code = self.cursor.fetchone()[0]
		return (self.lineEdit_int_IdCmd.text(),
		code,
		self.lineEdit_float_PrixUnitaire.text(),
		self.lineEdit_float_Quantite.text(),
		self.lineEdit_float_PrixGlobal.text(),
		"{}-{}-{}".format(self.dateEditDateLivraison.date().year(), self.dateEditDateLivraison.date().month(), self.dateEditDateLivraison.date().day()))

	def setTextDetail(self, text):
		self.lineEdit_int_IdCmd.setText(text[0])
		self.comboBoxRefProduit.setCurrentText(text[1])
		self.lineEdit_float_PrixUnitaire.setText(text[2])
		self.lineEdit_float_Quantite.setText(text[3])
		self.dateEditDateLivraison.setDate(QDate(int(text[5].split("-")[0]), int(text[5].split("-")[1]), int(text[5].split("-")[2])))

	def ClickedWidget(self, widget, Type):
		self.pushButtonRechercher.setEnabled(True)
		self.labelClicked = "".join(widget.text().split(" "))+"_"+Type

	def initComboBoxFournisseur(self):
		self.cursor.execute("SELECT nomfournisseur FROM fournisseur ORDER BY nomfournisseur")
		codes = self.cursor.fetchall()
		countMax = self.comboBoxCodeFournisseur.count()
		for _ in range(countMax):
			self.comboBoxCodeFournisseur.removeItem(0)
		for code in codes:
			self.comboBoxCodeFournisseur.addItem(str(code[0]))

	def initComboBoxRefProduit(self):
		self.cursor.execute("SELECT nomproduit FROM produit ORDER BY nomproduit")
		codes = self.cursor.fetchall()
		countMax = self.comboBoxRefProduit.count()
		for _ in range(countMax):
			self.comboBoxRefProduit.removeItem(0)
		for code in codes:
			self.comboBoxRefProduit.addItem(str(code[0]))

	#initialiser l'entete
	def initEntete(self):
		self.cursor.execute("SELECT max(codecommande) FROM entete")
		Max = self.cursor.fetchone()[0]
		if not Max: Max = 0
		self.lineEdit_int_CodeCmd.setText(str(int(Max)+1))
		self.initComboBoxFournisseur()

	#initialiser detail
	def initDetail(self):
		self.lineEdit_int_IdCmd.setText("1")
		self.initComboBoxRefProduit()
		self.lineEdit_float_Quantite.setText("0")
		self.lineEdit_float_PrixUnitaire.setText("0")
		self.lineEdit_float_PrixGlobal.setText("0")
		self.tableWidgetDetailDisplay.clearContents()
		self.tableWidgetDetailDisplay.setRowCount(0)

	def calculTotalPrix(self, text):
		if isFloat(self.lineEdit_float_PrixUnitaire.text()) and isFloat(self.lineEdit_float_Quantite.text()):
			prixUnitaire = float(self.lineEdit_float_PrixUnitaire.text())
			quantite = float(self.lineEdit_float_Quantite.text())
			resultat = int(prixUnitaire*quantite*100)/100.0
			self.lineEdit_float_PrixGlobal.setText(str(resultat))

	#quand une cellule est cliqué
	def CellClicked(self, row, column):
		self.selectedRow = row
		self.pushButtonAjouterDetail.setEnabled(False)
		self.pushButtonModifierDetail.setEnabled(True)
		if not self.pushButtonModifier.isEnabled(): self.pushButtonSupprimerDetail.setEnabled(True)
		if self.pushButtonModifier.isEnabled(): 
			self.pushButtonEffacerDetail.setEnabled(True)
			self.pushButtonInsererDetail.setEnabled(False)

	def AjouterDetail(self):
		data = self.getTextDetail()
		self.tableWidgetDetailDisplay.setRowCount(self.tableWidgetDetailDisplay.rowCount()+1)
		row = self.tableWidgetDetailDisplay.rowCount()
		self.setTextDetailTable(row, data)
		self.lineEdit_int_IdCmd.setText(str(int(self.lineEdit_int_IdCmd.text())+1))
		self.tableWidgetDetailDisplay.sortItems(0)

	def ModiferDetail(self):
		row = []
		for i in range(6):
			row.append(self.tableWidgetDetailDisplay.item(self.selectedRow, i).text())
		self.setTextDetail(row)
		self.tableWidgetDetailDisplay.removeRow(self.selectedRow)
		if not self.pushButtonRechercher.isEnabled(): self.pushButtonAjouterDetail.setEnabled(True)
		self.pushButtonModifierDetail.setEnabled(False)
		self.pushButtonSupprimerDetail.setEnabled(False)
		self.pushButtonInsererDetail.setEnabled(False)
		if self.pushButtonRechercher.isEnabled(): self.pushButtonInsererDetail.setEnabled(True)

	def SupprimerDetail(self):
		self.tableWidgetDetailDisplay.removeRow(self.selectedRow)
		for i in range(self.tableWidgetDetailDisplay.rowCount()):
			self.tableWidgetDetailDisplay.setItem(i, 0, QTableWidgetItem(str(i+1)))
		self.lineEdit_int_IdCmd.setText(str(int(self.tableWidgetDetailDisplay.item(i, 0).text())+1))
		self.tableWidgetDetailDisplay.sortItems(0)
		if not self.pushButtonRechercher.isEnabled(): self.pushButtonAjouterDetail.setEnabled(True)
		self.pushButtonModifierDetail.setEnabled(False)
		self.pushButtonSupprimerDetail.setEnabled(False)
		self.pushButtonInsererDetail.setEnabled(False)

	def InsererDetail(self):
		print(self.getTextDetail())
		query = "INSERT INTO detail VALUES (%s, %s, %s, %s, %s, %s, %s)"
		data = [*self.getTextDetail(), self.getTextEntete()[0]]
		self.cursor.execute(query, data)
		self.db.commit()
		self.AjouterDetail()

	def EffacerDetail(self):
		codecommande = self.lineEdit_int_CodeCmd.text()
		idcommande = self.tableWidgetDetailDisplay.item(self.selectedRow, 0).text()
		self.cursor.execute("DELETE FROM detail WHERE idcommande=%s AND codecommande=%s", (idcommande, codecommande))
		self.db.commit()
		self.SupprimerDetail()
		self.pushButtonAjouterDetail.setEnabled(False)


	def Nouveau(self):
		self.initEntete()
		self.initDetail()
		self.pushButtonRechercher.setEnabled(False)
		self.pushButtonModifier.setEnabled(False)
		self.pushButtonSupprimer.setEnabled(False)
		self.pushButtonAvant.setEnabled(False)
		self.pushButtonArriere.setEnabled(False)
		self.pushButtonValider.setEnabled(True)
		self.pushButtonSupprimerDetail.setEnabled(False)
		self.pushButtonModifierDetail.setEnabled(False)
		self.pushButtonInsererDetail.setEnabled(False)
		self.pushButtonAjouterDetail.setEnabled(True)
		self.pushButtonEffacerDetail.setEnabled(False)

	def Valider(self):
		#pour l'instant on valide just l'entete
		query = "INSERT INTO entete VALUES (%s, %s, %s)"
		self.cursor.execute(query, self.getTextEntete())
		query = "INSERT INTO detail VALUES (%s, %s, %s, %s, %s, %s, %s)"
		for data in self.getTextDetailTable():
			data.append(str(self.lineEdit_int_CodeCmd.text()))
			self.cursor.execute(query, data)
		self.db.commit()
		self.Nouveau()

	def Rechercher(self):
		cle, reponce = QInputDialog.getText(self.widgetCentral, "clé de recherche", "clé:")
		Type = self.labelClicked.split("_")[1]
		self.labelClicked = self.labelClicked.split("_")[0]
		if cle:
			if Type == "int" and not isInt(cle):
				QMessageBox.warning(self.widgetCentral, "Erreur", "le type de clé est incorrect")
			else:
				query = "SELECT * FROM entete WHERE {}=%s".format(self.labelClicked,)
				self.cursor.execute(query, (cle, ))
				entete = self.cursor.fetchone()
				query = "SELECT * FROM detail WHERE {}=%s".format(self.labelClicked,)
				self.cursor.execute(query, (cle, ))
				details = self.cursor.fetchall()
				if entete: 
					self.setTextEntete(entete)
					if details:
						self.tableWidgetDetailDisplay.setRowCount(len(details))
						row = 0
						for detail in details:
							detail = [*detail]
							detail[5] = "{}-{}-{}".format(detail[5].year, detail[5].month, detail[5].day)
							for i in range(len(detail[:-1])):
								self.tableWidgetDetailDisplay.setItem(row, i, QTableWidgetItem(str(detail[i])))
							row += 1
						self.lineEdit_int_IdCmd.setText(str(int(self.tableWidgetDetailDisplay.item(row-1, 0).text())+1))
					self.pushButtonValider.setEnabled(False)
					self.pushButtonModifier.setEnabled(True)
					self.pushButtonSupprimer.setEnabled(True)
					self.pushButtonInsererDetail.setEnabled(True)
					self.pushButtonAjouterDetail.setEnabled(False)
				else:
					QMessageBox.information(self.widgetCentral, "Resultat", "La valeur n'existe pas")

				self.labelClicked = None
		self.pushButtonRechercher.setEnabled(False)

	def Modifier(self):
		entete = self.getTextEntete()
		details = self.getTextDetailTable()
		query = "UPDATE entete SET codefournisseur = %s, datecommande = %s WHERE codecommande = %s"
		self.cursor.execute(query, (*entete[1:], entete[0]))
		query = "UPDATE detail SET refproduit = %s, prixunitaire = %s, quantite = %s, prixglobal = %s, datelivraison = %s WHERE idcommande = %s AND codecommande = %s"
		for detail in details:
			self.cursor.execute(query, (*detail[1:], detail[0], entete[0]))
		self.db.commit()
		self.Nouveau()

	def Supprimer(self):
		entete = self.getTextEntete()[0]
		query = "DELETE FROM entete WHERE codecommande = %s"
		self.cursor.execute(query, (entete))
		self.db.commit()
		self.Nouveau()

	def Premier(self):
		try:
			self.cursor.execute("SELECT * FROM entete ORDER BY codecommande")
			entete = self.cursor.fetchall()[0]
			self.cursor.execute("SELECT * FROM detail WHERE codecommande = %s ORDER BY idcommande", (entete[0], ))
			details = self.cursor.fetchall()
			self.setTextEntete(entete)
			self.tableWidgetDetailDisplay.setRowCount(0)
			if len(details):
				for detail in details:
					detail = [*detail]
					detail[5] = "{}-{}-{}".format(detail[5].year, detail[5].month, detail[5].day)
					self.tableWidgetDetailDisplay.setRowCount(self.tableWidgetDetailDisplay.rowCount()+1)
					self.setTextDetailTable(self.tableWidgetDetailDisplay.rowCount(), detail)
			self.pushButtonValider.setEnabled(False)
			self.pushButtonModifier.setEnabled(True)
			self.pushButtonSupprimer.setEnabled(True)
			self.pushButtonAvant.setEnabled(True)
			self.pushButtonArriere.setEnabled(True)
			self.index = 0
		except:
			QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")


	def Dernier(self):
		try:
			self.cursor.execute("SELECT * FROM entete ORDER BY codecommande")
			entete = self.cursor.fetchall()[-1]
			self.cursor.execute("SELECT * FROM detail WHERE codecommande = %s ORDER BY idcommande", (entete[0], ))
			details = self.cursor.fetchall()
			self.setTextEntete(entete)
			self.tableWidgetDetailDisplay.setRowCount(0)
			if len(details):
				for detail in details:
					detail = [*detail]
					detail[5] = "{}-{}-{}".format(detail[5].year, detail[5].month, detail[5].day)
					self.tableWidgetDetailDisplay.setRowCount(self.tableWidgetDetailDisplay.rowCount()+1)
					self.setTextDetailTable(self.tableWidgetDetailDisplay.rowCount(), detail)
			self.pushButtonValider.setEnabled(False)
			self.pushButtonModifier.setEnabled(True)
			self.pushButtonSupprimer.setEnabled(True)
			self.pushButtonAvant.setEnabled(True)
			self.pushButtonArriere.setEnabled(True)
			self.cursor.execute("SELECT max(codecommande) FROM entete")
			Max = self.cursor.fetchone()[0]
			if not Max: Max = 0
			self.index = Max
		except:
			QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Avant(self):
		self.cursor.execute("SELECT count(codecommande) FROM entete")
		lengh = self.cursor.fetchone()[0]
		if self.index<lengh-1:
			self.index += 1
			try:
				self.cursor.execute("SELECT * FROM entete ORDER BY codecommande")
				entete = self.cursor.fetchall()[self.index]
				self.cursor.execute("SELECT * FROM detail WHERE codecommande = %s ORDER BY idcommande", (entete[0], ))
				details = self.cursor.fetchall()
				self.setTextEntete(entete)
				self.tableWidgetDetailDisplay.setRowCount(0)
				if len(details):
					for detail in details:
						detail = [*detail]
						detail[5] = "{}-{}-{}".format(detail[5].year, detail[5].month, detail[5].day)
						self.tableWidgetDetailDisplay.setRowCount(self.tableWidgetDetailDisplay.rowCount()+1)
						self.setTextDetailTable(self.tableWidgetDetailDisplay.rowCount(), detail)
			except :
				QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Arriere(self):
		self.cursor.execute("SELECT count(codecommande) FROM entete")
		lengh = self.cursor.fetchone()[0]
		if self.index>0:
			self.index -= 1
			try:
				self.cursor.execute("SELECT * FROM entete ORDER BY codecommande")
				entete = self.cursor.fetchall()[self.index]
				self.cursor.execute("SELECT * FROM detail WHERE codecommande = %s ORDER BY idcommande", (entete[0], ))
				details = self.cursor.fetchall()
				self.setTextEntete(entete)
				self.tableWidgetDetailDisplay.setRowCount(0)
				if len(details):
					for detail in details:
						detail = [*detail]
						detail[5] = "{}-{}-{}".format(detail[5].year, detail[5].month, detail[5].day)
						self.tableWidgetDetailDisplay.setRowCount(self.tableWidgetDetailDisplay.rowCount()+1)
						self.setTextDetailTable(self.tableWidgetDetailDisplay.rowCount(), detail)
			except :
				QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Imprimer(self):
		entete = self.getTextEntete()
		entete = [*entete]
		self.cursor.execute("SELECT nomfournisseur FROM fournisseur WHERE codefournisseuri = %s", (entete[1], ))
		entete[1] = self.cursor.fetchone()[0]
		detail = self.getTextDetailTable()
		for i in range(len(detail)):
			detail[i] = [*detail[i]]
			self.cursor.execute("SELECT nomproduit FROM produit WHERE codeproduit = %s", (detail[i][1], ))
			detail[i][1] = self.cursor.fetchone()[0]
		printPDFEnteteDetail("entetedetail", entete, detail)

	def ImprimerTout(self):
		QMessageBox.information(self.widgetCentral, "Maintenance", "Entrain de develepement")

	def Visualiser(self):
		QMessageBox.information(self.widgetCentral, "Maintenance", "Entrain de develepement")
