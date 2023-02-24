from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime
import csv

def addcsv(datalist):
    with open('data.csv','a',newline='') as file:
        fw=csv.writer(file) #fw=file Writer
        fw.writerow(datalist) #datalist=['pen','pencil']

def readcsv():
    with open('data.csv',newline='')as file:
        fr=csv.reader(file) #fr=file reader
        data=list(fr)
    return data
###############################################################

GUI=Tk()
GUI.title('Knowledge note')
GUI.geometry('400x400')

#B1=ttk.Button(GUI,text='How much money do you have?')
#B1.pack(ipadx=20,ipady=20)

def Button2():
    text='1)Enter what you have learned in Python101 class.\n 2)Clik Enter button.'
    messagebox.showinfo('Help',text)

FB2= Frame(GUI)
FB2.place(x=180,y=320)
B2=ttk.Button(FB2,text='How to use this programs?',command=Button2)
B2.pack(ipadx=15,ipady=15)

##########################################################

LF1=ttk.LabelFrame(GUI,text='Enter your data')
LF1.pack()

lbl_title=ttk.Label(LF1,text="title: ")
lbl_title.pack(pady=10)

v_data=StringVar() #spacial variable use in gui
E1=ttk.Entry(LF1,textvariable=v_data)
E1.pack(padx=20,pady=0)

lbl_detail=ttk.Label(LF1,text="detail: ")
lbl_detail.pack(pady=10)

B_data=StringVar() #spacial variable use in gui
E2=ttk.Entry(LF1,textvariable=B_data)
E2.pack(padx=20,pady=0)

def SaveData():
    t=datetime.now().strftime('%Y%m%d %H%M')
    data1=v_data.get()
    data2=B_data.get()
    text=[t,data1,data2]
    addcsv(text)
    v_data.set('')
    B_data.set('')

B4=ttk.Button(LF1,text='save',command=SaveData)
B4.pack(pady=10,ipadx=10,ipady=10)



GUI.mainloop()
