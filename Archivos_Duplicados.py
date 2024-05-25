
import os
import hashlib

class ArchivosDuplicados:
	def __init__(self, url_carpeta):
		self.carpeta = os.chdir(url_carpeta)
		self.lista_archivos = []
		self.lista_duplicados = []
		self.lista_tamaño = []
		self.lista_hashes = []
		self.contador = 0 

	def obtener_archivos(self):
		print("Todos archivos:\n")

		for ruta, directorio, archivo in os.walk(os.getcwd()):
			for i in archivo:
				print(i)
				self.lista_archivos.append(i)

	def comparar_nombres(self):
		print("\nNombres duplicados:\n")
		while self.contador < len(self.lista_archivos):
			for i in range(0, len(self.lista_archivos)):

				if self.lista_archivos[self.contador] == self.lista_archivos[i]:
					self.lista_duplicados.append(self.lista_archivos[i])

			self.contador += 1
				
		print(self.lista_duplicados)
		print("Prueba 1 completa")

	def comparar_tamaño(self):

		try:
			print("\nTamaños duplicados:\n")

			while self.contador < len(self.lista_archivos):
				for i in range(0, len(self.lista_archivos)):

					if os.path.getsize(self.lista_archivos[self.contador]) == os.path.getsize(self.lista_archivos[i]):
						self.lista_tamaño.append(self.lista_archivos[i])

				self.contador += 1
		except Exception:
			print("Error en el sistema")

		finally:
			print(self.lista_tamaño)	
			print("Prueba 2 completa")

	def comparar_hashes(self):

		try:
			print("\n Hashes duplicados: \n")
			for i in range(0, len(self.lista_archivos)):
				self.hashes = hashlib.new("sha256", open(self.lista_archivos[i], "rb").read()).hexdigest()
				self.lista_hashes.append(self.hashes)	

			while self.contador < len(self.lista_archivos):
				for i in range(0, len(self.lista_archivos)):

					if self.lista_hashes[self.contador] == self.lista_hashes[i]:
						self.lista_hashes.append([i])

				self.contador += 1		

		except Exception:
			print("Error del sistema")

		finally:
			print(self.lista_hashes)
			print("Prueba 3 completa\n")

	def test_duplicacion(self):
		self.nombres = input("¿Tienes nombres duplicados?: ")
		self.tamaño = input("¿Tienes tamaños duplicados?: ")
		self.hash = input("¿Tienes hashes duplicados?: ")

		if self.nombres.lower() == "si" and self.tamaño == "si":
			print("Hay probabilidades de duplicacion")

		elif self.hash.lower() == "si":
			print("Hay archivos duplicados")

		else:
			print("No hay archivos duplicados")
		
archivos_duplicados = ArchivosDuplicados("C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Practica")
archivos_duplicados.obtener_archivos()
archivos_duplicados.comparar_nombres()
archivos_duplicados.comparar_tamaño()
archivos_duplicados.comparar_hashes()
archivos_duplicados.test_duplicacion()