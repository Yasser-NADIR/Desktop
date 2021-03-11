import jinja2
import pypandoc
import os

fileSystem = jinja2.FileSystemLoader(searchpath="./PrintFunction/templates")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("fournisseurTemplate.html")

def render(data, name=None):
	if not name: name="./fournisseur.docx"
	resultat = template.render(codefournisseuri=data[0],codefournisseur=data[1],nomfournisseur=data[2],tel=data[3],fax=data[4])
	with open("resultat.html", "w") as f:
		f.write(resultat)
	pypandoc.convert(source='resultat.html', format='html', to='docx', outputfile=name)
	#os.remove("resultat.html")