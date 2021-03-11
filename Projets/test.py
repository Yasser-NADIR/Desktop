from tkinter import *


class demineur :
	def __init__(self):
		self.nbr_case = int()
		self.i = 0
		self.j = 0
		self.liste_button_i = []
		self.liste_button_j = []
		self.liste_label_i = []
		self.liste_labal_j = []
		self.liste_variables_label = []
		self.fenetre = Tk()
	def create_label(self,x) :
		self.nbr_case = x
		count = 0
		for i in range(self.nbr_case) :
			self.liste_label_j = []
			for j in range(self.nbr_case) :
				#self.liste_variables_label.insert(count, StringVar())
				label = Label(self.fenetre,text = count)#,textvariable = self.liste_variables_label[count])
				self.liste_label_j.insert(j,label)
				label.grid(row = i,column = j,ipadx = 10,ipady = 2)
				count += 1
			self.liste_label_i.insert(i,self.liste_label_j)
	def create_button(self) :
		count = 0
		for i in range(self.nbr_case) : 
			self.liste_button_j = []
			for j in range(self.nbr_case) :
				print(i," ",j)
				button = Button(self.liste_label_i[i][j])
				self.liste_button_j.insert(j,button)
				button.grid(row = i,column = j,ipadx = 10,ipady = 2)
			self.liste_button_i.insert(i,self.liste_button_j)
	def create_destroy_button(self) :
		Button(self.fenetre,text = "supression des buttons ",command = self.destroy_button).grid(row = self.nbr_case,column = 0,columnspan = 5)
	def destroy_button(self) :
		print("i = ",self.i,"j = ",self.j)
		if self.i < self.nbr_case :
			if self.j < self.nbr_case :
				self.liste_button_i[self.i][self.j].destroy()
				self.j += 1
			elif self.j == self.nbr_case :
				self.j = 0
				self.i += 1
				if self.i != self.nbr_case and self.j != self.nbr_case :
					self.liste_button_i[self.i][self.j].destroy()
					self.j += 1
				else :
					self.i,self.j = 0,0
					self.create_button(self.nbr_case)
	def self_destroy_button(self,nom) :
		pass



if __name__ == '__main__' :
	window = demineur()
	window.create_label(3)
	window.create_button()
	window.fenetre.mainloop()
