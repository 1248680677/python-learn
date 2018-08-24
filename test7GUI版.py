#07_05_kitchen_sink.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='属性值').grid(row=0, column=0)
        Entry(frame, text='属性').grid(row=0, column=1)
        Button(frame, text='检定').grid(row=0, column=2)
	Spinbox(frame, values=('a','b','c')).grid(row=3)
root = Tk()
root.wm_title('检定')
app = App(root)
root.mainloop()
