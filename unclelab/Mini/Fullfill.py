from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Money Tracking')
width = 600
height = 800
x = 450
y = 10
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#FFEDDC')

F1 = Frame(root, width=580, height=660,bg='white')
FF1 = Frame(F1)
A1 = Label(FF1,text='รายการ',font=('TH Sarabun New',25))
A1.grid(row=0)

FF1.pack()
F1.pack(pady=10)

F2 = Frame(root, width=600,height=100,)

B1 = Button(F2,text='บันทึก',font=('TH Sarabun New',20),fg='black',bg='#F0D579',command='')
B1.grid(row=0,column=0,ipady=20,ipadx=30,sticky=W)
Blank1 = Label(F2,text='',bg='#FFEDDC')
Blank1.grid(row=0,column=1,ipady=40,ipadx=50)
B2 = Button(F2,text='ยกเลิก',font=('TH Sarabun New',20),fg='black',bg='#F0D579',command='')
B2.grid(row=0,column=2,ipady=20,ipadx=30,sticky=E)


F2.pack()

root.mainloop()