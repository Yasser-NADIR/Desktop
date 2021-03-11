from Entete_Detial import Ui_EnteteDetail
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QTableWidgetItem

class EnteteDetail(Ui_EnteteDetail):
	def __init__(self, widgetCentral, db):
		super(EnteteDetail, self).__init__()
		self.setupUi(widgetCentral)
		self.widgetCentral.close()

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
		
		self.label_code_cmd.mousePressEvent = lambda a: self.ClickedWidget(self.label_code_cmd, "int")
		#liaison des evenements
		self.pushButtonNouveau.clicked.connect(self.Nouveau)
		self.pushButtonValider.clicked.connect(self.Valider)
		self.pushButtonRechercher.clicked.connect(self.Rechercher)
		"""
		self.pushButtonModifier.clicked.connect(self.Modifier)
		self.pushButtonSupprimer.clicked.connect(self.Supprimer)
		self.pushButtonPremier.clicked.connect(self.Premier)
		self.pushButtonDernier.clicked.connect(self.Dernier)
		self.pushButtonAvant.clicked.connect(self.Avant)
		self.pushButtonArriere.clicked.connect(self.Arriere)
		self.pushButtonImprimer.clicked.connect(self.Imprimer)
		self.pushButtonImprimerTout.clicked.connect(self.ImprimerTout)
		self.pushButtonVisualiser.clicked.connect(self.Visualiser)
		"""
		#calcule prix global quand on modifie le prix unitaire ou la quantité
		self.lineEdit_int_Quantitedemd.textChanged.connect(self.calculTotalPrix)
		self.lineEdit_real_prix_unitaire.textChanged.connect(self.calculTotalPrix)
	
		#les bottons qui manipulent la partie detail
		self.pushButtonAjouterDetail.clicked.connect(self.AjouterDetail)
		self.pushButtonModifierDetail.clicked.connect(self.ModiferDetail)
		self.pushButtonSupprimerDetail.clicked.connect(self.SupprimerDetail)
		"""
		self.pushButtonInsererDetail.clicked.connect(self.InsererDetail)
		self.pushButtonEffacerDetail.clicked.connect(self.EffacerDetail)
		"""
		#quand il faut activer modifier et supprimer detail
		#quand un item de tableau est selectionné
		self.tableWidgetViewDetail.cellClicked.connect(self.CellClicked)

	#les fonctions intermidiaire
	#getText donne le contenue de tout les champ de l'entete
	def getTextEntete(self):
		#self.cursor.execute("SELECT code_frnsi FROM t_frns WHERE nom_frns=%s", (self.comboBox_code_frnsi.currentText(), ))
		#code_frnsi = self.cursor.fetchone()[0]
		#self.cursor.execute("SELECT code_societe FROM t_societe WHERE code_societe=%s", (self.comboBox_code_societe.currentText(), ))
		#code_societe = self.cursor.fetchone()[0]
		return (self.lineEdit_int_code_cmd.text(),
				self.lineEdit_text_refmarche.text(),
				1,
				1,
				"{}-{}-{}".format(self.dateEdit_date_cmd.date().year(), self.dateEdit_date_cmd.date().month(), self.dateEdit_date_cmd.date().day()),
				self.lineEdit_text_flag.text(),
				self.lineEdit_text_remarques.text(),
				self.lineEdit_text_util_ENT_cmd.text(),
				self.lineEdit_text_flag_ENT_cmd.text(),
				self.lineEdit_text_remarque_ENT_cmd.text(),
				)

	#setText remplie tous les champs de l'entete par des valeur passé par argument
	def setTextEntete(self, text):
		self.lineEdit_int_code_cmd.setText(text[0])
		self.lineEdit_text_refmarche.setText(text[1])
		self.dateEdit_date_cmd.setDate(QDate(text[4].year, text[4].month, text[4].day))
		self.lineEdit_text_flag.setText(text[5])
		self.lineEdit_text_remarques.setText(text[6])
		self.lineEdit_text_util_ENT_cmd.setText(text[7])
		self.lineEdit_text_flag_ENT_cmd.setText(text[8])
		self.lineEdit_text_remarque_ENT_cmd.setText(text[9])

	def getTextDetailTable(self):
		rows = []
		nbrRow = self.tableWidgetViewDetail.rowCount()
		for i in range(nbrRow):
			row = []
			for j in range(self.tableWidgetViewDetail.columnCount()):
				row.append(self.tableWidgetViewDetail.item(i, j).text())
			rows.append(row)
		return rows

	def setTextDetailTable(self, row, text):
		for i in range(len(text)):
			self.tableWidgetViewDetail.setItem(row-1, i, QTableWidgetItem(str(text[i])))

	def getTextDetail(self):
		#self.cursor.execute("SELECT code_produit FROM t_produits WHERE code_produit = %s", (self.comboBox_code_produit.currentText(), ))
		#code_produit = self.cursor.fetchone()[0]
		#self.cursor.execute("SELECT code_unite FROM t_unite WHERE code_unite = %s", (self.comboBox_code_unite.currentText(), ))
		#code_unite = self.cursor.fetchone()[0]
		return (self.lineEdit_int_ld_cmd.text(),
		1,
		self.lineEdit_int_Quantitedemd.text(),
		self.lineEdit_float_prix_global.text(),
		"{}-{}-{}".format(self.dateEdit_dat_liv_souhaitee.date().year(), self.dateEdit_dat_liv_souhaitee.date().month(), self.dateEdit_dat_liv_souhaitee.date().day()),
		1,
		self.lineEdit_real_prix_unitaire.text(),
		self.lineEdit_text_remarq.text(),
		self.lineEdit_text_util_DET_cmd.text(),
		self.lineEdit_text_flag_DET_cmd.text(),
		self.lineEdit_remarque_DET_cmd.text()
		)
		

	def setTextDetail(self, text):
		self.lineEdit_int_ld_cmd.setText(text[0])
		self.comboBox_code_produit.setCurrentText(text[1])
		self.lineEdit_int_Quantitedemd.setText(text[2])
		self.lineEdit_real_prix_unitaire.setText(text[3])
		self.dateEdit_dat_liv_souhaitee.setDate(QDate(int(text[4].split("-")[0]), int(text[4].split("-")[1]), int(text[4].split("-")[2])))
		self.comboBox_code_unite.setCurrentText(text[5])
		self.lineEdit_float_prix_global.setText(text[6])
		self.lineEdit_text_remarq.setText(text[7])
		self.lineEdit_text_util_DET_cmd.setText(text[8])
		self.lineEdit_text_flag_DET_cmd.setText(text[9])
		self.lineEdit_remarque_DET_cmd.setText(text[10])

	def ClickedWidget(self, widget, Type):
		self.pushButtonRechercher.setEnabled(True)
		self.labelClicked = widget.text()+"_"+Type

	def initComboBoxFournisseur(self):
		self.cursor.execute("SELECT nom_frns FROM t_frns ORDER BY nom_frns")
		codes = self.cursor.fetchall()
		countMax = self.comboBox_code_frnsi.count()
		for _ in range(countMax):
			self.comboBox_code_frnsi.removeItem(0)
		for code in codes:
			self.comboBox_code_frnsi.addItem(str(code[0]))

	def initComboBoxSociete(self):
		self.cursor.execute("SELECT nom_societe FROM t_societe ORDER BY nom_societe")
		codes = self.cursor.fetchall()
		countMax = self.comboBox_code_societe.count()
		for _ in range(countMax):
			self.comboBox_code_societe.removeItem(0)
		for code in codes:
			self.comboBox_code_societe.addItem(str(code[0]))

	def initComboBoxProduit(self):
		self.cursor.execute("SELECT nom_produit FROM t_produits ORDER BY nom_produit")
		codes = self.cursor.fetchall()
		countMax = self.comboBox_code_produit.count()
		for _ in range(countMax):
			self.comboBox_code_produit.removeItem(0)
		for code in codes:
			self.comboBox_code_produit.addItem(str(code[0]))

	def initComboBoxUnite(self):
		self.cursor.execute("SELECT libelle_unite FROM t_unite ORDER BY libelle_unite")
		codes = self.cursor.fetchall()
		countMax = self.comboBox_code_unite.count()
		for _ in range(countMax):
			self.comboBox_code_unite.removeItem(0)
		for code in codes:
			self.comboBox_code_unite.addItem(str(code[0]))

	#initialiser l'entete
	def initEntete(self):
		self.cursor.execute("SELECT max(code_cmd) FROM ent_cmd")
		Max = self.cursor.fetchone()[0]
		if not Max: Max = 0
		self.lineEdit_int_code_cmd.setText(str(int(Max)+1))
		self.initComboBoxFournisseur()
		self.initComboBoxSociete()
		self.lineEdit_text_refmarche.setText("xxx")
		self.lineEdit_text_flag.setText("xxx")
		self.lineEdit_text_remarques.setText("xxx")
		self.lineEdit_text_util_ENT_cmd.setText("xxx")
		self.lineEdit_text_flag_ENT_cmd.setText("xxx")
		self.lineEdit_text_remarque_ENT_cmd.setText("xxx")

	#initialiser detail
	def initDetail(self):
		self.lineEdit_int_ld_cmd.setText("1"),
		self.lineEdit_int_Quantitedemd.setText("0"),
		self.lineEdit_real_prix_unitaire.setText("0"),
		self.lineEdit_float_prix_global.setText("0")
		self.lineEdit_text_remarq.setText("xxxx"),
		self.lineEdit_text_util_DET_cmd.setText("xxxx"),
		self.lineEdit_text_flag_DET_cmd.setText("xxxx"),
		self.lineEdit_remarque_DET_cmd.setText("xxxxx")
		self.initComboBoxUnite()
		self.initComboBoxProduit()
		self.tableWidgetViewDetail.setRowCount(0)

	def calculTotalPrix(self, text):
    	#after importing magicfunction module
		"""
		if isFloat(self.lineEdit_real_prix_unitaire.text()) and isFloat(self.lineEdit_int_Quantitedemd.text()):
			prixUnitaire = float(self.lineEdit_real_prix_unitaire.text())
			quantite = float(self.lineEdit_int_Quantitedemd.text())
			resultat = int(prixUnitaire*quantite*100)/100.0
			self.lineEdit_real_prix_global.setText(str(resultat))
		"""
		try:
			prixUnitaire = float(self.lineEdit_real_prix_unitaire.text())
			quantite = float(self.lineEdit_int_Quantitedemd.text())
			resultat = int(prixUnitaire*quantite*100)/100.0
			self.lineEdit_float_prix_global.setText(str(resultat))
		except:
			self.lineEdit_float_prix_global.setText("0")
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
		self.tableWidgetViewDetail.setRowCount(self.tableWidgetViewDetail.rowCount()+1)
		row = self.tableWidgetViewDetail.rowCount()
		self.setTextDetailTable(row, data)
		self.lineEdit_int_ld_cmd.setText(str(int(self.lineEdit_int_ld_cmd.text())+1))
		self.tableWidgetViewDetail.sortItems(0)

	def ModiferDetail(self):
		row = []
		for i in range(self.tableWidgetViewDetail.columnCount()):
			row.append(self.tableWidgetViewDetail.item(self.selectedRow, i).text())
		self.setTextDetail(row)
		self.tableWidgetViewDetail.removeRow(self.selectedRow)
		if not self.pushButtonRechercher.isEnabled(): self.pushButtonAjouterDetail.setEnabled(True)
		self.pushButtonModifierDetail.setEnabled(False)
		self.pushButtonSupprimerDetail.setEnabled(False)
		self.pushButtonInsererDetail.setEnabled(False)
		if self.pushButtonRechercher.isEnabled(): self.pushButtonInsererDetail.setEnabled(True)

	def SupprimerDetail(self):
		
		for i in range(self.tableWidgetViewDetail.rowCount()):
			self.tableWidgetViewDetail.setItem(i, 0, QTableWidgetItem(str(i+1)))
		self.tableWidgetViewDetail.removeRow(self.selectedRow)
		self.lineEdit_int_ld_cmd.setText(str(int(self.tableWidgetViewDetail.rowCount())+1))
		for i in range(self.tableWidgetViewDetail.rowCount()):
    			self.tableWidgetViewDetail.setItem(i, 0, QTableWidgetItem(str(i+1)))
		if not self.pushButtonRechercher.isEnabled(): self.pushButtonAjouterDetail.setEnabled(True)
		self.pushButtonModifierDetail.setEnabled(False)
		self.pushButtonSupprimerDetail.setEnabled(False)
		self.pushButtonInsererDetail.setEnabled(False)

	def InsererDetail(self):
		query = "INSERT INTO det_cmd VALUES (%s, %s, %s, %s, %s, %s, %s)"
		data = [*self.getTextDetail(), self.getTextEntete()[0]]
		self.cursor.execute(query, data)
		self.db.commit()
		self.AjouterDetail()

	def EffacerDetail(self):
		codecommande = self.lineEdit_int_code_cmd.text()
		idcommande = self.tableWidgetViewDetail.item(self.selectedRow, 0).text()
		self.cursor.execute("DELETE FROM det_cmd WHERE id_cmd=%s AND fk_cmd=%s", (idcommande, codecommande))
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
		query = "INSERT INTO ent_cmd VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		self.cursor.execute(query, self.getTextEntete())
		
		query = "INSERT INTO det_cmd VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		for data in self.getTextDetailTable():
			data.append(str(self.lineEdit_int_code_cmd.text()))
			self.cursor.execute(query, data)
		self.db.commit()
		self.Nouveau()

	def Rechercher(self):
		cle, reponce = QInputDialog.getText(self.widgetCentral, "clé de recherche", "clé:")
		Type = self.labelClicked.split("_")[-1]
		self.labelClicked = "_".join((self.labelClicked.split("_")[0], self.labelClicked.split("_")[1]))
		if cle:
			query = "SELECT * FROM ent_cmd WHERE {}=%s".format(self.labelClicked,)
			self.cursor.execute(query, (cle, ))
			entete = self.cursor.fetchone()
			query = "SELECT * FROM det_cmd WHERE fk_cmd=%s"
			self.cursor.execute(query, (cle, ))
			details = self.cursor.fetchall()
			print(entete)
			for d in details:
				print(d)
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
			"""
			try:
				int(cle)
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
			except:
				QMessageBox.warning(self.widgetCentral, "Erreur", "le type de clé est incorrect")
				self.labelClicked = None
		self.pushButtonRechercher.setEnabled(False)
		"""
"""
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
		pass
	def ImprimerTout(self):
		QMessageBox.information(self.widgetCentral, "Maintenance", "Entrain de develepement")

	def Visualiser(self):
		QMessageBox.information(self.widgetCentral, "Maintenance", "Entrain de develepement")

"""