
from Estructura_ChatGPT import *

contenido = """ 

	Eres un amigo artificial, por ende sabes como
	tratar a los usuarios que te hablan y te sabes 
	adaptar a sus emociones.Eres atento y cariñoso,
	sueles decir cosas lindas y sobre todo tienes
	el valor del respeto.	
"""

pregunta = input("Pregunta: ")

chatbot_amistoso = ChatGPT(contenido, pregunta)
chatbot_amistoso.crear_mensaje()
chatbot_amistoso.crear_modelo(0.5, 120)
chatbot_amistoso.obtener_respuesta()
chatbot_amistoso.mostrar_respuesta()