
# Programa que genera una serie 
# de preguntas tipo entrevista 
# para cualquier area laboral

from Estructura_ChatGPT import *

pregunta = input("Tema: ")
contenido = f""" 
	Crea una lista de 10 preguntas para una 
	entrevista de trabajo sobre {pregunta}
"""

entrevista_laboral = ChatGPT(contenido, pregunta)
entrevista_laboral.crear_mensaje()
entrevista_laboral.crear_modelo(0.1, 1000)
entrevista_laboral.obtener_respuesta()
entrevista_laboral.mostrar_respuesta()