
import tkinter as tk
import time

window = tk.Tk()
window.title("CLOCK")
window.resizable(0, 0)
window.geometry("450x250")
window.iconbitmap("../IMG/Reloj.ico")

window.columnconfigure(0, weight = 15)
window.rowconfigure(0, weight = 15)
window.columnconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

def clock():
	hour = time.strftime("%r")
	day = time.strftime("%A")
	month = time.strftime("%d-%m-%Y")

	resizing = hour_interfaces.winfo_height()
	full_change = int((resizing - 5) * 0.32)

	hour_interfaces.config(text = hour, font = ("", full_change))
	day_interfaces.config(text = day, font = ("", 15))
	date_interfaces.config(text = month, font = ("", 15))

	window.after(1000, clock)

hour_interfaces = tk.Button(window, fg = "aqua", bg = "black",
	cursor = "clock", relief = "groove", bd = 3, activebackground = "#ff0266")
hour_interfaces.grid(row = 0, sticky = "snew", ipadx = 20 , ipady = 5)

day_interfaces = tk.Button(window, fg = "green2", bg = "gray2",
	cursor = "clock", relief = "groove", bd = 3, activebackground = "#ff0266")
day_interfaces.grid(row = 1, sticky = "snew")

date_interfaces = tk.Button(window, fg = "blue", bg = "gray3",
	cursor = "clock", relief = "groove", bd = 2, activebackground = "#00B0FF")
date_interfaces.grid(row = 2, sticky = "snew")

clock()

window.mainloop()