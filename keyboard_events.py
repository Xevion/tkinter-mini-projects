import tkinter as tk

root = tk.Tk()

def key(event):
    print("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = tk.Frame(root, width=100, height=100)
label = tk.Label(frame, text="Help")
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
label.pack()
 

root.mainloop()