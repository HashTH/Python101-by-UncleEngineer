from tkinter import *
from tkinter import ttk
import subprocess
import sqlite3

def open_main():
    root.destroy()
    subprocess.Popen(['python', 'unclelab\Mini\Mini.py'])

def open_add():
    root.destroy()
    subprocess.Popen(['python', 'unclelab\Mini\Fullfill.py'])

def open_Report():
    root.destroy()
    subprocess.Popen(['python', 'unclelab\Mini\Report.py'])

root = Tk()
root.title('Money Tracking')
width = 600
height = 800
x = 450
y = 10
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#FFEDDC')

F1 = Frame(root, width=580, height=600,bg='white')

treeview = ttk.Treeview(F1, columns=('รายการ','จำนวนเงิน'),show='headings')
treeview.heading('รายการ',text='รายการ')
treeview.heading('จำนวนเงิน',text='จำนวนเงิน')

conn = sqlite3.connect('unclelab\Mini\Mini.db')
cursur = conn.cursor()
cursur.execute('SELECT name,SUM(value) FROM finance GROUP BY name')
rows = cursur.fetchall()



for row in rows:
        treeview.insert('','end',values=(row[0],row[1]))
conn.close()
treeview.pack(fill=BOTH,expand=True)

F1.pack(pady=5,padx=5,fill=BOTH,expand=True)

F2 = Frame(root, width=600,height=100,)

B1 = Button(F2,text='หน้าหลัก',width=17,height=1,font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command=open_main)
B1.grid(row=0,column=0,ipady=10,ipadx=0)
B2 = Button(F2,text='บันทึกรายการ',font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command=open_add)
B2.grid(row=0,column=1,ipady=10,ipadx=30)
B2 = Button(F2,text='รายงาน',font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command=open_Report)
B2.grid(row=0,column=2,ipady=10,ipadx=50)

F2.pack(pady=5)

root.mainloop()