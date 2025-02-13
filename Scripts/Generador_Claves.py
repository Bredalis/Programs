
# Generador de contraseñas seguras

from faker import Faker

def claves_seguras(longitud: int):
	try:
		if longitud < 8 or longitud > 128:
			return "Longitud mínima 8 y máxima 128."

		clave = Faker().password(length = longitud)
		return f"Tu contraseña segura:", clave 
	
	except Exception as e:
		return f"Error inesperado: {e}"