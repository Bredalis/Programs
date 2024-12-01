
import sqlite3 as sqlite
import pandas as pd

class Contactos:
	def __init__(self, url):
<<<<<<< HEAD
=======
		
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
		self.bbdd = sqlite.connect(url)
		self.cursor = self.bbdd.cursor()

	def instruccion(self):
		self.instruccion = f"SELECT Nombres, Numero_Telefonico FROM Contactos"
		self.cursor.execute(self.instruccion)

	def obtener_datos(self):
		self.datos = self.cursor.fetchall()

	def crear_df(self):
		self.df = pd.DataFrame(self.datos, 
<<<<<<< HEAD
			columns = ["Nombres", "Número Telefónico"])
=======
			columns = ["nombres", "numero_telefonico"])
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

	def mostrar_contactos(self):
		print(self.df) 

# Mostra contactos

print("Contactos:\n")
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
bbdd = Contactos("../BBDD/Contactos.db")
bbdd.instruccion()
bbdd.obtener_datos()
bbdd.crear_df()
bbdd.mostrar_contactos()