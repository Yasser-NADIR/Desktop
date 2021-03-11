from socket import *
from threading import *
import sys

host = ''
port = 1234

class ThreadReseption(Thread) :
	def __init__(self,conn) :
		Thread.__init__(self)
		self.connxion = conn
	def run(self) :
		nom = self.getName()
		while 1 :
			msg_recu = self.connxion.recv(1024).decode("Utf8")
			if not msg_recu or msg_recu.upper() == "FIN" :
				break
			message = "%s>%s"%(nom,msg_recu)
			print(message)
			for client in dict_conn :
				if client != nom :
					dict_conn[client].send(message.encode("Utf8"))
		print("client %s est deconnecté"%nom)
		del dict_conn[nom]
		self.connxion.close()

if __name__ == '__main__' :
	connexion_principal = socket(AF_INET,SOCK_STREAM)
	try :
		connexion_principal.bind((host,port))
	except :
		print("echec de la liaison")
		sys.exit()
	print("le liaison est reussi")
	connexion_principal.listen(5)
	dict_conn = {}
	while 1 :
		connxion,adresse = connexion_principal.accept()
		th_R = ThreadReseption(connxion)
		th_R.start()
		it = th_R.getName()
		dict_conn[it] = connxion
		print("client %s, connetcté a l'adresse %s, le port %s"%(it,adresse[0],adresse[1]))
		message = "vous etes connecte au serveur"
