import math
from tkinter import *

WORK_MIN = 0.1
BREAK_MIN = 0.3
LONG_BREAK_MIN = 0.6

cycles = 0
timer = None


def start_timer():
    global cycles
    cycles += 1

    work_sec = WORK_MIN * 60
    short_break_sec = BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if cycles % 8 == 0:
        count_time(long_break_sec)
        status.config(text="Long Break")
    elif cycles % 2 == 0:
        count_time(short_break_sec)
        status.config(text="Short Break")
    else:
        count_time(work_sec)
        status.config(text="Work...")

def reset_timer():
    global cycles
    cycles = 0
    window.after_cancel(timer)
    status.config(text="")
    timer_label.config(text="00:00")
    check_marks.config(text="")


def count_time(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_time, count - 1)
    else:
        start_timer()
        marks = ""
        times_completed = math.floor(cycles/2)
        for _ in range(times_completed):
            marks += "✅"
        check_marks.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

title = Label(text="Timer")
title.grid(column=1, row=0)

timer_label = Label(text="00:00")
timer_label.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="")
check_marks.grid(column=1, row=3)

status = Label(text="")
status.grid(column=1, row=4)

window.mainloop()
