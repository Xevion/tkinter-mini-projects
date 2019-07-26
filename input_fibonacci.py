from tkinter import *
import os, sys, ctypes

class App:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.master.title("Fibonacci")
        frame1.pack()
        frame2 = Frame(master)
        frame2.pack()

        # Declare textVar for textbox
        self.textVar = StringVar()
        self.textVar.set("2")

        # Setting up textbox, plus/minus buttons and a update button
        self.entry = Entry(frame2)
        self.entry.insert(0,"1")
        self.label = Label(frame1, textvariable=self.textVar)
        self.flabel = Label(frame2, text="nth=")
        self.ubutton = Button(frame2, text = "Update", command=self.fibonacci)
        self.pbutton = Button(frame2, text="+", command=self.plus)
        self.mbutton = Button(frame2, text="-", command=self.minus)

        # Pack everything
        self.label.pack(side=LEFT, padx=5)
        self.flabel.pack(side=LEFT, pady=5)
        self.entry.pack(side=LEFT, pady=5, padx=(0,5))
        self.ubutton.pack(side=LEFT, pady=5, padx=(5,0))
        self.pbutton.pack(side=LEFT, pady=5)
        self.mbutton.pack(side=LEFT, pady=5, padx=(0,5))

    # Adds one to the textbox's integer then updates the Label
    def plus(self):
        string = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(int(string) + 1))
        self.fibonacci()

    # Takes away one from the textbox's integer then updates the Label
    def minus(self):
        string = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(int(string) - 1))
        self.fibonacci()

    # Sets the text of the Label to nth integer of the Fibonacci sequence
    # Supports negatives
    def fibonacci(self):
        n = self.entry.get()
        negative = int(n) < 0
        x = 1;y = 1;z = 0
        for _ in range(abs(int(n))):
            z = x
            x = x + y
            y = z
        if negative: x *= -1
        self.textVar.set(str(x))

root = Tk()
root.iconbitmap(os.path.join(sys.path[0], 'img', 'ico.ico'))
root.resizable(False, False)
app = App(root)
root.mainloop()