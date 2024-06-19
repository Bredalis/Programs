
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

	condiciones = [
		usuario == "piedra" and maquina == "tijera", 
		usuario == "papel" and maquina == "piedra", 
		usuario == "tijera" and maquina == "papel"]

	if usuario != maquina:
		return "Perdiste :("

	if (condiciones[0]) or (condiciones[1]) or (condiciones[2]):
		return "Ganaste"

	return "Empate"

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