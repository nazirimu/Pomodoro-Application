from tkinter import *
from PIL import ImageTk, Image
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

# variables
reps = 0
completed_checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # Resets the timer when it is called, clearing the old labels.
    global reps, completed_checks
    reps = 0
    completed_checks = ""
    checkmarks.config(text=completed_checks)
    label_1.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    # The window after_cancel command stops the timer from running
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_counter():
    global reps
    reps += 1

    # Converting the minutes into seconds
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    # If statements to determine what cycle the application is currently running at
    if reps % 8 == 0:
        label_1.config(text="Break", fg=GREEN, bg=YELLOW)
        time = long_break
    elif reps % 2 == 0:
        label_1.config(text="Break", fg=PINK, bg=YELLOW)
        time = short_break
    else:
        label_1.config(text="Work", fg=RED, bg=YELLOW)
        time = work_time

    # Calling the count down function
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, completed_checks, timer

    # Converts the seconds into minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # if the seconds are less than 10, dynamic typing is used to keep the text aesthetically pleasing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Displays the time by configuring the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # prevents the counter from going into negative and restarts it
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            completed_checks += "✓"
        checkmarks.config(text=completed_checks)
        start_counter()


# ---------------------------- UI SETUP ------------------------------- #
# Setting up the window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Setting up the canvas with the tomato image

# # Canvas is the same dimensions as the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# # Opens the image using pillow
tomato_img = ImageTk.PhotoImage(Image.open("tomato.png"))

# # x and y location are approximately half of the dimensions
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons

# # Start button
start_button = Button(text="Start", highlightthickness=0, command=start_counter)
start_button.grid(row=2, column=0)

# # Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Label

label_1 = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_1.grid(row=0, column=1)

# Checks

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmarks.grid(row=3, column=1)

window.mainloop()
