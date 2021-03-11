from socket import *
from threading import *
import sys

host = 'localhost'
port = 1234

class ThreadEmission(Thread) :
	def __init__(self,conn) :
		Thread.__init__(self)
		self.connexion = conn
	def run(self) :
		while 1 :
			msg_emis = input("")
			self.connexion.send(msg_emis.encode("Utf8"))

class ThreadReseption(Thread) :
	def __init__(self,conn) :
		Thread.__init__(self)
		self.connexion = conn
	def run(self) :
		while 1 :
			msg_recu = self.connexion.recv(1024)
			if not msg_recu or msg_recu.upper() == "FIN" :
				break
			print(msg_recu)
		print("la connexion est interrompue")
		th_E._stop()
		self.connexion.close()

connexion_principal = socket(AF_INET,SOCK_STREAM)
try :
	connexion_principal.connect((host,port))
except :
	print("echec de la connexion")
	sys.exit()
prin("la connexion est etabli")
th_R = ThreadReseption(connexion_principal)
th_E = ThreadEmission(connexion_principal)
th_R.start()
th_E.start()
