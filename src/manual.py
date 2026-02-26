
import tkinter as tk


def show_manual(filepath, icon=None, color=None):
    """Display a manual file in a popup window."""
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    window = tk.Tk()
    window.title("Instruction Manual")
    window.resizable(False, False)
    window.config(bg=color)
    
    if icon:
        window.iconbitmap(icon)

    tk.Label(window, text=content, bg=color).pack()
    window.mainloop()
