#07_05_kitchen_sink.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='属性值').grid(row=0, column=0)
        Entry(frame, text='属性').grid(row=0, column=1)
        Button(frame, text='检定').grid(row=0, column=2)
        #Listbox
        listbox = Listbox(frame, height=3, selectmode=SINGLE)
        for item in ['普通', '困难', '极难']:
            listbox.insert(END, item)
        listbox.grid(row=1, column=1)
root = Tk()
root.wm_title('检定')
app = App(root)
root.mainloop()
