import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
import sqlite3
import subprocess

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

# Define Treeview styles
style = ttk.Style()
style.configure("Treeview", font=('TH Sarabun New', 18), rowheight=30)
style.configure("Treeview.Heading", font=('TH Sarabun New', 20, 'bold'), anchor="center")  # Set anchor to center for treeview headers

F1 = Frame(root,bg='white')

treeview = ttk.Treeview(F1, columns=('รายการ', 'จำนวนเงิน'), show='headings',height=2)
treeview.heading('รายการ', text='รายการ')  # Column 1 header
treeview.heading('จำนวนเงิน', text='จำนวนเงิน')  # Column 2 header

conn = sqlite3.connect('unclelab\Mini\Mini.db')
cursor = conn.cursor()
cursor.execute('SELECT name,SUM(value) FROM finance GROUP BY name ORDER BY name DESC')
rows = cursor.fetchall()

tag = 'blue_tag'  # Start with the blue tag

for row in rows:
    treeview.insert('', 'end', values=(row[0], row[1]), tags=(tag), iid=row[0])
    tag = 'pink_tag' if tag == 'blue_tag' else 'blue_tag'  # Swap between blue and pink tag

# Extract labels and sizes from the retrieved data
name = [row[0] for row in rows]
value = [row[1] for row in rows]

# Specify the path to the Thai font file
font_path = 'unclelab\\Mini\\THSarabunNew.ttf'

# Set up a seaborn plot
sns.set(style='whitegrid')

# Create a Figure object
fig = Figure(figsize=(6, 6), dpi=100)
ax = fig.add_subplot(111)

# Create a pie chart on the Figure object
ax.pie(value, labels=name, autopct='%1.1f%%', startangle=90)
ax.set_title('กราฟแสดงรายการทางการเงิน', fontproperties='TH Sarabun New', fontsize=20)

# Create a FigureCanvasTkAgg object to display the Figure in tkinter
canvas = FigureCanvasTkAgg(fig, master=F1)
canvas.get_tk_widget().pack()

conn.close()

treeview.tag_configure('blue_tag', background='#E8F4FD')
treeview.tag_configure('pink_tag', background='#FCE8F3')
treeview.pack(ipadx=90)

F1.pack(pady=5, padx=5,ipadx=90)

F2 = Frame(root, width=600,height=100,)

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