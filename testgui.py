#07_05_kitchen_sink.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='属性值').grid(row=0, column=0)
	#Label(frame, text='test').grid(row=1, column=0)
        Entry(frame, text='Entry').grid(row=0, column=1)
        Button(frame, text='检定').grid(row=0, column=2)
        #check_var = StringVar()
        #check = Checkbutton(frame, text='普通', variable=checkeasy_var, onvalue='Y', offvalue='N')
        #check.grid(row=1, column=0)
	#check_var = StringVar()
        #check = Checkbutton(frame, text='困难', variable=checkhard_var, onvalue='Y', offvalue='N')
        #check.grid(row=1, column=0)
	#check_var = StringVar()
        #check = Checkbutton(frame, text='极难', variable=checkhardest_var, onvalue='Y', offvalue='N')
        #check.grid(row=1, column=0)
        #Radiobutton set
        #radio_frame = Frame(frame)
        #radio_selection = StringVar()
        #b1 = Radiobutton(radio_frame, text='portrait', 
        #    variable=radio_selection, value='P')
        #b1.pack(side=LEFT)
        #b2 = Radiobutton(radio_frame, text='landscape', 
        #    variable=radio_selection, value='L')
        #b2.pack(side=LEFT)
        #radio_frame.grid(row=1, column=2)
        #Scale
        #scale_var = IntVar()
        #Scale(frame, from_=1, to=10, orient=HORIZONTAL,
        #      variable=scale_var).grid(row=2, column=0)
        #Label(frame, textvariable=scale_var, 
        #      font=("Helvetica", 36)).grid(row=2, column=1)
        #Spinbox
        Spinbox(frame, values=('普通','困难','极难')).grid(row=3,column=2)
root = Tk()
root.wm_title('检定')
app = App(root)
root.mainloop()
