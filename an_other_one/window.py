from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
import psycopg2
#importation de la feunetre principal
from MainWindow import Ui_mainWindow
#importation des widgets
from fournisseur import FournisseurWidget
from familleProduit import FamilleProduitWidget
from produit import ProduitWidget
from entetedetail import EnteteDetailWidget
#testing: importation 
from PyQt5.QtWidgets import QDockWidget

class MainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.showMaximized()
		#creation des base de donné
		self.initDataBase()
		#la connexion à la base de donnée
		self.db = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="dbApp1")
		#la creation des widget
		self.fournisseurWidget = FournisseurWidget(self.widgetCentral, self.db)
		self.familleProduit = FamilleProduitWidget(self.widgetCentral, self.db)
		self.produit = ProduitWidget(self.widgetCentral, self.db)
		self.enteteDetail = EnteteDetailWidget(self.widgetCentral, self.db)

	def initDataBase(self):
		db = psycopg2.connect(host="localhost", user="postgres", password="azerty")
		db.autocommit = True
		cursor = db.cursor()
		try:
			cursor.execute("CREATE DATABASE dbApp1")
		except:
			pass

		cursor.close()
		db.close()
		db = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="dbApp1")
		cursor = db.cursor()
		try:
			cursor.execute("""CREATE TABLE public.fournisseur
							(
							    codefournisseuri integer NOT NULL,
							    codefournisseur text COLLATE pg_catalog."default",
							    nomfournisseur text COLLATE pg_catalog."default",
							    tel text COLLATE pg_catalog."default",
							    fax text COLLATE pg_catalog."default",
							    CONSTRAINT fournisseur_pkey PRIMARY KEY (codefournisseuri)
							)
							WITH (
							    OIDS = FALSE
							)
							TABLESPACE pg_default;

							ALTER TABLE public.fournisseur
							    OWNER to postgres;""")
		except:
			pass

		try:
			cursor.execute("""CREATE TABLE public.familleproduit
							(
							    codefamilleproduit integer NOT NULL,
							    nomfamilleproduit text COLLATE pg_catalog."default",
							    CONSTRAINT familleproduit_pkey PRIMARY KEY (codefamilleproduit)
							)
							WITH (
							    OIDS = FALSE
							)
							TABLESPACE pg_default;

							ALTER TABLE public.familleproduit
							    OWNER to postgres;""")
		except:
			pass

		try:
			cursor.execute("""CREATE TABLE public.produit
							(
							    codeproduit integer NOT NULL,
							    codefamilleproduit integer,
							    nomproduit text COLLATE pg_catalog."default",
							    CONSTRAINT produit_pkey PRIMARY KEY (codeproduit),
							    CONSTRAINT codefamilleproduit FOREIGN KEY (codefamilleproduit)
							        REFERENCES public.familleproduit (codefamilleproduit) MATCH SIMPLE
							        ON UPDATE CASCADE
							        ON DELETE CASCADE
							)
							WITH (
							    OIDS = FALSE
							)
							TABLESPACE pg_default;

							ALTER TABLE public.produit
							    OWNER to postgres;""")
		except:
			pass

		try:
			cursor.execute("""CREATE TABLE public.entete
								(
								    codecommande integer NOT NULL,
								    codefournisseur integer,
								    datecommande date,
								    CONSTRAINT entete_pkey PRIMARY KEY (codecommande),
								    CONSTRAINT entete_codefournisseur_fkey FOREIGN KEY (codefournisseur)
								        REFERENCES public.fournisseur (codefournisseuri) MATCH SIMPLE
								        ON UPDATE CASCADE
								        ON DELETE CASCADE
								)
								WITH (
								    OIDS = FALSE
								)
								TABLESPACE pg_default;

								ALTER TABLE public.entete
								    OWNER to postgres;""")
		except:
			pass
		
		try:
			cursor.execute("""CREATE TABLE public.detail
								(
								    idcommande integer NOT NULL,
								    refproduit integer,
								    prixunitaire double precision,
								    quantite integer,
								    prixglobal double precision,
								    datelivraison date,
								    codecommande integer NOT NULL,
								    CONSTRAINT detail_pkey PRIMARY KEY (codecommande, idcommande),
								    CONSTRAINT detail_codecommande_fkey FOREIGN KEY (codecommande)
								        REFERENCES public.entete (codecommande) MATCH SIMPLE
								        ON UPDATE CASCADE
								        ON DELETE CASCADE
								        NOT VALID,
								    CONSTRAINT detail_refproduit_fkey FOREIGN KEY (refproduit)
								        REFERENCES public.produit (codeproduit) MATCH SIMPLE
								        ON UPDATE CASCADE
								        ON DELETE CASCADE
								        NOT VALID
								)
								WITH (
								    OIDS = FALSE
								)
								TABLESPACE pg_default;

								ALTER TABLE public.detail
								    OWNER to postgres;""")
		except:
			pass

		db.commit()
		cursor.close()
		db.close()


	@pyqtSlot()
	def on_actionFournisseur_triggered(self):
		self.fournisseurWidget.widgetCentral.show()
		self.familleProduit.widgetCentral.close()
		self.produit.widgetCentral.close()
		self.enteteDetail.widgetCentral.close()

	@pyqtSlot()
	def on_actionFamilleProduit_triggered(self):
		self.fournisseurWidget.widgetCentral.close()
		self.familleProduit.widgetCentral.show()
		self.produit.widgetCentral.close()
		self.enteteDetail.widgetCentral.close()

	@pyqtSlot()
	def on_actionProduit_triggered(self):
		cursor = self.db.cursor()
		cursor.execute("SELECT count(codefamilleproduit) FROM familleproduit")
		langh = cursor.fetchone()[0]
		if not langh:
			QMessageBox.warning(self.widgetCentral, "Erreur", "Il faut créer au moin une famille produit")
			self.on_actionFamilleProduit_triggered()
			return 
		self.fournisseurWidget.widgetCentral.close()
		self.familleProduit.widgetCentral.close()
		self.produit.widgetCentral.show()
		self.enteteDetail.widgetCentral.close()

	@pyqtSlot()
	def on_actionEntete_Detail_triggered(self):
		cursor = self.db.cursor()
		cursor.execute("SELECT count(codefournisseuri) FROM fournisseur")
		langhFournisseur = cursor.fetchone()[0]
		cursor = self.db.cursor()
		cursor.execute("SELECT count(codeproduit) FROM produit")
		langhProduit = cursor.fetchone()[0]
		if not langhFournisseur:
			QMessageBox.warning(self.widgetCentral, "Erreur", "Il faut créer au moin un fournisseur")
			self.on_actionFournisseur_triggered()
			return
		if not langhProduit:
			QMessageBox.warning(self.widgetCentral, "Erreur", "Il faut créer au moin un produit")
			self.on_actionProduit_triggered()
			return
		self.fournisseurWidget.widgetCentral.close()
		self.familleProduit.widgetCentral.close()
		self.produit.widgetCentral.close()
		self.enteteDetail.widgetCentral.show()

	@pyqtSlot()
	def on_actionClose_triggered(self):
		self.fournisseurWidget.widgetCentral.close()
		self.familleProduit.widgetCentral.close()
		self.produit.widgetCentral.close()
		self.enteteDetail.widgetCentral.close()
