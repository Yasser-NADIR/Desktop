import jinja2
import pypandoc
from xhtml2pdf import pisa
import time
import os

fileSystem = jinja2.FileSystemLoader(searchpath="./template")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("templateImpression.html")

def toWord(data, name):
	filename="{}.docx".format(time.strftime("%Y%m%d%H%M%S"))
	if name: filename = name
	render = template.render(codefournisseuri=data[0],codefournisseur=data[1],nomfournisseur=data[2],tel=data[3],fax=data[4])
	with open("resultat.html", "w") as f:
		f.write(render)
	pypandoc.convert(source='resultat.html', format='html', to='docx', outputfile=filename, extra_args=['-RTS'])
	

def toPDF(data, name):
	filename="{}.pdf".format(time.strftime("%Y%m%d%H%M%S"))
	if name: filename = name	
	render = template.render(codefournisseuri=data[0],codefournisseur=data[1],nomfournisseur=data[2],tel=data[3],fax=data[4])
	with open("resultat.html", "w") as f:
		f.write(render)
	with open(filename, "wb") as f:
		pisa.CreatePDF(render, dest=f)
		