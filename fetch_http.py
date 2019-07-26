import json, os, sys
from tkinter import *
import requests as r
from functools import partial

api_url = 'http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}'
file = open(os.path.join(sys.path[0], 'api_key.dat'), 'r')
key = file.read()

def fetch(zc, cc, api):
    url = api_url.format(zc, cc, key)
    response = r.get(url)
    content = response.json()
    return content

class App:
    def __init__(self, master):
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)

        self.outputvar = StringVar()
        self.zipvar = StringVar()
        
        self.zipentry = Entry(self.frame1, textvariable=self.zipvar)

        self.fetchbtn = Button(self.frame1, text="Fetch!", command=lambda:self.fetch(self.zipvar.get()))
        self.output = Label(self.frame2, textvariable=self.outputvar, wraplength=300)
        
        self.frame1.pack()
        self.frame2.pack()

        self.zipentry.pack(padx=5,pady=5)
        self.fetchbtn.pack(padx=5)
        self.output.pack()
    
    def fetch(self, zipcode):
        if zipcode == '': return None
        content = fetch(zipcode, 'us', key)
        if str(content['cod'])[0] != '2':
            print('Unpredicted Status Code Found')
            print(content)
            print()
            return None
        self.outputvar.set(content['weather'])
root = Tk()
app = App(root)
root.mainloop()