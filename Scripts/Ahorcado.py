
# Librerías
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
	ventana = tk.Tk()
	ventana.title("Ahorcado")
	ventana.resizable(0, 0)

	ruta = Image.open("../IMG/Ahorcado.ico")
	imagen = ImageTk.PhotoImage(ruta)

	etiqueta = tk.Label(ventana, image = imagen)
	etiqueta.pack()
	ventana.mainloop()

def seleccionar_palabra():
	try:
		categoria = str(input("Ingrese el tipo de categoría entre (Comida, Sentimientos, Países, Nombres, Cosas, Animales, Artístas): ")).capitalize()

		print(f"La categoría es: {categoria}")
		palabra = random.choice(categorias[categoria])
		return palabra
			
	except Exception as e:
		print(f"Error inesperado: {e}")

def inicializar_tablero(palabra):	
	return ["_"] * len(palabra)

def mostrar_tablero(tablero):
	print(" ".join(tablero))

def pedir_letra():
	try:
		letra = str(input("Intoduce la letra: "))
		return letra.lower()
	
	except Exception as e:
		print(f"Error inesperado: {e}",)

def actualizar_tablero(palabra, tablero, letra):
	for i in range(len(palabra)):
		if palabra[i] == letra:
			tablero[i] = letra

def jugar_ahorcado():
	palabra = seleccionar_palabra()
	intentos_maximos = 6
	intentos = 0
	tablero = inicializar_tablero(palabra)

	try:
		while "_" in tablero and intentos < intentos_maximos:
			mostrar_tablero(tablero)
			letra = pedir_letra()

			if letra in palabra:
				actualizar_tablero(palabra, tablero, letra)
				print("¡Correcto!")
			else:
				intentos += 1

				for i in range(1, 6):
					if intentos == i:
						print(f"Te quedan {6 - i} intentos")
				print(f"Incorrecto. intentos {intentos}/{intentos_maximos}")
	
	except Exception as e:
		print(f"Error inesperado: {e}")

	if "_" in tablero:
		print("Perdiste :(")
		personaje_ahorcado()
		return

	print(f"Ganaste, la palabra era: {palabra}")

jugar_ahorcado()