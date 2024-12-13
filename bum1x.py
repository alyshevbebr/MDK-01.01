import os
import socket
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar

class FileExplorerApp:
    def __init__(self, master):
        self.master = master
        master.title("File Explorer")

        self.label = tk.Label(master, text="Выберите папку для поиска файлов:")
        self.label.pack()

        self.directory = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.directory, width=50)
        self.entry.pack()

        self.browse_button = tk.Button(master, text="Обзор", command=self.browse_directory)
        self.browse_button.pack()

        self.search_button = tk.Button(master, text="Поиск файлов", command=self.search_files)
        self.search_button.pack()

        self.file_list = Listbox(master, width=80, height=20)
        self.file_list.pack()

        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.file_list.yview)

    def browse_directory(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.directory.set(folder_selected)

    def search_files(self):
        self.file_list.delete(0, tk.END)  # Очистить список
        directory = self.directory.get()

        if not os.path.isdir(directory):
            messagebox.showerror("Ошибка", "Выберите действительную папку.")
            return

        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    self.file_list.insert(tk.END, os.path.join(root, file))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
