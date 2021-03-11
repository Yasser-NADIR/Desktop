import random
import psycopg2

db = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="location")
cursor = db.cursor()


def codageGenerate():
	database = []
	query_table = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"
	query_datatype = "SELECT data_type FROM information_schema.columns WHERE table_schema = 'public' AND TABLE_NAME = %s;"

	db = psycopg2.connect(host="localhost", user="postgres", password="azerty", database="location")
	cursor = db.cursor()

	cursor.execute(query_table)
	tables = cursor.fetchall()
	for table in tables:
		cursor.execute(query_datatype, table)
		types = cursor.fetchall()
		codage = list()
		for t in types:
			if t[0] == 'integer' or t[0] == 'real':
				codage.append(1)
			elif t[0] == 'character varying':
				codage.append(2)
			elif t[0] == 'date':
				codage.append(3)
		codage = [*codage[1:]]
		database.append((table[0], codage))
	return database

def queryGenerate(dataType, rows=10, table=""):
	query = "insert into {} values".format(table)
	for i in range(rows):
		data = []
		data.append(i+1)
		for Type in dataType:
			if Type == 1:
				data.append(random.randint(1, 2))
			elif Type == 2:
				data.append("'{}'".format("".join([chr(random.randint(65, 90)) for _ in range(1)])))
			elif Type == 3:
				data.append("'{}-{}-{}'".format(random.randint(1999, 2020), random.randint(1, 12), random.randint(1, 28)))
		body = "("
		for ele in data:
			body += f"{ele},"
		body = body[:-1] + "),\n"
		query += body

	query = query[:-2] + ";\n"
	with open("test.sql", "a") as f:
		f.write(query)
	return query

database = codageGenerate()
queries = list()
with open("test.sql", "w") as f:
	f.write("")
for table in database:
	queries.append(queryGenerate(table[1], table=table[0]))

with open("test.sql", "r") as f:
	queries = f.read()