from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI=Tk()
GUI.title('Knowledge note')
GUI.geometry('500x400')

B1=ttk.Button(GUI,text='How much money do you have?')
B1.pack(ipadx=20,ipady=15)

def Button2():
    text='You have money 100 Bath'
    messagebox.showinfo('Clash Balace',text)

FB2= Frame(GUI)
FB2.place(x=50,y=200)
B2=ttk.Button(FB2,text='How much money do you have?',command=Button2)
B2.pack(ipadx=20,ipady=15)



GUI.mainloop()
