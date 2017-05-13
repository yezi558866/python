#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

def resize(ev=None):
	label.config(font='Helvetica -%d bold' % scale.get())

top = tkinter.Tk()
top.geometry('500x200')

label = tkinter.Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=tkinter.Y, expand=1)

scale = tkinter.Scale(top, from_=10, to=40, orient=tkinter.HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tkinter.X, expand=1)

quit = tkinter.Button(top, text='Quit', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()
tkinter.mainloop()