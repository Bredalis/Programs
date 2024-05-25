

# Obtener y mostrar contactos
# para el programa de whatsapp

import sqlite3 as sqlite
import pandas as pd

class Contactos:
	def __init__(self, url):
		
		self.bbdd = sqlite.connect(url)
		self.cursor = self.bbdd.cursor()

	def instruccion(self):
		self.instruccion = f"SELECT * FROM Contactos"
		self.cursor.execute(self.instruccion)

	def obtener_datos(self):
		self.datos = self.cursor.fetchall()

	def crear_df(self):
		self.df = pd.DataFrame(self.datos, 
			columns = ["id", "nombres", "numeros_telefonicos"])

	def borrar_columna(self):
		self.df = self.df.drop(["id"], axis = 1)

	def mostrar_contactos(self):
		print(self.df) 

# Mostra contactos

print("Contactos:\n")

url = "Contactos.db"
bbdd = Contactos(url)
bbdd.instruccion()
bbdd.obtener_datos()
bbdd.crear_df()
bbdd.borrar_columna()
bbdd.mostrar_contactos()