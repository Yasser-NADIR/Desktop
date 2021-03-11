from tkinter import *
from tkinter.messagebox import *

window = Tk()
entree1_v = StringVar()
def afficher_connexion() :
	global entree1_v
	def afficher_message(event) :
		showinfo("connexion verifié","vous etes connecté")
		window.destroy()
	label2 = Label(window,text = "entrez votre mot secret")
	label2.grid(row = 2,column = 0)
	entree1 = Entry(window,textvariable = entree1_v,show = '*')
	entree1.grid(row = 3,column = 0)
	entree1.bind("<Return>",afficher_message)
window.geometry("200x200")
window.title("boite de connexion")
window.resizable(width = False,height = False)
label1 = Label(window,text = "vous êtes ? : ")
label1.grid(row = 0,column = 0,pady = 10,padx = 65)
menu = Menubutton(window,text = "menu")
menu.grid(row = 1,column = 0,pady = 10,padx = 65)
me=Menu(menu,tearoff = False)
me.add_command(label = "yasser",command = afficher_connexion)
me.add_command(label = "soufiane",command = afficher_connexion)
me.add_command(label = "houssam",command = afficher_connexion)
menu.configure(menu = me)
window.mainloop()