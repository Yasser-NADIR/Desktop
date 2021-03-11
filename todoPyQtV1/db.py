import psycopg2

con = psycopg2.connect(
		host = "localhost",
		database = "dbApp",
		user = "postgres",
		password = "azerty"
	)

cur = con.cursor()

cur.execute("""DELETE FROM dbfournisseur
					WHERE code_fournisseuri = 3
					""")
print(con.commit())

cur.close

con.close()