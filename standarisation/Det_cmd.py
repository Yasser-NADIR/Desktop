from Det_cmdWidget import Ui_Det_cmd
from PyQt5.QtCore import pyqtSlot
import psycopg2


class Det_cmd(Ui_Det_cmd):
 def __init__(self, CentralWidget):
     super(Det_cmd, self).__init__()
     self.setupUi(CentralWidget)
     self.widgetCentralDet_cmd.close()
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
     txt_ld_cmd= self.lineEditld_cmd.text()
     txt_FK_cmd= self.lineEditFK_cmd.text()
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Quantitedemd= self.lineEditQuantitedemd.text()
     txt_prix_unitaire= self.lineEditprix_unitaire.text()
     txt_dat_liv_souhaitee= self.lineEditdat_liv_souhaitee.text()
     txt_prix_global= self.lineEditprix_global.text()
     txt_remarq= self.lineEditremarq.text()


# traitement sauvegarder
 def ajouter(self):
     txt_ld_cmd= self.lineEditld_cmd.text()
     txt_FK_cmd= self.lineEditFK_cmd.text()
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Quantitedemd= self.lineEditQuantitedemd.text()
     txt_prix_unitaire= self.lineEditprix_unitaire.text()
     txt_dat_liv_souhaitee= self.lineEditdat_liv_souhaitee.text()
     txt_prix_global= self.lineEditprix_global.text()
     txt_remarq= self.lineEditremarq.text()
     self.cursor.execute("""INSERT INTO Det_cmd VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (self.lineEditld_cmd.text(),self.lineEditFK_cmd.text(),self.lineEditcode_produit.text(),self.lineEditQuantitedemd.text(),self.lineEditprix_unitaire.text(),self.lineEditdat_liv_souhaitee.text(),self.lineEditprix_global.text(),self.lineEditremarq.text())""")
     self.db.commit()
     self.lineEditld_cmd.SetText("")
     self.lineEditFK_cmd.SetText("")
     self.lineEditcode_produit.SetText("")
     self.lineEditQuantitedemd.SetText("")
     self.lineEditprix_unitaire.SetText("")
     self.lineEditdat_liv_souhaitee.SetText("")
     self.lineEditprix_global.SetText("")
     self.lineEditremarq.SetText("")


# traitement UPDATE
 def modifier(self):
     txt_ld_cmd= self.lineEditld_cmd.text()
     txt_FK_cmd= self.lineEditFK_cmd.text()
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Quantitedemd= self.lineEditQuantitedemd.text()
     txt_prix_unitaire= self.lineEditprix_unitaire.text()
     txt_dat_liv_souhaitee= self.lineEditdat_liv_souhaitee.text()
     txt_prix_global= self.lineEditprix_global.text()
     txt_remarq= self.lineEditremarq.text()
#============================================================================
     sql_update_query = """UPDATE Det_cmd SET FK_cmd = %s,code_produit = %s,Quantitedemd = %s,prix_unitaire = %s,dat_liv_souhaitee = %s,prix_global = %s,remarq = %s WHERE ld_cmd = %s"""      
     self.cursor.execute(sql_update_query,(txt_FK_cmd,txt_code_produit,txt_Quantitedemd,txt_prix_unitaire,txt_dat_liv_souhaitee,txt_prix_global,txt_remarq))
#============================================================================
     self.db.commit()
     self.lineEditld_cmd.setText("")
     self.lineEditFK_cmd.setText("")
     self.lineEditcode_produit.setText("")
     self.lineEditQuantitedemd.setText("")
     self.lineEditprix_unitaire.setText("")
     self.lineEditdat_liv_souhaitee.setText("")
     self.lineEditprix_global.setText("")
     self.lineEditremarq.setText("")


# traitement suppresion
 def supprimer(self):
     txt_ld_cmd= self.lineEditld_cmd.text()
     txt_FK_cmd= self.lineEditFK_cmd.text()
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Quantitedemd= self.lineEditQuantitedemd.text()
     txt_prix_unitaire= self.lineEditprix_unitaire.text()
     txt_dat_liv_souhaitee= self.lineEditdat_liv_souhaitee.text()
     txt_prix_global= self.lineEditprix_global.text()
     txt_remarq= self.lineEditremarq.text()
     sql_delete_query = """delete  from Det_cmd  WHERE ld_cmd = %s"""        
     self.cursor.execute(sql_delete_query)
     self.db.commit()
     self.lineEditld_cmd.setText("")
     self.lineEditFK_cmd.setText("")
     self.lineEditcode_produit.setText("")
     self.lineEditQuantitedemd.setText("")
     self.lineEditprix_unitaire.setText("")
     self.lineEditdat_liv_souhaitee.setText("")
     self.lineEditprix_global.setText("")
     self.lineEditremarq.setText("")


# traitement trouver
 def trouver(self):
     txt_ld_cmd= self.lineEditld_cmd.text()
     txt_FK_cmd= self.lineEditFK_cmd.text()
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Quantitedemd= self.lineEditQuantitedemd.text()
     txt_prix_unitaire= self.lineEditprix_unitaire.text()
     txt_dat_liv_souhaitee= self.lineEditdat_liv_souhaitee.text()
     txt_prix_global= self.lineEditprix_global.text()
     txt_remarq= self.lineEditremarq.text()
     self.cursor.execute("SELECT FK_cmd,code_produit,Quantitedemd,prix_unitaire,dat_liv_souhaitee,prix_global,remarq FROM Det_cmd WHERE ld_cmd = %s" )
     resultat = self.cursor.fetchone()
     if resultat:
         self.lineEditValue2.setText(str(resultat[0]))
     else:
         QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement last
 def dernier(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement first
 def premier(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement precedent
 def precedent(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement suivant
 def suivant(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement tableau
 def tableau(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement etat
 def etat(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")


# traitement sortir
 def sortir(self):
             QMessageBox.critical(self.widgetCentralDet_cmd, " erreur! ", "la valeur n 'exite pas")
