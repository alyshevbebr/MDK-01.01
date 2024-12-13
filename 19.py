import tkinter as tk
from tkinter import filedialog

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.password = "999"
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.check_password)
        self.submit_button.pack()
        self.file_button = tk.Button(self, text="Open File", command=self.open_file, state="disabled")
        self.file_button.pack()

    def check_password(self):
        if self.password_entry.get() == self.password:
            self.file_button.config(state="normal")
            self.password_entry.config(state="disabled")
            self.submit_button.config(state="disabled")
        else:
            self.password_entry.delete(0, "end")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        # Add your file opening logic here
        print(f"File opened: {file_path}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()