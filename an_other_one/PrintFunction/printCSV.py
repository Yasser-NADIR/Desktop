import csv

def render(columns, contents, fileName):
	file = "{}.csv".format(fileName)
	with open(file, "w") as f:
		spam = csv.writer(f, delimiter=";")
		spam.writerow(columns)
		for content in contents:
			spam.writerow(content)
