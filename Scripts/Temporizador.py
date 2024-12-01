
# Librerías
import time
import pygame
import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Temporizador")
ventana.geometry("245x230")
ventana.resizable(0, 0)
ventana.iconbitmap("../IMG/Reloj.ico")

# Temporizador a terminado
def alarma():
	pygame.init()
	url = pygame.mixer.Sound("../Campana.mp3")
	pygame.mixer.Sound.play(url, 3)

def temporizador(minutos):
	segundos_totales = minutos * 60

	while segundos_totales > 0:
		minutos_restantes, segundos_restantes = divmod(segundos_totales, 60)
		print(f"{minutos_restantes}:{segundos_restantes}")	
		time.sleep(1)
		segundos_totales -= 1

	print("¡Tiempo terminado!")
	alarma()

cantidad = 1
temporizador(cantidad)

# Imagen de fondo
url = Image.open("../IMG/Reloj.ico")
img = ImageTk.PhotoImage(url)

tk.Label(ventana, image = img).pack() 
tk.Button(ventana, text = "Repetir", 
	command = lambda: temporizador(cantidad)).place(x = 12, y = 10)

ventana.mainloop()