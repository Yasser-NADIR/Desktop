import jinja2

systemFile = jinja2.FileSystemLoader(searchpath='./PrintFunction/templates')
env = jinja2.Environment(loader=systemFile)
template = env.get_template("template.html")

def render(columns, contents, fileName):
	resultat = template.render(columns=columns, contents=contents, len=len)
	file = "{}.html".format(fileName)
	with open(file, "w") as f:
		f.write(resultat)