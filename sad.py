# Full-Screen Window with Password Protection
import tkinter as tk
from tkinter import simpledialog

def check_password():
    password = simpledialog.askstring("Password", "Enter the password to close the window:")
    if password == "99945":
        root.destroy()

def disable_event():
    pass

root = tk.Tk()
root.title("Task Manager")
root.attributes('-fullscreen', True)
root.protocol("WM_DELETE_WINDOW", check_password)

# Disable specific hotkeys
root.bind("<Control-L>", disable_event)
root.bind("<Alt-F4>", disable_event)
root.bind("<Win-L>", disable_event)

label = tk.Label(root, text="КТО ПРОЧИТАЛ, ТОТ ЛОХ\n И ФАРХАТ ЛОХ", font=("Helvetica", 100))
label.pack(expand=True)

root.mainloop()
