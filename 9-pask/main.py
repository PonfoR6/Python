import tkinter
from tkinter import *

root = tkinter.Tk()
root.config(bg="LightBlue")
root.Title("ToDo-list")
root.geometry("500x500")
root.resizable(0, 0)

Label(root, text="To-Do List", bg="LightBlue", font=("Roboto Condensed", 12), wraplength=300).place(x=35, y=0)
tasks = Listbox(root, backgroundColor="Red", bg="DarkRed", font=("Roboto Condensed", 6), height=12, width=25)

scrollbar = Scrollbar(root, orientation=VERTICAL, commands=tasks.yview)
scrollbar.place(x=260, y=50, height=232)

tasks.config(yscrollcommand=scrollbar.set)

tasks.place(x=35, y=50)

with open("ToDoList.txt", "r+") as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

new_item_entry = Entry(root, width=38)
new_item_entry.place(x=35, y=310)

btn_add = Button(root, text="Add task", bg="Gray", width=10, font=("Roboto Condensed", 12),
                 command=lambda: add_item(new_item_entry, tasks))
btn_add.place(x=45, y=350)

btn_remove = Button(root, text="Remove Task", bg="Gray", width=10, font=("Roboto Condensed", 12),
                    command=lambda: remove_item(tasks))
btn_remove.place(x=150, y=350)

root.update()
root.mainloop()


def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open("ToDoList.txt", "a") as tasks_list_file:
        tasks_list_file.write(f"\n{new_task}")


def remove_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open("ToDoList.txt", "r+") as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
                tasks_list_file.write(line)

        tasks_list_file.close()
