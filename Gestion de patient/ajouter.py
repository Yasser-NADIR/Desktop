from ajouterWidget import Ui_AjouterWidget
from PyQt5.QtCore import pyqtSlot


class Ajouter(Ui_AjouterWidget):
	def __init__(self, centredWidget, db):
		super(Ajouter, self).__init__()
		self.setupUi(centredWidget)
		self.widget.close()
		self.labelAttention.close()
		self.pushButtonSauvgarder.setEnabled(False)
		self.lineEditWidgets = (self.lineEditNom,self.lineEditPrenom,self.lineEditTelephone)
		for widget in self.lineEditWidgets:
			widget.textChanged.connect(self.EnableSauvgarder)

		self.dateTimeEdit.dateTimeChanged.connect(self.dateTimeValide)

		self.db = db
		self.cursor = db.cursor()

	def EnableSauvgarder(self):
		for widget in self.lineEditWidgets:
			if widget.text() == "":
				self.pushButtonSauvgarder.setEnabled(False)
				return
		self.pushButtonSauvgarder.setEnabled(True)
		self.dateTimeValide(self.dateTimeEdit.dateTime())

	def dateTimeValide(self, dateTime):
		if dateTime.date().day()>10 and dateTime.date().month()>0 and dateTime.date().year()>2016:
			self.pushButtonSauvgarder.setEnabled(True)
			self.labelAttention.close()
		else :
			self.pushButtonSauvgarder.setEnabled(False)
			self.labelAttention.show()
