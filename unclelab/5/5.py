from tkinter import ttk
from googletrans import Translator
from tkinter import *
import tkinter.font

translator = Translator()

def translate_text(text):
    """แปลข้อความจากภาษาอังกฤษเป็นภาษาไทย"""
    translation = translator.translate(text, src='en', dest='th')
    return translation.text

def ask_question():
    """ตอบคำถาม"""
    question = question_entry.get()
    answer = translate_text(question)
    answer_label.config(text=answer)

# สร้างหน้าต่าง GUI
root = Tk()
root.title("โปรแกรมแปลภาษาอังกฤษเป็นไทย")

# กำหนดตัวอักษร
default_font = tkinter.font.Font(family='TH Sarabun New',size=30,weight='bold')
root.option_add("*Font",default_font)

# สร้าง Frame
frame_all = ttk.Frame(root)
frame_all.pack(padx=0,pady=100)

# สร้างช่องกรอกข้อความสำหรับถามคำถาม
question_label = ttk.Label(frame_all, text="กรอกคำศัพท์ภาษาอังกฤษ:")
question_label.pack(pady=10)

question_entry = Entry(frame_all)
question_entry.pack(pady=10)

# สร้างปุ่มสำหรับตอบคำถาม
ask_button = ttk.Button(frame_all, text="แปล", command=ask_question)
##ask_button.configure(font=default_font)
ask_button.pack(pady=10)

# สร้างป้ายแสดงคำตอบ
answer_label = ttk.Label(frame_all, text="")
answer_label.pack()

# กำหนดขนาดและตำแหน่งหน้าต่าง GUI ให้อยู่ตรงกลางจอ
root.update_idletasks()
width = (root.winfo_screenwidth()//2)
height = (root.winfo_screenheight()//2)
x = (root.winfo_screenwidth()//4)
y = (root.winfo_screenheight()//4)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# เริ่มต้น GUI และเข้าสู่ลูปการรอผู้ใช้ดำเนินการ
root.mainloop()
