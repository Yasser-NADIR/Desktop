from tkinter import *
from tkinter import ttk
from DataBase import *
from DataGrid import *
from exporter import *

class frame_form(Frame):
	"""docstring for """
	def __init__(self,master,label_text,label_width,**kwargs):
		super().__init__(master,**kwargs)
		self.label_text = label_text
		self.var_entre  = StringVar()
		self.label = Label(self,text=self.label_text,width=label_width,anchor=W)
		self.entre = Entry(self,textvariable=self.var_entre)
	def display(self):
		self.pack()
		self.label.pack(side=LEFT,padx=5,pady=5)
		self.entre.pack(side=LEFT,padx=5,pady=5)
	def value(self):
		return self.var_entre.get()
	def set(self,value):
		self.var_entre.set(str(value))
		

#root.winfo_geometry().split("+")[1:]
class creation_window:
	def __init__(self,master,geometry):
		self.window = master
		self.g = geometry
		self.window.geometry(f"100x100+{int(self.g[0])+1}+{int(self.g[1])+1}")
		self.window.title("Ouvrire une session")
		self.form1 = frame_form(self.window,label_text="Nom de l'utilisateur:")
		self.form2 = frame_form(self.window,label_text="Mot de passe:")
		self.ok = Button(self.window,text="Ok")
		self.annuler = Button(self.window,text="Annuler")
	def display(self):
		self.form1.display()
		self.form2.display()
		self.ok.pack()
		self.annuler.pack()
		self.window.deiconify()
	def ok(self):
		pass
	def annuler(self):
		pass

