from tkinter import *
from math import *
class canon :
	def __init__(self,boss,x,y) : 
		self.boss = boss
		self.x1 , self.y1 = x , y
		self.lbu = 50
		self.x2 , self.y2 = x + self.lbu , y
		self.buse = boss.create_line(self.x1,self.y1,self.x2,self.y2,width = 20)
		self.r = 20
		self.boss.create_oval(self.x1 - self.r,self.y1 - self.r,self.x1 + self.r,self.y1 + self.r,fill = "blue",width = 3)
		self.obus = self.boss.create_oval(x,y,x,y,fill = "red")
		self.anim = False
		self.xmax = int(self.boss.cget('width'))
		self.ymax = int(self.boss.cget('height'))
	def orienter(self,angle) :
		self.angle = float(angle)*2*pi/360
		self.x2 = self.x1 + self.lbu*cos(self.angle)
		self.y2 = self.y1 - self.lbu*sin(self.angle)
		self.boss.coords(self.buse,self.x1,self.y1,self.x2,self.y2)
	def feu(self) :
		if not self.anim : 
			self.anim = True 
			self.boss.coords(self.obus,self.x2 - 3,self.y2 - 3,self.x2 + 3,self.y2 + 3)
			v = 15
			self.vx = v*cos(self.angle)
			self.vy = -v*sin(self.angle)
			self.animer_obus()
	def animer_obus(self) :
		if self.anim :
			self.boss.move(self.obus,int(self.vx),int(self.vy))
			c = tuple(self.boss.coords(self.obus))
			x0 , y0 = self.xmax , self.ymax
			if c[0] > x0 or c[1] > y0 :
				self.anim = False
			self.vy += .5
			self.boss.after(30,self.animer_obus)
if __name__ == '__main__' :
	window = Tk()
	canvas = Canvas(window,width = 250,height = 250,bg = "ivory")
	canvas.pack(padx = 10,pady = 10)
	c1 = canon(canvas,50,200)
	s1 = Scale(window,label = "hausse",from_ = 90,to = 0,command = c1.orienter)
	s1.pack(side = LEFT,pady = 5)
	s1.set(25)
	Button(window,text = "FEU!",command = c1.feu).pack(side = LEFT)
	window.mainloop()