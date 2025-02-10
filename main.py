import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
count_down_running = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global count_down_running
    if count_down_running:
        window.after_cancel(timer)
    global reps
    reps += 1
    rep_label.config(text=reps)
    if reps % 2 != 0 & reps<8:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 2 == 0 & reps<8:
        timer_label.config(text="BREAK", fg=GREEN)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=GREEN)
        count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global count_down_running
    count_down_running = True
    minutes = count // 60  # Integer division to get minutes
    seconds = count % 60   # Remainder to get seconds
    
    # Format time as 00:00
    time_string = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_string)  # Update the timer text
    
    if count > 0:
        # Schedule the next update in 1000ms (1 second)
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            work_sessions = reps // 2
            check_marks.config(text="✓" * work_sessions)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Background image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="/Users/anastasialinchik/Angela/pomodoro-start/tomato.png")  # Make sure this image exists in your project folder
canvas.create_image(100, 112, image=tomato_img)  

# Add timer_text as a global variable we can update
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

rep_label = tk.Label(text=reps, font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
rep_label.grid(row=4, column=1)

start_button = tk.Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

check_marks = tk.Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
