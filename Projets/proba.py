lettres = "abcd"
lst_lettres = [x for x in lettres]
l = len(lettres)
l1 = [0 for x in range(l)]
i = 1
Max = len(lettres) - 1
complet = [Max for i in range(Max+1)]
all_proba = [[x for x in l1]]
lst_mot_probal = []
f = open("abcd.txt","w")

def incraimant(liste, ind):
	liste[ind] = 0
	liste[ind+1] += 1

def verifie(liste, ind):
	Max = len(liste) - 1
	complet = [Max for i in range(Max+1)]
	if ind != Max:
		if liste[ind] > Max:
			incraimant(liste,ind)

def verifie_all(liste):
	i = 0
	while i < len(liste):
		v = verifie(liste,i)
		i += 1


while l1 != complet:
	l1[0] += 1
	verifie_all(l1)
	all_proba.append([x for x in l1])


for i in all_proba:
	mot_probal = ""
	for j in i:
		mot_probal += lst_lettres[j]
	lst_mot_probal.append(mot_probal)
	f.write(mot_probal+"\n")
	
print(lst_mot_probal)