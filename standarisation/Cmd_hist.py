from Cmd_histWidget import Ui_Cmd_hist
from PyQt5.QtCore import pyqtSlot
import psycopg2


class Cmd_hist(Ui_Cmd_hist):
 def __init__(self, CentralWidget):
     super(Cmd_hist, self).__init__()
     self.setupUi(CentralWidget)
     self.widgetCentralCmd_hist.close()
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
     txt_code_cmd_incr= self.lineEditcode_cmd_incr.text()
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_trtmnt= self.lineEditdate_trtmnt.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()


# traitement sauvegarder
 def ajouter(self):
     txt_code_cmd_incr= self.lineEditcode_cmd_incr.text()
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_trtmnt= self.lineEditdate_trtmnt.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
     self.cursor.execute("""INSERT INTO Cmd_hist VALUES (%s,%s,%s,%s,%s,%s,%s)", (self.lineEditcode_cmd_incr.text(),self.lineEditcode_cmd.text(),self.lineEditrefmarche.text(),self.lineEditcode_frnsi.text(),self.lineEditdate_trtmnt.text(),self.lineEditflag.text(),self.lineEditremarques.text())""")
     self.db.commit()
     self.lineEditcode_cmd_incr.SetText("")
     self.lineEditcode_cmd.SetText("")
     self.lineEditrefmarche.SetText("")
     self.lineEditcode_frnsi.SetText("")
     self.lineEditdate_trtmnt.SetText("")
     self.lineEditflag.SetText("")
     self.lineEditremarques.SetText("")


# traitement UPDATE
 def modifier(self):
     txt_code_cmd_incr= self.lineEditcode_cmd_incr.text()
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_trtmnt= self.lineEditdate_trtmnt.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
#============================================================================
     sql_update_query = """UPDATE Cmd_hist SET code_cmd = %s,refmarche = %s,code_frnsi = %s,date_trtmnt = %s,flag = %s,remarques = %s WHERE code_cmd_incr = %s"""      
     self.cursor.execute(sql_update_query,(txt_code_cmd,txt_refmarche,txt_code_frnsi,txt_date_trtmnt,txt_flag,txt_remarques))
#============================================================================
     self.db.commit()
     self.lineEditcode_cmd_incr.setText("")
     self.lineEditcode_cmd.setText("")
     self.lineEditrefmarche.setText("")
     self.lineEditcode_frnsi.setText("")
     self.lineEditdate_trtmnt.setText("")
     self.lineEditflag.setText("")
     self.lineEditremarques.setText("")


# traitement suppresion
 def supprimer(self):
     txt_code_cmd_incr= self.lineEditcode_cmd_incr.text()
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_trtmnt= self.lineEditdate_trtmnt.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
     sql_delete_query = """delete  from Cmd_hist  WHERE code_cmd_incr = %s"""        
     self.cursor.execute(sql_delete_query)
     self.db.commit()
     self.lineEditcode_cmd_incr.setText("")
     self.lineEditcode_cmd.setText("")
     self.lineEditrefmarche.setText("")
     self.lineEditcode_frnsi.setText("")
     self.lineEditdate_trtmnt.setText("")
     self.lineEditflag.setText("")
     self.lineEditremarques.setText("")


# traitement trouver
 def trouver(self):
     txt_code_cmd_incr= self.lineEditcode_cmd_incr.text()
     txt_code_cmd= self.lineEditcode_cmd.text()
     txt_refmarche= self.lineEditrefmarche.text()
     txt_code_frnsi= self.lineEditcode_frnsi.text()
     txt_date_trtmnt= self.lineEditdate_trtmnt.text()
     txt_flag= self.lineEditflag.text()
     txt_remarques= self.lineEditremarques.text()
     self.cursor.execute("SELECT code_cmd,refmarche,code_frnsi,date_trtmnt,flag,remarques FROM Cmd_hist WHERE code_cmd_incr = %s" )
     resultat = self.cursor.fetchone()
     if resultat:
         self.lineEditValue2.setText(str(resultat[0]))
     else:
         QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement last
 def dernier(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement first
 def premier(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement precedent
 def precedent(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement suivant
 def suivant(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement tableau
 def tableau(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement etat
 def etat(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")


# traitement sortir
 def sortir(self):
             QMessageBox.critical(self.widgetCentralCmd_hist, " erreur! ", "la valeur n 'exite pas")
