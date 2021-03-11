from tkinter import *
import time

class DataGrid(LabelFrame):
	def __init__(self,master,columns,mode=0,**kwargs):
		super().__init__(master,**kwargs)
		self.mainColumn = []
		self.table      = []
		for c in columns:
			self.mainColumn.append(Label(self,text=c,relief=RIDGE))
		self.table.insert(0,self.mainColumn)
	def display(self):
		self.pack()
		i,j = 0,0
		for line in self.table:
			for c in line:
				c.grid(row=i,column=j)
				j += 1
			j  = 0
			i += 1
	def insert(self,values):
		line = list()
		for value in values:
			line.append(Label(self,text=value))
		self.table.append(line)
		self.display()
	def multiinsert(self,values):
		for v in values:
			self.insert(v)
	def vider(self):
		for table in self.table[1:]:
			for t in table:
				t.grid_forget()
		self.table = list()
		self.table.insert(0,self.mainColumn)

class DataGridV1(LabelFrame):
	def __init__(self,master,columns,mode=0,**kwargs):
		super().__init__(master,**kwargs)
		self.mainColumn = []
		self.table      = []
		self.lineNbr	= 1 
		self.values     = list()
		self.valeur		= list()
		self.selection	= int()
		self.table.insert(0,Frame(self))
		i = 0
		for c in columns:
			self.mainColumn.append(Label(self.table[0],text=c,relief=RIDGE))
			self.mainColumn[-1].grid(row=0,column=i)
			i += 1
	def display(self):
		self.pack()
		i,j = 1,0
		for line in self.table:
			line.pack()
			
	def insert(self,values):
		self.values.append(values)
		self.table.insert(self.lineNbr,LabelFrame(self,bg="red"))
		def printing(*args):
			self.selection = self.table.index(args[0].widget.grid_info()['in'])-1
			self.v = self.values[self.selection]
			print(self.v)
			self.supprimmerLine()
		i = 0
		for value in values:
			l = Label(self.table[self.lineNbr],text=value)
			l.grid(row=0,column=i)
			l.bind("<1>",printing)
			i += 1
		self.lineNbr += 1
		self.display()
	def multiinsert(self,values):
		for v in values:
			self.insert(v)
	def vider(self,*args):
		for t in self.table[1:]:
			t.pack_forget()
		self.table = self.table[0]
	def supprimmerLine(self):
		if len(self.table) > 1:
			self.table[self.selection+1].pack_forget()

#testing 
if __name__ == '__main__':
	root = Tk()

	tableau = DataGridV1(root,("c1","c2","c3"),text="tableau")
	tableau.multiinsert([["{}".format(x),"{}".format(x+1),"{}".format(x+2)] for x in range(10)])


	root.mainloop()