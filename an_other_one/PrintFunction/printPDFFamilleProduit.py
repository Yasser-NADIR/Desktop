import jinja2
from xhtml2pdf import pisa


fileSystem = jinja2.FileSystemLoader(searchpath="./PrintFunction/templates")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("familleProduitTemplate.html")

def render(data, name=None):
	resultat = template.render(codefamilleproduit=data[0], nomfamilleproduit=data[1])
	if not name: name="familleProduit"
	with open("{}.pdf".format(name), "wb") as f:
		pisa.CreatePDF(resultat, dest=f)
