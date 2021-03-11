from PyQt5.QtWidgets import QApplication 
from window import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow()
window.show()

rc = app.exec_()
sys.exit(rc)