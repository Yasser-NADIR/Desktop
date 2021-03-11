from FamilleProduitWidget import Ui_FamilleProduitWidget
from PyQt5.QtWidgets import QInputDialog
#boite de dialogue d'impression
from boxDialogImprimer import DialogImprimer
#pour l'impression
from PrintFunction import printPDFFamilleProduit
#importation de fonction de verification des champs
from function.magicFunction import *
import time
import random
#pour la visualisation
from visualisation import VisualisationWidget

class FamilleProduitWidget(Ui_FamilleProduitWidget):
	def __init__(self, widgetCentral, db):
		super(FamilleProduitWidget, self).__init__()
		self.setupUi(widgetCentral)
		self.widgetCentral.close()

		#la base de donnée
		self.db = db
		self.cursor = db.cursor()

		#cet attribut donne l'information sur label qui est cliqué, None si aucune label cliqué
		self.labelClicked = None

		self.Nouveau()

		#index est la positionnement de enregistrement quand on utilise avant ou arriere
		#-l donne le dernier enregistrement
		self.index = -1

		self.visualisation = VisualisationWidget(widgetCentral, "familleproduit", self)

		#les evenement lié avec les label cliqué
		self.labelFamilleProduit.mousePressEvent = lambda a: self.ClickedWidget(self.labelFamilleProduit, "int")
		self.labelNomFamilleProduit.mousePressEvent = lambda a: self.ClickedWidget(self.labelNomFamilleProduit, "text")

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
		return (self.lineEdit_int_CodeFamilleProduit.text(),
				self.lineEdit_text_NomFamilleProduit.text())

	#setText remplie tous les champs par des valeur passé par argument
	def setText(self, text):
		self.lineEdit_int_CodeFamilleProduit.setText(str(text[0]))
		self.lineEdit_text_NomFamilleProduit.setText(text[1])

	#apropos les labels cliqué
	#clickedWidget renvoi le nom de label et mis en disposition le botton rechercher
	def ClickedWidget(self, widget, Type):
		self.pushButtonRechercher.setEnabled(True)
		self.labelClicked = "".join(widget.text().split(" "))+"_"+Type

	def Nouveau(self):
		self.cursor.execute("SELECT max(codefamilleproduit) FROM familleproduit")
		Max = self.cursor.fetchone()[0]
		if not Max: Max = 0
		self.lineEdit_int_CodeFamilleProduit.setText(str(int(Max)+1))
		self.lineEdit_text_NomFamilleProduit.setText("xxx")
		self.pushButtonRechercher.setEnabled(False)
		self.pushButtonModifier.setEnabled(False)
		self.pushButtonSupprimer.setEnabled(False)
		self.pushButtonAvant.setEnabled(False)
		self.pushButtonArriere.setEnabled(False)
		self.pushButtonValider.setEnabled(True)


	def Valider(self):
		status = verification(self)
		if status:
			query = "INSERT INTO familleproduit(codefamilleproduit, nomfamilleproduit) VALUES (%s, %s)"
			self.cursor.execute(query, self.getText())
			self.db.commit()
			self.Nouveau()
		else:
			QMessageBox.warning(self.widgetCentral, "Status de enregistrement", "l'enregistrement n'est pas effectué")

	def Rechercher(self):
		cle, reponce = QInputDialog.getText(self.widgetCentral, "clé de recherche", "clé:")
		Type = self.labelClicked.split("_")[1]
		self.labelClicked = self.labelClicked.split("_")[0]
		if cle:
			if Type == "int" and not isInt(cle):
				QMessageBox.warning(self.widgetCentral, "Erreur", "le type de clé est incorrect")
			else:
				query = "SELECT * FROM familleproduit WHERE {}=%s".format(self.labelClicked,)
				self.cursor.execute(query, (cle, ))
				resultat = self.cursor.fetchone()
				if resultat: 
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
			query = "UPDATE familleproduit SET nomfamilleproduit=%s WHERE codefamilleproduit=%s"
			self.cursor.execute(query, (*text[1:], text[0]))
			self.db.commit()
			QMessageBox.information(self.widgetCentral, "Modification", "Traitement effectué avec succes")
			self.Nouveau()
		else:
			QMessageBox.warning(self.widgetCentral, "Status de la modification", "La modification n'est pas effectué")

	def Supprimer(self):
		text = self.getText()
		query = "DELETE FROM familleproduit WHERE codefamilleproduit=%s"
		self.cursor.execute(query, (text[0]))
		self.db.commit()
		QMessageBox.information(self.widgetCentral, "Suppression", "Traitement effectué avec succes")
		self.Nouveau()

	def Premier(self):
		query = "SELECT * FROM familleproduit ORDER BY codefamilleproduit"
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
		query = "SELECT * FROM familleproduit ORDER BY codefamilleproduit"
		self.cursor.execute(query)
		try:
			resultat = self.cursor.fetchall()[-1]
			self.setText(resultat)
			self.pushButtonValider.setEnabled(False)
			self.pushButtonModifier.setEnabled(True)
			self.pushButtonSupprimer.setEnabled(True)
			self.pushButtonAvant.setEnabled(True)
			self.pushButtonArriere.setEnabled(True)
			self.cursor.execute("SELECT max(codefamilleproduit) FROM familleproduit")
			Max = self.cursor.fetchone()[0]
			if not Max: Max = 0
			self.index = Max
		except:
			QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Avant(self):
		query = "SELECT * FROM familleproduit ORDER BY codefamilleproduit"
		self.cursor.execute("SELECT count(codefamilleproduit) FROM familleproduit")
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
		query = "SELECT * FROM familleproduit ORDER BY codefamilleproduit"
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
		DialogImprimer(self.getText(), "familleproduit", "familleproduit").exec()

	def ImprimerTout(self):
		query = "SELECT * FROM familleproduit ORDER BY codefamilleproduit"
		self.cursor.execute(query)
		resultats = self.cursor.fetchall()
		if resultats:
			for resultat in resultats:
				try:
					title = "impression\\familleproduit_{}.pdf".format(time.strftime("%Y%m%d%H%M%S")+str(randomr.randint(1, 10000)))
					printPDFFamilleProduit.render(resultat, title)
					time.sleep(1)
				except:
					pass
			QMessageBox.information(self.widgetCentral, "Impression", "l'ensemble des donné sont imprimées")
		
	def Visualiser(self):
		self.widgetCentral.close()
		self.visualisation.widgetCentral.show()
		