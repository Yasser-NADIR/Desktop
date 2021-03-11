from bs4 import BeautifulSoup
from lxml import etree

#pour cette fonction elle imprime comme <tab>content</tag>
def render2(nameTable, columns, rows, nameFile):
	root = etree.Element(nameTable)
	for row in rows:
		record_test = etree.SubElement(root, "record_test")
		for i in range(len(columns)):
			column = etree.SubElement(record_test, str(columns[i]))
			column.text = str(row[i])

	content = """<?xml version="1.0"?>\n{}""".format(etree.tostring(root, pretty_print=True).decode())
	file = "{}.xml".format(nameFile)
	with open(file, "w") as f:
		f.write(content)

#pour cette fonction elle imprime comme 
#<tab>
#	content
#</tag>
def render(nameTable, columns, rows, nameFile):
	#creation de l'entete de fichier xml
	soup = BeautifulSoup("""<?xml version="1.0"?>\n""", "lxml")
	#creation la tag principal qui est le nom de la table
	mainTag = soup.new_tag(nameTable)
	soup.append(mainTag)

	for row in rows:
		record_test = soup.new_tag("record_test")
		mainTag.append(record_test)
		for i in range(len(columns)):
			data = soup.new_tag(columns[i])
			data.string = str(row[i])
			record_test.append(data)
		
	content = str(soup.prettify())
	file = "{}.xml".format(nameFile)
	with open(file, "w") as f:
		f.write(content)