class frame_creation(Frame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.page = int()
		self.form1 = frame_form(self,label_text="Nom utilisateur",label_width=17)
		self.form2 = frame_form(self,label_text="Mot de passe",label_width=17)
		self.ok      = Button(self,text="Ok",width=7)
		self.annuler = Button(self,text="Annuler",command=self.annuler_f)
	def display(self):
		self.pack()
		self.form1.display()
		self.form2.display()
		self.annuler.pack(side=RIGHT,padx=5,pady=5)
		self.ok.pack(side=RIGHT,padx=10,pady=5)
	def ok_f(self):
		pass
	def annuler_f(self):
		self.pack_forget()

class frame(LabelFrame):
	def __init__(self,master,db,dbField,args,**kwargs):
		super().__init__(master,**kwargs)
		self.db = db
		self.dbField = dbField
		self.page = int()
		self.master = master
		self.args = args
		self.values = list()
		self.liste_form = list()
		width = 0
		for arg in args:
			width = max(width,len(arg))
		width += 5
		for arg in args:
			self.liste_form.append(frame_form(self,label_text=arg,label_width=width))
	def display(self):
		self.pack(side=LEFT,anchor=N)
		for form in self.liste_form:
			form.display()
	def value(self):
		self.values = list()
		for form in self.liste_form:
			self.values.append(form.value())
	def Nouveau(self):
		for form in self.winfo_children():
			form.pack_forget()
		self.display()
		for child in self.liste_form:
			child.var_entre.set("")
	def Valider(self):
		self.value()
		for v in self.values:
			if not v : return
		if self.values : Valider(self.db,self.dbField,self.values)
		self.Nouveau()
	def Rechercher(self):
		for form in self.winfo_children():
			form.pack_forget()
		rech = frame_form(self,label_text="Donnez id fournisseur pour rechercher",label_width=27)
		rech.display()
		table = DataGrid(self,self.args)
		def aller():
			Id = rech.value()
			if Id:
				table.vider()
				liste = Rechercher(self.db,"code_Fournisseuri",Id)
				table.multiinsert(liste)
		Button(rech,text="Rechercher",command=aller).pack(anchor=N)
	def Modifier(self):
		for form in self.winfo_children():
			form.pack_forget()
		mod = frame_form(self,label_text="Donnez id fournisseur pour modifier",label_width=27)
		mod.display()
		def modife():
			Id = mod.value()
			if Id:
				data = Rechercher(self.db,self.dbField[0],Id)[0]
				self.display()
				for i in range(len(self.liste_form)):
					self.liste_form[i].set(data[i])
				Button(self,text="modifier",command=valider).pack(side=BOTTOM)
		def valider():
			self.value()
			Id = mod.value()
			for v in self.values:
				if not v : return
			if self.values : Update(self.db,self.dbField,self.values,Id)
			self.display()
			for child in self.liste_form:
				child.var_entre.set("")
			self.Modifier()
		Button(mod,text="Rechercher",command=modife).pack()
	def Supprimer(self):
		for form in self.winfo_children():
			form.pack_forget()
		sup = frame_form(self,label_text="Donnez id pour supprimer",label_width=27)
		sup.display()
		def supprimer():
			Id = sup.value()
			if Id : Delete(self.db,self.dbField[0],Id)
		Button(sup,text="Rechercher",command=supprimer).pack()
	def PremierEnre(self):
		for form in self.winfo_children():
			form.pack_forget()
		first = Premier(self.db)
		self.display()
		for i in range(len(self.liste_form)):
				self.liste_form[i].set(first[i])
		self.page = 1
		def valider():
			self.value()
			for v in self.values:
				if not v : return
			Id = first[0]
			if self.values : Update(self.db,self.dbField,self.values,Id)
			self.display()
		Button(self,text="modifer",command=valider).pack()
	def DernierEnre(self):
		for form in self.winfo_children():
			form.pack_forget()
		last = Dernier(self.db)
		self.display()
		self.page = NombreEnr(self.db)-1
		for i in range(len(self.liste_form)):
				self.liste_form[i].set(last[i])
		def valider():
			self.value()
			for v in self.values:
				if not v : return
			Id = last[0]
			if self.values : Update(self.db,self.dbField,self.values,Id)
			self.display()
		Button(self,text="modifer",command=valider).pack()
	def Arrier(self):
		for form in self.winfo_children():
			form.pack_forget()
		self.display()
		if 0<self.page :
			self.page -= 1
			current = Demmande(self.db,self.page)
			for i in range(len(self.liste_form)):
				self.liste_form[i].set(current[i])
		def valider():
			self.value()
			for v in self.values:
				if not v : return
			Id = current[0]
			if self.values : Update(self.db,self.dbField,self.values,Id)
			self.display()
		Button(self,text="modifer",command=valider).pack()
	def Avant(self):
		for form in self.winfo_children():
			form.pack_forget()
		self.display()
		if self.page<NombreEnr(self.db)-1 :
			self.page += 1
			current = Demmande(self.db,self.page)
			for i in range(len(self.liste_form)):
				self.liste_form[i].set(current[i])
		def valider():
			self.value()
			for v in self.values:
				if not v : return
			Id = current[0]
			if self.values : Update(self.db,self.dbField,self.values,Id)
			self.display()
		Button(self,text="modifer",command=valider).pack()
	def AfficherTous(self):
		for form in self.winfo_children():
			form.pack_forget()
		table = DataGrid(self,self.args)
		table.display()
		data = Tous(self.db,self.dbField[0])
		table.multiinsert(data)
	def Imprimer(self):
		data = Tous(self.db,self.dbField[0])
		EnreExel("fournisser.xlsx",self.args,data)
	def Quitter(self):
		for child in self.master.winfo_children():
			if type(child) != Menu:
				child.pack_forget()

class frame_ameliorer(frame):
	def __init__(self,master,db,dbField,args,changes,**kwargs):
		super().__init__(master,db,dbField,args,**kwargs)
		for key,value in changes.items():
			self.liste_form[key].entre = value[0](self.liste_form[key],textvariable=self.liste_form[key].var_entre,values=value[1])

class frame_details(LabelFrame):
	def __init__(self,master,args,changes,**kwargs):
		super().__init__(master,**kwargs)
		self.liste_form = list()
		self.tableauData = DataGrid(self,args)
		self.values = list()
		width = 0
		for arg in args:
			width = max(width,len(args))
		for arg in args:
			self.liste_form.append(frame_form(self,label_text=arg,label_width=width))
		#les changement entre->combobox
		for key,value in changes.items():
			self.liste_form[key].entre = value[0](self.liste_form[key],textvariable=self.liste_form[key].var_entre,values=value[1])
	def display(self):
		self.pack(side=LEFT,anchor=N)
		for form in self.liste_form:
			form.display()
		self.tableauData.display()
	def value(self):
		self.values = list()
		for form in self.liste_form:
			self.values.append(form.value())
	def setEmpty(self):
		for form in self.liste_form:
			form.set("")
	def ajouter(self):
		self.value()
		for v in self.values:
			if not v : return
		self.tableauData.insert(self.values)
		self.setEmpty()

class frame_creation(Frame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.page = int()
		self.form1 = frame_form(self,label_text="Nom utilisateur",label_width=17)
		self.form2 = frame_form(self,label_text="Mot de passe",label_width=17)
		self.ok      = Button(self,text="Ok",width=7)
		self.annuler = Button(self,text="Annuler",command=self.annuler_f)
	def display(self):
		self.pack()
		self.form1.display()
		self.form2.display()
		self.annuler.pack(side=RIGHT,padx=5,pady=5)
		self.ok.pack(side=RIGHT,padx=10,pady=5)
	def ok_f(self):
		pass
	def annuler_f(self):
		self.pack_forget()

class frame_option(LabelFrame):
	def __init__(self,master,options,commands,**kwargs):
		super().__init__(master,**kwargs)
		self.buttonListe = list()
		for i in range(len(options)):
			self.buttonListe.append(Button(self,text=options[i],width=2,command=commands[i]))
	def display(self):
		self.pack(side=LEFT,anchor=N)
		for button in self.buttonListe:
			button.pack(pady=5)


