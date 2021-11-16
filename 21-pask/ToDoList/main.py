from tkinter import *

window = Tk()
window.title("ToDo List")
window.config(padx=100, pady=100)


def add_task():
    text = task_input.get()
    if len(text) > 0:
        toDo_listbox.insert(1, f"{text}")


def switch_to_prog():
    text = task_input.get()
    if len(text) > 0 and f"{text}" in toDo_listbox:
        inprog_listbox.insert(f"{text}")


title = Label(text="To-Do")
title.grid(column=1, row=0)

title = Label(text="In-progress")
title.grid(column=2, row=0)

title = Label(text="Done")
title.grid(column=3, row=0)

add_task = Button(text="Add task", command=add_task)
add_task.grid(column=4, row=5)

prog_task = Button(text="switch to prog", command=switch_to_prog)
prog_task.grid(column=4, row=6)

task_input = Entry(width=15)
task_input.grid(column=4, row=0)

toDo_listbox = Listbox(window, height=7)
toDo_listbox.grid(column=1, row=2)
inprog_listbox = Listbox(window, height=7)
inprog_listbox.grid(column=2, row=2)
done_listbox = Listbox(window, height=7)
done_listbox.grid(column=3, row=2)

window.mainloop()
