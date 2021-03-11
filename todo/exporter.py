from xlsxwriter import *


def enreColonne(papier,data,line):
	for i in range(len(data)):
		papier.write("""{}{}
			""".format(chr(ord("A")+i),line),
			"{}".format(data[i]))
def EnreExel(NomFichier,colonnes,data):
	documment = Workbook(NomFichier)
	papier = documment.add_worksheet()
	enreColonne(papier,colonnes,1)
	for i in range(len(data)):
		enreColonne(papier,data[i],i+2)
	documment.close()