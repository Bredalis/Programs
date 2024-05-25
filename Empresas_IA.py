
import pandas as pd
import sqlite3 as sqlite

class Empresas:

	def conectar_bbdd(self, bbdd):
		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()	

	def instruccion(self, nombre_tabla):
		self.cursor.execute(f"SELECT * FROM {nombre_tabla}")

	def obtener_datos(self):
		self.datos = self.cursor.fetchall()

	def crear_df(self, columnas):
		self.df = pd.DataFrame(self.datos, columns = columnas)

	def borrar_columna(self):
		self.df = self.df.drop("ID", axis = 1)

	def mostrar_df(self, empresa):
		print(f"\nDF {empresa}:\n")
		print(self.df)

# Mostrar datos de 
# empresas de IA

openai = Empresas()
openai.conectar_bbdd("Empresas_IA.db")
openai.instruccion("OpenAI")
openai.obtener_datos()
openai.crear_df(["ID", "Usuarios", "Modelos", "Empleados", "Sueldo", "Area_Laboral"])
openai.borrar_columna()
openai.mostrar_df("OpenAI")