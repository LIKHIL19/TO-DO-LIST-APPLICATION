import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

root = tk.Tk()
root.title("TO DO LIST APPLICATION")
root.geometry("500x650")
root.config(bg="lightblue")

label = tk.Label(root, text="TASKS", font=("Arial", 30), fg="white", bg="lightblue")
label.pack(pady=20)

frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

task_entry = tk.Entry(frame, font=("Arial", 18), width=22)
task_entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(frame, text="Add Task", font=("Arial", 14), command=add_task, bg="green", fg="white")
add_btn.grid(row=0, column=1, padx=5)

task_listbox = tk.Listbox(root, font=("Arial", 16), width=30, height=15, selectbackground="skyblue")
task_listbox.pack(pady=20)

remove_btn = tk.Button(root, text="Remove Selected", font=("Arial", 14), command=remove_task, bg="red", fg="white")
remove_btn.pack(pady=10)

root.mainloop()