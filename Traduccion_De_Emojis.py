
from Estructura_ChatGPT import *

solicitud = input("Solicitud: ")
contenido = """ 
	Se te proporcionará texto y tu tarea es 
	traducirlo a emojis. No utilice ningún texto 
	normal. Haz tu mejor esfuerzo solo con emojis
"""

traduccion_emojis = ChatGPT(contenido, solicitud)
traduccion_emojis.crear_mensaje()
traduccion_emojis.crear_modelo(0.8, 64)
traduccion_emojis.obtener_respuesta()
traduccion_emojis.mostrar_respuesta()