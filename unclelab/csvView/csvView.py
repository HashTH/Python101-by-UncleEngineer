import tkinter as tk
import csv
from tkinter import filedialog, messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("CSV Viewer")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_file_button = tk.Button(self, text="Select CSV File", command=self.select_file)
        self.select_file_button.pack(pady=10)

        self.table_label = tk.Label(self, text="No data to display")
        self.table_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                with open(file_path, newline='') as csvfile:
                    data = list(csv.reader(csvfile))
                    self.display_table(data)
            except csv.Error as e:
                messagebox.showerror("Error", f"Failed to read CSV file: {e}")

    def display_table(self, data):
        if len(data) == 0:
            self.table_label.config(text="No data to display")
        else:
            # Extract column headers and data rows
            headers = data[0]
            rows = data[1:]

            # Create a new top-level window to display the table
            table_window = tk.Toplevel(self.master)
            table_window.title("CSV Viewer - Table")
            table_frame = tk.Frame(table_window)
            table_frame.pack()

            # Create a table widget using a Text widget
            table_text = tk.Text(table_frame, wrap="none")
            table_text.pack(side="left", fill="both", expand=True)

            # Create a scrollbar for the table widget
            table_scrollbar = tk.Scrollbar(table_frame)
            table_scrollbar.pack(side="right", fill="y")

            # Link the scrollbar to the table widget
            table_scrollbar.config(command=table_text.yview)
            table_text.config(yscrollcommand=table_scrollbar.set)

            # Add the column headers to the table widget
            header_text = " | ".join(headers) + "\n"
            separator_text = "-" * (8 * len(headers) - 1) + "\n"
            table_text.insert("end", header_text)
            table_text.insert("end", separator_text)

            # Add the data rows to the table widget
            for row in rows:
                row_text = " | ".join(row) + "\n"
                table_text.insert("end", row_text)

            # Disable editing of the table widget
            table_text.config(state="disabled")

            # Resize the table columns to fit the data
            for i in range(len(headers)):
                table_text.columnconfigure(i, weight=1)

            # Display the table window
            table_window.mainloop()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
