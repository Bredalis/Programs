
# Libreria

import openai
openai.api_key = "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"

print("El programa es algo sencible, si ocurre un error por favor volver a ejecutar.\n")

# Creacion de emojis

contenido = """
Se te preguntara que pelicula es, tu tarea es mostrar 
emojis de peliculas de disney. No utilice 
ningún texto normal. Haz tu mejor esfuerzo solo con 
emojis"""

mensaje = [
	{"role": "system", "content": contenido},
	{"role": "user", "content": "Que pelicula es?"},
]

# Modelo y respuesta

respuesta = openai.chat.completions.create(
	model = "gpt-3.5-turbo",
	messages = mensaje,
	temperature = 0.8,
	max_tokens = 64
)

respuesta = respuesta.choices[0].message.content
print(respuesta)

# Creacion de nombres de peliculas

contenido_2 = """
Se te proporcionará una serie de emojis y tu tarea es 
traducirlo a nombres de peliculas. No utilice ningún texto. 
Haz tu mejor esfuerzo solo con el nombre de la pelicula""" 

mensaje_2 = [
	{"role": "system", "content": contenido_2},
	{"role": "user", "content": respuesta},
]

# Modelo y respuesta

respuesta_2 = openai.chat.completions.create(
	model = "gpt-3.5-turbo",
	messages = mensaje_2,
	temperature = 0.8,
	max_tokens = 64
)

respuesta_2 = respuesta_2.choices[0].message.content

# Inicio del juego

vidas = 3
pregunta = ""

while vidas != 0:

	pregunta = input("\n¿Que pelicula es?: ")

	if pregunta.lower() == "salir":
		break

	if pregunta == respuesta_2.lower():
		print("Tu ganas!")
		break

	else:
		vidas -= 1

		if vidas == 1:
			print(f"\nTe queda {vidas} vida")

		elif vidas == 0:
			print(f"Tu pierdes! | {vidas} vidas")

		else:
			print(f"\nTe quedan {vidas} vidas")