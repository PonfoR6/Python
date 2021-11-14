from tkinter import *
import tkinter as tk
from tkinter import ttk

window = Tk()
window.title("Project")
window.minsize(width=500, height=300)


def submit_form():
    text = str.get()
    texts = text[1:-1]
    string = Label(text=texts)
    string.grid(column=2, row=3)


def btn_exit():
    window.destroy()


var = IntVar()
R1 = Radiobutton(window, text="Option 1", variable=var, value=1)
R1.grid(column=2, row=3)

R2 = Radiobutton(window, text="Option 2", variable=var, value=2)
R2.grid(column=3, row=4)

R3 = Radiobutton(window, text="Option 3", variable=var, value=3)
R3.grid(column=4, row=5)

button = Button(text="Hello", command=submit_form)
button.grid(column=3, row=1)

button = Button(text="Exit", command=btn_exit)
button.grid(column=4, row=1)

canvas = Canvas(window, bg="white", height=300, width=300)

spin = Spinbox(window, from_=0, to=25)
spin.grid()

n = tk.StringVar()

monthchosen = ttk.Combobox(window, width=27,
                           textvariable=n)

monthchosen['values'] = (' January',
                         ' February',
                         ' March',
                         ' April',
                         ' May',
                         ' June',
                         ' July',
                         ' August',
                         ' September',
                         ' October',
                         ' November',
                         ' December')

monthchosen.grid(column=1, row=15)

monthchosen.current(1)

var1 = IntVar()
Checkbutton(window, text="checkbox", variable=var1).grid(row=0, sticky=W)

str = Entry(width=15)
str.grid(column=0, row=1)

window.mainloop()
