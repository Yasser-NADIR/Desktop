from PyQt5.QtWidgets import QWidget
from FournisseurModifierWidget import Ui_FounisseurModificationWidget

class ModifierWidget(Ui_FounisseurModificationWidget):
	def __init__(self, widget, db, afficher):
		super(ModifierWidget, self).__init__()
		self.widget = QWidget(widget)
		self.db = db
		self.cursor = db.cursor()
		self.cle = ""
		self.afficher = afficher

		self.setupUi(self.widget)
		self.widget.close()

		self.pushButtonSauvgarder.clicked.connect(self.sauvgarder)
		for wdg in (self.lineEditCodeFournisseuri,self.lineEditNomFournisseur,self.lineEditCodeFounisseur,self.lineEditRegistreCommerce,self.lineEditTelephone,self.lineEditFax,self.lineEditCorespondance,self.lineEditSiteWeb,self.lineEditEmail,self.lineEditFichier,self.lineEditAdresseBanque,self.lineEditCompteB,self.lineEditAdresseFournisseur,self.lineEditAdresse,self.lineEditAdresse1,self.lineEditRemarque1,self.lineEditRemarque2,self.lineEditFlag):
			wdg.textChanged.connect(self.test)

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

	def setText(self, data):
		if len(data) == 18:
			self.lineEditCodeFournisseuri.setText(str(data[0]))
			self.lineEditNomFournisseur.setText(str(data[1]))
			self.lineEditCodeFounisseur.setText(str(data[2]))
			self.lineEditRegistreCommerce.setText(str(data[3]))
			self.lineEditTelephone.setText(str(data[4]))
			self.lineEditFax.setText(str(data[5]))
			self.lineEditCorespondance.setText(str(data[6]))
			self.lineEditSiteWeb.setText(str(data[7]))
			self.lineEditEmail.setText(str(data[8]))
			self.lineEditFichier.setText(str(data[9]))
			self.lineEditAdresseBanque.setText(str(data[10]))
			self.lineEditCompteB.setText(str(data[11]))
			self.lineEditAdresseFournisseur.setText(str(data[12]))
			self.lineEditAdresse.setText(str(data[13]))
			self.lineEditAdresse1.setText(str(data[14]))
			self.lineEditRemarque1.setText(str(data[15]))
			self.lineEditRemarque2.setText(str(data[16]))
			self.lineEditFlag.setText(str(data[17]))

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
		
	def sauvgarder(self):
		data = self.getText()
		for d in data:
			if len(d) == 0:
				return
		dataSet = [d for d in data]
		dataSet.append(self.lineEditCodeFournisseuri.text())
		self.cursor.execute("""UPDATE dbfournisseur 
							SET code_fournisseuri=%s, nom_fournisseur=%s, code_fournisseur=%s, regc=%s, tel=%s, fax=%s, c_corresp=%s, siteweb=%s, email=%s, fichier=%s, adresse_banque=%s, compte_b=%s, adrs1=%s, adrs2=%s, adrs3=%s, rmq1=%s, rmq2=%s, flag=%s
							WHERE code_fournisseuri = %s
						""", dataSet)
		self.db.commit()
		self.cleanText()
		self.afficher()

	def test(self, a):
		print("le texte a été changé", a)