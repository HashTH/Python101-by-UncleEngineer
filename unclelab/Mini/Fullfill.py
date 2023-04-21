from tkinter import *
from tkinter import ttk
import subprocess
from datetime import datetime
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

def save_sql():
    name = drop1.get()
    detail = field1.get()
    value = field2.get()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if name and detail and value and created_at: #check if the field filled
        conn = sqlite3.connect('unclelab\Mini\Mini.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO finance(name,detail,value,created_at) values (?,?,?,?)',(name,detail,value,created_at))
        conn.commit()
        conn.close()
        root.destroy()
        subprocess.Popen(['python', 'unclelab\Mini\Mini.py'])

def validate_int(value):
    if value.isdigit():
        return True
    elif value == "":
        return True
    else:
        return False

root = Tk()
root.title('Money Tracking')
width = 600
height = 800
x = 450
y = 10
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#FFEDDC')

# Create main frame
F1 = Frame(root, width=580, height=660, bg='white')

# Frame for dropdown menu
FF1 = Frame(F1, bg='white')
A1 = ttk.Label(FF1, text='รายการ', font=('TH Sarabun New', 25, 'bold'), style='Label.TLabel')
A1.grid(row=0, column=0, ipady=10, sticky=W)
options = ['รายรับ', 'รายจ่าย']
selected_option = StringVar()
drop1 = ttk.Combobox(FF1, font=('TH Sarabun New', 20), textvariable=selected_option, values=options)
drop1.grid(row=0, column=1, padx=10, pady=10)
drop1.state(['readonly'])  # Make it readonly
FF1.pack(pady=50)

# Frame for entry field 1
FF2 = Frame(F1, bg='white')
A2 = ttk.Label(FF2, text='รายละเอียด', font=('TH Sarabun New', 25, 'bold'), style='Label.TLabel')
A2.grid(row=0, column=0, ipady=10, sticky=W)
field1 = ttk.Entry(FF2, font=('TH Sarabun New', 20))
field1.grid(row=0, column=1, padx=10, pady=10)
FF2.pack(pady=50)

# Frame for entry field 2
FF3 = Frame(F1, bg='white')
validate_cmd = root.register(validate_int)
A3 = ttk.Label(FF3, text='จำนวนเงิน', font=('TH Sarabun New', 25, 'bold'), style='Label.TLabel')
A3.grid(row=0, column=0, ipady=10, sticky=W)
field2 = ttk.Entry(FF3, font=('TH Sarabun New', 20), validate='key', validatecommand=(validate_cmd, '%P'))
field2.grid(row=0, column=1, padx=10, pady=10)
FF3.pack(pady=50)

F1.pack(pady=10, padx=10, fill=BOTH, expand=True)

# Define style for labels
style = ttk.Style()
style.configure('Label.TLabel', background='white')  # Set background color for labels

# Frame for buttons
F2 = Frame(root, width=600, height=100)
F2.pack(pady=10)

# Create style for buttons
button_style = ttk.Style()
button_style.configure('TButton', font=('TH Sarabun New', 20, 'bold'))

# Define button colors for different states
button_style.map('TButton', foreground=[('active', 'black'), ('disabled', 'gray')],
                 background=[('active', '#F0D579'), ('disabled', '#D3D3D3')])

# Button 1 - บันทึก
B1 = ttk.Button(F2, text='บันทึก', style='TButton', command=save_sql)
B1.grid(row=0, column=0, ipady=20, ipadx=30, sticky=W)

# Blank Label for spacing
Blank1 = ttk.Label(F2, text='', background='#FFEDDC')
Blank1.grid(row=0, column=1, ipady=40, ipadx=50)

# Button 2 - ยกเลิก
B2 = ttk.Button(F2, text='ยกเลิก', style='TButton', command=open_main)
B2.grid(row=0, column=2, ipady=20, ipadx=30, sticky=E)

root.mainloop()