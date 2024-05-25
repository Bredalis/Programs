
# Programa que automatiza
# el envio de mensajes de 
# Whatsapp y eleva la productividad

import pywhatkit as kt
import datetime
from  Contactos import *

class Mensajes:

	def informacion(self):
		print("\nHola!, manda mensajes a Whatsapp de manera automatizada")

		self.nombre = input("\nPara: ")
		self.numero_telefonico = input("Numero Telefonico: ")
		self.mensaje = input("Mensaje: ")

	def enviar_mensaje(self):
		try:

			self.hora_actual = datetime.datetime.now().time()

			kt.sendwhatmsg(self.numero_telefonico, self.mensaje, 
				self.hora_actual.hour, self.hora_actual.minute + 1, 
				40)
			
			print(f"\nListo se le envio el mensaje a {self.nombre}!")

		except Exception:
			print("Hubo en error, intentelo de nuevo")

mensaje = Mensajes()
mensaje.informacion()
mensaje.enviar_mensaje()