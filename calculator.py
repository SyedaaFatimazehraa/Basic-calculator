import tkinter as tk
from tkinter import messagebox
from tkinter import *

def add():
    try:
        result = float(num1.get()) + float(num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
def sub():
    try:
        result = float(num1.get()) - float(num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        
def mul():
    try:
        result = float(num1.get()) * float(num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
def div():
    try:
        result = float(num1.get()) / float(num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
def remind():
    try:
        result = float(num1.get()) %float(num2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
def per():
    try:
        result = float(num1.get()) / float(num2.get())*100.0
        result_label.config(text="Result: " + str(result+"%"))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")       

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='black')
root.geometry("400x200")

# Create entry fields
num1 = tk.Entry(root)
num1.pack()
num2 = tk.Entry(root)
num2.pack()

# Create button to perform addition
add_button = tk.Button(root, text="Add (+)", command=add)
add_button.pack()
sub_button = tk.Button(root, text="Subtract (-)", command=sub)
sub_button.pack()
mul_button = tk.Button(root, text="Multiply (x)", command=mul)
mul_button.pack()
rem_button = tk.Button(root, text="Reminder", command=remind)
rem_button.pack()
per_button = tk.Button(root, text="Percentage (%)", command=per)
mul_button.pack()
# Label to display result
result_label = tk.Label(root)
result_label.pack()
# Start GUI event loop
root.mainloop()

