
import sqlite3 as sqlite
import pandas as pd

class GestionDeProyectos:
	def __init__(self, url_bbdd):
		self.bbdd = sqlite.connect(url_bbdd)
		self.cursor = self.bbdd.cursor()

	def instruccion(self):

		self.cursor.execute("SELECT * FROM Proyectos")
		self.datos = self.cursor.fetchall()

	def crear_df(self):
		print("\nSistema de Gestión de Proyectos\n")
		self.df = pd.DataFrame(self.datos)
		self.df.columns = ["ID", "Nombre del proyecto", "Tipo de proyecto", 
		"Cantidad de integrantes", "Etapas del proyecto", "Duracion"]

	def eleminar_id(self):
		self.df = self.df.drop("ID", axis = 1)

	def mostrar_datos(self):
		print(self.df)

	def cerrar_bbdd(self):
		self.bbdd.close()

informacion_proyectos = GestionDeProyectos("Gestion_De_Proyectos.db")
informacion_proyectos.instruccion()
informacion_proyectos.crear_df()
informacion_proyectos.eleminar_id()
informacion_proyectos.mostrar_datos()
informacion_proyectos.cerrar_bbdd()