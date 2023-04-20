from tkinter import *
import subprocess

def open_add():
    root.destroy()
    subprocess.Popen(['python', 'Fullfill.py'])

root = Tk()
root.title('Money Tracking')
width = 600
height = 800
x = 450
y = 10
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#FFEDDC')

F1 = Frame(root, width=580, height= 690,bg='white')
F1.pack(pady=5,padx=5,fill=BOTH,expand=True)

F2 = Frame(root, width=600,height=100,)

B1 = Button(F2,text='หน้าหลัก',width=17,height=1,font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command='')
B1.grid(row=0,column=0,ipady=10,ipadx=0)
B2 = Button(F2,text='บันทึกรายการ',font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command=open_add)
B2.grid(row=0,column=1,ipady=10,ipadx=30)
B2 = Button(F2,text='รายงาน',font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command='')
B2.grid(row=0,column=2,ipady=10,ipadx=50)

F2.pack(pady=5)

root.mainloop()