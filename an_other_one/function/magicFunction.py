from PyQt5.QtWidgets import QMessageBox
import time

def isInt(txt: str):
	try:
		if txt and "." in txt:
			return False
		int(txt)
		return True
	except:
		return False

def isFloat(txt: str):
	try:
		float(txt)
		return True
	except:
		return False

def verification(org: object):
	elements = org.__dict__
	CORRECT = True
	for name, reference in elements.items():
		if "line" in name:
			Type = name.split("_")[1]
			name = name.split("_")[2]
			content = reference.text()
			if Type == 'int':
				if isInt(content):
					pass
				else:
					QMessageBox.warning(org.widgetCentral, "verification de type", f"le type de {name} n'est pas correct correct")
					CORRECT = False
			elif Type == "text":
				pass

	return CORRECT