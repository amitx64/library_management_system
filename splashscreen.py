import tkinter
from tkinter import *
from tkinter import ttk

class SplashScreen(object):
    def __init__(self, master):
        self.master = master
        frame_1 = Label(self.master, bd=1, borderwidth=2)
        frame_1.pack(side=TOP, fill="x")
        
        self.welcome_main_image = PhotoImage(file='welcome_image.png')
        self.img_lable = Label(frame_1, image=self.welcome_main_image, bg='gainsboro')
        self.img_lable.pack(side=TOP)
        # label_4 = Label(frame_2,text="")
        # label_4.grid(row=0, column=1, padx=100)