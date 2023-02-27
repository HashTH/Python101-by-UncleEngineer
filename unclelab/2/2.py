from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title('ปริศนาฟ้าแลบ')
root.geometry('500x350')

Question = ['เมืองหลวงของประเทศไทยคือ','ในหนึ่งสัปดาห์มีกี่วัน (ใส่แค่จำนวนเต็ม)']

Label1 = Label(root,text='ปริศนาฟ้าแลบ',font=('TH Sarabun New',30),fg='green')
Label1.pack(padx=10,pady=10)

F1 = Frame(root)
Q = Label(F1,text=random.choice(Question),font=('TH Sarabun New',20),fg='black',bg='lightblue')
Q.pack()

Answer = Text(F1,height=2,width=15,font=('TH Sarabun New',25),fg='purple',bg='pink')
Answer.pack()
F1.pack()

def printAnswer():
    Ans['text'] = Answer.get("1.0",'end-1c')
    print(Ans['text'])
    if Q['text'] == Question[0]:
        match Ans['text']:
            case 'กรุงเทพ':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case 'bangkok':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case 'BANGKOK':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case 'Bangkok':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case 'กรุงเทพมหานคร':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case _:
                messagebox.showinfo(title='เช็คคำตอบ', message='เป็นคำตอบที่ผิด, คราวหน้าเอาใหม่นะ สู้สู้')
    else:
        match Ans['text']:
            case '7':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case '๗':
                messagebox.showinfo(title='เช็คคำตอบ', message='ถูกต้องนะครับ')
            case _:
                messagebox.showinfo(title='เช็คคำตอบ', message='เป็นคำตอบที่ผิด, คราวหน้าเอาใหม่นะ สู้สู้')


Submit = Button(F1,text='Submit',font=('TH Sarabun New',20),fg='purple',bg='skyblue',command=printAnswer)
Submit.pack(padx=10,pady=10)

Ans = Label(F1,text="",font=('TH Sarabun New',16))
#Ans.pack()

Check = Label(F1,text="",font=('TH Sarabun New',16))
#Check.pack()

root.mainloop()