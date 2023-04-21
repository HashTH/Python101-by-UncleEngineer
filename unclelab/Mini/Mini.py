import os
import subprocess
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import END, BOTH, Button, Frame, Text

def open_main():
    root.destroy()
    subprocess.Popen(['python', os.path.join('unclelab', 'Mini', 'Mini.py')])

def open_add():
    root.destroy()
    subprocess.Popen(['python', os.path.join('unclelab', 'Mini', 'Fullfill.py')])

def open_Report():
    root.destroy()
    subprocess.Popen(['python', os.path.join('unclelab', 'Mini', 'Report.py')])

root = tk.Tk()
root.title('Money Tracking')
width = 600
height = 800
x = 450
y = 10
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#FFEDDC')


F1 = Frame(root, width=580, height=600, bg='white')

text1 = Text(F1, height=18.5, width=60, font=('TH Sarabun New', 20, 'bold'))
text1.pack()
try:
    conn = sqlite3.connect(os.path.join('unclelab', 'Mini', 'Mini.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT name,detail,value,created_at FROM finance order by id desc')
    rows = cursor.fetchall()

    for row in rows:
        text1.insert(END, f'รายการ: {row[0]}\n')
        text1.insert(END, f'รายละเอียด: {row[1]}\n')
        text1.insert(END, f'จำนวนเงิน: {row[2]}\n')
        text1.insert(END, f'บันทึกเมื่อ: {row[3]}\n')
        text1.insert(END, '-'*95+'\n')
    conn.close()
except sqlite3.Error as e:
    print(f"Error accessing database: {e}")

F1.pack(pady=5, padx=5, fill=BOTH, expand=True)

F2 = Frame(root, width=600,height=100,bg='#FFEDDC') # Updated background color of Frame F2

# Create style for buttons
button_style = ttk.Style()
button_style.configure('TButton', font=('TH Sarabun New', 20, 'bold'))

# Define button colors for different states
button_style.map('TButton', foreground=[('active', 'black'), ('disabled', 'gray')],
                 background=[('active', '#F0D579'), ('disabled', '#D3D3D3')])

B1 = ttk.Button(F2,text='หน้าหลัก',style='TButton',command=open_main)
B1.grid(row=0,column=0,ipady=10,ipadx=30)
B2 = ttk.Button(F2,text='บันทึกรายการ',style='TButton',command=open_add)
B2.grid(row=0,column=1,ipady=10,ipadx=30)
B2 = ttk.Button(F2,text='รายงาน',style='TButton',command=open_Report)
B2.grid(row=0,column=2,ipady=10,ipadx=50)

F2.pack(pady=5)

root.mainloop()