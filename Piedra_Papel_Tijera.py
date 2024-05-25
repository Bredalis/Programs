
# Libreria

import random

# Obtener eleccion del usuario

def obtener_opcion_usuario():
	
	usuario = input("Elije una (piedra, papel o tijera): ")

	while usuario.lower() not in ["piedra", "papel", "tijera"]:
		print("Eleccion incorrecta")

		usuario = input("Elije una (piedra, papel o tijera): ")

	return usuario

# Obtener eleccion de la maquina

def obtener_opcion_maquina():
	
	opciones = ["piedra", "papel", "tijera"]
	maquina = random.choice(opciones)

	return maquina

# Mostrar el resultado del juego

def determinar_resultado(usuario, maquina):

	if usuario == maquina:
		return "Empate"

	elif (usuario == "piedra" and maquina == "tijera") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):

		return "Ganaste"

	else:
		return "Perdiste :("

# Inicio del juego

def juega_piedra_papel_tijera():

	print("Bienvenido al juego contra ordenador de piedra, papel o tijera")

	usuario = obtener_opcion_usuario()
	maquina = obtener_opcion_maquina()
	resultado = determinar_resultado(usuario, maquina)

	print("Elejiste", usuario)
	print("La maquina elijio", maquina)
	print(resultado)

juega_piedra_papel_tijera()