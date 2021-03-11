from sqlite3 import *


conn = connect("DB.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS b_frns(
	code_Fournisseuri	INTEGER, 
	nom_Fournisseur	    TEXT,
	code_Fournisseur	INTEGER, 
	regc	            TEXT,	
	tel	                TEXT,	
	fax	                TEXT,	
	c_corresp	        TEXT,	
	siteweb	            TEXT,	
	email	            TEXT,	
	fichier	            TEXT,	
	adresse_banque	    TEXT,	
	compte_b	        TEXT,	
	adrs1	            TEXT,	
	adrs2	            TEXT,	
	adrs3	            TEXT,	
	rmq1	            TEXT,	
	rmq2	            TEXT,
	flag	            TEXT	
	);
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS b_stat(
	code_sts	INTEGER,	
	nom_sts		TEXT,	
	rmq			TEXT,	
	flag		TEXT	
);
""")

conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS catalfrns(
	Refproduitfrns		INTEGER,	
	Nom_produitfrns		TEXT	,
	Refproduit			INTEGER	,
	code_fournisseuri	INTEGER	,
	qte_min				INTEGER	,
	Prx_uni				REAL,
	code_tva			INTEGER	,
	code_rrr			INTEGER	,
	delai_app			INTEGER	,
	Indisponible		TEXT,	
	remarque			TEXT,
	flag				TEXT	
) ;
""")
conn.commit()



cursor.execute("""
CREATE TABLE IF NOT EXISTS det_cmd(
	ld_Ncommande		INTEGER	,
	Ncommanded			INTEGER	,
	Refproduit			INTEGER	,
	Quantitecmd			INTEGER	,
	code_un				INTEGER	,
	prix_unitaire		REAL,
	prx_tot				REAL,
	dat_liv_souhaitee	DATETIME,	
	code_stsd			TEXT,
	remarqued			TEXT	
);
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ent_cmd(
	Ncommande			INTEGER	,
	code_societe		INTEGER	,
	ndevis				INTEGER	,
	code_fournisseuri	INTEGER	,
	Date_commande		DATETIME,	
	code_fournisseur	INTEGER	,
	date_livraison		DATETIME,
	code_marchei		TEXT	,
	Destinataire		TEXT	,
	Adresse_livraison	TEXT	,
	Ville_livraison		TEXT	,
	code_sts			TEXT	,
	remarque			TEXT	
) ;
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS familleprd(
	code_famille	INTEGER	,
	code_famille_d	INTEGER	,
	famille			TEXT	,
	remarque		TEXT	,
	flag			TEXT	
	);
	""")
conn.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS produits(
	Refproduit		INTEGER	,
	Nom_produitfrns	TEXT	,
	code_famille	INTEGER	,
	Prx_uni			REAL	,
	Indisponible	TEXT	,
	code_sts		TEXT	,
	remarque		TEXT	,
	flag			TEXT	
	);
""")
conn.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS unite(
	code_un	INTEGER	,
	lib_un	TEXT	,
	remu	TEXT	,
	flag	TEXT	
	)
	""")	
conn.commit()


def Valider(table,colonne,args):
	cursor.execute("""
		INSERT INTO {}{}
		VALUES{}
		""".format(table,str(tuple(colonne)),str(tuple(args))))
	conn.commit()

def Rechercher(table,colonne,Id):
	cursor.execute("""
				SELECT * FROM {} WHERE {} = {}
		""".format(table,colonne,Id))
	return cursor.fetchall()



def Update(table,colonnes,valeurs,Id):
	if len(colonnes) == len(valeurs):
		for i in range(len(colonnes)):
			cursor.execute("""
						UPDATE {} SET {} = ?
						
						 WHERE {} = {}
				""".format(table,colonnes[i],colonnes[0],Id),(valeurs[i],))
			conn.commit()
	else : print("ERREUR : nombre des valeurs est different a {}".format(len(colonnes)))

def Delete(table,colonne,Id):
	cursor.execute("""
				DELETE FROM {} 
				WHERE {} = {}
		""".format(table,colonne,Id))

def Premier(table):
	cursor.execute("""
			SELECT * FROM {}
		""".format(table))
	return cursor.fetchall()[0]

def Dernier(table):
	cursor.execute("""
			SELECT * FROM {}
		""".format(table))
	return cursor.fetchall()[-1]

def Tous(table,ordre):
	cursor.execute("""
			SELECT * FROM {}
			ORDER BY {}
		""".format(table,ordre))
	return cursor.fetchall()

def NombreEnr(table):
	cursor.execute("""
			SELECT count(*) FROM {}
		""".format(table))
	return cursor.fetchall()[0][0]

def Demmande(table,emplace):
	cursor.execute("""
			SELECT * FROM {}
		""".format(table))
	return cursor.fetchall()[emplace]
