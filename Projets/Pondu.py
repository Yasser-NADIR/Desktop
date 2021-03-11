from random import *
from os import *
count = 0
count_l = 0
tentative = 10
liste_mot = []
liste_letre = []
gagner = False
for l in ("salut","monger","montagne") :
	liste_mot.insert(count,l)
	count += 1
emplacement = randint(0,2)
mot_choisi = liste_mot[emplacement]
for i in range(len(mot_choisi)) : 
	liste_letre.insert(i,i+1)
print(mot_choisi)
print("bievenu utilisateur dans le jeux pondu")
while tentative > 0 :
	l = input("svp entrez un caractere ")
	count_l = 0
	if len(l) == 1 :
		a = 0
		for k in mot_choisi :
			if l == k :
				liste_letre[count_l] = l
				a += 1
			count_l += 1
		if a != 0 : 
			print("Bravo !")
		else :
			print("essayer encore")
		print(liste_letre)
		b = 0
		for i in range(len(mot_choisi)) :
			if mot_choisi[i] == liste_letre[i] :
				b += 1
		tentative -= 1
		if b == len(mot_choisi) :
			print("Bravo ! tu as gagner")
			break
	else :
		print("svp entrez un seul caractere")