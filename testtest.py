#07_10_menus.py

from tkinter import *

class App:
	
    def __init__(self, master):
        self.entry_text = StringVar()
        frame = Frame(master)
        frame.pack() 
	Entry(master, textvariable=self.entry_text).pack()
        Label(frame, text='属性值').grid(row=0, column=0)
        Entry(frame, text='属性').grid(row=0, column=1)
        Button(frame, text='检定').grid(row=0, column=2)
        menubar = Menu(root)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Quit', command=exit)
        menubar.add_cascade(label='File', menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label='Fill', command=self.fill)
        menubar.add_cascade(label='Edit', menu=editmenu)
        
        master.config(menu=menubar)

    def fill(self):
        self.entry_text.set('abc') 
        
root = Tk()
app = App(root)

root.mainloop()

