
# Generador de contraseñas seguras

from faker import Faker

datos_random = Faker()

def claves_seguras(longitud):

	clave = datos_random.password(length = longitud)
	print("Tu clave segura: \n", clave)

claves_seguras(10)