
# Libraries
import time
import pygame
import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()
window.title("Timer")
window.geometry("245x230")
window.resizable(0, 0)
window.iconbitmap("../assets/images/clock.ico")


def alarm():
    """Play alarm sound when the timer finishes."""
    pygame.init()
    sound = pygame.mixer.Sound("../assets/audio/bell_sound.mp3")
    pygame.mixer.Sound.play(sound, 3)


def timer(minutes):
    """Countdown timer in minutes."""
    total_seconds = minutes * 60

    while total_seconds > 0:
        remaining_minutes, remaining_seconds = divmod(total_seconds, 60)
        print(f"{remaining_minutes}:{remaining_seconds}")
        time.sleep(1)
        total_seconds -= 1

    print("Time is up!")
    alarm()


amount = 0
timer(amount)

# Background image
image_path = Image.open("../assets/images/clock.ico")
img = ImageTk.PhotoImage(image_path)

tk.Label(window, image=img).pack()
tk.Button(
    window,
    text="Repeat",
    command=lambda: timer(amount)
).place(x=12, y=10)

window.mainloop()
