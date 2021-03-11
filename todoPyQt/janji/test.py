import jinja2


systemFile = jinja2.FileSystemLoader(searchpath="./")
env = jinja2.Environment(loader=systemFile)
template = env.get_template("template.html")

table = []


for i in range(3):
	row = []
	for j in range(8):
		string = f"{i+1}{j+1}"
		row.append(string)
	table.append(row)


output = template.render(socityName="yasser",codeCMD="xxx",refMarche="xxx",codeFrns="xxx",codeSociete="xxx",dateCmd="xxx",flag="xxx",remarque="xxx",table=table)

with open("resultat.html", "w") as f:
	f.write(output)
