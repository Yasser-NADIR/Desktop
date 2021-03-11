from tkinter import *
import time


#Precision un origine de graphe
OriginX = 100
OriginY = 100

#longueur de chaque segment
Longueur = 100

#le nid et la nourriture
Nest = (OriginX, OriginY + Longueur*2)
Food = (OriginX + Longueur*4, OriginY + Longueur*3)

#nombre des lines et colonnes
NombreLine = 4
NombreColonne = 5

#rayon des circles des positions
RayonCircle = 10

master = Tk()

canvas = Canvas(master, width=600, height=600)
canvas.pack()

#la creation des line
for i in range(NombreLine):
	canvas.create_line(OriginX, OriginY+Longueur*i, OriginX+Longueur*(NombreColonne-1), OriginY+Longueur*i)

#la creation des colonne
for i in range(NombreColonne):
	canvas.create_line(OriginX+Longueur*i, OriginY, OriginX+Longueur*i, OriginY+Longueur*(NombreLine-1))

#la creation des points et les textes de la position de chaque point
for i in range(NombreColonne):
	for j in range(NombreLine):
		canvas.create_oval(OriginX+Longueur*i-RayonCircle,OriginY+Longueur*j-RayonCircle,OriginX+Longueur*i+RayonCircle,OriginY+Longueur*j+RayonCircle,fill="grey")
		pos = f"{i+1}{j+1}"
		canvas.create_text(OriginX+1 + Longueur * i, OriginY + Longueur * j, text=pos, fill="white")
#importer image
img = PhotoImage(file="bug.png")

#extrait les information du fichier
with open("resultatFourmi1.txt", "r") as f:
	content = f.readlines()

#nettoyer \n
for i in range(len(content)):
	content[i] = content[i][:-1]

NombreFourmi = int(content[0])

#les chemin de fourmie
path = []
for c in content[1:]:
	sousPath = []
	for element in c.split(","):
		sousPath.append((int(element[0]), int(element[2])))
	path.append(sousPath)


#ensemble des fourmie
ant = [canvas.create_image(*Nest, image=img) for i in range(NombreFourmi)]
#position de chaque fourmi
pos = [Nest for i in range(NombreFourmi)]

master.update()
for i in range(max([len(m) for m in path[:-1]])):
	for j in range(len(path)-1):
		if i <len(path[j]):
			pos[j] = canvas.coords(ant[j])
			canvas.move(ant[j], path[j][i][0]*Longueur-pos[j][0], path[j][i][1]*Longueur-pos[j][1])
	time.sleep(0.5)
	master.update()


for a in ant:
	canvas.delete(a)

img = PhotoImage(file="ant.png")
ant = canvas.create_image(*Nest, image=img)
master.update()

for i in range(len(path[-1])):
	pos = canvas.coords(ant)
	canvas.move(ant, path[-1][i][0]*Longueur-pos[0], path[-1][i][1]*Longueur-pos[1])
	time.sleep(.5)
	master.update()


mainloop()