from tkinter import *
import commandok_v1
import bekeres_v2
import time 

def submit():
    szovag = entry.get()
    bekeres_v2.file(szovag)
    entry.delete(0, END)
    bekeres_v2.lista()

def resolts():
    bekeres_v2.commandok()

def click(event):
   entry.configure(state=NORMAL)
   entry.delete(0, END)
   entry.unbind('<Button-1>', clicked)      

window = Tk()

window.geometry("650x300")

submit = Button(window,text="submit",command=submit)
submit.pack()

resolts = Button(window,text="resolts",command=resolts)
resolts.pack()

entry = Entry()
entry.config(font=("Ink Free",40))
entry.config(width=25)
entry.insert(0,"show basic commands")
entry.pack()

clicked = entry.bind('<Button-1>', click)

window.mainloop()













