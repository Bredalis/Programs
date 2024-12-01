
# Librerías
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
import time
import pygame
import tkinter as tk
from PIL import Image, ImageTk

<<<<<<< HEAD
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
=======
interfaz = tk.Tk()
interfaz.title("Temporizador")
interfaz.geometry("245x230")
interfaz.resizable(0, 0)
interfaz.iconbitmap("../IMG/Reloj.ico")

# Funcion temporizadora

def temporizador(minutos):

	minutos = minutos
	segundos_totales = minutos * 60

	while segundos_totales > 0:

		minutos_restantes, segundos_restantes = divmod(segundos_totales, 60)
		print(minutos_restantes, ":", segundos_restantes)	
		time.sleep(1)

		segundos_totales -= 1

	print("¡Tiempo terminado!")
	sonido()

# Sonido que indica que la temporizacion a terminado

def sonido():

	pygame.init()

	url = pygame.mixer.Sound("../Campana.mp3")
	pygame.mixer.Sound.play(url, 5)

# Funcion para repetir la temporizacion

cantidad = 0

def repetir(cantidad):	
	temporizador(cantidad)

repetir(cantidad)

# Imagen

url = Image.open("../IMG/Reloj.ico")
img = ImageTk.PhotoImage(url)

tk.Label(interfaz, image = img).pack() 
tk.Button(interfaz, text = "Repetir", 
	command = lambda: repetir(cantidad)).place(x = 12, y = 10)

interfaz.mainloop()
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
