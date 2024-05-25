 
import sqlite3 as sqlite
import pandas as pd

class ClavesSeguras:

	def conectar_bbdd(self):
		self.url = "Contraseñas_Seguras.db"
		self.bbdd = sqlite.connect(self.url)
 
	def crear_cursor(self):
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
claves.conectar_bbdd()
claves.crear_cursor()
claves.ejecucion()
claves.crear_df()
claves.borrar_columna()
claves.informacion()