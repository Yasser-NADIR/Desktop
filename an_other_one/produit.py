from ProduitWidget import Ui_ProduitWidget
from PyQt5.QtWidgets import QInputDialog, QMessageBox
#boite de dialogue d'impression
from boxDialogImprimer import DialogImprimer
#pour l'impression
from PrintFunction import printPDFProduit
import random
import time
import os
#importation de fonction de verification des champs
from function.magicFunction import *
#pour la visualisation
from visualisation import VisualisationWidget

class ProduitWidget(Ui_ProduitWidget):
	def __init__(self, widgetCentral, db):
		super(ProduitWidget, self).__init__()
		self.setupUi(widgetCentral)
		self.widgetCentral.close()

		self.db = db
		self.cursor = db.cursor()

		#initialisationdes champs
		self.Nouveau()

		#cet attribut donne l'information sur label qui est cliqué, None si aucune label cliqué
		self.labelClicked = None

		#index est la positionnement de enregistrement quand on utilise avant ou arriere
		#-l donne le dernier enregistrement
		self.index = -1

		self.visualisation = VisualisationWidget(widgetCentral, "produit", self)

		#les evenement lié avec les label cliqué
		self.labelCodeProduit.mousePressEvent = lambda a: self.ClickedWidget(self.labelCodeProduit, "int")
		self.labelCodeFamilleProduit.mousePressEvent = lambda a: self.ClickedWidget(self.labelCodeFamilleProduit, "int")
		self.labelNomProduit.mousePressEvent = lambda a: self.ClickedWidget(self.labelNomProduit, "tex")

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

	#les fonctions intermidiaire
	#getText donne le contenue de tout les champ
	def getText(self):
		return (self.lineEdit_int_CodeProduit.text(),
				self.comboBoxCodeFamilleProduit.currentText(),
				self.lineEdit_text_NomProduit.text())

	#setText remplie tous les champs par des valeur passé par argument
	def setText(self, text):
		text = [*text]
		self.cursor.execute("SELECT nomfamilleproduit FROM familleproduit WHERE codefamilleproduit = %s", (text[1], ))
		text[1] = self.cursor.fetchone()[0]

		self.lineEdit_int_CodeProduit.setText(str(text[0]))
		self.comboBoxCodeFamilleProduit.setCurrentText(text[1])
		self.lineEdit_text_NomProduit.setText(text[2])

	def ClickedWidget(self, widget, Type):
		self.pushButtonRechercher.setEnabled(True)
		self.labelClicked = "".join(widget.text().split(" "))+"_"+Type

	#pour initialiser le combobox codefamilleproduit
	def initComboBox(self):
		self.cursor.execute("SELECT nomfamilleproduit from familleproduit ORDER BY nomfamilleproduit")
		codes = self.cursor.fetchall()
		#en premier pas en supprime la liste qui deja existe
		nbrMax = self.comboBoxCodeFamilleProduit.count()
		for i in range(nbrMax):
			self.comboBoxCodeFamilleProduit.removeItem(0)
		#après on remplie le combobox
		for code in codes:
			self.comboBoxCodeFamilleProduit.addItem(str(*code))



	def Nouveau(self):
		self.cursor.execute("SELECT max(codeproduit) FROM produit")
		Max = self.cursor.fetchone()[0]
		if not Max: Max = 0
		self.lineEdit_int_CodeProduit.setText(str(int(Max)+1))
		self.initComboBox()
		self.lineEdit_text_NomProduit.setText("xxx")
		self.pushButtonRechercher.setEnabled(False)
		self.pushButtonModifier.setEnabled(False)
		self.pushButtonSupprimer.setEnabled(False)
		self.pushButtonAvant.setEnabled(False)
		self.pushButtonArriere.setEnabled(False)
		self.pushButtonValider.setEnabled(True)

	def Valider(self):
		status = verification(self)
		if status:
			query = "INSERT INTO produit VALUES (%s, %s, %s)"
			data = self.getText()
			data = [*data]
			self.cursor.execute("SELECT codefamilleproduit from familleproduit WHERE nomfamilleproduit = %s", (data[1],))
			data[1] = self.cursor.fetchone()[0]
			self.cursor.execute(query, data)
			self.db.commit()
			self.Nouveau()
		else:
			QMessageBox.warning(self.widgetCentral, "Status de enregistrement", "L'enregistrement n'est pas effectué")

	def Rechercher(self):
		cle, reponce = QInputDialog.getText(self.widgetCentral, "clé de recherche", "clé:")
		Type = self.labelClicked.split("_")[1]
		self.labelClicked = self.labelClicked.split("_")[0]
		if cle:
			if Type == "int" and not isInt(cle):
				QMessageBox.warning(self.widgetCentral, "Erreur", "le type de clé est incorrect")
			else:
				query = "SELECT * FROM produit WHERE {}=%s".format(self.labelClicked,)
				self.cursor.execute(query, (cle, ))
				resultat = self.cursor.fetchone()
				if resultat: 
					#premier indice et le dernier indice reference le code produit et le nom produit
					self.setText(resultat)
					self.pushButtonValider.setEnabled(False)
					self.pushButtonModifier.setEnabled(True)
					self.pushButtonSupprimer.setEnabled(True)
				else:
					QMessageBox.information(self.widgetCentral, "Resultat", "La valeur n'existe pas")

				self.labelClicked = None
		self.pushButtonRechercher.setEnabled(False)

	def Modifier(self):
		status = verification(self)
		if status:
			text = self.getText()
			query = "UPDATE produit SET codefamilleproduit=%s , nomproduit=%s WHERE codeproduit=%s"
			self.cursor.execute(query, (*text[1:], text[0]))
			self.db.commit()
			QMessageBox.information(self.widgetCentral, "Modification", "Traitement effectué avec succes")
			self.Nouveau()
		else:
			QMessageBox.warning(self.widgetCentral, "Status de la modification", "La modification n'est pas effectué")

	def Supprimer(self):
		text = self.getText()
		query = "DELETE FROM produit WHERE codeproduit=%s"
		self.cursor.execute(query, (text[0]))
		self.db.commit()
		QMessageBox.information(self.widgetCentral, "Suppression", "Traitement effectué avec succes")
		self.Nouveau()

	def Premier(self):
		query = "SELECT * FROM produit ORDER BY codeproduit"
		self.cursor.execute(query)
		try:
			resultat = self.cursor.fetchall()[0]
			self.setText(resultat)
			self.pushButtonValider.setEnabled(False)
			self.pushButtonModifier.setEnabled(True)
			self.pushButtonSupprimer.setEnabled(True)
			self.pushButtonAvant.setEnabled(True)
			self.pushButtonArriere.setEnabled(True)
			self.index = 0
		except:
			QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Dernier(self):
		query = "SELECT * FROM produit ORDER BY codeproduit"
		self.cursor.execute(query)
		try:
			resultat = self.cursor.fetchall()[-1]
			self.setText(resultat)
			self.pushButtonValider.setEnabled(False)
			self.pushButtonModifier.setEnabled(True)
			self.pushButtonSupprimer.setEnabled(True)
			self.pushButtonAvant.setEnabled(True)
			self.pushButtonArriere.setEnabled(True)
			self.cursor.execute("SELECT max(codeproduit) FROM produit")
			Max = self.cursor.fetchone()[0]
			if not Max: Max = 0
			self.index = Max
		except:
			QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Avant(self):
		query = "SELECT * FROM produit ORDER BY codeproduit"
		self.cursor.execute("SELECT count(codeproduit) FROM produit")
		lengh = self.cursor.fetchone()[0]
		self.cursor.execute(query)
		if self.index <lengh-1:
			self.index +=1
			try:
				resultat = self.cursor.fetchall()[self.index]
				self.setText(resultat)
				self.pushButtonValider.setEnabled(False)
				self.pushButtonModifier.setEnabled(True)
				self.pushButtonSupprimer.setEnabled(True)
			except:
				QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Arriere(self):
		query = "SELECT * FROM produit ORDER BY codeproduit"
		self.cursor.execute(query)
		if self.index > 0:
			self.index -=1
			try:
				resultat = self.cursor.fetchall()[self.index]
				self.setText(resultat)
				self.pushButtonValider.setEnabled(False)
				self.pushButtonModifier.setEnabled(True)
				self.pushButtonSupprimer.setEnabled(True)
			except:
				QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Imprimer(self):
		DialogImprimer(self.getText(), "produit", "produit").exec()

	def ImprimerTout(self):
		query = "SELECT * FROM produit ORDER BY codeproduit"
		self.cursor.execute(query)
		resultats = self.cursor.fetchall()
		if resultats:
			for resultat in resultats:
				try:
					title = "impression\\produit_{}".format(time.strftime("%Y%m%d%H%M%S")+str(random.randint(1, 10000)))
					printPDFProduit.render(resultat, title)
				except:
					pass
			QMessageBox.information(self.widgetCentral, "Impression", "l'ensemble des donné sont imprimées")

	def Visualiser(self):
		self.widgetCentral.close()
		self.visualisation.widgetCentral.show()
