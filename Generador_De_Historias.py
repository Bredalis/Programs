
from Estructura_ChatGPT import *

datos = """
	Para mi historia, quiero que el personaje principal se llame Lucas,
	sea de genero de suspenso y sea la playa
"""

contenido = f""" 
	Eres un experto creando historias largas e intrigantes. Escribe
	una historia con los (datos) que te pida el usuario, por ejemplo: 
	algun genero, personajes, lugares, dialogos, todas las cosas que 
	te pida el usuario. La hitoria no debe ser de mas de 5 parrafos.
	(datos) = {datos}.
"""

generador_de_historias = ChatGPT(contenido, datos)
generador_de_historias.crear_mensaje()
generador_de_historias.crear_modelo(1, 1000)
generador_de_historias.obtener_respuesta()
generador_de_historias.mostrar_respuesta()