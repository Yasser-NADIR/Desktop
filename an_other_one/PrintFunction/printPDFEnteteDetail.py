import jinja2
from xhtml2pdf import pisa
import os

fileSystem = jinja2.FileSystemLoader(searchpath="./PrintFunction/templates")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("enteteDetailTemplate.html")



def printPDFEnteteDetail(name, entete, detail):
	resultat = template.render(codecommande=entete[0], codefournisseur=entete[1], datecommande=entete[2], rows=detail)
	with open("impression\\{}.pdf".format(name), "wb") as f:
		pisa.CreatePDF(resultat, dest=f)
	os.system("impression\\{}.pdf".format(name))
