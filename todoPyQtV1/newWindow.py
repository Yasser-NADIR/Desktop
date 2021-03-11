from formule import Ui_Form
from PyQt5.QtWidgets import QWidget

class window2(Ui_Form):
	def __init__(self, centralMainWindow):
		super(window2, self).__init__()
		self.centralWindow2 = QWidget(centralMainWindow)
		self.setupUi(self.centralWindow2)
		self.centralWindow2.close()