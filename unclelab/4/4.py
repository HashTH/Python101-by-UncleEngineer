import csv
import datetime
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("โปรแกรมบันทึกการเข้าพัก")
root.geometry('250x350')

myTime = datetime.datetime.now()
strDate = myTime.strftime('%Y-%m-%d')
strTime = myTime.strftime('%H:%M:%S')

L0Head = Label(root,text="โปรแกรมบันทึกการเข้าพัก")
L0Head.grid(row=0,column=0,pady=5)

F1 = Frame(root)

variable = StringVar(F1)
variable.set(101)


L1Q = Label(F1,text="ชื่อ นามสกุล")
L2Q = Label(F1,text="เบอร์โทรศัพท์")
L3Q = Label(F1,text="ห้องพัก")

L1Q.grid(row=1,column=0,sticky=W,ipadx=10,pady=3)
L2Q.grid(row=2,column=0,sticky=W,ipadx=10,pady=3)
L3Q.grid(row=3,column=0,sticky=W,ipadx=10,pady=3)

E1Q = Entry(F1)
E2Q = Entry(F1)
E3Q = OptionMenu(F1,variable,'101','102','103','104','105','106','107','108','109','110')

E1Q.grid(row=1,column=1,pady=3)
E2Q.grid(row=2,column=1,pady=3)
E3Q.grid(row=3,column=1,pady=3)
F1.grid(row=1,column=0,padx=10,pady=10)


def saveCSV():
    E1= str(E1Q.get())
    E2= str(E2Q.get())
    E3= str(variable.get())
    data=[E1,E2,E3,strDate,strTime]
    #messagebox.showinfo(title='submit', message=data)
    with open('CheckIn.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)
        messagebox.showinfo(title='submit', message='บันทึกข้อมูลสำเร็จ')


F2 = Frame(root)
B = Button(F2,text="บันทึกข้อมูล",command=saveCSV)
B.pack()
F2.grid(row=2,column=0,padx=10,pady=10)

root.mainloop()