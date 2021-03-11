from FournisseurValideWidget import Ui_FounisseurValideWidget
from PyQt5.QtWidgets import QWidget


class ValiderWidget(Ui_FounisseurValideWidget):
	def __init__(self, widget):
		super(ValiderWidget, self).__init__()
		self.widget = QWidget(widget)
		self.setupUi(self.widget)

	def cleanText(self):
		self.lineEditCodeFournisseuri.setText("")
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

	def getText(self):
		return (
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
				)