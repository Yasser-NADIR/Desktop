from PyQt5.QtWidgets import QWidget
from FournisseurDefilerWidget import Ui_FournisseurDefilerWidget

class DefilerWidget(Ui_FournisseurDefilerWidget):
	def __init__(self, widget, cursor):
		super(DefilerWidget, self).__init__()
		self.widget = QWidget(widget)
		self.cursor = cursor
		self.index = None

		self.setupUi(self.widget)
		self.widget.close()

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


	def getData(self):
		self.cursor.execute("SELECT * FROM dbFournisseur")
		self.data = self.cursor.fetchall()
		print(self.data)

	def getFirstData(self):
		if self.data != None:
			self.index = 0
			return self.data[0]

	def getLastData(self):
		if self.data != None:
			self.index = len(self.data) - 1
			return self.data[-1]

	def getDataByIndex(self):
		if self.data != None:
			return self.data[self.index]

	def getNextData(self):
		if self.data != None:
			if self.index == None:
				return self.getFirstData()
			else:
				if self.index < len(self.data)-1:
					self.index += 1
				return self.getDataByIndex()

	def getpreviousData(self):
		if self.index == None:
			return self.getLastData()
		elif self.data != None:
			if self.index > 0:
				self.index -= 1
			return self.getDataByIndex()

	def Modifier(self):
		pass

	def Supprimer(self):
		pass