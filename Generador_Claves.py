
# Generador de contraseñas seguras

import numpy as np

alfabeto_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", 
	"I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
	"U", "V", "W", "X", "Y", "Z"]

alfabeto_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
	"j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
	"w", "x", "y", "z"]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

caracteres = ["!", "'", "#", "$", "%", "&", "(", ")", "*", "+", "-",
	".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "/", "]", "^", "_ ", 
	"`", "{", "|", "}", "~"]

def claves_seguras():
	alfabeto_mayusculas_random = np.random.choice(alfabeto_mayusculas, size = (3))
	alfabeto_minusculas_random = np.random.choice(alfabeto_minusculas, size = (3))
	numeros_random = np.random.choice(numeros, size = (3))
	caracteres_random = np.random.choice(caracteres, size = (3))

	# Concatenar los resultados
	clave = np.concatenate((alfabeto_mayusculas_random, 
		alfabeto_minusculas_random, numeros_random, caracteres_random))

	# Ponerlos aun mas aleatoreos
	clave = np.random.choice(clave, size = (len(clave)))

	print("Tu clave segura:")
	for i in range(0, len(clave)):
		print(clave[i], end = "")

	print("\n")

claves_seguras()