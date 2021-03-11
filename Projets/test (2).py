#list methods(checked) : append()/extend()/remove()/pop()/index()/sort()/reverse()/insert()/copy()/clear()
#dict methods (checked): clear()/copy()/items()/keys()/values()/get()/pop()/popitem()/update()/setdefault()/fromkeys()
#tkinter : les widgets-> frame,checkbutton,radiobutton,menubutton::menu/label/message/listbox/scrollbar/scales/entry/text/canvas?/messagebox?/filedialog/colorchooser
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

w = tkinter.Tk()
c = tkinter.Canvas(w,width=200,heigh=100,bg="black")
c.pack()
def test(event):
    c.create_oval(event.x,event.y,event.x+10,event.y+10,fill="red")
c.bind("<Button1-Motion>",test)
w.mainloop()