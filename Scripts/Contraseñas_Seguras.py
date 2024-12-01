 
import sqlite3 as sqlite
import pandas as pd

class ClavesSeguras:
	def __init__(self):
		self.bbdd = sqlite.connect("../BBDD/Contraseñas_Seguras.db")
		self.cursor = self.bbdd.cursor()

	def ejecucion(self):
		self.cursor.execute("SELECT Entidad, Claves FROM  Claves_Seguras")

	def crear_df(self):
		self.datos = self.cursor.fetchall()
		self.df = pd.DataFrame(self.datos, 
			columns = ["Entidades",  "Claves"])

	def informacion(self):
		print(self.df)

	def guardar_cambios(self):
		self.bbdd.commit()
		self.bbdd.close()

claves = ClavesSeguras()
claves.ejecucion()
claves.crear_df()
claves.informacion()