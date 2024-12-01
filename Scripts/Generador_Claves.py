
# Generador de contraseñas seguras

from faker import Faker

<<<<<<< HEAD
def claves_seguras(longitud: int):
	try:
		if longitud < 8 or longitud > 128:
			return "Longitud mínima 8 y máxima 128."

		clave = Faker().password(length = longitud)
		print(f"Tu contraseña segura: {clave}")
	
	except Exception as e:
		return f"Error inesperado: {e}"
=======
datos_random = Faker()

def claves_seguras(longitud):

	clave = datos_random.password(length = longitud)
	print("Tu clave segura: \n", clave)

claves_seguras(10)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
