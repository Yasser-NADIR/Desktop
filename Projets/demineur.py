from tkinter import *

"""class button :
	def __init__(self,w) :
		self.window = w
		self.liste = list()
		self.liste_button = list()
	def destroying_button(self,x,y) :
		def d(event) :
			self.liste_button[x][y].destroy()
		self.liste_button[i][j].bind("<1>",d)
	def create_button(self,x) :
		self.nbr_button = x
		for i in range(x) :
			self.liste = list()
			for j in range(x) :
				self.liste.insert(j,Button(self.window,command = self.destroying_button(self.liste_button[i][j].grid_info()['row'],self.liste_button[i][j].grid_info()['column']))) 
				self.liste[j].grid(row = i,column = j)
			self.liste_button.insert(i,self.liste)
			def destroying_button(event) :
				self

if __name__ == "__main__" :
	window = Tk()
	b = button(window)
	b.create_button(3)
	window.mainloop()"""
w =Tk()
b = Button(w)
b.grid(row = 1,column = 1)
b.flash()
print(b.grid_info()['column'])
w.mainloop()