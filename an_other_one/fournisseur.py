from FournisseurWidget import Ui_fournisseurWidget
from PyQt5.QtWidgets import QInputDialog, QMessageBox
#boite de dialogue d'impression
from boxDialogImprimer import DialogImprimer
#pour l'impression
from PrintFunction import printPDFFournisseur
import time
import random
#importation de fonction de verification des champs
from function.magicFunction import *
#pour la visualisation
from visualisation import VisualisationWidget


class FournisseurWidget(Ui_fournisseurWidget):
	def __init__(self, widgetCentral, db):
		#initialisation
		super(FournisseurWidget, self).__init__()
		self.setupUi(widgetCentral)
		self.widgetCentral.hide()

		#centralWidget lié avec la feunêtre et pas avec fournisseurwidget
		self.mainWidget = widgetCentral

		#la base de donnée
		self.db = db
		self.cursor = db.cursor()
		#initialisationdes champs
		self.Nouveau()

		#cet attribut donne l'information sur label qui est cliqué, None si aucune label cliqué
		self.labelClicked = None

		#index est la positionnement de enregistrement quand on utilise avant ou arriere
		#-l donne le dernier enregistrement
		self.index = -1

		self.visualisation = VisualisationWidget(widgetCentral, "fournisseur", self)

		#les evenement lié avec les label cliqué
		self.labelCodeFournisseuri.mousePressEvent = lambda a: self.ClickedWidget(self.labelCodeFournisseuri, "int")
		self.labelCodeFournisseur.mousePressEvent = lambda a: self.ClickedWidget(self.labelCodeFournisseur, "int")
		self.labelNomFournisseur.mousePressEvent = lambda a: self.ClickedWidget(self.labelNomFournisseur, "text")
		self.labelTel.mousePressEvent = lambda a: self.ClickedWidget(self.labelTel, "text")
		self.labelFax.mousePressEvent = lambda a: self.ClickedWidget(self.labelFax, "text")

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
		return (self.lineEdit_int_CodeFourmisseuri.text(),
				self.lineEdit_int_CodeFournisseur.text(),
				self.lineEdit_text_NomFournisseur.text(),
				self.lineEdit_text_Tel.text(),
				self.lineEdit_text_Fax.text())

	#setText remplie tous les champs par des valeur passé par argument
	def setText(self, text):
		self.lineEdit_int_CodeFourmisseuri.setText(str(text[0]))
		self.lineEdit_int_CodeFournisseur.setText(text[1])
		self.lineEdit_text_NomFournisseur.setText(text[2])
		self.lineEdit_text_Tel.setText(text[3])
		self.lineEdit_text_Fax.setText(text[4])

	#apropos les labels cliqué
	#clickedWidget renvoi le nom de label et mis en disposition le botton rechercher
	def ClickedWidget(self, widget, Type):
		self.pushButtonRechercher.setEnabled(True)
		self.labelClicked = "".join(widget.text().split(" "))+"_"+Type
		
	#en plus d'initialiser les champs par des valeurs par defaut
	#Nouveau desactivé les botton rechercher modifier supprimer avant et arriere
	#et activé le botton valider
	def Nouveau(self):
		self.cursor.execute("SELECT max(codefournisseuri) FROM fournisseur")
		Max = self.cursor.fetchone()[0]
		if not Max: Max = 0
		self.lineEdit_int_CodeFourmisseuri.setText(str(int(Max)+1))
		self.lineEdit_int_CodeFournisseur.setText("xxx")
		self.lineEdit_text_NomFournisseur.setText("xxx")
		self.lineEdit_text_Tel.setText("xxx")
		self.lineEdit_text_Fax.setText("xxx")
		self.pushButtonRechercher.setEnabled(False)
		self.pushButtonModifier.setEnabled(False)
		self.pushButtonSupprimer.setEnabled(False)
		self.pushButtonAvant.setEnabled(False)
		self.pushButtonArriere.setEnabled(False)
		self.pushButtonValider.setEnabled(True)

	#Valider sert à inserer les enregistrement
	def Valider(self):
		status = verification(self)
		if status:
			query = "INSERT INTO fournisseur VALUES (%s, %s, %s, %s, %s)"
			self.cursor.execute(query, self.getText())
			self.db.commit()
			self.Nouveau()
		else:
			QMessageBox.warning(self.widgetCentral, "Status de enregistrement", "L'enregistrement n'est pas effectué")

	#après le choix de critére de recherche
	#le botton recherer s'active et donne la possibilité
	#de donner le clé pour le critére
	#par la suite il active les botton modifier supprimer et desactive
	#le botton valider si il trouve des resultat
	#dans tous les cas le botton rechercher se desactive
	def Rechercher(self):
		cle, reponce = QInputDialog.getText(self.widgetCentral, "clé de recherche", "clé:")
		Type = self.labelClicked.split("_")[1]
		self.labelClicked = self.labelClicked.split("_")[0]
		if cle:
			if Type == "int" and not isInt(cle):
				QMessageBox.warning(self.widgetCentral, "Erreur", "le type de clé est incorrect")
			else:
				query = "SELECT * FROM fournisseur WHERE {}=%s".format(self.labelClicked,)
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
		
	#Modifier mettre à jou un enregistrement
	def Modifier(self):
		status = verification(self)
		if status:
			text = self.getText()
			query = "UPDATE fournisseur SET codefournisseur=%s , nomfournisseur=%s , tel=%s , fax=%s WHERE codefournisseuri=%s"
			self.cursor.execute(query, (*text[1:], text[0]))
			self.db.commit()
			QMessageBox.information(self.widgetCentral, "Modification", "Traitement effectué avec succes")
			self.Nouveau()
		else:
			QMessageBox.warning(self.widgetCentral, "Status de la modification", "La modification n'est pas effectué")

	#Supprimer supprime un enregistrement
	def Supprimer(self):
		text = self.getText()
		query = "DELETE FROM fournisseur WHERE codefournisseuri=%s"
		self.cursor.execute(query, (text[0]))
		self.db.commit()
		QMessageBox.information(self.widgetCentral, "Suppression", "Traitement effectué avec succes")
		self.Nouveau()

	#Premier affiche le premier enregistrement
	#si la base de donné et vide n'affiche rien
	#en plus elle active les botton avant et arriere
	#pour basculer dans les enregistrement
	def Premier(self):
		query = "SELECT * FROM fournisseur ORDER BY codefournisseuri"
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

	#Dernier affiche le dernier enregistrement
	#si la base de donné et vide n'affiche rien
	#en plus elle active les botton avant et arriere
	#pour basculer dans les enregistrement	
	def Dernier(self):
		query = "SELECT * FROM fournisseur ORDER BY codefournisseuri"
		self.cursor.execute(query)
		try:
			resultat = self.cursor.fetchall()[-1]
			self.setText(resultat)
			self.pushButtonValider.setEnabled(False)
			self.pushButtonModifier.setEnabled(True)
			self.pushButtonSupprimer.setEnabled(True)
			self.pushButtonAvant.setEnabled(True)
			self.pushButtonArriere.setEnabled(True)
			self.cursor.execute("SELECT max(codefournisseuri) FROM fournisseur")
			Max = self.cursor.fetchone()[0]
			if not Max: Max = 0
			self.index = Max
		except:
			QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	#Avant nous permet de basculer vers l'enregistrement suivant
	def Avant(self):
		query = "SELECT * FROM fournisseur ORDER BY codefournisseuri"
		self.cursor.execute("SELECT count(codefournisseuri) FROM fournisseur")
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

	#Arriere nous permet de basculer vers l'enregistrement precedent
	def Arriere(self):
		query = "SELECT * FROM fournisseur ORDER BY codefournisseuri"
		self.cursor.execute(query)
		if self.index > 0:
			self.index -= 1
			try:
				resultat = self.cursor.fetchall()[self.index]
				self.setText(resultat)
				self.pushButtonValider.setEnabled(False)
				self.pushButtonModifier.setEnabled(True)
				self.pushButtonSupprimer.setEnabled(True)
			except:
				QMessageBox.warning(self.widgetCentral, "Attention", "Il n'y a pas d'enregistrement")

	def Imprimer(self):
		DialogImprimer(self.getText(), "fournisseur", "fournisseur").exec()

	def ImprimerTout(self):
		query = "SELECT * FROM fournisseur ORDER BY codefournisseuri"
		self.cursor.execute(query)
		resultats = self.cursor.fetchall()
		if resultats:
			for resultat in resultats:
				try:
					title = "impression\\fournisseur_{}.pdf".format(time.strftime("%Y%m%d%H%M%S")+str(random.randint(1, 100000)))
					printPDFFournisseur.render(resultat, title)
				except :
					pass
			QMessageBox.information(self.widgetCentral, "Impression", "l'ensemble des donné sont imprimées")

	def Visualiser(self):
		self.widgetCentral.close()
		self.visualisation.widgetCentral.show()
