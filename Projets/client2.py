from socket import *
from threading import *
import sys

host = 'localhost'
port = 1234

class ThtreadReseption(Thread) : 
	def __init__(self,conn) :
		Thread.__init__(self)
		self.connexion = conn
	def run(self) :
		while 1 :
			msg_recu = self.connexion.recv(1024).decode("Utf8")
			print("*" + msg_recu + "*")
			if not msg_recu or msg_recu.upper() == "FIN" :
				break
			try :
				with open("main.c","w") as f :
					f.write(msg_recu)
			except :
				print("erreur")
		th_E._stop()
		print("la connexion est interronpue")
		self.connexion.close()
class ThreadEmmision(Thread) : 
	def __init__(self,conn) :
		Thread.__init__(self)
		self.connexion = conn
	def run(self) :
		while 1 :
			#msg_emis = input(">-")
			try :
				with open("main.c","w") as f :
					msg_emis = f.read()
			except :
				print("erreur")
			self.connexion.send(msg_emis.encode("Utf8"))
connexion_principal = socket(AF_INET,SOCK_STREAM)
try :
	connexion_principal.connect((host,port))
except :
	print("la connexion echoue")
	sys.exit()
print("la connexion est retabli")
th_E = ThreadEmmision(connexion_principal)
th_R = ThtreadReseption(connexion_principal)
th_E.start()
th_R.start()
