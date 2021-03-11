from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from MainWindow import Ui_MainWindow



from Ent_cmd import Ent_cmd
from Det_cmd import Det_cmd
from T_frns import T_frns
from T_produits import T_produits
from Cmd_hist import Cmd_hist



class MainWindow(QMainWindow, Ui_MainWindow):
 def __init__(self, parent=None):
     super(MainWindow, self).__init__(parent)
     self.setupUi(self)
     self.showMaximized()



     self.Ent_cmd = Ent_cmd(self.Centralwidget)
     self.Det_cmd = Det_cmd(self.Centralwidget)
     self.T_frns = T_frns(self.Centralwidget)
     self.T_produits = T_produits(self.Centralwidget)
     self.Cmd_hist = Cmd_hist(self.Centralwidget)



 @pyqtSlot()
 def on_actionEnt_cmd_triggered(self):
     self.Ent_cmd.widgetCentralEnt_cmd.show()
     self.Det_cmd.widgetCentralDet_cmd.close()
     self.T_frns.widgetCentralT_frns.close()
     self.T_produits.widgetCentralT_produits.close()
     self.Cmd_hist.widgetCentralCmd_hist.close()



 @pyqtSlot()
 def on_actionDet_cmd_triggered(self):
     self.Ent_cmd.widgetCentralEnt_cmd.close()
     self.Det_cmd.widgetCentralDet_cmd.show()
     self.T_frns.widgetCentralT_frns.close()
     self.T_produits.widgetCentralT_produits.close()
     self.Cmd_hist.widgetCentralCmd_hist.close()



 @pyqtSlot()
 def on_actionT_frns_triggered(self):
     self.Ent_cmd.widgetCentralEnt_cmd.close()
     self.Det_cmd.widgetCentralDet_cmd.close()
     self.T_frns.widgetCentralT_frns.show()
     self.T_produits.widgetCentralT_produits.close()
     self.Cmd_hist.widgetCentralCmd_hist.close()



 @pyqtSlot()
 def on_actionT_produits_triggered(self):
     self.Ent_cmd.widgetCentralEnt_cmd.close()
     self.Det_cmd.widgetCentralDet_cmd.close()
     self.T_frns.widgetCentralT_frns.close()
     self.T_produits.widgetCentralT_produits.show()
     self.Cmd_hist.widgetCentralCmd_hist.close()



 @pyqtSlot()
 def on_actionCmd_hist_triggered(self):
     self.Ent_cmd.widgetCentralEnt_cmd.close()
     self.Det_cmd.widgetCentralDet_cmd.close()
     self.T_frns.widgetCentralT_frns.close()
     self.T_produits.widgetCentralT_produits.close()
     self.Cmd_hist.widgetCentralCmd_hist.show()
