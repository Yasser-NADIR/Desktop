from bs4 import BeautifulSoup

with open("template.html") as f:
	content = f.read()

soup = BeautifulSoup(content, "html.parser")
table = soup.find("table")

NomSociete = soup.find(id="NomSociete")
codeCMD = soup.find(id="codeCMD")
refMarche = soup.find(id="refMarche")
codeFrns = soup.find(id="codeFrns")
codeSociete = soup.find(id="codeSociete")
dateCmd = soup.find(id="dateCmd")
flag = soup.find(id="flag")
remarque = soup.find(id="remarque")

NomSociete.string = ""
codeCMD.string = ""
refMarche.string = ""
codeFrns.string = ""
codeSociete.string = ""
dateCmd.string = ""
flag.string = ""
remarque.string = ""

tr = soup.new_tag("tr")
thead = table.find("thead")
thead.insert_after(tr)
for _ in range(8):
	td = soup.new_tag("td")
	td.string="xxx"
	tr.append(td)

with open("testTemplate.html", "w") as f:
	f.write(str(soup))
	
print(str(soup))