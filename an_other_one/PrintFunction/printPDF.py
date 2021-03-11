import jinja2
from xhtml2pdf import pisa
import os

systemFile = jinja2.FileSystemLoader(searchpath='./PrintFunction/templates')
env = jinja2.Environment(loader=systemFile)
template = env.get_template("template.html")

def render(columns, contents, fileName):
	resultat = template.render(columns=columns, contents=contents, len=len)
	file = "{}.pdf".format(fileName)

	with open(file, "wb") as f:
		pisa.CreatePDF(resultat, dest=f)

