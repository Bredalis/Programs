
import matplotlib.pyplot as plt

# Descargar manual

contenido = open("Manual.txt").read()
exec(contenido)

ruta = "Manual_Histograma.txt"
manual(ruta)

# Mostrar manual en consola

with open(ruta, "r", encoding = "utf-8") as contenido:
	contenido = contenido.read()
	print(contenido)

# Crear datos

habitos = ["Leer", "Programar", "Ejercicio", "Programar", 
			"Meditar", "Ejercicio", "Leer", "Programar"]

set_habitos = ["Ejercicio", "Programar", "Leer", "Meditar"]
dic_habitos = {"Leer": 0, "Programar": 1, "Ejercicio": 2, "Meditar": 3}

datos = [dic_habitos[string] for string in habitos]

# Histograma

plt.hist(datos, ec = "black", color = "pink", bins = len(set_habitos))
plt.xticks(range(len(set_habitos)), set_habitos)

plt.title("Productividad de Lucas")
plt.show()