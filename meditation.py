import random
import tkinter as tk
from pygame import mixer

mixer.init()

# Needs relaxing noise
noise = mixer.Sound("noise.wav")
noise.set_volume(0.15)
noise.play(-1)

# Needs relaxing song 
mixer.music.load("song.wav")
mixer.music.play(-1)
mixer.music.set_volume(0)

# lyrics of the song maybe
lyrics = open("lyrics.txt", "r").readlines()
lyrics_idx = 0

def create_black_screen():
    root = tk.Tk()
    
    # Make the window full screen
    root.configure(background='black')
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.config(cursor="none")

    # Giant text middle of the screen
    label = tk.Label(root, text="Close your eyes...", font=("Helvetica", 100), fg="gray", bg="black")
    label.pack(expand=True)

    def update_label():
        global lyrics_idx
        label.config(text=lyrics[lyrics_idx])
        lyrics_idx = (lyrics_idx + 1) % len(lyrics)
        label.after(3000, update_label)
    
    def alter_volume(increment):
        mixer.music.set_volume(mixer.music.get_volume() + increment)
        if 0 < mixer.music.get_volume() < 0.5:
            label.after(50, alter_volume, increment)
    
    def randomly_increment_volume():
        alter_volume(random.choice([-0.01, 0.01]))
        label.after(5000, randomly_increment_volume)
    
    label.after(1000, randomly_increment_volume)
    label.after(3000, update_label)
    root.mainloop()

create_black_screen()