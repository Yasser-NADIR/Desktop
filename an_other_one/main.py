from PyQt5.QtWidgets import QApplication
from window import MainWindow
import sys

app = QApplication(sys.argv)

main = MainWindow()

if __name__ == '__main__':
	
	main.show()

	app.exec_()

