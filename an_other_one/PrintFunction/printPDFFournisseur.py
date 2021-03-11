import jinja2
from xhtml2pdf import pisa


fileSystem = jinja2.FileSystemLoader(searchpath="./PrintFunction/templates")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("fournisseurTemplate.html")

def render(data, name=None):
	resultat = template.render(codefournisseuri=data[0],
		codefournisseur=data[1],
		nomfournisseur=data[2],
		tel=data[3],
		fax=data[4])
	if not name: name="fournisseur"
	with open("{}.pdf".format(name), "wb") as f:
		pisa.CreatePDF(resultat, dest=f)
