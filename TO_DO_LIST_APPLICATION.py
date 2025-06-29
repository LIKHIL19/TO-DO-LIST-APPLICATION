import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

root = tk.Tk()
root.title("TO DO LIST")
root.geometry("600x620")
root.configure(bg="#e9f5ed")

# Fonts
title_font = Font(family="Segoe UI", size=26, weight="bold")
task_font = Font(family="Segoe UI", size=14)
strikethrough_font = Font(family="Segoe UI", size=14, overstrike=1)

# Track crossed items
crossed_indices = set()

# Title
tk.Label(root, text="TO DO LIST", font=title_font, bg="#e9f5f1", fg="#1b4332").pack(pady=15)

# Frame for list
list_frame = ttk.Frame(root)
list_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Listbox
my_list = tk.Listbox(
    list_frame, font=task_font, width=40, height=10, borderwidth=0, 
    bg="white", fg="#333", selectbackground="#b7e4c7", activestyle="none"
)
my_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=my_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
my_list.config(yscrollcommand=scrollbar.set)

# Label above Entry
tk.Label(root, text="Add a New Task Below", font=("Segoe UI", 12, "bold"), bg="#e9f5f1", fg="#1b4332").pack()

# Entry
entry = ttk.Entry(root, font=task_font, width=30)
entry.pack(pady=(5, 15))

# Functions
def add_item():
    task = entry.get().strip()
    if task:
        my_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_item():
    selected = my_list.curselection()
    if selected:
        my_list.delete(selected[0])

def cross_off_item():
    selected = my_list.curselection()
    if selected:
        my_list.itemconfig(selected[0], fg="white", selectbackground="#252021")

def uncross_item():
    selected = my_list.curselection()
    if selected:
        my_list.itemconfig(selected[0], fg="#333", selectbackground="#d1e7dd")

def delete_crossed():
    for i in reversed(range(my_list.size())):
        if i in crossed_indices:
            my_list.delete(i)
    crossed_indices.clear()

def delete_all():
    my_list.delete(0, tk.END)
    crossed_indices.clear()

# Buttons
button_frame1 = ttk.Frame(root)
button_frame1.pack(pady=5)

button_frame2 = ttk.Frame(root)
button_frame2.pack(pady=5)

ttk.Button(button_frame1, text=" Add ", width=15, command=add_item).grid(row=0, column=0, padx=10)
ttk.Button(button_frame1, text=" Delete ", width=15, command=delete_item).grid(row=0, column=1, padx=10)

ttk.Button(button_frame2, text=" Cross ", width=15, command=cross_off_item).grid(row=0, column=0, padx=10)
ttk.Button(button_frame2, text=" Uncross ", width=15, command=uncross_item).grid(row=0, column=1, padx=10)
ttk.Button(button_frame2, text=" Delete Crossed ", width=20, command=delete_crossed).grid(row=1, column=0, columnspan=2, pady=10)

# Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="Clear List", command=delete_all)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
