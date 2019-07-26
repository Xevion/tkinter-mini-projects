from tkinter import *



root = Tk()
frame = Frame(root)
listbox = Listbox(frame)

def callback(event):
    print('Callback', event)
    listbox.delete(ACTIVE)

frame.bind("<Double-Button-1>", callback)
frame.pack()
listbox.pack()

for i in range(20):
    listbox.insert(END, str(i))


root.mainloop()