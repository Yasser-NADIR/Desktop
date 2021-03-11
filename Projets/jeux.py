import tkinter
import random
class button:
    def __init__(self,master,x,y):
        self.master = master
        self.x = x
        self.y = y
        self.button = tkinter.Button(self.master,command=self.detruire)
        self.button.grid(row=self.y,column=self.x,ipadx=5,ipady=3)
    def detruire(self):
        self.button.destroy()
class num:
    def __init__(self,master,x,y,n):
        self.n = n
        self.master = master
        self.x = x
        self.y = y
        self.label = tkinter.Label(self.master)
        self.label.grid(row=self.y,column=self.x,ipadx=5,ipady=6)
    def bombe(self):
        if random.randint(0,1):
            self.label["text"] = "X"
            return 1
        else :
            self.label["text"] = self.n
            return 0
if __name__ == "__main__":
    w = tkinter.Tk()
    i = 0
    list_bombe,liste = list(),list()
    while(i<3):
        j = 0
        while(j<3):
            n = random.randrange(1,4)
            l = num(w,j,i,n)
            l.bombe()
            #liste.append(l.bombe())
            button(w,j,i)
            j+=1
        list_bombe.append(liste)
        i+=1
    w.mainloop()