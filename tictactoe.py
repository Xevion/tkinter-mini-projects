from tkinter import *
import os, sys, random, string

class App:
    def __init__(self, master):
        frame1 = Frame(master)
        frame2 = Frame(master)
        frame3 = Frame(master)
        frame4 = Frame(master)
        frame1.bind("<Key>", self.key)
        frame2.bind("<Key>", self.key)
        frame3.bind("<Key>", self.key)
        frame4.bind("<Key>", self.key)
        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()

        self.vars = []
        self.marker = ["X", "O"]
        self.turn = True #True for p1, False for p2
        self.turnvar = StringVar()
        self.turnvar.set("Player " + self.getPlayer())
        for x in range(3):
            self.vars.append([])
            for y in range(3):
                self.vars[x].append(StringVar())
                self.vars[x][y].set("☐")

        self.btns = [[], [], []]
        # Button 1 - Top Left
        self.btns[0].append(Button(frame1, textvariable=self.vars[0][0], command=lambda: self.btnUpdate(0,0)))
        self.btns[0][0].pack(side=LEFT, pady=5, padx=5)
        # Button 2 - Top Middle
        self.btns[0].append(Button(frame1, textvariable=self.vars[0][1], command=lambda: self.btnUpdate(0,1)))
        self.btns[0][1].pack(side=LEFT, pady=5, padx=5)
        # Button 3 - Top Right
        self.btns[0].append(Button(frame1, textvariable=self.vars[0][2], command=lambda: self.btnUpdate(0,2)))
        self.btns[0][2].pack(side=LEFT, pady=5, padx=5)
        # Button 4 - Middle Left
        self.btns[1].append(Button(frame2, textvariable=self.vars[1][0], command=lambda: self.btnUpdate(1,0)))
        self.btns[1][0].pack(side=LEFT, pady=5, padx=5)
        # Button 5 - Middle Middle
        self.btns[1].append(Button(frame2, textvariable=self.vars[1][1], command=lambda: self.btnUpdate(1,1)))
        self.btns[1][1].pack(side=LEFT, pady=5, padx=5)
        # Button 6 - Middle Right
        self.btns[1].append(Button(frame2, textvariable=self.vars[1][2], command=lambda: self.btnUpdate(1,2)))
        self.btns[1][2].pack(side=LEFT, pady=5, padx=5)
        # Button 7 - Bottom Left
        self.btns[2].append(Button(frame3, textvariable=self.vars[2][0], command=lambda: self.btnUpdate(2,0)))
        self.btns[2][0].pack(side=LEFT, pady=5, padx=5)
        # Button 8 - Bottom Middle
        self.btns[2].append(Button(frame3, textvariable=self.vars[2][1], command=lambda: self.btnUpdate(2,1)))
        self.btns[2][1].pack(side=LEFT, pady=5, padx=5)
        # Button 9 - Bottom Right
        self.btns[2].append(Button(frame3, textvariable=self.vars[2][2], command=lambda: self.btnUpdate(2,2)))
        self.btns[2][2].pack(side=LEFT, pady=5, padx=5)
        # Quit Button
        self.quit = Button(frame4, text='Quit', command=frame4.quit)
        self.quit.pack(side=LEFT, pady=5, padx=5)
        # Player Turn Label
        self.playerlabel = Label(frame4, textvariable=self.turnvar)
        self.playerlabel.pack(side=LEFT, pady=5, padx=5)

    def key(self, event):
        print("pressed ", repr(event.char))

    def cycle(self):
        self.turn = not self.turn

    def printboard(self):
        for x in self.vars:
            for y in x:
                print(y.get(), end=' ')
            print()
        print()

    def getPlayer(self, inverse=False):
        if(self.turn):
            return self.marker[0]
        else:
            return self.marker[1]

    def rowSame(self, row):
        if len(row) > 1:
            cache = row[0]
            for x in row:
                if x != cache:
                    return False
                cache = x
        if(row[0] == '☐'):
            return False
        return True
    
    def checkBoard(self):
        for row in range(3):
            x1, x2, x3, y1, y2, y3 = row, row, row, 0, 1, 2
            if(self.vars[x1][y1].get() == self.vars[x2][y2].get() == self.vars[x3][y3].get()):
                self.winningBtns(x1, y1, x2, y2, x3, y3)
                return self.vars[x1][y1].get()

        for col in range(3):
            x1, x2, x3, y1, y2, y3 = 0, 1, 2, col, col, col
            if(self.vars[x1][y1].get() == self.vars[x2][y2].get() == self.vars[x3][y3].get()):
                self.winningBtns(x1, y1, x2, y2, x3, y3)
                return self.vars[0][col].get()

        x1, x2, x3, y1, y2, y3 = 0, 1, 2, 0, 1, 2
        if(self.vars[x1][y1].get() == self.vars[x2][y2].get() == self.vars[x3][y3].get()):
            self.winningBtns(x1, y1, x2, y2, x3, y3)
            return self.vars[1][1].get()

        x1, x2, x3, y1, y2, y3 = 0, 1, 2, 2, 1, 0
        if(self.vars[x1][y1].get() == self.vars[x2][y2].get() == self.vars[x3][y3].get()):
            self.winningBtns(x1, y1, x2, y2, x3, y3)
            return self.vars[1][1].get()
        return '☐'

    def winningBtns(self, x1, y1, x2, y2, x3, y3):
        x = [self.vars[x1][y1].get(), self.vars[x2][y2].get(), self.vars[x3][y3].get()]
        for y in x:
            if y == '☐':
                return False
        print("WinningBtns --- {},{}   {},{}   {},{}".format(x1, y1, x2, y2, x3, y3))
        self.btns[x1][y1].config(disabledforeground='red')
        self.btns[x2][y2].config(disabledforeground='red')
        self.btns[x3][y3].config(disabledforeground='red')

    def update(self):
        self.printboard()
        response = self.checkBoard()
        if(response != '☐'):
            print("Winner: " + response)
            self.disableAll()
        else:
            self.cycle()
            self.turnvar.set("Player " + self.getPlayer())

    def disableAll(self):
        for x in range(3):
            for y in range(3):
                self.btns[x][y].config(state='disabled')

    # Update game board based on who's turn
    def btnUpdate(self, x, y):
        self.btns[x][y].config(state="disabled")
        self.vars[x][y].set(self.getPlayer())
        self.update()
    
root = Tk()
root.wm_attributes("-topmost", 1)
root.overrideredirect(1) # Disable Titlebar
root.iconbitmap(os.path.join(sys.path[0], 'img', 'ico.ico')) # Icon for Application
root.resizable(False, False) #Disable resizing
root.geometry("+1000+500") #Make it appear in the middle

app = App(root)
root.mainloop()