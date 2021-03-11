from sqlite3 import *

fichierdonnes = """C:\\Users\\Administrateur\\Desktop\\db_test.sq3"""
conn = connect(fichierdonnes)
cur = conn.cursor()
#cur.execute("CREATE TABLE membre(age INTEGER,nom TEXT,taille REAL)")
#cur.execute("INSERT INTO membre(age,nom,taille) VALUES (19,'YASSER',1.23)")
#cur.execute("INSERT INTO membre(age,nom,taille) VALUES (19,'SOUFIANE',1.22)")
#conn.commit()
cur.execute("SELECT * FROM membre")
print("notre tableau ")
for l in cur :
	print(l)
cur.close()
conn.close()
