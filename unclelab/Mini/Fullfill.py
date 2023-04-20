from tkinter import *
from tkinter import ttk
import subprocess
import csv

def save_CSV():
    data = [['รายการ','รายละเอียด','จำนวนเงิน'],
           [drop1.get(),field1.get(),field2.get()]]
    with open('moneyTrack.csv','w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)
    open_Mini()

def validate_int(value):
    if value.isdigit():
        return True
    elif value == "":
        return True
    else:
        return False


def open_Mini():
    root.destroy()
    subprocess.Popen(['python', 'Mini.py'])

root = Tk()
root.title('Money Tracking')
width = 600
height = 800
x = 450
y = 10
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#FFEDDC')

F1 = Frame(root, width=580, height=660,bg='white')

FF1 = Frame(F1,bg='white')
A1 = Label(FF1,text='รายการ',font=('TH Sarabun New',25,'bold'),bg='white')
A1.grid(row=0,column=0,ipady=10,sticky=W)
options = ['รายรับ','รายจ่าย']
selected_option = StringVar()
drop1 = ttk.Combobox(FF1,font=('TH Sarabun New',20),textvariable=selected_option,values=options)
drop1.grid(row=0,column=2,ipadx=10,ipady=10)
FF1.pack(pady=50)

FF2 = Frame(F1,bg='white')
A2 = Label(FF2,text='รายละเอียด',font=('TH Sarabun New',25,'bold'),bg='white')
A2.grid(row=0,column=0,ipady=10,sticky=W)
field1 = Entry(FF2,font=('TH Sarabun New',20))
field1.grid(row=0,column=2,ipadx=10,ipady=10)
FF2.pack(pady=50)

FF3 = Frame(F1,bg='white')
validate_cmd = root.register(validate_int)
A3 = Label(FF3,text='จำนวนเงิน',font=('TH Sarabun New',25,'bold'),bg='white')
A3.grid(row=0,column=0,ipady=10,sticky=W)
field2 = Entry(FF3,font=('TH Sarabun New',20),validate='key',validatecommand=(validate_cmd,'%P'))
field2.grid(row=0,column=2,ipadx=10,ipady=10)
FF3.pack(pady=50)

F1.pack(pady=10,padx=10,fill=BOTH,expand=True)

F2 = Frame(root, width=600,height=100,)

B1 = Button(F2,text='บันทึก',font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command=save_CSV)
B1.grid(row=0,column=0,ipady=20,ipadx=30,sticky=W)
Blank1 = Label(F2,text='',bg='#FFEDDC')
Blank1.grid(row=0,column=1,ipady=40,ipadx=50)
B2 = Button(F2,text='ยกเลิก',font=('TH Sarabun New',20,'bold'),fg='black',bg='#F0D579',command=open_Mini)
B2.grid(row=0,column=2,ipady=20,ipadx=30,sticky=E)


F2.pack(pady=10)

root.mainloop()