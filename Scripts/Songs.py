
<<<<<<< HEAD
=======
# Listas de canciones 
# favoritas para escuchar

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
import sqlite3 as sqlite

class ListaDeCanciones():
	def __init__(self, tipo):
<<<<<<< HEAD
		self.bbdd = sqlite.connect("../BBDD/Songs.db")
		self.cursor = self.bbdd.cursor()
		self.tipo = tipo
		self.lista = []
=======

		self.lista = []
		self.bbdd = sqlite.connect("../BBDD/Songs.db")
		self.cursor = self.bbdd.cursor()
		self.tipo = tipo
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

	def crear_instruccion(self, columna):
		self.instruccion = f"SELECT {columna} FROM Lista_Canciones"

	def obtener_datos(self):
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

	def agregar_datos(self):
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
		for i in self.datos:
			self.lista.append(i[0])

	def mostrar_datos(self):
		print(self.lista)

	def informacion(self):
<<<<<<< HEAD
		print(f"\nCanciones {self.tipo}:")
=======
		print(f"\nCanciones {self.tipo}: \n")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

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
<<<<<<< HEAD
tristes = Tristes("Tristes")
pop = Pop("PoP")
kpop = Kpop("K-pop")

generos = [tristes, pop, kpop]
tipos = ["Tristes", "Pop", "Kpop"]

for i in range(0, len(generos)):
	generos[i].crear_instruccion(tipos[i])
=======

tristes = Tristes("tristes")
pop = Pop("pop")
kpop = Kpop("kpop")

generos = [tristes, pop, kpop]
columnas = ["Tristes", "Pop", "Kpop"]

for i in range(0, len(generos)):
	generos[i].crear_instruccion(columnas[i])
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	generos[i].obtener_datos()
	generos[i].agregar_datos()
	generos[i].informacion()