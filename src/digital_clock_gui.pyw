
import tkinter as tk
import time


window = tk.Tk()
window.title("CLOCK")
window.geometry("450x250")
window.iconbitmap("../assets/images/clock.ico")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=15)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)


def update_clock():
    """Updates the clock display every second."""
    current_time = time.strftime("%r")
    current_day = time.strftime("%A")
    current_date = time.strftime("%d-%m-%Y")

    resizing = hour_display.winfo_height()
    font_size = int((resizing - 5) * 0.32)

    hour_display.config(text=current_time, font=("", font_size))
    day_display.config(text=current_day, font=("", 15))
    date_display.config(text=current_date, font=("", 15))

    window.after(1000, update_clock)


hour_display = tk.Button(
    window,
    fg="aqua",
    bg="black",
    cursor="clock",
    relief="groove",
    bd=3,
    activebackground="#ff0266"
)
hour_display.grid(row=0, sticky="nsew", ipadx=20, ipady=5)

day_display = tk.Button(
    window,
    fg="green2",
    bg="gray2",
    cursor="clock",
    relief="groove",
    bd=3,
    activebackground="#ff0266"
)
day_display.grid(row=1, sticky="nsew")

date_display = tk.Button(
    window,
    fg="blue",
    bg="gray3",
    cursor="clock",
    relief="groove",
    bd=2,
    activebackground="#00B0FF"
)
date_display.grid(row=2, sticky="nsew")


update_clock()
window.mainloop()
