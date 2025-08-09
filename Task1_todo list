# Codesoft Python Internship Project 1 - To-Do List
# Created by Vaibhav Sharma - Improved To-Do App

import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
FILE_NAME = "tasks.txt"

# Add a new task
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks()
    else:
        messagebox.showinfo("Info", "Please select a task to delete.")

# Mark task as completed
def mark_done(event=None):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        if not task.endswith(" ✅"):
            listbox.delete(index)
            listbox.insert(index, task + " ✅")
            listbox.itemconfig(index, {'fg': 'green'})
            save_tasks()

# Save tasks to file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f:
                task = line.strip()
                if task:
                    idx = listbox.size()
                    listbox.insert(tk.END, task)
                    if task.endswith(" ✅"):
                        listbox.itemconfig(idx, {'fg': 'green'})

# GUI setup
root = tk.Tk()
root.title("To-Do List - Vaibhav Sharma")
root.geometry("450x500")
root.config(bg="#1e1e2f")  # Dark theme

tk.Label(root, text="📋 My Task List", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white").pack(pady=10)

entry_frame = tk.Frame(root, bg="#1e1e2f")
entry_frame.pack(pady=5)
entry = tk.Entry(entry_frame, font=("Arial", 12), width=30)
entry.pack(side=tk.LEFT, padx=5)
tk.Button(entry_frame, text="Add ➕", command=add_task, bg="#4CAF50", fg="white").pack(side=tk.LEFT)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Mark Done ✅", command=mark_done, bg="#2196F3", fg="white", width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete 🗑️", command=delete_task, bg="#f44336", fg="white", width=12).grid(row=0, column=1, padx=5)

# Listbox with scrollbar
list_frame = tk.Frame(root, bg="#1e1e2f")
list_frame.pack(pady=10)
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(list_frame, font=("Arial", 12), width=40, height=15, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Double-click to mark done
listbox.bind("<Double-1>", mark_done)

# Load saved tasks
load_tasks()

root.mainloop()
