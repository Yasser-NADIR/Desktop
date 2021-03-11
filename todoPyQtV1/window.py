from PyQt5.QtWidgets import QMainWindow, QWidget
from mainWindow import Ui_MainWindow
from Fournisseur import fournisseurWidget
from newWindow import window2
from PyQt5.QtCore import pyqtSlot
import psycopg2

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.fournisseurWidget = fournisseurWidget(self.centralwidget)
        self.newWindow2 = window2(self.centralwidget)


    @pyqtSlot()
    def on_actionFournisseur_triggered(self):
        self.fournisseurWidget.widget.show()
        self.newWindow2.centralWindow2.close()

    @pyqtSlot()
    def on_actionClient_triggered(self):
        self.newWindow2.centralWindow2.show()
        self.fournisseurWidget.widget.close()