
import openai

class ChatGPT:
	def __init__(self, contenido, pregunta):
		openai.api_key = "sk-proj-BFO5TeYjGjUrFcfMwVy9T3BlbkFJd61BI454CJuNNvmOiOFv"
		self.contenido = contenido
		self.pregunta = pregunta

	def crear_mensaje(self):
		self.mensaje = [
			{"role": "system", "content": self.contenido},
			{"role": "user", "content": self.pregunta},
		]

	def crear_modelo(self, temperatura = 0, tokens = 0, top = 0):
		self.respuesta = openai.chat.completions.create(
			model = "gpt-3.5-turbo",
			messages = self.mensaje,
			temperature = temperatura,
			max_tokens = tokens,
			top_p = top
		)

	def obtener_respuesta(self):
		self.respuesta = self.respuesta.choices[0].message.content

	def mostrar_respuesta(self):
		print("\nRespuesta:", self.respuesta)