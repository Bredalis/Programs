 
import sqlite3 as sqlite
import pandas as pd

class ClavesSeguras:
	def __init__(self):
		self.bbdd = sqlite.connect("Contraseñas_Seguras.db")
		self.cursor = self.bbdd.cursor()

	def ejecucion(self):
		self.cursor.execute("SELECT * FROM  Claves_Seguras")

	def crear_df(self):
		self.datos = self.cursor.fetchall()
		self.df = pd.DataFrame(self.datos, 
			columns = ["id", "Entidades",  "Claves"])

	def borrar_columna(self):
		self.df = self.df.drop("id", axis = 1)

	def informacion(self):
		print(self.df)

	def guardar_cambios(self):
		self.bbdd.commit()
		self.bbdd.close()

claves = ClavesSeguras()
claves.ejecucion()
claves.crear_df()
claves.borrar_columna()
claves.informacion()