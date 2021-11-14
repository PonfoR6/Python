from tkinter import *

window = Tk()
window.title("Login")
window.minsize(width=500, height=300)


def submit_form():
    if username.get() == "user" and password.get() == "pass":
        window1 = Tk()
        window1.title("Main page")
        window1.minsize(width=500, height=300)


username = Entry(width=15)
username.grid(column=0, row=1)

password = Entry(width=15)
password.grid(column=0, row=2)

button = Button(text="submit", command=submit_form)
button.grid(column=1, row=2)

window.mainloop()
