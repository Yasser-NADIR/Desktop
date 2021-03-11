from PyQt5.QtWidgets import QMainWindow, QWidget
from mainWindow import Ui_MainWindow
from Fournisseur import fournisseurWidget
from newWindow import window2
from Commande import commandeWidget
from PyQt5.QtCore import pyqtSlot
import psycopg2

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initDatabase()
        self.showMaximized()
        self.db = psycopg2.connect(
                host = "localhost",
                database = "dbapp",
                user = "postgres",
                password = "azerty"
            )
        self.fournisseurWidget = fournisseurWidget(self.centralwidget, self.db)
        self.newWindow2 = window2(self.centralwidget)
        self.commandewidget = commandeWidget(self.centralwidget)


    @pyqtSlot()
    def on_actionFournisseur_triggered(self):
        self.fournisseurWidget.widget.show()
        self.fournisseurWidget.Nouveau()
        self.newWindow2.centralWindow2.close()
        self.commandewidget.widgetCentral.close()

    @pyqtSlot()
    def on_actionClient_triggered(self):
        self.fournisseurWidget.widget.close()
        self.newWindow2.centralWindow2.show()
        self.commandewidget.widgetCentral.close()

    @pyqtSlot()
    def on_actionENT_Commande_triggered(self):
        self.fournisseurWidget.widget.close()
        self.newWindow2.centralWindow2.close()
        self.commandewidget.widgetCentral.show()
    
    def initDatabase(self):
        try :
            con = psycopg2.connect(host="localhost", user="postgres", password="azerty")
            con.autocommit = True
            cur = con.cursor()
            cur.execute("CREATE DATABASE dbapp")
            cur.close()
            con.close()

            con = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="dbapp")
            cur = con.cursor()
            cur.execute("CREATE TABLE dbfournisseur(code_fournisseuri bigint, nom_fournisseur text, code_fournisseur bigint, regc text, tel text, fax text, c_corresp text, siteweb text, email text, fichier text, adresse_banque text, compte_b text, adrs1 text, adrs2 text, adrs3 text, rmq1 text, rmq2 text, flag text)")
            con.commit()
            cur.close()
            con.close()
        except:
            pass