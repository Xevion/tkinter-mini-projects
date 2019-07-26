import tkinter as tk
from tkinter import ttk
import faker, random

fake = faker.Faker()

class App(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.tree = ttk.Treeview(self.parent, columns=['Name'])
        self.button = tk.Entry(self.parent, )
        self.tree.heading('#0', text='Index')
        self.tree.heading('#1', text='Name')
        self.tree.column('#0', anchor=tk.CENTER)
        self.tree.column('#1', anchor=tk.CENTER)

        self.items = []
        for _ in range(10):
            self.items.append(self.tree.insert('', 'end', text=_+1, values=(fake.name())))

        self.button.grid(column=0, row=0, columnspan=1, rowspan=1, padx=5, pady=5, sticky='NEWS')
        self.tree.grid(column=0, row=1, columnspan=3, rowspan=1, padx=5, pady=5)
    
    def update(self):
       print('Update received')
       self.tree.detach(random.choice(self.items))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()