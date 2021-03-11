from PyQt5.QtWidgets import QApplication
from window import mainWindow
import sys

app = QApplication(sys.argv)

main = mainWindow()
main.show()

if __name__ == '__main__':
	app.exec_()