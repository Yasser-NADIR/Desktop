from T_frnsWidget import Ui_T_frns
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import psycopg2


class T_frns(Ui_T_frns):
 def __init__(self, CentralWidget):
     super(T_frns, self).__init__()
     self.setupUi(CentralWidget)
     self.widgetCentralT_frns.close()
     self.db = psycopg2.connect(host="localhost", user="postgres", password="azertyuiop789+", database="dbapp")
     self.cursor = self.db.cursor()
     self.pushButton_new.clicked.connect(self.vider)
     self.pushButton_add.clicked.connect(self.ajouter)
     self.pushButton_upd.clicked.connect(self.modifier)
     self.pushButton_rmv.clicked.connect(self.supprimer)
     self.pushButton_find.clicked.connect(self.trouver)
     self.pushButton_lst.clicked.connect(self.dernier)
     self.pushButton_fst.clicked.connect(self.premier)
     self.pushButton_prev.clicked.connect(self.precedent)
     self.pushButton_next.clicked.connect(self.suivant)
     self.pushButton_grid.clicked.connect(self.tableau)
     self.pushButton_report.clicked.connect(self.etat)
     self.pushButton_exit.clicked.connect(self.sortir)


# traitement du premier test
 def vider(self):
     txt_code_frnsi= self.txt_code_frnsi.setText("")
     txt_Date_deb= self.txt_Date_deb.setText("")
     txt_capital= self.txt_capital.setText("")
     txt_rmq_type_etat= self.txt_rmq_type_etat.setText("")
     txt_nom_frns= self.txt_nom_frns.setText("")
     txt_regc= self.txt_regc.setText("")
     txt_tel= self.txt_tel.setText("")
     txt_fax= self.txt_fax.setText("")
     txt_adrs1= self.txt_adrs1.setText("")
     txt_rmq1= self.txt_rmq1.setText("")


# traitement sauvegarder
 def ajouter(self):
     txt_code_frnsi= self.txt_code_frnsi.text()
     txt_Date_deb= self.txt_Date_deb.text()
     txt_capital= self.txt_capital.text()
     txt_rmq_type_etat= self.txt_rmq_type_etat.text()
     txt_nom_frns= self.txt_nom_frns.text()
     txt_regc= self.txt_regc.text()
     txt_tel= self.txt_tel.text()
     txt_fax= self.txt_fax.text()
     txt_adrs1= self.txt_adrs1.text()
     txt_rmq1= self.txt_rmq1.text()
     self.cursor.execute("""INSERT INTO T_frns VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
          (self.txt_code_frnsi.text(),self.txt_Date_deb.text(),self.txt_capital.text(),self.txt_rmq_type_etat.text(),
          self.txt_nom_frns.text(),self.txt_regc.text(),self.txt_tel.text(),self.txt_fax.text(),self.txt_adrs1.text(),
          self.txt_rmq1.text() ) )
     self.db.commit()
     self.txt_code_frnsi.setText("")
     self.txt_Date_deb.setText("")
     self.txt_capital.setText("")
     self.txt_rmq_type_etat.setText("")
     self.txt_nom_frns.setText("")
     self.txt_regc.setText("")
     self.txt_tel.setText("")
     self.txt_fax.setText("")
     self.txt_adrs1.setText("")
     self.txt_rmq1.setText("")


# traitement UPDATE
 def modifier(self):
     txt_code_frnsi= self.txt_code_frnsi.text()
     txt_Date_deb= self.txt_Date_deb.text()
     txt_capital= self.txt_capital.text()
     txt_rmq_type_etat= self.txt_rmq_type_etat.text()
     txt_nom_frns= self.txt_nom_frns.text()
     txt_regc= self.txt_regc.text()
     txt_tel= self.txt_tel.text()
     txt_fax= self.txt_fax.text()
     txt_adrs1= self.txt_adrs1.text()
     txt_rmq1= self.txt_rmq1.text()
#============================================================================
     sql_update_query = """UPDATE T_frns SET Date_deb = %s,capital = %s,rmq_type_etat = %s,nom_frns = %s,regc = %s,tel = %s,fax = %s,adrs1 = %s,rmq1 = %s WHERE code_frnsi = %s"""      
     self.cursor.execute(sql_update_query,(txt_Date_deb,txt_capital,txt_rmq_type_etat,txt_nom_frns,txt_regc,txt_tel,txt_fax,txt_adrs1,txt_rmq1, txt_code_frnsi))
#============================================================================
     self.db.commit()
     self.txt_code_frnsi.setText("")
     self.txt_Date_deb.setText("")
     self.txt_capital.setText("")
     self.txt_rmq_type_etat.setText("")
     self.txt_nom_frns.setText("")
     self.txt_regc.setText("")
     self.txt_tel.setText("")
     self.txt_fax.setText("")
     self.txt_adrs1.setText("")
     self.txt_rmq1.setText("")


# traitement suppresion
 def supprimer(self):
     txt_code_frnsi= self.txt_code_frnsi.text()
     txt_Date_deb= self.txt_Date_deb.text()
     txt_capital= self.txt_capital.text()
     txt_rmq_type_etat= self.txt_rmq_type_etat.text()
     txt_nom_frns= self.txt_nom_frns.text()
     txt_regc= self.txt_regc.text()
     txt_tel= self.txt_tel.text()
     txt_fax= self.txt_fax.text()
     txt_adrs1= self.txt_adrs1.text()
     txt_rmq1= self.txt_rmq1.text()
     sql_delete_query = """delete  from T_frns  WHERE code_frnsi = %s"""        
     self.cursor.execute(sql_delete_query, (txt_code_frnsi, ))
     self.db.commit()
     self.txt_code_frnsi.setText("")
     self.txt_Date_deb.setText("")
     self.txt_capital.setText("")
     self.txt_rmq_type_etat.setText("")
     self.txt_nom_frns.setText("")
     self.txt_regc.setText("")
     self.txt_tel.setText("")
     self.txt_fax.setText("")
     self.txt_adrs1.setText("")
     self.txt_rmq1.setText("")


# traitement trouver
 def trouver(self):
     txt_code_frnsi= self.txt_code_frnsi.text()
     txt_Date_deb= self.txt_Date_deb.text()
     txt_capital= self.txt_capital.text()
     txt_rmq_type_etat= self.txt_rmq_type_etat.text()
     txt_nom_frns= self.txt_nom_frns.text()
     txt_regc= self.txt_regc.text()
     txt_tel= self.txt_tel.text()
     txt_fax= self.txt_fax.text()
     txt_adrs1= self.txt_adrs1.text()
     txt_rmq1= self.txt_rmq1.text()
     self.cursor.execute("SELECT Date_deb,capital,rmq_type_etat,nom_frns,regc,tel,fax,adrs1,rmq1 FROM T_frns WHERE code_frnsi = %s", ('a',))#WHERE code_frnsi = %s
     resultat = self.cursor.fetchone()
     if resultat:
         self.txt_code_frnsi.setText(str(resultat[0]))
     else:
         QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement last
 def dernier(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement first
 def premier(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement precedent
 def precedent(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement suivant
 def suivant(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement tableau
 def tableau(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement etat
 def etat(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")


# traitement sortir
 def sortir(self):
             QMessageBox.critical(self.widgetCentralT_frns, " erreur! ", "la valeur n 'exite pas")
