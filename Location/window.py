from PyQt5.QtWidgets import QMainWindow
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import psycopg2

from enteteDetail import EnteteDetail

class mainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(mainWindow, self).__init__()
		self.setupUi(self)
		self.showMaximized()
		
		self.db = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="location")

		self.enteteDetail = EnteteDetail(self.widgetCentral, self.db)

	@pyqtSlot()
	def on_actionoption1_triggered(self):
		self.enteteDetail.widgetCentral.show()

