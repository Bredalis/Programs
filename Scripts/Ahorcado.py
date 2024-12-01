
# Librerías
<<<<<<< HEAD
import tkinter as tk
from PIL import Image, ImageTk
import random

# Lectura de datos
manual_contenido = open("../TXT/Manual.txt", "r").read()
exec(manual_contenido)
manual("../TXT/Manual_Ahorcado.txt")

# Categorías de palabras
manual_contenido = open("../TXT/Categorias_Ahorcado.txt", "r").read()
exec(manual_contenido)

categorias = {
	"Comida": comida, "Sentimientos": sentimientos, "Países": paises, 
	"Nombres": nombres, "Cosas": cosas, "Animales": animales,
	"Artístas": artistas
}

# Mecánica del juego
def personaje_ahorcado():
=======

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

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	ventana = tk.Tk()
	ventana.title("Ahorcado")
	ventana.resizable(0, 0)

	ruta = Image.open("../IMG/Ahorcado.ico")
<<<<<<< HEAD
=======
	
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	imagen = ImageTk.PhotoImage(ruta)

	etiqueta = tk.Label(ventana, image = imagen)
	etiqueta.pack()
<<<<<<< HEAD
	ventana.mainloop()

def seleccionar_palabra():
	try:
		categoria = str(input("Ingrese el tipo de categoría entre (Comida, Sentimientos, Países, Nombres, Cosas, Animales, Artístas): ")).capitalize()

		print(f"La categoría es: {categoria}")
		palabra = random.choice(categorias[categoria])
		return palabra
			
	except Exception as e:
		print(f"Error inesperado: {e}")
=======

	ventana.mainloop()

def seleccionar_palabra():

	try:
		categoria = str(input("Ingrese el tipo de categoria entre (Comida, Sentimientos, Paises, Nombres, Cosas, Animales, Artistas): ")).capitalize()

		print(f"La categoria es: {categoria}")
		palabra = random.choice(categorias[categoria])

		return palabra
			
	except Exception as e:
		print("Error:", e)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

def inicializar_tablero(palabra):	
	return ["_"] * len(palabra)

def mostrar_tablero(tablero):
	print(" ".join(tablero))

def pedir_letra():
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	try:
		letra = str(input("Intoduce la letra: "))
		return letra.lower()
	
	except Exception as e:
<<<<<<< HEAD
		print(f"Error inesperado: {e}",)

def actualizar_tablero(palabra, tablero, letra):
	for i in range(len(palabra)):
=======
		print("Error:", e)

def actualizar_tablero(palabra, tablero, letra):

	for i in range(len(palabra)):

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
		if palabra[i] == letra:
			tablero[i] = letra

def jugar_ahorcado():
<<<<<<< HEAD
=======
	
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	palabra = seleccionar_palabra()
	intentos_maximos = 6
	intentos = 0
	tablero = inicializar_tablero(palabra)

	try:
		while "_" in tablero and intentos < intentos_maximos:
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
			mostrar_tablero(tablero)
			letra = pedir_letra()

			if letra in palabra:
<<<<<<< HEAD
				actualizar_tablero(palabra, tablero, letra)
				print("¡Correcto!")
=======

				actualizar_tablero(palabra, tablero, letra)
				print("Correcto!")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

			else:
				intentos += 1

				for i in range(1, 6):
<<<<<<< HEAD
					if intentos == i:
						print(f"Te quedan {6 - i} intentos")
				print(f"Incorrecto. intentos {intentos}/{intentos_maximos}")
	
	except Exception as e:
		print(f"Error inesperado: {e}")
=======

					if intentos == i:
						print(f"Te quedan {6 - i} intentos")

				print("Incorrecto. intentos {}/{}".format(intentos, intentos_maximos))
	
	except Exception as e:
		print("Error:", e)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

	if "_" in tablero:
		print("Perdiste :(")
		personaje_ahorcado()
		return

<<<<<<< HEAD
	print(f"Ganaste, la palabra era: {palabra}")
=======
	print("Ganaste, la palabra era:", palabra)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

jugar_ahorcado()