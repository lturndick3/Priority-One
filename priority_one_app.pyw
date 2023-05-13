from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
__author__ = "LOUIS C. TURNDICK III"
__copyright__ = "Copyright © 2023 LOUIS C. TURNDICK III"
__contact__ = "louisturndickiii@gmail.com"
__license__ = "Public Domain"
__version__ = "1.0"


import sys
print("\nPython Copyright Information")
print(sys.copyright)


tasks = []


def add_task():
    task = task_entry.get()
    if task != "":
        priority = int(priority_entry.get())
        tasks.append((priority, task))
        update_list()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)


def update_list():
    tasks.sort()
    task_list.delete(0, tk.END)
    for priority, task in tasks:
        task_list.insert(tk.END, f"{priority}: {task}")


def export_list():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path != "":
        with open(file_path, "w") as f:
            for priority, task in tasks:
                f.write(f"{priority}: {task}\n")


# create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x300")
ico = Image.open('AdobeStock_86694478_Preview.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# create task entry widgets
task_label = tk.Label(root, text="Task:")
task_label.grid(row=0, column=0)
task_entry = tk.Entry(root)
task_entry.grid(row=0, column=1)

# create priority entry widgets
priority_label = tk.Label(root, text="Priority (1-5):")
priority_label.grid(row=1, column=0)
priority_entry = tk.Entry(root)
priority_entry.grid(row=1, column=1)

# create add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2)

# create task list widget
task_list = tk.Listbox(root)
task_list.grid(row=3, column=0, columnspan=2)

# create export button
export_button = tk.Button(root, text="Export List", command=export_list)
export_button.grid(row=4, column=0, columnspan=2)

# start main event loop
root.mainloop()
