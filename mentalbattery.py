import tkinter as tk
from random import randint
from math import floor

# TODO: There is cases that we start with a higher bias mental
#       For example, if we have a good night sleep, we start with a higher mental
#       Or if we have a good day, we start with a higher mental
#       (Or the opposite, if the opposite happens)

# NOTE: Doing some other activities required a higher level of mental, than other activities
# After certain % amount of mental, you unlock the extra mental options

# NOTE: Some activities reduce your mental <- Don't do this

# NOTE: Some unexpected mental reducers occur

# NOTE: All activities reduce your focus Battery

# NOTE: Focus != Mental

# Create a battery like UI, with a bar that fills up as you check the boxes of the activities
activities = ["nap", "train", "learn", "evolution", "play", "music", "eat", "family", "asmr", "coffee/tea", "games", "shower", "irl"]
done = [x for x in activities[:randint(1, len(activities) // 2)]]
    
def create_mentalhealth_battery(activities, done):
    activities = sorted(activities, key=lambda x: x in done, reverse=True)

    root = tk.Tk()
    root.overrideredirect(True)
    root.configure(bg="#000000", padx=10, pady=10)

    x, y = root.winfo_screenwidth() - root.winfo_reqwidth(), 0
    root.geometry(f"+{x}+{y}")

    # Draw the battery from top to bottom
    energy = len(done) / len(activities)
    batt_color = floor(energy * 255)
    batt_color = f"#{255 - batt_color:02x}{batt_color:02x}00"

    energy_label = tk.Label(root, text=f"{floor(energy * 100)}%", bg=batt_color, font="Helvetica 20 bold")
    energy_label.pack(fill=tk.X, pady=5)

    for i, activity in enumerate(activities[::-1]):
        ischarge = len(activities) - i <= len(done)
        bg, fg = (batt_color, "black") if ischarge else ("#000000", "gray")

        fill = tk.Frame(root, bg=bg, height=20)
        fill.pack(fill=tk.X, pady=1)

        label = tk.Label(fill, text=activity.upper(), bg=bg, fg=fg, font="Helvetica 20 bold")
        label.pack(fill=tk.X, padx=5, pady=5)

        def on_click(_, activity=activity):
            if activity in done:
                done.remove(activity)
            else:
                done.append(activity)
            root.destroy()
            create_mentalhealth_battery(activities, done)
        
        fill.bind("<Button-1>", on_click)
        label.bind("<Button-1>", on_click)

    root.mainloop()

if __name__ == "__main__":
    create_mentalhealth_battery(activities, done)