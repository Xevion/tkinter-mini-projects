from tkinter import *
from tkinter import ttk
import string, random, faker

fake = faker.Faker()

class App:
    def __init__(self, root):
        self.root = root
        self.tree = ttk.Treeview(self.root, columns=['Integer'])
        self.button = Button(root, text='Randomly Choose', command=self.randomSet)
        self.button2 = Button(root, text='Randomly Choose2', command=self.randomSet)
        self.button1 = Button(root, text='Randomly Choose1', command=self.randomSet)
        
        # Create values
        # rnd = lambda x : ''.join(random.choices(list(string.ascii_letters), k=x))    
        self.values = [fake.name() for i in range(1, 30)]

        # Create tree ids and insert values
        self.tree.heading('#0', text='String')
        self.tree.heading('#1', text='Integer')
        self.tree.column('#0', anchor=CENTER)
        self.tree.column('#1', anchor=CENTER)

        self.ids = []
        for value in self.values:
            tree_id = self.tree.insert("", "end", text=value, values=random.randint(0, len(self.values)))
            self.ids.append(tree_id)
        
        # Grid buttons and tree
        self.tree.grid(column=0, row=0, columnspan=3, padx=5, pady=5)
        self.button2.grid(column=2, row=1, columnspan=1, padx=5, pady=5, sticky=N+E+W+S)
        self.button1.grid(column=1, row=1, columnspan=1, padx=5, pady=5, sticky=N+E+W+S)
        self.button.grid(column=0, row=1, columnspan=1, padx=5, pady=5, sticky=N+E+W+S)
    
    # Selection items randomly
    def randomSet(self):
        minLength = int(len(self.ids) / 2.0)
        self.choices = []
        while len(self.choices) < minLength:
            choice = random.choice(self.ids)
            if choice not in self.choices:
                self.choices.append(choice)
        self.tree.selection_set(self.choices)

root = Tk()
App(root)
root.mainloop()