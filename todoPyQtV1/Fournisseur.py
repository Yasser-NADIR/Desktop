from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from valideWidget import ValiderWidget
from PyQt5.QtCore import pyqtSlot
from FournisseurWidget import Ui_FounisseurValideWidget
from rechercherWidget import Rechercher
from modifierWidget import ModifierWidget
from supprimerWidget import SupprimerWidget
from defilerWidget import DefilerWidget
from afficherWidget import AfficherWidget
from imprimerWidget import ImprimerWidget
import psycopg2

class fournisseurWidget(Ui_FounisseurValideWidget):
	def __init__(self, centralwidget):
		super(fournisseurWidget, self).__init__()

		self.centralwidget = centralwidget
		self.widget = QWidget(centralwidget)
		self.setupUi(self.widget)
		self.widget.close()
		self.widgets = {}
		self.db = psycopg2.connect(
				host = "localhost",
				database = "dbApp",
				user = "postgres",
				password = "azerty"
			)
		self.cursor = self.db.cursor()

		self.valideWidget = ValiderWidget(self.widgetCentredFournisseur)
		self.widgets["valide"] = [1, self.valideWidget]
		self.rechercherWidget = Rechercher(self.widgetCentredFournisseur, self.cursor)
		self.widgets["rechercher"] = [0, self.rechercherWidget]
		self.modifierWidget = ModifierWidget(self.widgetCentredFournisseur, self.db)
		self.widgets["modifier"] = [0, self.modifierWidget]
		self.supprimerWidget = SupprimerWidget(self.widgetCentredFournisseur, self.db)
		self.widgets["supprimer"] = [0, self.supprimerWidget]
		self.defilerWidget = DefilerWidget(self.widgetCentredFournisseur, self.cursor)
		self.widgets["defiler"] = [0, self.defilerWidget]
		self.afficherWidget = AfficherWidget(self.widgetCentredFournisseur, self.cursor)
		self.widgets["afficher"] = [0, self.afficherWidget]
		self.imprimerWidget = ImprimerWidget(self.widgetCentredFournisseur, self.cursor)
		self.widgets["imprimer"] = [0, self.imprimerWidget]
		self.pushButtonSortir.clicked.connect(self.widget.close)

		self.pushButtonNouveau.clicked.connect(self.Nouveau)
		self.pushButtonValider.clicked.connect(self.Valider)
		self.pushButtonRechercher.clicked.connect(self.Rechercher)
		self.pushButtonModifier.clicked.connect(self.Modifier)
		self.pushButtonSupprimer.clicked.connect(self.Supprimer)
		self.pushButtonDernier.clicked.connect(self.Dernier)
		self.pushButtonPremier.clicked.connect(self.Premier)
		self.pushButtonDefilerArrier.clicked.connect(self.Arrier)
		self.pushButtonDefilerAvant.clicked.connect(self.Avant)
		self.pushButtonAfficher.clicked.connect(self.Afficher)
		self.pushButtonImprimer.clicked.connect(self.Imprimer)

		self.defilerWidget.pushButtonModifer.clicked.connect(self.defilerWigetSetToModifierWidget)
		self.defilerWidget.pushButtonSupprimer.clicked.connect(self.defilerWigetSetToSupprimerWidget)

	def displayWidget(self, widgetName):
		if self.widgets[widgetName][0] == 0:
			for key, value in self.widgets.items():
				if value[0] == 1:
					self.widgets[key][0] = 0
					self.widgets[key][1].widget.close()
					self.widgets[widgetName][0] = 1
					self.widgets[widgetName][1].widget.show()
					break

	def Nouveau(self):
		self.displayWidget("valide")
		self.valideWidget.cleanText()


	def Valider(self):
		if self.widgets["valide"]:
			data = self.valideWidget.getText()
			for d in data :
				if not d: return
			self.cursor.execute("INSERT INTO dbfournisseur VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
			self.db.commit()
			self.Nouveau()

	def Rechercher(self):
		if self.widgets["rechercher"][0] == 0:
			self.rechercherWidget.cleanTable()
		self.displayWidget("rechercher")
		

	def Modifier(self):
		if self.widgets["modifier"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("modifier")

	def Supprimer(self):
		if self.widgets["supprimer"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("supprimer")

	def Dernier(self):
		if self.widgets["defiler"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("defiler")
		self.defilerWidget.getData()
		self.defilerWidget.setText(self.defilerWidget.getLastData())

	def Premier(self):
		if self.widgets["defiler"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("defiler")
		self.defilerWidget.getData()
		self.defilerWidget.setText(self.defilerWidget.getFirstData())

	def Arrier(self):
		if self.widgets["defiler"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("defiler")
		self.defilerWidget.getData()
		self.defilerWidget.setText(self.defilerWidget.getpreviousData())

	def Avant(self):
		if self.widgets["defiler"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("defiler")
		self.defilerWidget.getData()
		self.defilerWidget.setText(self.defilerWidget.getNextData())

	def defilerWigetSetToModifierWidget(self):
		self.Modifier()
		self.modifierWidget.setText(self.defilerWidget.getDataByIndex())

	def defilerWigetSetToSupprimerWidget(self):
		self.Supprimer()
		self.supprimerWidget.setText(self.defilerWidget.getDataByIndex())

	def Afficher(self):
		if self.widgets["afficher"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("afficher")
		self.afficherWidget.setData()

	def Imprimer(self):
		if self.widgets["imprimer"][0] == 0:
			self.modifierWidget.cleanText()
		self.displayWidget("imprimer")
		self.imprimerWidget.writeOnExel()
		