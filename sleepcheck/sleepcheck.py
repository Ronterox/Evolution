import os
import time
import tkinter as tk
from PIL import Image, ImageTk

# Small window right below that puts a check automatically every 25 minutes interval
# And if you click it will put an X on the interval and show a window with a message
# "Yo you need to sleep, go to bed now you got distracted after (25 - moment of click in interval) minutes"

root = tk.Tk()
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
        MESSAGE = f"You need to sleep, go to bed now!, you got distracted after {distraction_time:.0f} minutes"
        popup = tk.Toplevel(root)
        popup.configure(bg="#000000")
        popup.overrideredirect(True)

        # Center the window
        x = root.winfo_screenwidth() // 2
        y = root.winfo_screenheight() // 2
        popup.geometry(f"+{x}+{y}")
        
        # Draw the message
        label = tk.Label(popup, text=MESSAGE, bg="#000000", fg="#ffffff", font="Helvetica 20 bold")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        # Draw the gif
        gif = Image.open("sleep.gif")
        frames = []
        for i in range(gif.n_frames):
            gif.seek(i)
            frames.append(ImageTk.PhotoImage(gif.copy().convert("RGBA")))
        label = tk.Label(popup, image=frames[0], bg="#000000")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        # Animate the gif
        def animate(i):
            nonlocal frames
            label.configure(image=frames[i])
            if i == len(frames) - 1:
                frames = frames[::-1]
            popup.after(100, lambda: animate((i + 1) % len(frames)))

        animate(0) 

        # Draw the button
        button = tk.Button(popup, text="OK", command=popup.destroy, bg="#000000", fg="#ffffff", font="Helvetica 20 bold")
        button.pack(fill=tk.X, padx=5, pady=5)

        popup.grab_set()
        popup.wait_window()

        exit()
        
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