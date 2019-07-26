import random, datetime
from tkinter import ttk
from tkinter import *

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_interface()
    
    def init_interface(self):
        # Window Configurations
        self.parent.title("Window Title")
        self.parent.config(background="lavender")
        # self.parent.grid_rowconfigure(0, weight=1)
        # self.parent.grid_columnconfigure(0, weight=1)

        # Item Name Area
        self.item_label = Label(self.parent, text="Name:", bg="lavender")
        self.item_entry = Entry(self.parent)
        self.item_label.grid(row=0, column=0, sticky=E, ipadx=2, ipady=2, padx=5, pady=5)
        self.item_entry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        # Doses Area
        self.dose_label = Label(self.parent, text="Dose:", bg="lavender")
        self.dose_entry = Entry(self.parent)
        self.dose_label.grid(row=1, column=0, sticky=E, ipadx=2, ipady=2, padx=5, pady=5)
        self.dose_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        # Date Area
        self.date_label = Label(self.parent, text="Date Modified:", bg="lavender")
        self.date_entry = Entry(self.parent)
        self.date_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.date_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # Button Area
        self.submit_button = Button(self.parent, text="Insert", command=self.insert_data)
        self.exit_button = Button(self.parent, text = "Exit", command=self.parent.quit)
        self.submit_button.grid(row=1, column=2, rowspan=3, padx=5, pady=5, ipadx=15, ipady=15)
        self.exit_button.grid(row=1, column=3, rowspan=3, padx=5, pady=5, ipadx=15, ipady=15)

        # Tree View Setup
        self.i = 0
        self.tree = ttk.Treeview(self.parent, columns=('Dose', 'Modification Date'))
        for index, string in enumerate(['Item', 'Dose', 'Modification Date']):
            self.tree.heading('#{}'.format(index), text=string)
            self.tree.column('#{}'.format(index), stretch=YES)
        self.tree.grid(row=3, column=0, columnspan=4, padx=5, pady=(0, 5))        

    def insert_data(self):
        # Require dose entry
        time = datetime.datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
        if self.date_entry.get() != "": # If timestamp is provided
            time = self.date_entry.get()
        mg = "{} mg".format(self.dose_entry.get())
        text = "Item_{}".format(self.i)
        self.tree.insert('', 'end', text=text, values=(mg, time))
        self.i += 1

def main():
    root = Tk()
    x = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()