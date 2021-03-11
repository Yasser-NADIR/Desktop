from tkinter import * 

#Fenetre tkinter
window = Tk()
window.title("boite de connexion")
window.resizable(width = False,height = False)
#Les variables des widgets
entre1_v = StringVar()
label1_v = StringVar()
label1_v.set("")
#Les fonctions
def afficher_texte() :
	if label1_v.get() == "" : 
		label1_v.set(entre1_v.get())
		entre1_v.set("")
	else : 
		label1_v.set(label1_v.get() + "\n" + entre1_v.get())
		entre1_v.set("")
#les widgets
frame1 = Frame(window,width = 200,height = 190,bg = "white")
frame1.grid(row = 0,column = 0)
frame2 = Frame(window,)
frame2.grid(row = 1,column = 0)
button = Button(frame2,text = "Envoyer",command = afficher_texte)
button.grid(row = 0,column = 1)
entre1 = Entry(frame2,textvariable = entre1_v)
entre1.grid(row = 0,column = 0,ipadx = 13)
entre1.bind("<Return>",afficher_texte)
label1 = Label(frame1,textvariable = label1_v)
label1.grid()

window.mainloop()