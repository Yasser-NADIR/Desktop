from PyQt5.QtWidgets import QApplication
from window import mainWindow
import sys

app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec_()