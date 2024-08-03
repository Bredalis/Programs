
# Librerias

from PIL import Image, ImageTk
import tkinter as tk
import random

# Lectura de datos

contenido = open("../TXT/Manual.txt", "r").read()
exec(contenido)

manual("../TXT/Manual_Ahorcado.txt")

# Categorias de palabras

contenido = open("../TXT/Categorias_Ahorcado.txt", "r").read()
exec(contenido)

categorias = {
	"Comida": comida, "Sentimientos": sentimientos, "Paises": paises, 
	"Nombres": nombres, "Cosas": cosas, "Animales": animales,
	"Artistas": artistas
}

# Mecanica del juego

def personaje_ahorcado():

	ventana = tk.Tk()
	ventana.title("Ahorcado")
	ventana.resizable(0, 0)

	ruta = Image.open("../IMG/Ahorcado.ico")
	
	imagen = ImageTk.PhotoImage(ruta)

	etiqueta = tk.Label(ventana, image = imagen)
	etiqueta.pack()

	ventana.mainloop()

def seleccionar_palabra():

	categoria = input("Ingrese el tipo de categoria entre (Comida, Sentimientos, Paises, Nombres, Cosas, Animales, Artistas): ").capitalize()

	print(f"La categoria es: {categoria}")
	palabra = random.choice(categorias[categoria])

	return palabra

def inicializar_tablero(palabra):	
	return ["_"] * len(palabra)

def mostrar_tablero(tablero):
	print(" ".join(tablero))

def pedir_letra():

	letra = input("Intoduce la letra: ")
	return letra.lower()

def actualizar_tablero(palabra, tablero, letra):

	for i in range(len(palabra)):

		if palabra[i] == letra:
			tablero[i] = letra

def jugar_ahorcado():
	
	palabra = seleccionar_palabra()
	intentos_maximos = 6
	intentos = 0
	tablero = inicializar_tablero(palabra)

	while "_" in tablero and intentos < intentos_maximos:

		mostrar_tablero(tablero)
		letra = pedir_letra()

		if letra in palabra:

			actualizar_tablero(palabra, tablero, letra)
			print("Correcto!")

		else:

			intentos += 1

			for i in range(1, 6):

				if intentos == i:
					print(f"Te quedan {6 - i} intentos")

			print("Incorrecto. intentos {}/{}".format(intentos, intentos_maximos))

	if "_" in tablero:
		print("Perdiste :(")
		personaje_ahorcado()
		return

	print("Ganaste, la palabra era:", palabra)

jugar_ahorcado()