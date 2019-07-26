from tkinter import *

# I have no honest idea of what is going on here, but it works, so that's cool.

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.minsize()
        self.master.config()

        self.labelvar = StringVar()
        self.master.bind('<Key>', lambda event:self.met(event))
        # Bind seems to pass an event, lambda can handle it and pass this event to a def
        self.frame = Frame() # Frame within Frame? Hmm?
        self.frame.pack(fill='both', expand=True)
        self.label = Label(self, textvariable=self.labelvar) # Label for Keyboard String
        self.label.pack()
        self.pack()

    # Handles keyboard updates, passes then to key(event) for printing without flush
    def met(self, event):
        self.key(event)
        self.labelvar.set(event.keysym)


    @staticmethod
    def key(event):
        print(event.keysym, end=' ', flush=True)

root = Tk()
root.wm_attributes("-topmost", 1)
app = Application(root)
root.mainloop()