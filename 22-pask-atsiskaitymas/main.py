import random
from tkinter import *
from tkinter.ttk import *

import pyperclip


def low():
    text_box.delete(0, END)

    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    elif var.get() == 2:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")


def generate():
    password1 = low()
    text_box.insert(10, password1)


def copy1():
    random_password = text_box.get()
    pyperclip.copy(random_password)


window = Tk()
window.config(padx=100, pady=100)
var = IntVar()
var1 = IntVar()

window.title("Random Password Generator")

random_password = Label(window, text="Password")
random_password.grid(row=0)
text_box = Entry(window)
text_box.grid(row=0, column=1)

length_lbl = Label(window, text="Length")
length_lbl.grid(row=1)

clipboard = Button(window, text="Copy", command=copy1)
clipboard.grid(row=1, column=2)
pass_generator = Button(window, text="Generate", command=generate)
pass_generator.grid(row=0, column=2)

radbtn_low = Radiobutton(window, text="Low", variable=var, value=1)
radbtn_low.grid(row=2, column=0)

radbtn_middle = Radiobutton(window, text="Medium", variable=var, value=2)
radbtn_middle.grid(row=2, column=1)

radbtn_strong = Radiobutton(window, text="Strong", variable=var, value=3)
radbtn_strong.grid(row=2, column=2)

pass_length = Combobox(window, textvariable=var1)

pass_length['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 20, 25, 30, 35, 40, 45, 50, "Custom length")
pass_length.current(0)
pass_length.bind('<<ComboboxSelected>>')
pass_length.grid(column=1, row=1)

window.mainloop()
