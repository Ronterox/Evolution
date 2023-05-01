import tkinter as tk
from typing import List, Tuple

activities_loop: Tuple[List[str], List[str]] = (["video", "read"], ["programming", "physical status"])
states_loop = [0, 0]
index = 0

def create_deliberate_loop():
    root = tk.Tk()
    root.overrideredirect(True)
    root.configure(bg="#000000", padx=10, pady=10)

    margin_right, margin_top = 60, 30
    x, y = root.winfo_screenwidth() - root.winfo_reqwidth() - margin_right, margin_top
    root.geometry(f"+{x}+{y}")

    def on_click(_):
        global index
        index = (index + 1) % 2

        # This is a HACK lol
        root.destroy()
        create_deliberate_loop()

    for i, activities in enumerate(activities_loop):
        bg, fg = ("green", "white") if i == index else ("#000000", "gray")

        fill = tk.Frame(root, bg=bg, height=20)
        fill.pack(fill=tk.X, pady=1)
        
        if activities == activities_loop[index - 1]:
            states_loop[index] = (states_loop[index] + 1) % len(activities)

        activity = activities[states_loop[i - 1]]

        label = tk.Label(fill, text=activity.upper(), bg=bg, fg=fg, font="Helvetica 20 bold")
        label.pack(fill=tk.X, padx=5, pady=5)
        
        label.bind("<Button-1>", on_click)
    
    print(states_loop)

    root.mainloop()

if __name__ == "__main__":
    create_deliberate_loop()