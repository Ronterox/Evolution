import os
import time
import tkinter as tk, tkinter.messagebox

# Small window right below that puts a check automatically every 25 minutes interval
# And if you click it will put an X on the interval and show a window with a message
# "Yo you need to sleep, go to bed now you got distracted after (25 - moment of click in interval) minutes"

root = tk.Tk()
root.title("Sleep Check")
root.resizable(False, False)
root.overrideredirect(True)
root.configure(bg="#000000")

TIME_IN_DAY = 24 * 60
start = time.time() / 60 % TIME_IN_DAY

def get_distraction_time():
    return time.time() / 60 % TIME_IN_DAY - start

def show_message(check):
    distraction_time = get_distraction_time()
    if distraction_time <= 15:
        check.config(state="disabled")
        tkinter.messagebox.showinfo("Sleep Check", f"You need to sleep, go to bed now you got distracted after {distraction_time:.0f} minutes")
        # Linux lock screen
        os.system("xdg-screensaver lock")
    else:
        check.deselect()
    
checks = []
for i in range(0, TIME_IN_DAY, 25):
    check = tk.Checkbutton(root, bg="#000000", fg="#ffffff", selectcolor="green", activebackground="green", activeforeground="green", highlightbackground="#000000", highlightcolor="#000000")
    check.grid(row=0, column=i // 25)
    if start > i:
        check.config(state="disabled")
        check.select()
    else:
        check.config(command=lambda check=check: show_message(check))
        checks.append((check, i))

MIN_IN_MS = 60 * 1000 * 25

def update_start():
    global start
    start = time.time() / 60 % TIME_IN_DAY
    for check, i in checks:
        if start > i:
            check.select()
        else:
            check.config(state="normal")
            check.deselect()
    root.after(MIN_IN_MS, update_start)

root.after(MIN_IN_MS, update_start)

root.mainloop()