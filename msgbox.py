from tkinter import *
import ctypes, random

user32 = ctypes.windll.user32
monitor_x,monitor_y = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(monitor_x, monitor_y)

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    
    def new_window(self):
        for x in range(1000):
            global monitor_x, monitor_y
            self.newWindow = Toplevel(self.master)
            width, height, xoffset, yoffset = 500, 150, random.randint(0, monitor_x), random.randint(0, monitor_y)
            self.newWindow.geometry("%dx%d%+d%+d" % (width, height, xoffset, yoffset))
            self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.quitButton = Button(self.frame, text = 'Quit', command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = Tk()
    root.geometry = ("+{}+{}".format(monitor_x, monitor_y))
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()