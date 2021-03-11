from T_produitsWidget import Ui_T_produits
from PyQt5.QtCore import pyqtSlot
import psycopg2


class T_produits(Ui_T_produits):
 def __init__(self, CentralWidget):
     super(T_produits, self).__init__()
     self.setupUi(CentralWidget)
     self.widgetCentralT_produits.close()
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
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Nom_produit= self.lineEditNom_produit.text()
     txt_code_un= self.lineEditcode_un.text()
     txt_Prx_uni= self.lineEditPrx_uni.text()
     txt_Indisponible= self.lineEditIndisponible.text()
     txt_flag= self.lineEditflag.text()
     txt_remarque= self.lineEditremarque.text()


# traitement sauvegarder
 def ajouter(self):
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Nom_produit= self.lineEditNom_produit.text()
     txt_code_un= self.lineEditcode_un.text()
     txt_Prx_uni= self.lineEditPrx_uni.text()
     txt_Indisponible= self.lineEditIndisponible.text()
     txt_flag= self.lineEditflag.text()
     txt_remarque= self.lineEditremarque.text()
     self.cursor.execute("""INSERT INTO T_produits VALUES (%s,%s,%s,%s,%s,%s,%s)", (self.lineEditcode_produit.text(),self.lineEditNom_produit.text(),self.lineEditcode_un.text(),self.lineEditPrx_uni.text(),self.lineEditIndisponible.text(),self.lineEditflag.text(),self.lineEditremarque.text())""")
     self.db.commit()
     self.lineEditcode_produit.SetText("")
     self.lineEditNom_produit.SetText("")
     self.lineEditcode_un.SetText("")
     self.lineEditPrx_uni.SetText("")
     self.lineEditIndisponible.SetText("")
     self.lineEditflag.SetText("")
     self.lineEditremarque.SetText("")


# traitement UPDATE
 def modifier(self):
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Nom_produit= self.lineEditNom_produit.text()
     txt_code_un= self.lineEditcode_un.text()
     txt_Prx_uni= self.lineEditPrx_uni.text()
     txt_Indisponible= self.lineEditIndisponible.text()
     txt_flag= self.lineEditflag.text()
     txt_remarque= self.lineEditremarque.text()
#============================================================================
     sql_update_query = """UPDATE T_produits SET Nom_produit = %s,code_un = %s,Prx_uni = %s,Indisponible = %s,flag = %s,remarque = %s WHERE code_produit = %s"""      
     self.cursor.execute(sql_update_query,(txt_Nom_produit,txt_code_un,txt_Prx_uni,txt_Indisponible,txt_flag,txt_remarque))
#============================================================================
     self.db.commit()
     self.lineEditcode_produit.setText("")
     self.lineEditNom_produit.setText("")
     self.lineEditcode_un.setText("")
     self.lineEditPrx_uni.setText("")
     self.lineEditIndisponible.setText("")
     self.lineEditflag.setText("")
     self.lineEditremarque.setText("")


# traitement suppresion
 def supprimer(self):
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Nom_produit= self.lineEditNom_produit.text()
     txt_code_un= self.lineEditcode_un.text()
     txt_Prx_uni= self.lineEditPrx_uni.text()
     txt_Indisponible= self.lineEditIndisponible.text()
     txt_flag= self.lineEditflag.text()
     txt_remarque= self.lineEditremarque.text()
     sql_delete_query = """delete  from T_produits  WHERE code_produit = %s"""        
     self.cursor.execute(sql_delete_query)
     self.db.commit()
     self.lineEditcode_produit.setText("")
     self.lineEditNom_produit.setText("")
     self.lineEditcode_un.setText("")
     self.lineEditPrx_uni.setText("")
     self.lineEditIndisponible.setText("")
     self.lineEditflag.setText("")
     self.lineEditremarque.setText("")


# traitement trouver
 def trouver(self):
     txt_code_produit= self.lineEditcode_produit.text()
     txt_Nom_produit= self.lineEditNom_produit.text()
     txt_code_un= self.lineEditcode_un.text()
     txt_Prx_uni= self.lineEditPrx_uni.text()
     txt_Indisponible= self.lineEditIndisponible.text()
     txt_flag= self.lineEditflag.text()
     txt_remarque= self.lineEditremarque.text()
     self.cursor.execute("SELECT Nom_produit,code_un,Prx_uni,Indisponible,flag,remarque FROM T_produits WHERE code_produit = %s" )
     resultat = self.cursor.fetchone()
     if resultat:
         self.lineEditValue2.setText(str(resultat[0]))
     else:
         QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement last
 def dernier(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement first
 def premier(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement precedent
 def precedent(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement suivant
 def suivant(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement tableau
 def tableau(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement etat
 def etat(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")


# traitement sortir
 def sortir(self):
             QMessageBox.critical(self.widgetCentralT_produits, " erreur! ", "la valeur n 'exite pas")
