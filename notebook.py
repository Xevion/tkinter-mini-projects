from tkinter import ttk
from tkinter import *
import random, string


gen = lambda length, sample=string.ascii_letters : ''.join(random.choices(list(sample), k=length))

class Window(Frame):
    def __init__(self, master=None):
        self.master = master
        
        # Master Notebook
        n = ttk.Notebook(root)
        tabs = []

        for x in range(1, 21):
            tab = ttk.Frame(n)
            label = Label(tab, wraplength=500, text=gen(500))
            tabs.append((tab, label))
            
            label.pack()
            n.add(tabs[-1][0], text='Tab ' + str(x))
    
        n.grid(column=0, row=0)

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()