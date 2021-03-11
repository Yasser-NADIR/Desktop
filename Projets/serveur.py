from socket import *
from threading import *
import sys

host = ''
port = 1234

class ThreadEmission(Thread) :
	def __init__(self,conn) : 
		Thread.__init__(self)
		self.connexion = conn
	def run(self) :
		nom = self.getName()
		while 1 :
			msg_recu = self.connexion.recv(1024).decode("Utf8")
			if not msg_recu or msg_recu.upper() == "FIN" :
				break
			message = "%s> %s"%(nom,msg_recu)
			print(message)
			for cle in conn_client :
				if cle != nom :
					conn_client[cle].send(message.encode("Utf8"))
		self.connexion.close()
		del conn_client[nom]
		print("client %s deconnecte"%nom)
mysocket = socket(AF_INET,SOCK_STREAM)
try :
	mysocket.bind((host,port))
except :
	print("la liaison de socket a l'adresse est echoue")
	sys.exit()
print("serveur pret en attent de requetes")
mysocket.listen(5)
conn_client = {}
while 1 :
	connexion , adresse = mysocket.accept()
	th = ThreadEmission(connexion)
	th.start()
	it = th.getName()
	conn_client[it] = connexion
	print("client %s connecté, adresse ip %s, port %s"%(it,adresse[0],adresse[1]))
	message = "vous stes connecte,envoyer un message"
