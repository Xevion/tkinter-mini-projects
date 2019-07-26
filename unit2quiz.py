from tkinter import *
import random, sys, os, ctypes

class App:
    def __init__(self, master):
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame1.pack()
        self.frame2.pack()

        self.query = StringVar()
        self.query.set("Question")

        self.label = Label(self.frame1, textvariable=self.query)
        self.label.pack(padx=5, pady=5)

        # Quit Button
        self.quit = Button(self.frame2, text="Quit", command=self.frame2.quit)
        self.quit.pack(padx=5, pady=5)

root = Tk()
root.wm_attributes("-topmost", 1)
root.overrideredirect(1) # Disable Titlebar
root.iconbitmap(os.path.join(sys.path[0], 'img', 'ico.ico')) # Icon for Application
root.resizable(False, False) #Disable resizing

# get screen res for windows
app = App(root)

user32 = ctypes.windll.user32
x,y = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # Monitor Height/Width Tuple
h,w = root.winfo_width(), root.winfo_height() # Window Height/Width Tuple
x,y = x-h, y-w

print("x","y")
print(x,y)
print("h","w")
print(h,w)

root.geometry("+{}+{}".format(x//2,y//2)) #Make it appear in the middle
root.mainloop()