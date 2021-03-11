from PyQt5.QtWidgets import QWidget
from FournisseurSupprimerWidget import Ui_FournisseurSupprimerWidget

class SupprimerWidget(Ui_FournisseurSupprimerWidget):
	def __init__(self, widget, db):
		super(SupprimerWidget, self).__init__()
		self.widget = QWidget(widget)
		self.db = db
		self.cursor = db.cursor()
		self.cle = ""
		self.setupUi(self.widget)
		self.widget.close()

		self.pushButtonRechercher.clicked.connect(self.rechercher)
		self.pushButtonSupprimer.clicked.connect(self.supprimer)

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

	def rechercher(self):
		self.cle = self.lineEditCle.text()
		self.lineEditCle.setText("")
		self.cursor.execute("SELECT * FROM dbfournisseur WHERE code_fournisseuri = %s", (self.cle, ))
		resultat = self.cursor.fetchone()
		
		if resultat:
			self.setText(resultat)

	def supprimer(self):
		self.cursor.execute("""
				DELETE FROM dbfournisseur
				WHERE code_fournisseuri = %s
				""", (self.cle, ) )
		self.db.commit()
		self.cleanText()