
from Estructura_ChatGPT import *

pregunta = input("Pregunta: ")
contenido = """ 
	Eres un cocinero/chef experto, es decir, sabes todo sobre
	la comida y sus derivados. Estaras hablando con un usuario
	que te hara preguntas sobre cocina y tu tarea es responderle
	ya sea con conceptos, recetas para preparar algo, etc. Recuerda
	ser claro. Y al final de tu respuesta siempre dile algo lindo
	como un lema, frase o una buena despedida alusivo a la cocina.
"""

experto_en_cocina = ChatGPT(contenido, pregunta)
experto_en_cocina.crear_mensaje()
experto_en_cocina.crear_modelo(0.5, 120)
experto_en_cocina.obtener_respuesta()
experto_en_cocina.mostrar_respuesta()