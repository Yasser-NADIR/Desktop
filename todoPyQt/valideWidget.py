from FournisseurValideWidget import Ui_FounisseurValideWidget
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
import os
import webbrowser


class ValiderWidget(Ui_FounisseurValideWidget):
	def __init__(self, widget):
		super(ValiderWidget, self).__init__()
		self.widget = QWidget(widget)
		self.setupUi(self.widget)

		self.lineEditCodeFounisseur.textChanged.connect(self.verifierEntier)
		self.pushButtonAjouterImage.clicked.connect(self.ajouterImage)
		self.pushButtonAjouterCatalogue.clicked.connect(self.ajouterCatalogue)

	def cleanText(self):
		self.lineEditNomFournisseur.setText("")
		self.lineEditCodeFounisseur.setText("")
		self.lineEditRegistreCommerce.setText("")
		self.lineEditTelephone.setText("")
		self.lineEditFax.setText("")
		self.lineEditCorespondance.setText("")
		self.lineEditSiteWeb.setText("")
		self.lineEditEmail.setText("")
		self.lineEditFichier.setText("")
		self.lineEditAdresseBanque.setText("")
		self.lineEditCompteB.setText("")
		self.lineEditAdresseFournisseur.setText("")
		self.lineEditAdresse.setText("")
		self.lineEditAdresse1.setText("")
		self.lineEditRemarque1.setText("")
		self.lineEditRemarque2.setText("")
		self.lineEditFlag.setText("")
		self.dataImage = ("", "")
		self.dataCatalogue = ("", "")

	def getText(self):
		return [
			self.lineEditCodeFournisseuri.text(),
			self.lineEditNomFournisseur.text(),
			self.lineEditCodeFounisseur.text(),
			self.lineEditRegistreCommerce.text(),
			self.lineEditTelephone.text(),
			self.lineEditFax.text(),
			self.lineEditCorespondance.text(),
			self.lineEditSiteWeb.text(),
			self.lineEditEmail.text(),
			self.lineEditFichier.text(),
			self.lineEditAdresseBanque.text(),
			self.lineEditCompteB.text(),
			self.lineEditAdresseFournisseur.text(),
			self.lineEditAdresse.text(),
			self.lineEditAdresse1.text(),
			self.lineEditRemarque1.text(),
			self.lineEditRemarque2.text(),
			self.lineEditFlag.text()
			]

	def setDefaultValue(self):
		self.lineEditNomFournisseur.setText("xxxx")
		self.lineEditCodeFounisseur.setText("1")
		self.lineEditRegistreCommerce.setText("xxxx")
		self.lineEditTelephone.setText("xxxx")
		self.lineEditFax.setText("xxxx")
		self.lineEditCorespondance.setText("xxxx")
		self.lineEditSiteWeb.setText("xxxx")
		self.lineEditEmail.setText("xxxx")
		self.lineEditFichier.setText("xxxx")
		self.lineEditAdresseBanque.setText("xxxx")
		self.lineEditCompteB.setText("xxxx")
		self.lineEditAdresseFournisseur.setText("xxxx")
		self.lineEditAdresse.setText("xxxx")
		self.lineEditAdresse1.setText("xxxx")
		self.lineEditRemarque1.setText("xxxx")
		self.lineEditRemarque2.setText("xxxx")
		self.lineEditFlag.setText("xxxx")

	def verifierEntier(self, text):
		txt = self.lineEditCodeFounisseur.text()
		if len(txt) and (txt[-1].isdigit() == 0 or txt[-1] == '²'):
			self.lineEditCodeFounisseur.setText(txt[:-1])

	def ajouterImage(self):
		name = QFileDialog.getOpenFileName(self.widget, "Ajouter une image", os.getcwd(),"image (*.png *.jpg *.jpeg);;tous (*.*)")
		with open(name[0], "rb") as file:
			data = file.read()

		extension = name[0].split(".")[-1]
		self.dataImage = (data, extension)
		image = QPixmap(name[0])
		image = image.scaled(151,101)
		self.labelImage.setPixmap(image)


	def ajouterCatalogue(self):
		name = QFileDialog.getOpenFileName(self.widget, "Ajouter une catalogue", os.getcwd(),"image (*.png *.jpg *.jpeg);; pdf (*.pdf);;tous (*.*)")
		with open(name[0], "rb") as file:
			data = file.read()

		extension = name[0].split(".")[-1]
		self.dataCatalogue = (data, extension)

		if extension == "pdf":
			webbrowser.open_new(name[0])
			self.labelCatalogue.clear()
		else:
			image = QPixmap(name[0])
			image = image.scaled(141,81)
			self.labelCatalogue.setPixmap(image)

	def cleanImages(self):
		self.labelCatalogue.clear()
		self.labelImage.clear()
