import ftplib

ftp = ftplib.FTP("158.69.62.133")
ftp.login("youssfi", "qwerty")

def send(nom_fichier):
	try:
		with open(nom_fichier, "rb") as f:
			print("envoi ...")
			ftp.storbinary("STOR {}".format(nom_fichier), f)
	except:
		print("le fichier n'exsite pas")

def recv(nom_enre, nom_fichier):
	with open(nom_enre, "wb") as f:
		ftp.retrbinary("RETR {}".format(nom_fichier), f.write)

send("fichier.pdf")
#recv("reception.txt", "Fichier.xml")

ftp.close()