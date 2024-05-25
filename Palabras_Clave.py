
# Obtiene palabras clave 
# de un bloque de texto

from Estructura_ChatGPT import *

contenido = """ 
	Se le proporcionará un bloque de texto y su tarea 
	será extraer de él una lista de palabras clave	
"""

pregunta = input("Texto: ")

palabras_clave = ChatGPT(contenido, pregunta)
palabras_clave.crear_mensaje()
palabras_clave.crear_modelo(0.5, 64)
palabras_clave.obtener_respuesta()
palabras_clave.mostrar_respuesta()