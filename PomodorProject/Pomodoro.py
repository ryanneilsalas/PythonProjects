from tkinter import *
import math

# Constants
Pink = "#e2979c"
Red = "#e7305b"
Green = "#9bdeac"
Yellow = "#f7f5dd"
Font_Name = "Courier"
Work_Min = 25
Short_Break_Min = 5
Long_Break_Min = 20
reps = 0
this_timer = NONE


# Timer Mechanism
def start_timer():
    btn_start.config(state=DISABLED)
    global reps
    reps += 1

    if reps % 2 == 1 or reps == 1:
        count_down(Work_Min * 60)

        lbl_state.config(text="Work", fg=Green)

    elif reps % 8 == 0:
        lbl_state.config(text="Break", fg=Red)
        count_down(Long_Break_Min * 60)
    else:
        lbl_state.config(text="Break", fg=Pink)
        count_down(Short_Break_Min * 60)


# Countdown Mechanism
def count_down(count):
    global reps
    global this_timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count_min < 1 and int(count_sec) < 1:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        lbl_check.config(text=mark)
    if count > 0:
        this_timer = window.after(1000, count_down, count - 1)


def reset():
    global reps
    window.after_cancel(this_timer)
    lbl_state.config(text="Timer", fg=Green)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    lbl_check.config(text="")
    btn_start.config(state=ACTIVE)


# UI SETUP

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=Yellow)

canvas = Canvas(width=200, height=224, bg=Yellow, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(Font_Name, 21, "bold"))
canvas.grid(column=1, row=1)

lbl_state = Label(text="Timer", font=(Font_Name, 30, "bold"), bg=Yellow, fg=Green)
lbl_state.grid(column=1, row=0)
lbl_check = Label(font=(Font_Name, 10, "bold"), bg=Yellow, fg=Green)
lbl_check.grid(column=1, row=3)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2, padx=10, pady=10)

btn_reset = Button(text="Reset", command=reset)
btn_reset.grid(column=2, row=2, padx=10, pady=10)

window.mainloop()
