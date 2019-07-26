from tkinter import *

x = 1
y = 1
z = 0

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.textVar = StringVar()

        # Lambda Version
        # self.button = Button(
        #     frame, textvariable=self.textVar, command=lambda: self.textVar.set(fibonacci())
        # )
        # self.button.pack()
        
        # tkinter Version, using separate functions
        self.button = Button(
            frame, textvariable=self.textVar, command=self.update
        )
        self.button.pack()

    def update(self):
        self.textVar.set(str(fibonacci()))
        
def fibonacci():
    global x, y, z
    z = x
    x = x + y
    y = z
    return x

root = Tk()
app = App(root)
root.mainloop()