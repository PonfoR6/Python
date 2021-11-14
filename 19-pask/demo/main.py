from tkinter import *

window = Tk()
window.title("Demo")


def button_used():
    print("Button used")


def spinbox_used():
    print(spinbox.get())


def checkbox_used():
    print(check_state.get())


def listbox_used(event):
    print(event)
    print(list)


label = Label(text="label")
label.pack()

button = Button(text="Button", command=button_used)
button.pack()

entry = Entry(width=30)
entry.insert(END, string="Text inserted")
entry.pack()

text = Text(height=5, width=30)
text.pack()

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used())
spinbox.pack()

check_state = IntVar()
check_button = Checkbutton(text="Hello", variable=check_state, command=checkbox_used)
check_button.pack()

list_box = Listbox(height=4)
colors = ["red", "green", "blue"]

for item in colors:
    list_box.insert(colors.index(item), item)

list_box.bind("<<ListBoxSelect>>", listbox_used)
list_box.pack()

window.mainloop()
