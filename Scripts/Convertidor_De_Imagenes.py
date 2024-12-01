
from PIL import Image

<<<<<<< HEAD
def conversion(url, nombre, tipo, ruta):
	ruta = f"{ruta}/{nombre}.{tipo}"
=======
def conversion(url, nombre, tipo):

	ruta = nombre + "." + tipo
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	imagen_original = Image.open(url)
	imagen_original.save(ruta, format = tipo)