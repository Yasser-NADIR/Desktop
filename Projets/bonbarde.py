import tkinter
import math

class canon:
    def __init__(self,boss,x,y):
        self.boss = boss
        self.x1, self.y1 = x, y
        self.lbu = 50
        self.x2, self.y2 = x+self.lbu, y
        self.buse = boss.create_line(self.x1,self.y1,self.x2,self.y2,width=10)
        r = 15
        boss.create_oval(x-r,y-r,x+r,y+r,width=3,fill='blue')
    def orienter(self,angle):
        self.angle = float(angle)*2*math.pi/360
        self.x2 = self.x1 + self.lbu*math.cos(self.angle)
        self.y2 = self.y1 - self.lbu*math.sin(self.angle)
        self.boss.coords(self.buse,self.x1,self.y1,self.x2,self.y2)

if __name__ == "__main__":
    w = tkinter.Tk()
    can = tkinter.Canvas(w,width=200,height=200,bg='ivory')
    can.pack()
    c = canon(can,20,200)
    s = tkinter.Scale(w,label="angle",from_=90,to=0,command=c.orienter)
    s.pack()
    w.mainloop()