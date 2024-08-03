
# Listas de canciones 
# favoritas para escuchar

import sqlite3 as sqlite

class ListaDeCanciones():
	def __init__(self, tipo):

		self.lista = []
		self.bbdd = sqlite.connect("../BBDD/Songs.db")
		self.cursor = self.bbdd.cursor()
		self.tipo = tipo

	def crear_instruccion(self, columna):
		self.instruccion = f"SELECT {columna} FROM Lista_Canciones"

	def obtener_datos(self):

		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

	def agregar_datos(self):

		for i in self.datos:
			self.lista.append(i[0])

	def mostrar_datos(self):
		print(self.lista)

	def informacion(self):
		print(f"\nCanciones {self.tipo}: \n")

		for i in self.lista:
			print("\t-", i)

class Tristes(ListaDeCanciones):
	def __init__(self, tipo):
		super().__init__(tipo)

class Pop(ListaDeCanciones):
	def __init__(self, tipo):
		super().__init__(tipo)

class Kpop(ListaDeCanciones):
	def __init__(self, tipo):
		super().__init__(tipo)

# Mostrar canciones

tristes = Tristes("tristes")
pop = Pop("pop")
kpop = Kpop("kpop")

generos = [tristes, pop, kpop]
columnas = ["Tristes", "Pop", "Kpop"]

for i in range(0, len(generos)):
	generos[i].crear_instruccion(columnas[i])
	generos[i].obtener_datos()
	generos[i].agregar_datos()
	generos[i].informacion()