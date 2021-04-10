import math
from tkinter import *

# -- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
stars = " "
timer = None


# -- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global stars

    reps = 0
    stars = " "

    # stop the timer
    win.after_cancel(timer)

    # change title
    title_lbl.config(text="timer", fg=GREEN)

    # zero config
    canvas.itemconfig(timer_text, text="00:00")


# -- TIMER MECHANISM --------------------------- #
def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_lbl.config(text="break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        title_lbl.config(text="break", fg=PINK)
        count_down(short_break)
    else:
        title_lbl.config(text="work", fg=GREEN)
        count_down(work_time)


# -- UI SETUP ---------------------------------- #
win = Tk()
win.title("pomodoro timer")
win.config(padx=100, pady=50, bg=YELLOW)

# title
title_lbl = Label(
    text="Timer",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 50)
)

title_lbl.grid(
    column=1,
    row=0
)

# image
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightthickness=0
)

canvas.create_image(
    100, 112,
    image=tomato_img
)

canvas.grid(column=1, row=1)

# title
timer_text = canvas.create_text(
    100, 130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)

# buttons
start_but = Button(
    text="start",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 20, "bold"),
    highlightthickness=0,
    command=start_timer
)

start_but.grid(column=0, row=2)

reset_but = Button(
    text="reset",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 20, "bold"),
    highlightthickness=0,
    command=reset_timer
)

reset_but.grid(column=2, row=2)

# checkmarks
check_marks = Label(
    text='',
    bg=YELLOW,
    fg=GREEN,
    highlightthickness=0
)

check_marks.grid(column=1, row=3)


# -- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    global stars
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    formatted_count = f"{count_min:02.0f}:{count_sec:02.0f}"

    canvas.itemconfig(timer_text, text=formatted_count)

    if count > 0:
        timer = win.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            stars += "✔︎ "
            check_marks.config(text=stars)
        start_timer()


win.mainloop()
