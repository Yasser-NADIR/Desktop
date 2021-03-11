import jinja2
from xhtml2pdf import pisa


fileSystem = jinja2.FileSystemLoader(searchpath="./PrintFunction/templates")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("produitTemplate.html")

def render(data, name=None):
	resultat = template.render(codeproduit=data[0],
		codefamilleproduit=data[1],
		nomproduit=data[2])
	if not name: name="produit"
	with open("{}.pdf".format(name), "wb") as f:
		pisa.CreatePDF(resultat, dest=f)
