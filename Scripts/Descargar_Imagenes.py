
import requests

print("Este es un programa para descargar imagenes de tipo .png, .jpg y .gift")

url = input("Ingrese la url: ")
nombre = input("Ingrese el nombre de la imagen: ")
tipo = input("Ingrese el tipo de imagen que quiere: ")

def descargar_imagen(url, nombre, tipo):

	ruta = nombre + tipo
	imagen = requests.get(url).content

	with open(ruta, "wb") as archivo:
		archivo.write(imagen)

descargar_imagen(url, nombre, tipo)