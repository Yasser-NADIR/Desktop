from MainWidow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
import ftplib

class mainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(mainWindow, self).__init__(parent)
		self.setupUi(self)
		self.fileName = ""

	@pyqtSlot()
	def on_pushButtonAjouter_clicked(self):
		self.fileName = QFileDialog.getOpenFileName(self, "choisi un fichier pour l'envoyer", filter="tous (*.*)")[0]
		self.labelNomFichier.setText(self.fileName.split("/")[-1])
		self.pushButtonEnvoyer.setEnabled(True)

	@pyqtSlot()
	def on_pushButtonEnvoyer_clicked(self):
		ftp = ftplib.FTP("158.69.62.133")
		ftp.login("youssfi", "qwerty")
		with open(self.fileName, "rb") as f:
			ftp.storbinary("STOR {}".format(self.fileName.split("/")[-1]), f)
		ftp.close()
		self.pushButtonEnvoyer.setEnabled(False)
		self.labelNomFichier.setText("")
