from PyQt5.QtWidgets import QMainWindow
from mainWindow import Ui_MainWindow
from datetime import date
from PyQt5.QtCore import pyqtSlot
from ajouter import Ajouter
import psycopg2
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		for i in range(18):
			self.tableWidget.setRowHeight(i, 35)
		#mettre en place le mois et l'année courrant
		self.labelDateToday.setText(self.getCurrentDate()[:-3])
		
		#mettre en place le entete celon les jours
		for i in range(7):
			item = self.tableWidget.horizontalHeaderItem(i)
			item.setText(self.get7Days()[i])

		#la connexion vers la base de donnée
		try:
			self.db = psycopg2.connect(host="localhost", database="dbgestion", user="postgres", password="azerty")
			self.cursor = self.db.cursor()
		except:
			print("erreur de la connexion a la base de donnée")
			sys.exit(-1)

		#la creation de la widget ajout de patient
		self.prenderRDV = Ajouter(self.widgetCentral, self.db)

		self.trierPatient()

	def getCurrentDate(self):
		mois = ("Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre")
		m = int(date.today().strftime("%m"))
		y = date.today().strftime("%Y")
		d = date.today().strftime("%d")
		return f"{mois[m-1]} {y} {d}"

	def get7Days(self):
		days = []
		y = int(date.today().strftime("%Y"))
		m = int(date.today().strftime("%m"))
		d  = int(date.today().strftime("%d"))
		if m in (1, 3, 5, 7, 8, 10, 12):
			reste = 31 - d + 1
		elif m in (4, 6, 9, 11):
			reste = 30 - d + 1
		else:
			if y%4 == 0:
				reste = 29 - d + 1
			else:
				reste = 28 - d + 1
		if reste < 7:
			for i in range(reste):
				days.append(str(d+i))
			for i in range(7-reste):
				days.append(str(i+1))
		else:
			for i in range(7):
				days.append(str(d+i))
		return days


	def getPatient(self):
		self.cursor.execute("""SELECT nom_patient, prenom_patient, date_, heure, commentaire
							FROM utilisateur, resume
							WHERE utilisateur.id_patient = resume.id_patient
							ORDER BY date_, heure""")
		return self.cursor.fetchall()

	def getCurrentPatient(self):
		m = int(date.today().strftime("%m"))
		y = int(date.today().strftime("%Y"))
		d = int(date.today().strftime("%d"))
		today = f"{y}-{m}-{d}"
		today7 = f"{y}-{m}-{d+7}"
		#apres 7 jours il y en a deux cas exeptionnelle : 
		#la fin du moin 7éme jours est inferieur a le jours courrant ex 28/04 -7-> 04/5 :: 04 < 28
		#la fin du mois 12 alors le mois prochain est le 1 pas 12+1
		if int(self.get7Days()[-1]) < int(self.get7Days()[1]) :
				if m != 12:
					today7 = f"{y}-{m+1}-{int(self.get7Days()[-1])}"
				else:
					today7 = f"{y}-01-{int(self.get7Days()[-1])}"
		

		
		self.cursor.execute("""SELECT nom_patient, prenom_patient, commentaire, num, date_, heure
							FROM utilisateur, resume
							WHERE utilisateur.id_patient = resume.id_patient AND date_ BETWEEN %s AND %s
							ORDER BY date_, heure """,(today, today7))
		return self.cursor.fetchall()

	def trierPatient(self):
		patient = self.getCurrentPatient()
		day = {}
		week = {}
		
		hour = 8
		for i in range(19):
			if i < 4:
				if i%2 == 0 :
					string = f"0{hour}:00"
				else:
					string = f"0{hour}:30"
					hour += 1
			else:
				if i%2 == 0 :
					string = f"{hour}:00"
				else:
					string = f"{hour}:30"
					hour += 1
			day[string] = None

		for i in range(7):
			print(self.get7Days()[i])
			week[self.get7Days()[i]] = day

		

	@pyqtSlot()
	def on_pushButtonPrendreRDV_clicked(self):
		self.widget.close()
		self.prenderRDV.widget.show()

