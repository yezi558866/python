#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial
import tkinter

root = tkinter.Tk()
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button1')
b2 = MyButton(text='Button2')
qb = MyButton(text='QUIT', bg='red', command=root.quit)

b1.pack()
b2.pack()
qb.pack(fill=tkinter.X, expand=1)
root.title('FPA!')
root.mainloop()