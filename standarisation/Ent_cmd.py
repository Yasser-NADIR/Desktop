from Ent_cmdWidget import Ui_Ent_cmd
from PyQt5.QtCore import pyqtSlot
import psycopg2


class Ent_cmd(Ui_Ent_cmd):
 def __init__(self, CentralWidget):
     super(Ent_cmd, self).__init__()
     self.setupUi(CentralWidget)
     self.widgetCentralEnt_cmd.close()
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
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_cmd= self.lineEditdate_cmd.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()


# traitement sauvegarder
 def ajouter(self):
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_cmd= self.lineEditdate_cmd.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
     self.cursor.execute("""INSERT INTO Ent_cmd VALUES (%s,%s,%s,%s,%s,%s)", (self.lineEditcode_cmd.text(),self.lineEditrefmarche.text(),self.lineEditcode_frnsi.text(),self.lineEditdate_cmd.text(),self.lineEditflag.text(),self.lineEditremarques.text())""")
     self.db.commit()
     self.lineEditcode_cmd.SetText("")
     self.lineEditrefmarche.SetText("")
     self.lineEditcode_frnsi.SetText("")
     self.lineEditdate_cmd.SetText("")
     self.lineEditflag.SetText("")
     self.lineEditremarques.SetText("")


# traitement UPDATE
 def modifier(self):
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_cmd= self.lineEditdate_cmd.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
#============================================================================
     sql_update_query = """UPDATE Ent_cmd SET refmarche = %s,code_frnsi = %s,date_cmd = %s,flag = %s,remarques = %s WHERE code_cmd = %s"""      
     self.cursor.execute(sql_update_query,(txt_refmarche,txt_code_frnsi,txt_date_cmd,txt_flag,txt_remarques))
#============================================================================
     self.db.commit()
     self.lineEditcode_cmd.setText("")
     self.lineEditrefmarche.setText("")
     self.lineEditcode_frnsi.setText("")
     self.lineEditdate_cmd.setText("")
     self.lineEditflag.setText("")
     self.lineEditremarques.setText("")


# traitement suppresion
 def supprimer(self):
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_cmd= self.lineEditdate_cmd.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
     sql_delete_query = """delete  from Ent_cmd  WHERE code_cmd = %s"""        
     self.cursor.execute(sql_delete_query)
     self.db.commit()
     self.lineEditcode_cmd.setText("")
     self.lineEditrefmarche.setText("")
     self.lineEditcode_frnsi.setText("")
     self.lineEditdate_cmd.setText("")
     self.lineEditflag.setText("")
     self.lineEditremarques.setText("")


# traitement trouver
 def trouver(self):
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_cmd= self.lineEditdate_cmd.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
     self.cursor.execute("SELECT refmarche,code_frnsi,date_cmd,flag,remarques FROM Ent_cmd WHERE code_cmd = %s" )
     resultat = self.cursor.fetchone()
     if resultat:
         self.lineEditValue2.setText(str(resultat[0]))
     else:
         QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement last
 def dernier(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement first
 def premier(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement precedent
 def precedent(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement suivant
 def suivant(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement tableau
 def tableau(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement etat
 def etat(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement sortir
 def sortir(self):
             QMessageBox.critical(self.widgetCentralEnt_cmd, " erreur! ", "la valeur n 'exite pas")
