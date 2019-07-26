from tkinter import *
from functools import partial
import string

buttons = list(string.printable)
print(buttons)
root = Tk()

def txt(text):
    print(text)

for b in buttons:
    btn = Button(root, text=b, command=partial(txt, b))
    btn.pack(side=LEFT,pady=5)

root.mainloop()